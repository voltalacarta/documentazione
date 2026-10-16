---
titolo: Questionario di sicurezza per fornitori
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, modelli, modello]
---

# Questionario di sicurezza per fornitori

*Da inviare ad agenzie web, sviluppatori, hosting, piattaforme SaaS e fornitori di servizi AI prima della scelta o del rinnovo.*

*Fornitore: [NOME] — Servizio: [DESCRIZIONE] — Compilato da: [NOME, RUOLO] — Data: [DATA]*

Le domande hanno un codice (A1, B2…) da citare nelle risposte. Quelle marcate **★** sono **bloccanti**: una risposta negativa richiede una motivazione e un piano di rimedio.

## A. Organizzazione

- **A1.** ★ Avete un referente per la sicurezza? Nome e contatto.
- **A2.** Avete certificazioni o attestazioni (ISO/IEC 27001, SOC 2, CSA STAR, ACN Cloud qualificato)? Allegare il certificato e l'ambito.
- **A3.** Il vostro personale riceve formazione periodica sulla sicurezza?
- **A4.** Siete soggetti NIS2? Siete fabbricanti ai sensi del Cyber Resilience Act per i prodotti che ci fornite?

## B. Dati e privacy

- **B1.** ★ Firmate un accordo di trattamento dati (art. 28 GDPR)?
- **B2.** ★ Dove sono conservati e trattati i dati (paesi, data center)? Ci sono trasferimenti extra UE e su quale base?
- **B3.** Quali sub-responsabili usate? Ci avvisate in caso di modifica?
- **B4.** Per servizi AI: i nostri dati vengono usati per addestrare modelli? Per quanto vengono conservati prompt e risposte?
- **B5.** Come vengono cancellati i dati a fine contratto, e in che tempi?

## C. Accessi

- **C1.** ★ MFA obbligatoria per tutti i vostri accessi amministrativi ai nostri sistemi?
- **C2.** Gli accessi del vostro personale sono individuali (nessun account condiviso) e revocati alla cessazione?
- **C3.** Possiamo vedere e revocare gli accessi dei vostri tecnici?
- **C4.** Il servizio supporta per i nostri utenti SSO (SAML/OIDC), MFA e passkey?

## D. Sviluppo (per agenzie e software house)

- **D1.** ★ Seguite uno standard di sviluppo sicuro? (es. OWASP ASVS 5.0 — indicare il livello)
- **D2.** ★ Usate controllo di versione con revisione del codice e analisi automatiche (SAST, dipendenze, segreti)?
- **D3.** Come gestite i segreti (chiavi API, password)? Sono mai nel codice?
- **D4.** Eseguite test di sicurezza o penetration test prima della consegna? Condividete il report?
- **D5.** Per quanto tempo garantite aggiornamenti di sicurezza dopo la consegna, e a quali condizioni?
- **D6.** Chi è proprietario del codice, dei domini e degli account a fine progetto?

## E. Infrastruttura e operazioni

- **E1.** ★ Backup: frequenza, conservazione, copia off-site/immutabile, test di ripristino?
- **E2.** ★ Entro quanto ci notificate un incidente di sicurezza che ci riguarda? (atteso: senza ingiustificato ritardo, e comunque in tempo per rispettare le nostre 24/72 ore)
- **E3.** Tempi di applicazione delle patch critiche?
- **E4.** Monitoraggio e log: cosa registrate, per quanto, possiamo ottenerli in caso di incidente?
- **E5.** Protezione da DDoS e WAF inclusi?
- **E6.** Disponibilità garantita (SLA) e piano di continuità?

## F. Supply chain

- **F1.** Mantenete un inventario delle componenti (SBOM) di ciò che ci fornite?
- **F2.** Come scegliete e aggiornate librerie e plugin di terze parti?

## Valutazione (a cura nostra)

| Area | Esito (OK / Da migliorare / Non accettabile) | Note |
|---|---|---|
| Organizzazione | | |
| Dati e privacy | | |
| Accessi | | |
| Sviluppo | | |
| Infrastruttura | | |
| Supply chain | | |
| **Decisione** | | |
