# Documentazione — Volta la carta

Questa è la **fonte unica di verità** della documentazione generale.
Tutto ciò che viene deciso, stabilito o standardizzato finisce qui, come file Markdown (`.md`), versionato con Git.

> **Regola d'oro:** se non è scritto qui, non è stato deciso.

## Mappa

| Sezione | Contenuto | Quando usarla |
| --- | --- | --- |
| [`00-meta/`](00-meta/README.md) | Regole di questo repository: convenzioni, struttura, glossario | Prima di scrivere qualcosa di nuovo |
| [`10-decisioni/`](10-decisioni/README.md) | Registro delle decisioni (una decisione = un file) | Quando si "sancisce" qualcosa |
| [`20-infrastruttura/`](20-infrastruttura/README.md) | Ambiente di lavoro: GitHub, ambiente cloud, sicurezza | Per sapere *com'è fatto* il sistema |
| [`25-sicurezza-web/`](25-sicurezza-web/README.md) | Sicurezza di siti e progetti digitali: best practice, configurazioni, modelli, normativa | Per progettare, commissionare o verificare un sito |
| [`30-conoscenza/`](30-conoscenza/README.md) | Second brain e gestione della conoscenza | Per sapere *come si organizzano* note e appunti |
| [`40-procedure/`](40-procedure/README.md) | Procedure operative passo-passo | Per sapere *come si fa* una cosa |
| [`50-progetti/`](50-progetti/README.md) | Schede dei progetti | Per lo stato di un'iniziativa |
| [`90-archivio/`](90-archivio/README.md) | Documenti superati o chiusi | Mai cancellare: si archivia |
| [`_modelli/`](_modelli/README.md) | Modelli pronti da copiare | Per creare un nuovo documento |

## Come contribuire in 30 secondi

1. Scegli la sezione giusta (vedi tabella sopra).
2. Copia il modello adatto da [`_modelli/`](_modelli/README.md). Per una decisione: `python3 strumenti/nuova-decisione.py "Titolo"`.
3. Compila l'intestazione (frontmatter, con una `sintesi` di una riga) e scrivi il contenuto.
4. Fai commit con un messaggio chiaro (vedi [convenzioni](00-meta/convenzioni.md#messaggi-di-commit)) e push.

**Indici, registro delle decisioni e [`INDICE.md`](INDICE.md) si aggiornano da soli**, e il documento compare nel grafo del second brain. Ogni progetto nuovo ha una repo propria: vedi [nuovo progetto](40-procedure/nuovo-progetto.md).

Le regole complete sono in [`00-meta/convenzioni.md`](00-meta/convenzioni.md).

## Decisioni in vigore

Le decisioni sono elencate in [`10-decisioni/README.md`](10-decisioni/README.md).
