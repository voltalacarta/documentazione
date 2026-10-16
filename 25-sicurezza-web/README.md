---
titolo: Sicurezza web
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, indice]
prossima_revisione: 2027-01-15
versione: 1.3.0
---

# 25 · Sicurezza web

Knowledge base di best practice (aggiornata al 2026) per progettare, sviluppare e gestire siti e applicazioni web sicuri. Ogni file tratta **un solo argomento**, ha metadati di revisione propri e può essere aggiornato in modo indipendente dagli altri.

> **Come usarla.**
>
> - **Nasce un nuovo progetto?** Classificalo con [`16-progetti/profili-di-progetto.md`](16-progetti/profili-di-progetto.md); se lo affidi a un'agenzia, inserisci nel contratto [`requisiti-capitolato.md`](16-progetti/requisiti-capitolato.md).
> - **Devi configurare un server o un framework?** Parti dal [ricettario](13-ricettario/README.md).
> - **Stai per andare online?** Usa [`checklist/pre-lancio.md`](checklist/pre-lancio.md) e [`check-headers.py`](14-automazione/scripts/check-headers.py).
> - **Vuoi capire un argomento?** Segui le cartelle 00–12.

## Struttura

```text
25-sicurezza-web/
├── README.md                     ← sei qui (indice)
├── changelog.md                  ← storico delle modifiche
├── contribuire.md                ← regole per aggiornare la base
├── fonti.md                      ← bibliografia centralizzata
│
├── 00-fondamenti/
│   ├── principi.md               ← difesa in profondità, minimo privilegio, secure by default
│   ├── owasp-top10-2025.md       ← la mappa dei rischi e i rimandi ai file
│   ├── owasp-asvs-5.md           ← lo standard di verifica (requisiti testabili)
│   └── threat-modeling.md
│
├── 01-autenticazione/
│   ├── passkey-webauthn.md
│   ├── password-nist.md
│   ├── mfa-e-recupero-account.md
│   └── sessioni-e-cookie.md
│
├── 02-autorizzazione/
│   ├── controllo-accessi.md
│   └── ssrf.md
│
├── 03-input-e-output/
│   ├── injection.md
│   ├── xss.md
│   ├── csrf.md
│   └── upload-file.md
│
├── 04-browser/
│   ├── content-security-policy.md
│   ├── trusted-types.md
│   ├── header-di-sicurezza.md
│   └── cors.md
│
├── 05-crittografia/
│   ├── tls-e-hsts.md
│   ├── post-quantum.md
│   └── dati-e-segreti.md
│
├── 06-supply-chain/
│   ├── dipendenze.md
│   ├── npm-dopo-shai-hulud.md
│   └── ci-cd.md
│
├── 07-api/
│   └── owasp-api-top10.md
│
├── 08-ai-llm/
│   ├── owasp-llm-top10.md
│   └── agenti-e-strumenti.md
│
├── 09-infrastruttura/
│   ├── hardening-configurazione.md
│   ├── waf-rate-limiting-bot.md
│   └── cms-e-hosting.md
│
├── 10-operazioni/
│   ├── logging-e-alert.md
│   ├── gestione-errori.md
│   ├── incident-response.md
│   ├── backup-e-continuita.md
│   └── vulnerability-disclosure.md
│
├── 11-sdlc/
│   ├── devsecops.md
│   └── testing-di-sicurezza.md
│
├── 12-normativa-ue/
│   ├── gdpr.md
│   ├── nis2-italia.md
│   └── cyber-resilience-act.md
│
├── 13-ricettario/                ← configurazioni pronte
│   ├── README.md                 ← set comune e stato di verifica
│   ├── nginx-security.conf
│   ├── apache.htaccess
│   ├── caddyfile                 ← da rinominare in Caddyfile
│   ├── netlify-headers           ← da rinominare in _headers
│   ├── vercel.json
│   ├── express-security.js
│   ├── nextjs-proxy.ts
│   ├── django-settings-security.py
│   ├── laravel-security-headers.php
│   └── wordpress-hardening.md
│
├── 14-automazione/               ← controlli automatici
│   ├── README.md
│   ├── scripts/check-headers.py  ← verifica di un sito (testato)
│   ├── scripts/kb-revisioni.py   ← scadenze di questa base (testato)
│   ├── github/workflows/security.yml
│   ├── github/dependabot.yml
│   ├── github/renovate.json
│   └── config/                   ← npmrc, pre-commit, gitignore
│
├── 15-modelli/                   ← documenti da compilare
│   ├── security.txt
│   ├── politica-divulgazione.md
│   ├── piano-risposta-incidenti.md
│   ├── registro-violazioni.csv
│   ├── registro-asset-e-accessi.csv
│   ├── questionario-fornitori.md
│   └── procedura-accessi.md
│
├── 16-progetti/                  ← impostare i progetti futuri
│   ├── profili-di-progetto.md    ← dal tipo di progetto ai requisiti
│   └── requisiti-capitolato.md   ← clausole per contratti con agenzie
│
├── 17-formazione/
│   ├── regole-per-redattori.md
│   └── quiz.md
│
└── checklist/
    ├── pre-lancio.md
    └── revisione-periodica.md
```

