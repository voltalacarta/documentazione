---
titolo: CMS, plugin e hosting
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, infrastruttura]
prossima_revisione: 2027-01-15
owasp: [A03:2025, A02:2025]
---

# CMS, plugin e hosting

> **In sintesi.** Per la maggior parte dei siti (WordPress, Joomla, Drupal, PrestaShop, Shopify con app) il rischio principale non è il codice scritto in casa, ma **plugin e temi** di terze parti non aggiornati e gli accessi amministrativi deboli.

## Pratiche per CMS self-hosted

### 🔴 Obbligatorio

- Core, plugin e temi **sempre aggiornati**; aggiornamenti automatici per le release di sicurezza.
- **Rimuovi** (non solo disattiva) plugin e temi inutilizzati.
- Installa solo plugin mantenuti attivamente, con molte installazioni e aggiornamenti recenti; mai versioni "nulled" o crackate (sono un vettore di malware frequente).
- Account amministratore con **MFA** (meglio passkey), nome utente non ovvio, nessun account condiviso.
- **Backup** automatici, esterni al server, testati (vedi [backup-e-continuita](../10-operazioni/backup-e-continuita.md)).

### 🟠 Raccomandato

- Ruoli minimi per i redattori (in WordPress: *Editor*/*Author*, non *Administrator*).
- Area di amministrazione limitata per IP o dietro autenticazione aggiuntiva.
- Disattiva l'editor di file dal pannello (`DISALLOW_FILE_EDIT` in WordPress) e XML-RPC se non serve.
- Permessi dei file corretti: il web server non deve poter scrivere sul codice, solo nelle cartelle di upload.
- Plugin/servizio di sicurezza con WAF e scansione malware, oppure WAF del CDN.
- Abbonati agli advisory di sicurezza del CMS e dei plugin principali (es. database Wordfence o Patchstack per WordPress).

### 🟢 Avanzato

- Architettura **headless/statica** (il CMS genera contenuti, il sito pubblico è statico): riduce enormemente la superficie d'attacco.

## Scelta dell'hosting

| Criterio | Cosa chiedere |
|---|---|
| Aggiornamenti | Versioni di PHP/Node/OS supportate e aggiornate dal provider? |
| Isolamento | Account isolati tra clienti nell'hosting condiviso? |
| Backup | Frequenza, conservazione, ripristino self-service, copia off-site |
| TLS | Certificati automatici, TLS 1.3, HTTP/3 |
| Accessi | MFA sul pannello, SFTP/SSH con chiavi (no FTP in chiaro) |
| Protezione | WAF, anti-DDoS, scansione malware inclusi? |
| Localizzazione dati | Data center nell'UE e contratto di trattamento (art. 28 GDPR) |
| Log | Accesso ai log di accesso ed errori |

## Fonti

- [HDSUPPLY-7RULES], [OLIGO-BP] — vedi [fonti.md](../fonti.md)
