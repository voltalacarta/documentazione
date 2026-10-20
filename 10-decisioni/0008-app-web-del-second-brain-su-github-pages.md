---
titolo: App web del second brain su GitHub Pages
stato: accettato
creato: 2026-10-20
aggiornato: 2026-10-20
tag: [decisioni, second-brain, github, sicurezza]
sintesi: Un'app statica in una repo pubblica legge e scrive il second brain privato con l'API di GitHub e un token personale; zero dipendenze, CSP rigida.
collegati: [0005, 0007]
---

# 0008 · App web del second brain su GitHub Pages

## Contesto

Il second brain si apriva con Codespaces o github.dev, che sono comodi al computer ma pesanti dal telefono, oppure con Obsidian più un plugin Git. Serviva un'interfaccia web sempre pronta per leggere, scrivere e navigare il grafo, gratuita e senza server. La repo `second-brain` è **privata**, e GitHub Pages pubblica pagine visibili a tutti, sul piano gratuito solo da repo pubbliche: le note non si possono pubblicare lì.

## Decisione

- L'app sta nella repo **pubblica** [`second-brain-app`](https://github.com/voltalacarta/second-brain-app) e contiene **solo codice**. È pubblicata su <https://voltalacarta.github.io/second-brain-app/> dall'Action *Test e pubblicazione*, che prima esegue test unitari e prove in Chromium contro un'API di GitHub simulata con dati inventati.
- I dati non passano mai da Pages. L'app legge e scrive `second-brain` con l'**API REST di GitHub**, usando un **token fine-grained** dell'utente: una sola repo, permesso *Contents* in lettura e scrittura. Il token resta nel browser e va solo a `api.github.com`.
- Ogni salvataggio è un **commit atomico** (`note: …`), anche quando sposta o archivia più file insieme. Il push fa partire l'Action *Aggiorna il grafo*, e l'app rilegge `grafo.json` e `indice.jsonl` appena il bot ha finito.
- **Zero dipendenze.** Il renderer Markdown è scritto apposta, applica l'escape a tutto e non lascia passare HTML grezzo né link `javascript:`. Una Content Security Policy permette solo script propri e connessioni verso `api.github.com`.
- Le regole del second brain valgono anche nell'app: `_grafo/`, `grafo.md` e `.github/` sono in sola lettura, e non si cancella niente, si archivia in `40-archivio/`.

## Alternative considerate

| Alternativa | Perché scartata |
| --- | --- |
| Pages direttamente da `second-brain` | Richiede un piano a pagamento, e le note sarebbero comunque pubbliche |
| Sito con login lato server (OAuth) | Serve un server da mantenere e da pagare |
| Obsidian Publish o servizi esterni | A pagamento, dati fuori da GitHub |
| Solo Codespaces o github.dev | Lenti dal telefono; Codespaces consuma ore di calcolo |
| Librerie da CDN (marked, DOMPurify, mermaid) | Codice di terzi accanto al token; con la CSP solo `'self'` si riduce la superficie d'attacco |

## Conseguenze

- ✅ Second brain leggibile e modificabile da qualunque browser e dal telefono, anche come app installata, senza costi e senza server.
- ✅ Tutto resta su GitHub: cronologia, permessi, Actions e grafo funzionano come prima.
- ⚠️ Il token fine-grained scade, al massimo dopo un anno (90 giorni consigliati), e va rinnovato. Procedura: [Usare il second brain](../40-procedure/usare-il-second-brain.md#app-web-consigliata).
- ⚠️ I diagrammi Mermaid si vedono come codice nell'app; il disegno resta su GitHub.
- ⚠️ Prima di ogni modifica all'app: `npm test && npm run build && npm run e2e`. Mai dati veri nei test della repo pubblica.
