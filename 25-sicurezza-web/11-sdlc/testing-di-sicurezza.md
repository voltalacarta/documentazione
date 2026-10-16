---
titolo: Testing di sicurezza
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, sdlc]
prossima_revisione: 2027-04-15
---

# Testing di sicurezza

> **In sintesi.** Nessuno strumento trova tutto. SAST e SCA trovano problemi nel codice e nelle dipendenze, DAST trova problemi nell'applicazione in esecuzione, il penetration test umano trova i difetti di logica e di autorizzazione che gli strumenti non capiscono.

## Tipi di test

| Tipo | Cosa trova | Quando | Strumenti (esempi, open source in grassetto) |
|---|---|---|---|
| **SAST** | Pattern pericolosi nel codice | Ogni PR | **Semgrep**, **CodeQL**, SonarQube, Snyk Code |
| **SCA** | Dipendenze vulnerabili/malevole | Ogni build + giornaliero | **OSV-Scanner**, **Trivy**, Dependabot, Renovate, Socket |
| **Secret scanning** | Credenziali nel codice e nella storia | Pre-commit + ogni push | **Gitleaks**, **TruffleHog**, GitHub push protection |
| **IaC / container** | Configurazioni cloud e immagini insicure | Ogni build | **Checkov**, **Trivy**, **KICS** |
| **DAST** | Vulnerabilità a runtime | Su staging, ogni rilascio o notte | **ZAP**, **Nuclei**, Burp Suite |
| **Test di autorizzazione** | IDOR, escalation | In CI con utenti di test | test automatici dedicati, Burp Autorize |
| **Fuzzing** | Crash e casi limite nei parser | Componenti critici | **RESTler**, **Schemathesis** (API), OSS-Fuzz |
| **Penetration test** | Logica, catene di vulnerabilità | Prima del lancio, poi annuale e a ogni cambio rilevante | Fornitore qualificato |
| **Red teaming AI** | Prompt injection, fughe di dati | Se integri LLM | **Promptfoo**, **garak** |

## Pratiche

- 🔴 Almeno SCA + secret scanning in CI per qualunque progetto.
- 🟠 SAST con regole adatte al linguaggio, soglia di blocco sulle sole gravità alte per non generare rumore.
- 🟠 DAST in modalità autenticata (con utenti di test), altrimenti vede solo la superficie pubblica.
- 🟠 Penetration test prima del go-live per siti con login, pagamenti o dati personali; chiedi che il perimetro includa autorizzazione e logica di business.
- 🟠 Gestisci i risultati come ticket con priorità e scadenza, non come report da archiviare.
- 🟢 Verifica dei requisiti ASVS come criteri di accettazione automatizzati (header, cookie, TLS).

## Fonti

- [PALTECH-BP], [A10-WEBSEC], [RADWARE-15BP] — vedi [fonti.md](../fonti.md)
