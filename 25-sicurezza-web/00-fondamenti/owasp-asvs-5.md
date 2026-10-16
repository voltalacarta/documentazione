---
titolo: OWASP ASVS 5.0 — Standard di verifica
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, fondamenti]
prossima_revisione: 2027-04-15
asvs: [V1-V17]
---

# OWASP ASVS 5.0

> **In sintesi.** Se la Top 10 dice *quali* rischi esistono, l'Application Security Verification Standard dice *cosa verificare*, con requisiti testabili. La versione 5.0.0 è uscita a maggio 2025, prima major release dopo la 4.0.3 del 2021.

## Caratteristiche principali della 5.0

- Circa **350 requisiti in 17 capitoli**, completamente riorganizzati rispetto alla 4.x.
- Tre **livelli** (L1, L2, L3): ciascuna organizzazione sceglie il livello in base alla sensibilità dei dati e alla funzione dell'applicazione. La 5.0 abbassa la soglia d'ingresso al L1 e amplia molto il L3.
- Introduce l'obbligo di **decisioni di sicurezza documentate**: si può scegliere come implementare un requisito, purché la scelta sia motivata per iscritto.
- Fornisce una mappatura bidirezionale 4.x ↔ 5.0 per la migrazione; le corrispondenze con altri standard (ISO 27001, NIST, PCI DSS) passano dal progetto OWASP CRE.
- Per i sistemi AI è in sviluppo un progetto separato, **AISVS**.

## Capitoli (V1–V17)

Elenco verificato il 2026-10-15 sull'indice ASVS 5.0 dell'OWASP Cheat Sheet Series.

| Capitolo | Tema | File di questa base |
|---|---|---|
| V1 | Encoding e sanitizzazione | [injection](../03-input-e-output/injection.md), [xss](../03-input-e-output/xss.md) |
| V2 | Validazione e logica di business | [controllo-accessi](../02-autorizzazione/controllo-accessi.md) |
| V3 | Sicurezza del frontend web | [04-browser](../04-browser/header-di-sicurezza.md) |
| V4 | API e servizi web | [owasp-api-top10](../07-api/owasp-api-top10.md) |
| V5 | Gestione dei file | [upload-file](../03-input-e-output/upload-file.md) |
| V6 | Autenticazione | [01-autenticazione](../01-autenticazione/passkey-webauthn.md) |
| V7 | Gestione delle sessioni | [sessioni-e-cookie](../01-autenticazione/sessioni-e-cookie.md) |
| V8 | Autorizzazione | [controllo-accessi](../02-autorizzazione/controllo-accessi.md) |
| V9 | Token autocontenuti (JWT) | [sessioni-e-cookie](../01-autenticazione/sessioni-e-cookie.md) |
| V10 | OAuth e OIDC | [mfa-e-recupero-account](../01-autenticazione/mfa-e-recupero-account.md) |
| V11 | Crittografia | [dati-e-segreti](../05-crittografia/dati-e-segreti.md) |
| V12 | Comunicazione sicura | [tls-e-hsts](../05-crittografia/tls-e-hsts.md) |
| V13 | Configurazione | [hardening](../09-infrastruttura/hardening-configurazione.md) |
| V14 | Protezione dei dati | [gdpr](../12-normativa-ue/gdpr.md) |
| V15 | Codice e architettura sicuri | [principi](principi.md), [dipendenze](../06-supply-chain/dipendenze.md) |
| V16 | Logging ed errori | [logging-e-alert](../10-operazioni/logging-e-alert.md) |
| V17 | WebRTC | — |

## Come adottarlo

1. 🔴 Scegli il livello target: **L1** per siti vetrina e piccoli e-commerce con pagamento esternalizzato; **L2** per applicazioni con account e dati personali (la scelta tipica); **L3** per sanità, finanza, infrastrutture critiche.
2. 🟠 Converti i requisiti del livello in *user story* o criteri di accettazione.
3. 🟠 Usalo nei contratti con fornitori e nei capitolati ("conforme ad ASVS 5.0 L2").
4. 🟢 Automatizza la verifica dei requisiti testabili (header, TLS, cookie) in CI.

## Fonti

- [OWASP-ASVS], [OWASP-CS-ASVS], [ASVS-SOFTWAREMILL], [ASVS-INTERTEK] — vedi [fonti.md](../fonti.md)
