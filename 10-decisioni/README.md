---
titolo: Registro delle decisioni
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-15
tag: [decisioni, indice]
---

# 10 · Registro delle decisioni

Qui finisce **tutto ciò che viene sancito**. Una decisione = un file numerato.

## Decisioni

| N. | Decisione | Stato | Data |
| --- | --- | --- | --- |
| [0001](0001-registrare-le-decisioni.md) | Registrare le decisioni in questo repository | accettato | 2026-10-15 |
| [0002](0002-github-come-base-di-lavoro.md) | GitHub come base unica di lavoro | accettato | 2026-10-15 |
| [0003](0003-ambiente-di-sviluppo-solo-cloud.md) | Ambiente di sviluppo solo cloud con GitHub Codespaces | accettato | 2026-10-15 |
| [0004](0004-second-brain-markdown-su-github.md) | Second brain in Markdown su GitHub | accettato | 2026-10-15 |
| [0005](0005-strumenti-online-gratuiti.md) | Strumenti online gratuiti per editor e second brain | accettato | 2026-10-15 |

## Come si registra una decisione

1. Copia [`_modelli/decisione.md`](../_modelli/decisione.md) in questa cartella con il numero successivo: `0006-titolo-breve.md`.
2. Compila contesto, decisione, alternative e conseguenze.
3. Stato iniziale `proposto`; diventa `accettato` quando è approvata.
4. Aggiungi la riga nella tabella qui sopra.

## Regole

- **Le decisioni accettate non si riscrivono.** Se cambia idea, si crea una nuova decisione che la *sostituisce*, e nella vecchia si imposta `stato: superato` e `sostituito-da: 00XX`.
- I numeri non si riutilizzano mai, anche se una decisione viene scartata.
- Una decisione deve essere breve: se servono dettagli operativi, vanno in `20-infrastruttura/` o `40-procedure/` e la decisione li linka.
