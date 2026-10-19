---
titolo: Convenzioni di scrittura
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-19
tag: [meta, convenzioni]
sintesi: "Nomi dei file, intestazioni, stati, link, commit"
---

# Convenzioni di scrittura

## Formato

- Tutto è **Markdown** (`.md`), codifica UTF-8, a capo Unix (LF).
- Un documento tratta **un solo argomento**. Se cresce troppo, si divide in più file in una sottocartella.
- Lingua: **italiano**. I termini tecnici restano in inglese quando è l'uso comune (commit, branch, repository).

## Nomi di file e cartelle

- Solo minuscole, numeri e trattini: `ambiente-cloud.md`, non `Ambiente Cloud.md`.
- Niente accenti, spazi o caratteri speciali nei nomi (restano nel contenuto).
- Le cartelle di primo livello hanno un prefisso numerico a decine (`10-`, `20-`…): vedi [struttura](struttura.md).
- Le decisioni sono numerate in sequenza a 4 cifre: `0001-titolo-breve.md`.
- Ogni cartella ha un `README.md` che fa da indice.

## Intestazione (frontmatter)

Ogni documento inizia con questo blocco:

```yaml
---
titolo: Titolo leggibile del documento
stato: bozza          # vedi tabella stati
creato: AAAA-MM-GG
aggiornato: AAAA-MM-GG
tag: [parola, altra-parola]
sintesi: Una riga che dice di cosa parla il documento.
---
```

- **`sintesi`** (consigliato): una frase, al massimo 200 caratteri. Compare negli indici, in `INDICE.md` e nel grafo. Se manca, viene presa in automatico la prima frase del documento.
- Facoltativi: `responsabile`, `sostituisce`, `sostituito-da`, `collegati` (numeri di decisioni), `concetti` (parole chiave in più per il grafo), `prossima_revisione`.

Il controllo automatico (`strumenti/controlla.py`) verifica campi, stati e date a ogni push.

### Stati

| Stato | Significato |
| --- | --- |
| `bozza` | In lavorazione, non ancora valido |
| `proposto` | Pronto per essere approvato (usato soprattutto per le decisioni) |
| `attivo` / `accettato` | In vigore. `accettato` si usa per le decisioni, `attivo` per gli altri documenti |
| `superato` | Sostituito da un altro documento (indicare `sostituito-da`) |
| `archiviato` | Non più rilevante; spostato in `90-archivio/` |

## Parti generate automaticamente

Non vanno modificate a mano: vengono riscritte a ogni push.

| Cosa | Generato da |
| --- | --- |
| Tabelle tra `<!-- indice:inizio -->` e `<!-- indice:fine -->` nei `README.md` | `strumenti/indici.py` |
| Registro in `10-decisioni/README.md` (marcatore `indice:inizio decisioni`) | `strumenti/indici.py` |
| `INDICE.md`, mappa compatta di tutti i documenti | `strumenti/indici.py` |

Per far indicizzare una cartella nuova basta mettere i due marcatori nel suo `README.md`.

## Link

- Link **relativi** tra documenti: `[Codespaces](../20-infrastruttura/ambiente-cloud.md)`.
- Mai link a file sul computer locale.
- Quando si sposta o rinomina un file, si aggiornano i link che puntano a esso (il controllo automatico segnala quelli rotti).

## Stile

- Frasi brevi, una idea per paragrafo.
- Titolo `#` uno solo per file; poi `##` e `###`.
- Tabelle per confronti, elenchi per passi e opzioni.
- Date sempre in formato ISO: `2026-10-15`.

## Messaggi di commit

Formato: `tipo(sezione): descrizione breve`

| Tipo | Uso |
| --- | --- |
| `docs` | Nuovo contenuto o modifica sostanziale |
| `decisione` | Nuova decisione o cambio di stato di una decisione |
| `fix` | Correzioni (refusi, link rotti) |
| `struttura` | Spostamenti, rinomine, nuove cartelle |
| `chore` | Configurazione del repository |

Esempio: `decisione(10): 0004 adottare il modello PARA per le note`

## Cosa NON va qui

- Password, token, chiavi API, IBAN, dati personali sensibili → password manager.
- File pesanti (video, grandi PDF, immagini non compresse) → archivio esterno, qui solo il link.
- Bozze personali e appunti grezzi → second brain (vedi [conoscenza](../30-conoscenza/README.md)).
