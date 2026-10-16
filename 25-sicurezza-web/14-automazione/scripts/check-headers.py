#!/usr/bin/env python3
"""
check-headers.py — verifica rapida degli header di sicurezza, dei cookie,
del redirect HTTPS e di alcuni file sensibili esposti.

Solo libreria standard. Esegue richieste GET normali, come un browser:
usalo SOLO su siti di cui sei responsabile o che hai l'autorizzazione a testare.

Uso:
    python3 check-headers.py https://example.it
    python3 check-headers.py https://example.it --json
    python3 check-headers.py https://example.it --no-exposure   # salta il controllo dei file esposti

Codice di uscita: 0 se nessun problema bloccante, 1 altrimenti (utile in CI).

Riferimento: 04-browser/header-di-sicurezza.md della knowledge base.
Rev. 2026-10-15
"""
from __future__ import annotations

import argparse
import http.client
import json
import re
import ssl
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import asdict, dataclass

UA = "check-headers/1.0 (+security self-check)"
TIMEOUT = 15


@dataclass
class Risultato:
    controllo: str
    esito: str          # OK | AVVISO | ERRORE
    dettaglio: str


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):  # noqa: D401
        return None


def fetch(url: str, follow: bool = True):
    handlers = [] if follow else [NoRedirect()]
    opener = urllib.request.build_opener(*handlers)
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    try:
        resp = opener.open(req, timeout=TIMEOUT)
        return resp.status, resp.headers, resp.geturl(), resp.read(4096)
    except urllib.error.HTTPError as e:
        return e.code, e.headers, url, e.read(4096) if e.fp else b""


def check_headers(h, https: bool) -> list[Risultato]:
    r: list[Risultato] = []
    get = lambda k: h.get(k)  # noqa: E731

    # HSTS
    hsts = get("Strict-Transport-Security")
    if not https:
        r.append(Risultato("HSTS", "ERRORE", "La pagina finale non è servita in HTTPS"))
    elif not hsts:
        r.append(Risultato("HSTS", "ERRORE", "Header assente"))
    else:
        m = re.search(r"max-age=(\d+)", hsts)
        age = int(m.group(1)) if m else 0
        if age < 31536000:
            r.append(Risultato("HSTS", "AVVISO", f"max-age={age}: consigliato almeno 31536000 (1 anno)"))
        else:
            extra = " + includeSubDomains" if "includesubdomains" in hsts.lower() else ""
            r.append(Risultato("HSTS", "OK", f"max-age={age}{extra}"))

    # CSP
    csp = get("Content-Security-Policy")
    csp_ro = get("Content-Security-Policy-Report-Only")
    if not csp and not csp_ro:
        r.append(Risultato("CSP", "AVVISO", "Nessuna Content-Security-Policy"))
    else:
        pol = (csp or "").lower()
        problemi = []
        if csp:
            if "frame-ancestors" not in pol and not get("X-Frame-Options"):
                problemi.append("manca frame-ancestors (clickjacking)")
            if "object-src" not in pol and "default-src 'none'" not in pol:
                problemi.append("manca object-src 'none'")
            if "script-src" in pol and "'unsafe-inline'" in pol and "nonce-" not in pol and "sha256-" not in pol:
                problemi.append("'unsafe-inline' senza nonce/hash: protezione XSS debole")
            strict = "nonce-" in pol or "sha256-" in pol or "sha384-" in pol
        else:
            strict = False
        stato = "AVVISO" if problemi else "OK"
        det = "; ".join(problemi) if problemi else ("strict (nonce/hash)" if strict else "presente (di base)")
        if csp_ro:
            det += " | Report-Only presente"
        r.append(Risultato("CSP", stato, det))

    # Header semplici
    attesi = {
        "X-Content-Type-Options": (lambda v: v and v.lower() == "nosniff", "ERRORE", "atteso 'nosniff'"),
        "Referrer-Policy": (lambda v: bool(v) and v.lower() not in ("unsafe-url", "no-referrer-when-downgrade"),
                            "AVVISO", "consigliato 'strict-origin-when-cross-origin'"),
        "Cross-Origin-Opener-Policy": (lambda v: bool(v), "AVVISO", "consigliato 'same-origin'"),
        "Permissions-Policy": (lambda v: bool(v), "AVVISO", "consigliato: disattivare le API non usate"),
    }
    for nome, (ok, gravita, consiglio) in attesi.items():
        v = get(nome)
        r.append(Risultato(nome, "OK" if ok(v) else gravita, v if ok(v) else f"{'assente' if not v else v} — {consiglio}"))

    # Clickjacking
    if not get("X-Frame-Options") and "frame-ancestors" not in (csp or "").lower():
        r.append(Risultato("Clickjacking", "ERRORE", "Né X-Frame-Options né CSP frame-ancestors"))

    # Fughe di informazioni
    for nome in ("Server", "X-Powered-By", "X-AspNet-Version", "X-Generator"):
        v = get(nome)
        if v and re.search(r"\d", v):
            r.append(Risultato(f"Header {nome}", "AVVISO", f"rivela la versione: '{v}'"))
        elif v and nome != "Server":
            r.append(Risultato(f"Header {nome}", "AVVISO", f"rivela la tecnologia: '{v}'"))

    # Cookie
    for c in h.get_all("Set-Cookie") or []:
        nome = c.split("=", 1)[0].strip()
        low = c.lower()
        mancanti = [a for a in ("secure", "httponly", "samesite") if a not in low]
        if "httponly" in mancanti and not re.search(r"sess|auth|token|login|sid", nome, re.I):
            mancanti.remove("httponly")  # cookie non di sessione: HttpOnly non sempre necessario
        r.append(Risultato(f"Cookie {nome}", "AVVISO" if mancanti else "OK",
                           ("mancano: " + ", ".join(mancanti)) if mancanti else "Secure, HttpOnly, SameSite"))
    return r


