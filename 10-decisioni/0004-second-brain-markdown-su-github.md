---
titolo: Second brain in Markdown su GitHub
stato: accettato
creato: 2026-10-15
aggiornato: 2026-10-15
tag: [decisioni, second-brain, conoscenza, obsidian]
collegati: [0002, 0003]
---

# 0004 · Second brain in Markdown su GitHub

## Contesto

Si vuole un second brain stile Obsidian, ma interamente remoto. Obsidian di base salva le note in locale.

## Decisione

Opzione **A**: un **repository privato** di note Markdown su GitHub, compatibile con Obsidian.

- Note in Markdown con `[[wikilink]]`.
- **Dal browser:** Codespaces o github.dev con l'estensione **Foam** (backlink, grafo, note giornaliere).
- **Da telefono:** app Obsidian mobile con il plugin Git (facoltativo).
- **Con Claude:** organizzazione, collegamenti, riassunti e nuove note direttamente nel repository.

## Alternative considerate

| Opzione | Perché scartata |
| --- | --- |
| B · Obsidian + Obsidian Sync | A pagamento, richiede le app installate su ogni dispositivo |
| C · Notion, Capacities, Tana | Note non in file Markdown propri, dipendenza dal fornitore |

## Conseguenze

- ✅ Nessun lock-in: le note restano file di testo.
- ✅ Storico completo di ogni modifica.
- ✅ Claude può lavorare sulle note.
- ⚠️ Git gestisce male file pesanti: immagini compresse, PDF grandi fuori dal repository.
- ⚠️ Nessun dato sensibile nelle note (password, IBAN).

## Dettagli

- [Second brain](../30-conoscenza/second-brain.md)
