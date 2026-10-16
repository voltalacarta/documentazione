---
titolo: Sicurezza delle API (OWASP API Security Top 10:2023)
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, api]
prossima_revisione: 2027-04-15
owasp: [A01:2025, A02:2025]
asvs: [V4]
---

# Sicurezza delle API

> **In sintesi.** Le API espongono direttamente la logica di business e i dati, senza l'interfaccia che "nasconde" i campi. OWASP mantiene una lista dedicata, aggiornata l'ultima volta il 7 giugno 2023 (prima edizione 2019).

## OWASP API Security Top 10:2023

| # | Rischio | Contromisura chiave |
|---|---|---|
| API1 | Broken Object Level Authorization (BOLA) | Controllo di proprietà su ogni oggetto → [controllo-accessi](../02-autorizzazione/controllo-accessi.md) |
| API2 | Broken Authentication | Token robusti, rate limit sul login → [01-autenticazione](../01-autenticazione/sessioni-e-cookie.md) |
| API3 | Broken Object Property Level Authorization | Allowlist dei campi in lettura e scrittura (no mass assignment, no *excessive data exposure*) |
| API4 | Unrestricted Resource Consumption | Limiti su richieste, dimensione, paginazione, costo → [waf-rate-limiting-bot](../09-infrastruttura/waf-rate-limiting-bot.md) |
| API5 | Broken Function Level Authorization | Endpoint admin protetti per ruolo, non per oscurità |
| API6 | Unrestricted Access to Sensitive Business Flows | Anti-automazione su acquisti, registrazioni, coupon |
| API7 | Server Side Request Forgery | → [ssrf](../02-autorizzazione/ssrf.md) |
| API8 | Security Misconfiguration | → [hardening](../09-infrastruttura/hardening-configurazione.md), [cors](../04-browser/cors.md) |
| API9 | Improper Inventory Management | Catalogo di tutte le API e versioni; dismissione delle vecchie |
| API10 | Unsafe Consumption of APIs | Validare anche le risposte delle API di terzi |

## Pratiche

### 🔴 Obbligatorio

- **Validazione con schema** di ogni richiesta (OpenAPI + validatore, Zod, Pydantic): tipi, lunghezze, campi ammessi; rifiuta i campi sconosciuti.
- **Risposte minime**: serializza con DTO espliciti, mai l'oggetto del database intero.
- Autenticazione su ogni endpoint (tranne quelli dichiarati pubblici) e autorizzazione a livello di oggetto **e** di proprietà.
- **Paginazione obbligatoria** con limite massimo; timeout e limiti di dimensione del body.
- Errori senza dettagli interni (vedi [gestione-errori](../10-operazioni/gestione-errori.md)).

### 🟠 Raccomandato

- **Inventario** delle API (specifica OpenAPI versionata), incluse versioni vecchie, ambienti di test esposti e API "ombra".
- Rate limiting per utente/chiave/IP e quote per i flussi di business sensibili.
- API key solo per identificare client server-to-server, mai come unico meccanismo per utenti finali.
- **GraphQL**: limita profondità e complessità delle query, disattiva l'introspection in produzione, applica l'autorizzazione nei resolver.
- Webhook in ingresso: verifica la firma HMAC e il timestamp (anti-replay).

### 🟢 Avanzato

- API gateway con policy centralizzate, mTLS tra servizi interni.
- Test DAST specifici per API guidati dalla specifica OpenAPI.

## Fonti

- [SCMAG-API], [AKAMAI-API], [A10-WEBSEC] — vedi [fonti.md](../fonti.md)
