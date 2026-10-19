# Claude · regole della documentazione

Fonte unica di verità di Volta la carta: **tutto ciò che viene sancito finisce qui** (o nella repo del progetto).

## Spendere pochi token

1. **Non esplorare.** Orientati con `INDICE.md` (una riga per file: percorso · titolo · stato · sintesi) o `grep -i "parola" INDICE.md`. Apri solo i file che servono.
2. **Non aggiornare a mano** indici, registro delle decisioni e `INDICE.md`: dopo il push li rigenera l'Action *Aggiorna gli indici*.
3. Clone superficiale: `git clone --depth 1`. Leggi `00-meta/convenzioni.md` solo se hai un dubbio di forma.

## Quando l'utente sancisce qualcosa

1. `python3 strumenti/nuova-decisione.py "Titolo" --tag a,b --collegati N --sintesi "Una riga."` → crea `10-decisioni/NNNN-….md` con il numero giusto.
2. Compila Contesto, Decisione, Alternative, Conseguenze. Brevi.
3. Se servono dettagli operativi: documento in `20-` (com'è fatto) o `40-` (come si fa), collegato alla decisione.
4. Un progetto nuovo ha una repo propria: `python3 strumenti/nuovo-progetto.py <cartella> --nome … --descrizione …`.
5. `python3 strumenti/controlla.py`, poi commit `decisione(10): NNNN titolo` e push.

## Regole fisse

- Frontmatter: `titolo`, `stato`, `creato`, `aggiornato`, `tag`; consigliato `sintesi` (una riga).
- Decisioni accettate: mai riscritte. Si crea una nuova con `--sostituisce N` e la vecchia diventa `superato`.
- Mai cancellare: archiviare in `90-archivio/`. Nomi file minuscoli con trattini. Link relativi.
- Mai segreti o dati sensibili.
