---
titolo: Header HTTP di sicurezza
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, browser]
prossima_revisione: 2027-04-15
owasp: [A02:2025]
asvs: [V3, V12]
---

# Header HTTP di sicurezza

> **In sintesi.** Gli header attivano protezioni del browser indipendenti dal codice applicativo. Costano poco e vanno configurati una volta sola, a livello di server, proxy o CDN.

## Set di base

| Header | Valore consigliato | Livello | Protegge da |
|---|---|---|---|
| `Strict-Transport-Security` | `max-age=63072000; includeSubDomains; preload` | 🔴 | Downgrade a HTTP, SSL stripping |
| `Content-Security-Policy` | Policy strict, vedi [CSP](content-security-policy.md) | 🟠 | XSS, injection |
| `X-Content-Type-Options` | `nosniff` | 🔴 | MIME sniffing |
| `Referrer-Policy` | `strict-origin-when-cross-origin` | 🔴 | Fuga di URL e token nei referrer |
| `Cross-Origin-Opener-Policy` | `same-origin` (o `same-origin-allow-popups` se usi popup OAuth/pagamenti) | 🟠 | Attacchi tra finestre, XS-Leaks |
| `Cross-Origin-Resource-Policy` | `same-origin` / `same-site` | 🟠 | Inclusione delle tue risorse da altri siti |
| `Permissions-Policy` | `camera=(), microphone=(), geolocation=(), payment=()` (abilita solo ciò che serve) | 🟠 | Abuso di API del browser |
| `CSP frame-ancestors` | `'self'` o `'none'` | 🔴 | Clickjacking |
| `X-Frame-Options` | `DENY` / `SAMEORIGIN` | 🟠 | Clickjacking (per browser vecchi) |
| `Cross-Origin-Embedder-Policy` | `require-corp` | 🟢 | Insieme a COOP abilita il *cross-origin isolation* (mitigazione tipo Spectre) |
| `Cache-Control` | `no-store` su pagine con dati personali | 🔴 | Dati sensibili in cache condivise |

## Da rimuovere

- `Server`, `X-Powered-By`, `X-AspNet-Version`: rivelano tecnologia e versione.
- `X-XSS-Protection`: deprecato; impostalo a `0` o rimuovilo, la protezione è affidata alla CSP.

## Esempio nginx

```nginx
add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;
add_header X-Content-Type-Options "nosniff" always;
add_header Referrer-Policy "strict-origin-when-cross-origin" always;
add_header Cross-Origin-Opener-Policy "same-origin" always;
add_header Permissions-Policy "camera=(), microphone=(), geolocation=()" always;
add_header Content-Security-Policy "frame-ancestors 'self'; object-src 'none'; base-uri 'none'" always;
server_tokens off;
```

> Nota nginx: `add_header` in un blocco `location` annulla quelli ereditati dal blocco superiore. Centralizza in un file incluso.

## Fetch Metadata

I browser moderni inviano `Sec-Fetch-Site`, `Sec-Fetch-Mode`, `Sec-Fetch-Dest`. Una *resource isolation policy* lato server può rifiutare richieste cross-site inattese: vedi [csrf](../03-input-e-output/csrf.md).

## Come verificarlo

- securityheaders.com, Mozilla HTTP Observatory, test automatico in CI con `curl -I`.

## Fonti

- [WEBDEV-HEADERS], [ALERT-HEADERS], [AZION-HEADERS], [DEVTO-HEADERS] — vedi [fonti.md](../fonti.md)
