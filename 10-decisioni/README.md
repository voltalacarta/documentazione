---
titolo: Registro delle decisioni
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-19
tag: [decisioni, indice]
---

# 10 · Registro delle decisioni

Qui finisce **tutto ciò che viene sancito**. Una decisione = un file numerato.

## Decisioni

<!-- indice:inizio decisioni -->
<!-- Generato da strumenti/indici.py: le modifiche qui dentro vengono sovrascritte. -->

| N. | Decisione | Stato | Data |
| --- | --- | --- | --- |
| [0001](0001-registrare-le-decisioni.md) | Registrare le decisioni in questo repository | accettato | 2026-10-15 |
| [0002](0002-github-come-base-di-lavoro.md) | GitHub come base unica di lavoro | accettato | 2026-10-15 |
| [0003](0003-ambiente-di-sviluppo-solo-cloud.md) | Ambiente di sviluppo solo cloud con GitHub Codespaces | accettato | 2026-10-15 |
| [0004](0004-second-brain-markdown-su-github.md) | Second brain in Markdown su GitHub | accettato | 2026-10-15 |
| [0005](0005-strumenti-online-gratuiti.md) | Strumenti online gratuiti per editor e second brain | accettato | 2026-10-15 |
| [0006](0006-riferimento-sicurezza-web.md) | Knowledge base di sicurezza web come riferimento per i progetti digitali | proposto | 2026-10-16 |
| [0007](0007-grafo-della-conoscenza-automatico-su-tutte-le-repo.md) | Grafo della conoscenza automatico su tutte le repo | accettato | 2026-10-19 |
| [0008](0008-app-web-del-second-brain-su-github-pages.md) | App web del second brain su GitHub Pages | accettato | 2026-10-20 |

<!-- indice:fine -->

## Come si registra una decisione

1. `python3 strumenti/nuova-decisione.py "Titolo" --tag a,b --collegati 3 --sintesi "Una riga."`: crea il file con il numero successivo e i metadati compilati (il modello è [`_modelli/decisione.md`](../_modelli/decisione.md)).
2. Compila contesto, decisione, alternative e conseguenze.
3. Stato iniziale `proposto`; diventa `accettato` quando è approvata.
4. Commit e push: **il registro qui sopra si aggiorna da solo**.

## Regole

- **Le decisioni accettate non si riscrivono.** Se cambia idea, si crea una nuova decisione che la *sostituisce*, e nella vecchia si imposta `stato: superato` e `sostituito-da: 00XX`.
- I numeri non si riutilizzano mai, anche se una decisione viene scartata.
- Una decisione deve essere breve: se servono dettagli operativi, vanno in `20-infrastruttura/` o `40-procedure/` e la decisione li linka.