def check_https_redirect(url: str) -> Risultato:
    p = urllib.parse.urlparse(url)
    http_url = urllib.parse.urlunparse(("http", p.netloc, p.path or "/", "", "", ""))
    try:
        status, h, _, _ = fetch(http_url, follow=False)
    except Exception as e:  # noqa: BLE001
        return Risultato("Redirect HTTP→HTTPS", "AVVISO", f"porta 80 non raggiungibile ({e.__class__.__name__})")
    loc = (h.get("Location") or "") if h else ""
    if status in (301, 308) and loc.startswith("https://"):
        return Risultato("Redirect HTTP→HTTPS", "OK", f"{status} → {loc}")
    if status in (302, 307) and loc.startswith("https://"):
        return Risultato("Redirect HTTP→HTTPS", "AVVISO", f"redirect temporaneo {status}: preferire 301/308")
    return Risultato("Redirect HTTP→HTTPS", "ERRORE", f"HTTP risponde {status} senza redirect a HTTPS")


def check_tls(url: str) -> Risultato:
    p = urllib.parse.urlparse(url)
    if p.scheme != "https":
        return Risultato("TLS", "ERRORE", "URL non HTTPS")
    host, port = p.hostname, p.port or 443
    ctx = ssl.create_default_context()
    try:
        conn = http.client.HTTPSConnection(host, port, timeout=TIMEOUT, context=ctx)
        conn.connect()
        ver = conn.sock.version()
        conn.close()
    except ssl.SSLCertVerificationError as e:
        return Risultato("TLS", "ERRORE", f"certificato non valido: {e.verify_message}")
    except Exception as e:  # noqa: BLE001
        return Risultato("TLS", "AVVISO", f"connessione diretta non riuscita ({e.__class__.__name__}); verifica con SSL Labs")
    # Prova se accetta TLS < 1.2
    vecchio = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    vecchio.check_hostname = False
    vecchio.verify_mode = ssl.CERT_NONE
    try:
        vecchio.minimum_version = ssl.TLSVersion.TLSv1
        vecchio.maximum_version = ssl.TLSVersion.TLSv1_1
        c2 = http.client.HTTPSConnection(host, port, timeout=TIMEOUT, context=vecchio)
        c2.connect()
        c2.close()
        return Risultato("TLS", "ERRORE", f"negoziato {ver}, ma il server accetta anche TLS 1.0/1.1")
    except Exception:  # noqa: BLE001 — rifiuto atteso (o client locale senza supporto)
        pass
    return Risultato("TLS", "OK" if ver == "TLSv1.3" else "AVVISO",
                     f"negoziato {ver}" + ("" if ver == "TLSv1.3" else ": abilitare TLS 1.3"))