## Indice per rischio OWASP Top 10:2025

| Rischio | File principali |
|---|---|
| A01 Broken Access Control | [controllo-accessi](02-autorizzazione/controllo-accessi.md), [ssrf](02-autorizzazione/ssrf.md) |
| A02 Security Misconfiguration | [hardening](09-infrastruttura/hardening-configurazione.md), [header](04-browser/header-di-sicurezza.md), [cors](04-browser/cors.md) |
| A03 Software Supply Chain Failures | [dipendenze](06-supply-chain/dipendenze.md), [npm](06-supply-chain/npm-dopo-shai-hulud.md), [ci-cd](06-supply-chain/ci-cd.md) |
| A04 Cryptographic Failures | [tls](05-crittografia/tls-e-hsts.md), [post-quantum](05-crittografia/post-quantum.md), [segreti](05-crittografia/dati-e-segreti.md) |
| A05 Injection | [injection](03-input-e-output/injection.md), [xss](03-input-e-output/xss.md), [csp](04-browser/content-security-policy.md) |
| A06 Insecure Design | [threat-modeling](00-fondamenti/threat-modeling.md), [principi](00-fondamenti/principi.md) |
| A07 Authentication Failures | cartella [01-autenticazione](01-autenticazione/) |
| A08 Software or Data Integrity Failures | [ci-cd](06-supply-chain/ci-cd.md), [csrf](03-input-e-output/csrf.md) |
| A09 Security Logging and Alerting Failures | [logging-e-alert](10-operazioni/logging-e-alert.md) |
| A10 Mishandling of Exceptional Conditions | [gestione-errori](10-operazioni/gestione-errori.md) |

## Livelli di priorità usati nei file

- 🔴 **Obbligatorio** — da fare in qualunque sito in produzione.
- 🟠 **Raccomandato** — standard per siti con login, dati personali o pagamenti.
- 🟢 **Avanzato** — per applicazioni ad alto rischio o con requisiti normativi.

## Manutenzione

Oltre ai campi standard del repository (vedi [convenzioni](../00-meta/convenzioni.md)), ogni documento di questa sezione ha nel frontmatter `prossima_revisione` e, dove serve, i riferimenti `owasp` e `asvs`. Per i nuovi documenti usa il modello [`scheda-sicurezza-web.md`](../_modelli/scheda-sicurezza-web.md).

Un controllo automatico mensile apre una issue su GitHub quando ci sono revisioni scadute (vedi [revisioni-sicurezza-web.yml](../.github/workflows/revisioni-sicurezza-web.yml)). Per trovare a mano i file da rivedere e i marcatori `⚠️ da verificare` ancora aperti:

```bash
python3 25-sicurezza-web/14-automazione/scripts/kb-revisioni.py --radice 25-sicurezza-web --giorni 30
```

Le regole per aggiornare sono in [contribuire.md](contribuire.md); ogni modifica va registrata in [changelog.md](changelog.md).

> ⚠️ Questa base non sostituisce una consulenza legale né un penetration test. Le sezioni normative sono una sintesi orientativa.
