---
titolo: Logging, monitoraggio e alert
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, operazioni]
prossima_revisione: 2027-04-15
owasp: [A09:2025]
asvs: [V16]
---

# Logging, monitoraggio e alert

> **In sintesi.** Il nome della categoria OWASP 2025 è cambiato in *Logging and **Alerting** Failures*: un log che nessuno guarda non serve. Registra gli eventi di sicurezza, proteggili, e fai in modo che qualcuno venga avvisato quando succede qualcosa di anomalo.

## Cosa registrare

| Evento | Campi minimi |
|---|---|
| Login riuscito / fallito, logout | utente, IP, user agent, esito, metodo (password/passkey/SSO) |
| Cambio password, email, MFA, passkey | utente, chi ha fatto la modifica, da dove |
| Accessi negati (403) | utente, risorsa, motivo |
| Azioni amministrative | chi, cosa, su quale oggetto, prima/dopo |
| Errori di validazione ripetuti, input anomali | endpoint, IP, conteggio |
| Eventi CSP/Trusted Types | report del browser |
| Deploy e modifiche di configurazione | chi, versione, ambiente |

## Cosa **non** registrare

- 🔴 Password, token di sessione, codici OTP, chiavi API, numeri di carta completi, dati particolari in chiaro.
- 🔴 Maschera o pseudonimizza i dati personali dove non servono (vedi [gdpr](../12-normativa-ue/gdpr.md)).

## Pratiche

### 🔴 Obbligatorio

- Log in formato **strutturato** (JSON) con timestamp UTC sincronizzato (NTP) e ID di correlazione per richiesta.
- Protezione contro la *log injection*: encoding dei caratteri di controllo (`\r`, `\n`).
- Log centralizzati **fuori** dal server applicativo (un attaccante con accesso al server non deve poterli cancellare).
- Conservazione definita e documentata (bilanciando esigenze investigative e minimizzazione GDPR).

### 🟠 Raccomandato

- **Alert** con soglie e destinatari chiari: picchi di login falliti, molti 403 da un utente, nuovo admin creato, modifica ai workflow CI, errori 5xx anomali.
- Monitoraggio esterno di disponibilità e certificati.
- Log in sola aggiunta / immutabili (WORM) per i log di audit.
- Esercitazioni: verifica periodica che un alert arrivi davvero a qualcuno.

### 🟢 Avanzato

- SIEM (Wazuh, Elastic, Splunk, Microsoft Sentinel, Google SecOps) con regole di correlazione.
- Mappatura delle regole su MITRE ATT&CK.

## Fonti

- [OWASP-T10], [OLIGO-BP] — vedi [fonti.md](../fonti.md)
