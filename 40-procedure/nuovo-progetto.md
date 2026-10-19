---
titolo: Nuovo progetto
stato: attivo
creato: 2026-10-19
aggiornato: 2026-10-19
tag: [procedure, progetti, github]
sintesi: "Creare la repo di un progetto nuovo con la struttura standard: decisioni, indici automatici, controlli e collegamento al grafo."
collegati: [0002, 0007]
---

# Nuovo progetto

## Scopo

Ogni progetto ha **una repo propria**, con la stessa struttura di tutte le altre. Così ciò che si decide per quel progetto ha un posto preciso, gli indici si aggiornano da soli e il progetto compare nel grafo del second brain.

## Passi

1. **Crea la repo vuota** su [github.com/new](https://github.com/new): nome in minuscolo con trattini, *Private* o *Public*, **senza** README né altri file.
2. **Chiedi a Claude:** *"Prepara la repo voltalacarta/nome-repo per il progetto X: …descrizione…"*. Claude la collega e lancia:

   ```bash
   python3 strumenti/nuovo-progetto.py ../nome-repo --nome "Nome del progetto" --descrizione "Una riga."
   ```

   La repo riceve: `README.md`, `CLAUDE.md`, `docs/` con il registro delle decisioni, gli strumenti, le Actions (controlli e indici), il Codespace.
3. **Registra il progetto** qui, con una scheda in `50-progetti/` dal [modello](../_modelli/progetto.md) che punti alla repo.
4. Se la repo è **privata**, controlla che esista il token `KG_TOKEN`: vedi [collegare le repo al grafo](collegare-le-repo-al-grafo.md).

## Cosa contiene la repo

| Percorso | A cosa serve |
| --- | --- |
| `README.md` | Cos'è il progetto e dove trovare cosa |
| `CLAUDE.md` | Regole brevi per Claude, pensate per spendere pochi token |
| `docs/` | Documenti del progetto; l'indice si aggiorna da solo |
| `docs/decisioni/` | Decisioni del progetto (`python3 strumenti/nuova-decisione.py "Titolo"`) |
| `INDICE.md` | Mappa compatta di tutti i file, generata |
| `.kg.yml` | Come la repo entra nel grafo |

## Decisioni: qui o nel progetto?

| La decisione riguarda… | Va in |
| --- | --- |
| Solo quel progetto (tecnologie, scelte di contenuto) | `docs/decisioni/` della repo del progetto |
| Tutta l'organizzazione (strumenti, metodi, regole) | `documentazione/10-decisioni/` |

## Verifica

Dopo il primo push, nella scheda **Actions** della repo nuova i controlli sono verdi; entro qualche ora la repo compare in [grafo.md](https://github.com/voltalacarta/second-brain/blob/main/grafo.md).
