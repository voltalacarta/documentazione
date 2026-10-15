# Istruzioni per Claude

Questo repository è la **fonte unica di verità** della documentazione generale di Volta la carta. Tutto ciò che viene deciso finisce qui.

## Prima di scrivere

- Leggi [`00-meta/convenzioni.md`](00-meta/convenzioni.md) e [`00-meta/struttura.md`](00-meta/struttura.md).
- Scrivi in **italiano**, frasi brevi.

## Quando l'utente "sancisce" qualcosa

1. Crea una decisione in `10-decisioni/` dal modello `_modelli/decisione.md`, con il numero successivo libero.
2. Se servono dettagli operativi, aggiorna o crea il documento nella sezione giusta (`20-` com'è fatto, `40-` come si fa) e collegalo.
3. Aggiorna gli indici: `README.md` della sezione e, per le decisioni, la tabella in `10-decisioni/README.md`.
4. Se tocca un progetto, aggiorna la scheda in `50-progetti/`.
5. Aggiorna il campo `aggiornato` nel frontmatter dei file modificati.

## Regole fisse

- Non riscrivere decisioni accettate: creane una nuova che le sostituisce e marca la vecchia `superato`.
- Non cancellare documenti: archiviali in `90-archivio/`.
- Nomi file: minuscole, trattini, niente accenti.
- Link relativi; verifica che non si rompano quando sposti file.
- Mai segreti o dati sensibili nel repository.
- Messaggi di commit: `tipo(sezione): descrizione` (vedi convenzioni).

## Controlli

Prima del commit esegui `npx markdownlint-cli2 "**/*.md"` e correggi gli errori.
