---
titolo: Content Security Policy (CSP)
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, browser]
prossima_revisione: 2027-04-15
owasp: [A05:2025, A02:2025]
asvs: [V3]
---

# Content Security Policy (CSP)

> **In sintesi.** Usa una **CSP strict** basata su nonce (siti renderizzati dal server) o su hash (SPA e siti statici). Le CSP basate su allowlist di domini sono facilmente aggirabili e non sono più considerate efficaci contro le XSS.

## CSP strict con nonce (consigliata per rendering server-side)

```http
Content-Security-Policy:
  script-src 'nonce-{RANDOM}' 'strict-dynamic';
  object-src 'none';
  base-uri 'none';
  frame-ancestors 'self';
  report-to csp-endpoint;
```

```html
<script nonce="{RANDOM}" src="/app.js"></script>
```

- Il nonce è casuale, **diverso a ogni risposta**, ≥ 128 bit.
- `'strict-dynamic'` permette agli script fidati di caricarne altri senza elencare domini.
- Le pagine con nonce **non devono essere messe in cache** condivisa con lo stesso nonce.

## CSP strict con hash (SPA, siti statici)

```http
Content-Security-Policy:
  script-src 'sha256-{HASH_DELLO_SCRIPT_INLINE}' 'strict-dynamic';
  object-src 'none';
  base-uri 'none';
```

Lo script inline (bootstrap) carica il resto dell'applicazione; molti bundler possono calcolare gli hash in build.

## Direttive aggiuntive utili

| Direttiva | Valore tipico | Scopo |
|---|---|---|
| `frame-ancestors` | `'self'` o `'none'` | Anti-clickjacking (sostituisce `X-Frame-Options`) |
| `form-action` | `'self'` | Impedisce l'invio di form verso domini esterni |
| `upgrade-insecure-requests` | — | Converte richieste http in https |
| `require-trusted-types-for` | `'script'` | Vedi [trusted-types](trusted-types.md) |

## Percorso di adozione

1. 🟠 Pubblica la policy in `Content-Security-Policy-Report-Only` e raccogli i report (endpoint proprio o servizi come Report URI).
2. 🟠 Aggiungi nonce/hash agli script legittimi; elimina gli handler inline (`onclick=`) e gli URL `javascript:`.
3. 🟠 Valuta la policy con **CSP Evaluator** di Google.
4. 🔴 Passa in modalità enforce, mantenendo il reporting attivo.

## Errori comuni

- `'unsafe-inline'` in `script-src` senza nonce/hash: rende la CSP quasi inutile contro le XSS.
- Allowlist di CDN pubblici (es. tutto `cdn.jsdelivr.net`): ospitano anche codice dell'attaccante.
- Dimenticare `object-src 'none'` e `base-uri`.

## Fonti

- [WEBDEV-HEADERS], [AZION-HEADERS], [REPORTURI-ASVS] — vedi [fonti.md](../fonti.md)
