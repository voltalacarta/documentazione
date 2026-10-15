---
titolo: Aggiornare la documentazione
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-15
tag: [procedure, documentazione]
collegati: [0001]
---

# Aggiornare la documentazione

## Scopo

Aggiungere o modificare un documento in questo repository mantenendo struttura e coerenza.

## Prerequisiti

- Accesso in scrittura al repository [`voltalacarta/documentazione`](https://github.com/voltalacarta/documentazione).
- Aver letto le [convenzioni](../00-meta/convenzioni.md).

## Tre modi per farlo

### A · Chiedere a Claude (il più semplice)

Basta descrivere cosa è stato deciso o cosa va documentato. Claude sceglie la sezione, usa il modello giusto, aggiorna gli indici e fa il commit.

### B · Dal browser con github.dev (modifiche rapide)

1. Apri il repository su GitHub e premi `.`.
2. Crea o modifica il file nella sezione giusta.
3. Aggiorna il `README.md` della sezione.
4. Nel pannello *Source Control* scrivi il messaggio di commit e conferma.

### C · Con un Codespace (lavori più grandi)

1. *Code* → *Codespaces* → *Create codespace on main*.
2. Lavora sui file; l'estensione markdownlint segnala gli errori di formato.
3. Commit e push dal pannello *Source Control*.

## Passi comuni

1. **Scegli la sezione** (vedi la mappa nel [README](../README.md)).
2. **Copia il modello** da [`_modelli/`](../_modelli/README.md).
3. **Compila il frontmatter**: titolo, stato, date, tag.
4. **Scrivi il contenuto** seguendo lo [stile](../00-meta/convenzioni.md#stile).
5. **Aggiorna l'indice** della sezione (il suo `README.md`).
6. **Se è una decisione**, aggiungila anche alla tabella in [`10-decisioni/README.md`](../10-decisioni/README.md).
7. **Commit** con il [formato previsto](../00-meta/convenzioni.md#messaggi-di-commit).

## Verifica

Dopo il push, la scheda *Actions* del repository mostra l'esito dei controlli automatici (formato Markdown e link). Se un controllo fallisce, il dettaglio indica file e riga da correggere.
