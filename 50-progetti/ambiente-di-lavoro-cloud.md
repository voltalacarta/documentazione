---
titolo: Ambiente di lavoro cloud
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-19
tag: [progetti, infrastruttura, cloud]
sintesi: "Mettere in opera GitHub, Codespaces e second brain"
collegati: [0001, 0002, 0003, 0004, 0005, 0007]
---

# Ambiente di lavoro cloud

## Obiettivo

Un ambiente di lavoro "chiavi in mano" interamente nel cloud: documentazione, sviluppo e second brain su GitHub, senza usare il computer locale.

## Stato

**In corso.** Avviato il 2026-10-15.

## Attività

| # | Attività | Stato |
| --- | --- | --- |
| 1 | Collegare Claude a GitHub | ✅ fatto |
| 2 | Creare la struttura del repository `documentazione` | ✅ fatto |
| 3 | Scegliere gli strumenti online gratuiti (decisione 0005) | ✅ fatto |
| 4 | Preparare struttura, modelli e configurazione Foam/Obsidian del second brain | ✅ fatto |
| 5 | Creare su GitHub il repository privato `second-brain` e caricare la struttura | ✅ fatto |
| 5b | Decidere la visibilità di `documentazione` (oggi pubblico) | ⏳ da fare |
| 5c | Grafo della conoscenza automatico su tutte le repo (decisione 0007) | ✅ fatto |
| 5d | Indici, registro e mappa compatta automatici in `documentazione` | ✅ fatto |
| 5e | Modello per le repo dei nuovi progetti | ✅ fatto |
| 5f | Creare il token `KG_TOKEN` per far entrare nel grafo le repo private | ⏳ da fare (utente) |
| 6 | Proteggere l'account GitHub (2FA/passkey) | ⏳ da fare |
| 7 | Applicare le impostazioni di costo di Codespaces | ⏳ da fare |
| 8 | Creare il repository `dotfiles` | ⏳ da fare |
| 9 | Definire lo stack e il `devcontainer.json` dei progetti di codice | ⏳ da fare |
| 10 | Decidere metodo e frequenza del backup | ⏳ da fare |
| 11 | Decidere le automazioni (nota giornaliera, revisione settimanale) | 🔶 in parte: manutenzione generata a ogni aggiornamento del grafo |

## Riferimenti

- Decisioni: [0001](../10-decisioni/0001-registrare-le-decisioni.md), [0002](../10-decisioni/0002-github-come-base-di-lavoro.md), [0003](../10-decisioni/0003-ambiente-di-sviluppo-solo-cloud.md), [0004](../10-decisioni/0004-second-brain-markdown-su-github.md), [0005](../10-decisioni/0005-strumenti-online-gratuiti.md)
- [Ambiente cloud](../20-infrastruttura/ambiente-cloud.md) · [Sicurezza](../20-infrastruttura/sicurezza.md) · [Second brain](../30-conoscenza/second-brain.md)
