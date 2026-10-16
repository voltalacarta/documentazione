---
titolo: Knowledge base di sicurezza web come riferimento per i progetti digitali
stato: proposto
creato: 2026-10-16
aggiornato: 2026-10-16
tag: [decisioni, sicurezza, sicurezza-web, progetti]
collegati: [0002]
---

# 0006 · Knowledge base di sicurezza web come riferimento per i progetti digitali

## Contesto

Sono previsti progetti digitali (siti, applicazioni), non ancora definiti. Serve un riferimento unico sulle pratiche di sicurezza del 2026, da usare fin dalla progettazione e nei rapporti con agenzie e fornitori. Il documento [Sicurezza](../20-infrastruttura/sicurezza.md) copre solo l'ambiente di lavoro interno.

## Decisione

1. La sezione [`25-sicurezza-web/`](../25-sicurezza-web/README.md) è il **riferimento** per la sicurezza di ogni progetto digitale.
2. Ogni nuovo progetto parte dalla classificazione in [profili di progetto](../25-sicurezza-web/16-progetti/profili-di-progetto.md): il profilo stabilisce il livello OWASP ASVS 5.0 e i controlli obbligatori.
3. Se il progetto è affidato a terzi, il contratto include i [requisiti di sicurezza per capitolati](../25-sicurezza-web/16-progetti/requisiti-capitolato.md), dopo revisione legale.
4. Nessun sito va online senza la [checklist pre-lancio](../25-sicurezza-web/checklist/pre-lancio.md) completata nelle voci obbligatorie.
5. La sezione si mantiene aggiornata con il ciclo descritto in [contribuire](../25-sicurezza-web/contribuire.md). Un controllo automatico mensile segnala le revisioni scadute.

## Alternative considerate

| Alternativa | Perché scartata |
| --- | --- |
| Decidere caso per caso, progetto per progetto | Requisiti incoerenti e difficili da verificare |
| Affidarsi solo alle agenzie | Ciò che non è scritto nel contratto non è dovuto |
| Adottare direttamente OWASP ASVS senza adattamenti | Standard completo ma troppo esteso da usare senza una guida |

## Conseguenze

- ✅ Requisiti uguali e verificabili per tutti i progetti.
- ✅ Contratti con fornitori più forti, con un collaudo di sicurezza definito.
- ⚠️ La sezione va mantenuta: le parti su normativa e strumenti invecchiano in pochi mesi.
- ⚠️ Le parti legali (capitolato, piano incidenti, divulgazione) richiedono una revisione legale prima dell'uso.

## Dettagli

- [Sezione Sicurezza web](../25-sicurezza-web/README.md)
- [Profili di progetto](../25-sicurezza-web/16-progetti/profili-di-progetto.md)
- [Checklist pre-lancio](../25-sicurezza-web/checklist/pre-lancio.md)
