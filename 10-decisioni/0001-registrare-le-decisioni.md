---
titolo: Registrare le decisioni in questo repository
stato: accettato
creato: 2026-10-15
aggiornato: 2026-10-15
tag: [decisioni, governance, meta]
---

# 0001 · Registrare le decisioni in questo repository

## Contesto

Le scelte su strumenti, metodi e organizzazione vengono prese in conversazioni sparse e rischiano di perdersi. Serve un luogo unico, consultabile e con lo storico delle modifiche.

## Decisione

- Il repository [`voltalacarta/documentazione`](https://github.com/voltalacarta/documentazione) è la **fonte unica di verità** della documentazione generale.
- Tutto ciò che viene sancito viene scritto qui in Markdown.
- Ogni decisione ha una scheda numerata in `10-decisioni/`, secondo il formato ADR semplificato del [modello](../_modelli/decisione.md).
- Struttura e regole sono descritte in [`00-meta/`](../00-meta/README.md).

## Alternative considerate

| Alternativa | Perché scartata |
| --- | --- |
| Google Docs / Drive | Niente storico chiaro delle decisioni, struttura poco rigorosa, formato chiuso |
| Notion | Comodo, ma contenuti non in file aperti e dipendenza dal fornitore |
| Wiki di GitHub | Meno controllabile (niente pull request né controlli automatici) |

## Conseguenze

- ✅ Storico completo e reversibile grazie a Git.
- ✅ File di testo aperti, leggibili ovunque e da strumenti AI.
- ✅ Controlli automatici su formato e link.
- ⚠️ Serve disciplina: una decisione non scritta qui non vale.
