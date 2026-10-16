---
titolo: OWASP Top 10:2025
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, fondamenti]
prossima_revisione: 2027-04-15
owasp: [A01-A10:2025]
---

# OWASP Top 10:2025

> **In sintesi.** È il documento di consapevolezza di riferimento sui rischi delle applicazioni web, aggiornato circa ogni 3-4 anni su dati reali. L'edizione 2025, presentata in bozza a novembre 2025 al Global AppSec, sostituisce quella del 2021.

## La lista

| # | Categoria | Novità rispetto al 2021 | Approfondimento |
|---|---|---|---|
| A01 | Broken Access Control | Resta al primo posto; **assorbe la SSRF** (ex A10:2021) | [controllo-accessi](../02-autorizzazione/controllo-accessi.md), [ssrf](../02-autorizzazione/ssrf.md) |
| A02 | Security Misconfiguration | Sale dal 5° al 2° posto | [hardening](../09-infrastruttura/hardening-configurazione.md) |
| A03 | Software Supply Chain Failures | **Nuova**: allarga "Vulnerable and Outdated Components" a build, registri e distribuzione | [06-supply-chain](../06-supply-chain/dipendenze.md) |
| A04 | Cryptographic Failures | Scende dal 2° posto | [05-crittografia](../05-crittografia/tls-e-hsts.md) |
| A05 | Injection | Scende dal 3° posto; include XSS e SQLi | [injection](../03-input-e-output/injection.md), [xss](../03-input-e-output/xss.md) |
| A06 | Insecure Design | — | [threat-modeling](threat-modeling.md) |
| A07 | Authentication Failures | Rinominata | [01-autenticazione](../01-autenticazione/passkey-webauthn.md) |
| A08 | Software or Data Integrity Failures | — | [ci-cd](../06-supply-chain/ci-cd.md) |
| A09 | Security Logging and Alerting Failures | Enfasi su **alert**, non solo log | [logging-e-alert](../10-operazioni/logging-e-alert.md) |
| A10 | Mishandling of Exceptional Conditions | **Nuova** | [gestione-errori](../10-operazioni/gestione-errori.md) |

## Dati da ricordare

- Nei test che alimentano la classifica, **controllo degli accessi difettoso e configurazioni errate sono stati riscontrati nel 100% delle applicazioni** analizzate. Sono quindi le prime due aree da verificare in qualunque progetto.
- La metodologia combina dati di test (prevalenza) con CVE raggruppate per CWE e punteggi CVSS medi (sfruttabilità e impatto), più un sondaggio della comunità per i rischi emergenti.
- La tendenza generale: l'attenzione si sposta dagli errori di implementazione puntuali verso **configurazione, architettura e supply chain**.

## Come usarla (e come non usarla)

- ✅ Come linguaggio comune tra sviluppatori, management e fornitori.
- ✅ Come punto di partenza per formazione e priorità.
- ❌ Non è uno standard di verifica: per requisiti testabili usa [ASVS 5.0](owasp-asvs-5.md).
- ❌ Non copre API e LLM in modo specifico: vedi [OWASP API Top 10](../07-api/owasp-api-top10.md) e [OWASP LLM Top 10](../08-ai-llm/owasp-llm-top10.md).

## Fonti

- [OWASP-T10], [FASTLY-T10], [RADWARE-T10], [HCL-T10] — vedi [fonti.md](../fonti.md)
