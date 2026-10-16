---
titolo: Ricettario di configurazioni
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, ricettario]
prossima_revisione: 2027-04-15
owasp: [A02:2025, A04:2025, A05:2025]
---

# Ricettario di configurazioni

> **In sintesi.** Configurazioni di partenza, pronte da copiare, per gli stack più comuni. Applicano lo stesso set di protezioni descritto in [header-di-sicurezza](../04-browser/header-di-sicurezza.md), [tls-e-hsts](../05-crittografia/tls-e-hsts.md) e [sessioni-e-cookie](../01-autenticazione/sessioni-e-cookie.md).

## Il set comune

Tutte le ricette applicano:

| Protezione | Valore |
|---|---|
| HSTS | `max-age=63072000; includeSubDomains` (aggiungi `preload` solo dopo aver verificato tutti i sottodomini) |
| `X-Content-Type-Options` | `nosniff` |
| `Referrer-Policy` | `strict-origin-when-cross-origin` |
| `Cross-Origin-Opener-Policy` | `same-origin` |
| `Permissions-Policy` | fotocamera, microfono, geolocalizzazione, pagamenti disattivati |
| CSP **di base** (enforce) | `frame-ancestors 'self'; object-src 'none'; base-uri 'self'; form-action 'self'; upgrade-insecure-requests` |
| CSP **strict** (report-only) | `script-src 'nonce-…' 'strict-dynamic'` o hash, da portare in enforce dopo l'analisi dei report |
| Header da rimuovere | `Server` (versione), `X-Powered-By` |

La CSP di base **non rompe** quasi nessun sito: blocca clickjacking, plugin e cambi di `<base>`. La CSP strict, che protegge davvero dalle XSS, va introdotta in report-only (vedi [content-security-policy](../04-browser/content-security-policy.md)).

## Ricette

| Stack | File |
|---|---|
| nginx | [nginx-security.conf](nginx-security.conf) |
| Apache / hosting condiviso | [apache.htaccess](apache.htaccess) |
| Caddy | [caddyfile](caddyfile) |
| Netlify | [netlify-headers](netlify-headers) (rinomina in `_headers`) |
| Vercel | [vercel.json](vercel.json) |
| Node.js / Express | [express-security.js](express-security.js) |
| Next.js | [nextjs-proxy.ts](nextjs-proxy.ts) (`proxy.ts` da Next.js 16, `middleware.ts` fino alla 15) |
| Django | [django-settings-security.py](django-settings-security.py) |
| Laravel | [laravel-security-headers.php](laravel-security-headers.php) |
| WordPress | [wordpress-hardening.md](wordpress-hardening.md) |

## Come adottarle

1. Applica la ricetta in **staging**.
2. Verifica con [`check-headers.py`](../14-automazione/scripts/check-headers.py), securityheaders.com e Mozilla Observatory.
3. Controlla che le funzioni del sito (login, pagamenti, embed video, mappe, analytics) funzionino ancora.
4. Raccogli per qualche settimana i report della CSP strict, sistema le violazioni legittime, poi passala in enforce.

## Stato di verifica (2026-10-15)

| Ricetta | Verifica eseguita |
|---|---|
| Express | sintassi (`node --check`) ✅ |
| Django | sintassi (`py_compile`) ✅ · impostazioni CSP confrontate con la documentazione ufficiale di Django 6.0 ✅ |
| Laravel | sintassi (`php -l`) ✅ |
| Vercel | JSON valido ✅ |
| Next.js | allineato alla guida ufficiale CSP di Next.js (marzo 2026) ✅ · non compilato qui (registro npm non raggiungibile) |
| nginx, Caddy, Apache, Netlify | non eseguite qui: prova con `nginx -t`, `caddy validate`, `apachectl configtest` prima del deploy |

Fonti delle ricette framework: [DJANGO-CSP], [NEXTJS-CSP] — vedi [fonti.md](../fonti.md)

> ⚠️ Le ricette sono punti di partenza. Servizi esterni (pagamenti in iframe, mappe, chat, analytics) possono richiedere eccezioni in CSP e `Permissions-Policy`.
