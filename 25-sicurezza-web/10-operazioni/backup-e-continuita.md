---
titolo: Backup e continuità operativa
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, operazioni]
prossima_revisione: 2027-10-15
---

# Backup e continuità operativa

> **In sintesi.** Un backup non testato è un'ipotesi. Contro il ransomware serve almeno una copia che l'attaccante non possa cancellare né cifrare.

## Regola 3-2-1-1-0

- **3** copie dei dati
- su **2** supporti/servizi diversi
- **1** copia off-site (altro provider o regione)
- **1** copia **immutabile** o offline (object lock, WORM, air gap)
- **0** errori al test di ripristino

## Pratiche

- 🔴 Backup automatici di database, file caricati dagli utenti, configurazioni e segreti (cifrati).
- 🔴 Credenziali dei backup **separate** da quelle di produzione: chi compromette il server non deve poter cancellare i backup.
- 🔴 Backup cifrati, con chiavi conservate altrove.
- 🔴 **Test di ripristino** periodici (almeno trimestrali) e cronometrati.
- 🟠 Obiettivi espliciti: **RPO** (quanti dati posso perdere) e **RTO** (in quanto tempo devo tornare online).
- 🟠 Retention sufficiente a coprire compromissioni scoperte in ritardo (settimane/mesi), compatibilmente con il GDPR.
- 🟢 Infrastruttura ricostruibile da codice (IaC) per ripartire anche se il provider è compromesso.

## Fonti

- Pratica consolidata; nessuna fonte datata specifica.