ESPOSTI = ["/.git/HEAD", "/.env", "/.DS_Store", "/wp-config.php.bak", "/backup.zip",
           "/phpinfo.php", "/server-status", "/.well-known/security.txt"]


def check_exposure(base: str) -> list[Risultato]:
    r = []
    for path in ESPOSTI:
        url = urllib.parse.urljoin(base, path)
        try:
            status, _, final, body = fetch(url, follow=False)
        except Exception:  # noqa: BLE001
            continue
        if path == "/.well-known/security.txt":
            if status == 200 and b"contact:" in body.lower():
                r.append(Risultato("security.txt", "OK", "presente"))
            else:
                r.append(Risultato("security.txt", "AVVISO", "assente (RFC 9116)"))
            continue
        if status == 200:
            # .git/HEAD ha una firma riconoscibile; per gli altri basta un 200 non HTML
            sospetto = (path == "/.git/HEAD" and body.startswith(b"ref:")) or (
                path != "/.git/HEAD" and b"<html" not in body[:500].lower())
            if sospetto:
                r.append(Risultato(f"Esposto {path}", "ERRORE", "il file risponde 200: rimuovilo o bloccalo"))
    return r


def main() -> int:
    ap = argparse.ArgumentParser(description="Verifica header di sicurezza di un sito di cui sei responsabile.")
    ap.add_argument("url")
    ap.add_argument("--json", action="store_true", help="output JSON")
    ap.add_argument("--no-exposure", action="store_true", help="salta il controllo dei file esposti")
    ap.add_argument("--no-tls", action="store_true", help="salta i controlli TLS e redirect")
    a = ap.parse_args()

    url = a.url if "://" in a.url else "https://" + a.url
    try:
        status, h, final, _ = fetch(url)
    except Exception as e:  # noqa: BLE001
        print(f"Impossibile raggiungere {url}: {e}", file=sys.stderr)
        return 2

    risultati = [Risultato("Risposta", "OK" if status < 400 else "AVVISO", f"{status} da {final}")]
    if not a.no_tls:
        risultati.append(check_tls(final))
        if urllib.parse.urlparse(url).scheme == "https":
            risultati.append(check_https_redirect(url))
    risultati += check_headers(h, final.startswith("https://"))
    if not a.no_exposure:
        risultati += check_exposure(final)

    errori = sum(r.esito == "ERRORE" for r in risultati)
    avvisi = sum(r.esito == "AVVISO" for r in risultati)

    if a.json:
        print(json.dumps({"url": url, "errori": errori, "avvisi": avvisi,
                          "risultati": [asdict(r) for r in risultati]}, ensure_ascii=False, indent=2))
    else:
        icone = {"OK": "✅", "AVVISO": "⚠️ ", "ERRORE": "❌"}
        print(f"\nControllo di {url}\n")
        for r in risultati:
            print(f"{icone[r.esito]} {r.controllo:<32} {r.dettaglio}")
        print(f"\nTotale: {errori} errori, {avvisi} avvisi.")
        print("Approfondisci con SSL Labs, Mozilla Observatory e un DAST (es. ZAP).\n")
    return 1 if errori else 0


if __name__ == "__main__":
    sys.exit(main())
