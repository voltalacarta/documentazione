---
titolo: Grafo della conoscenza automatico su tutte le repo
stato: accettato
creato: 2026-10-19
aggiornato: 2026-10-19
tag: [decisioni, second-brain, automazione, grafo, token-ai]
sintesi: "Un motore deterministico nel second brain collega tutte le repo, i documenti e i concetti, e mantiene indici compatti per spendere pochi token."
collegati: [0001, 0002, 0004, 0005]
---

# 0007 · Grafo della conoscenza automatico su tutte le repo

## Contesto

I progetti cresceranno molto, in più repo. Servono tre cose insieme:

1. **Tutto si aggiorna da solo:** indici, registro delle decisioni, collegamenti, grafo.
2. **Pochi token:** Claude non deve rileggere i file per orientarsi né riscrivere a mano indici e tabelle.
3. **Un grafo visibile** che colleghi repo, documenti, parole chiave e concetti, e che resti leggibile con migliaia di file.

## Decisione

### Regole

- **Tutto ciò che viene sancito in chat finisce in una repo GitHub.** Le decisioni vanno in `documentazione/10-decisioni/`. Un progetto nuovo ha una repo propria, creata dal [modello di progetto](../_modelli/repo-progetto/README.md).
- **Gli script fanno il lavoro ripetitivo, Claude scrive solo il contenuto nuovo.** Indici, registri, grafo e controlli sono generati da GitHub Actions con script deterministici, senza modelli AI.
- **Prima si cerca negli indici compatti, poi si apre un file.** Ogni repo ha la sua mappa a una riga per file (`INDICE.md`). Il second brain ha la mappa di tutte (`_grafo/indice.jsonl`).

### Componenti

| Dove | Cosa | Quando gira |
| --- | --- | --- |
| `documentazione/strumenti/indici.py` | Indici di sezione, registro decisioni, `INDICE.md` | Action *Aggiorna gli indici*, a ogni push |
| `documentazione/strumenti/controlla.py` | Controllo di frontmatter, stati, date, numeri delle decisioni | Action *Controlli*, a ogni push e PR |
| `documentazione/strumenti/nuova-decisione.py` | Nuova decisione con il numero giusto, già compilata nei metadati | A mano o da Claude |
| `second-brain/.github/kg/` | Il **motore del grafo**: legge tutte le repo, estrae concetti e link, genera le viste | Action *Aggiorna il grafo*, ogni 3 ore, a ogni push e su avviso |

### Come il motore costruisce il grafo (zero token)

- **Scoperta:** tutte le repo del proprietario, via API GitHub. Le private richiedono il segreto `KG_TOKEN`.
- **Lettura incrementale:** clone superficiale e sparso dei soli file `.md`; una repo il cui commit non è cambiato non si riscarica.
- **Nodi:** repo, documenti, note del second brain, concetti.
- **Concetti:** da tag e campi del frontmatter (`tag`, `tags`, `concetti`, `owasp`, `asvs`), dal [vocabolario controllato](https://github.com/voltalacarta/second-brain/blob/main/_config/vocabolario.yml) cercato nel testo di tutte le repo, dalle voci dei glossari e dai `[[wikilink]]` alle note non ancora create.
- **Archi:** link tra file (anche tra repo diverse), decisioni `collegati`, tag, menzioni.
- **Viste:** `grafo.md` (diagramma Mermaid su GitHub), una pagina per repo e per concetto, note-ponte per Foam e Obsidian, grafo interattivo nel Codespace, indice compatto, manutenzione, parole chiave suggerite.
- **Scalabilità:** ogni diagramma ha un tetto di elementi; il dettaglio completo sta negli indici. I nomi delle pagine restano stabili nel tempo e si scrivono solo i file cambiati.

## Alternative considerate

| Alternativa | Perché scartata |
| --- | --- |
| Far aggiornare indici e collegamenti a Claude | Costa token a ogni modifica, ed è soggetto a dimenticanze |
| Estrarre i concetti con un modello AI nell'Action | Costo ricorrente e risultati non ripetibili |
| Obsidian Publish o GitHub Pages per il grafo | A pagamento, oppure note private rese pubbliche |
| Una repo per ogni decisione | Disperde le decisioni; un registro unico è più facile da consultare |

## Conseguenze

- ✅ Nessun lavoro manuale per indici, registro e grafo; nessun costo in token né in denaro.
- ✅ Claude si orienta leggendo poche righe di indice invece dei file.
- ✅ Una repo nuova compare nel grafo da sola, entro 3 ore.
- ⚠️ Le repo private entrano nel grafo solo dopo aver configurato `KG_TOKEN` (vedi [collegare le repo al grafo](../40-procedure/collegare-le-repo-al-grafo.md)).
- ⚠️ La qualità dei concetti dipende dal vocabolario: va arricchito ogni tanto, partendo dai suggerimenti generati.

## Dettagli

- [Second brain](../30-conoscenza/second-brain.md)
- [Collegare le repo al grafo](../40-procedure/collegare-le-repo-al-grafo.md)
- [Aggiornare la documentazione](../40-procedure/aggiornare-la-documentazione.md)
