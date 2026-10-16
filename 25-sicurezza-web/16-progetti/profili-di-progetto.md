---
titolo: Profili di progetto — requisiti in base al tipo
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, progetti]
prossima_revisione: 2027-04-15
owasp: [A06:2025]
asvs: [L1, L2, L3]
---

# Profili di progetto

> **In sintesi.** Quando nasce un nuovo progetto digitale, rispondi alle domande di classificazione: il profilo che ne esce dice quale livello ASVS adottare, quali controlli sono obbligatori e quali norme verificare. Serve a non sotto-proteggere un e-commerce né a sovraccaricare un sito vetrina.

## 1. Domande di classificazione

| # | Domanda | Sì → |
|---|---|---|
| 1 | Gli utenti creano un account o fanno login? | almeno profilo **B** |
| 2 | Si raccolgono dati personali oltre a un form di contatto (indirizzi, ordini, profili)? | almeno **B** |
| 3 | Si vendono prodotti o si incassano pagamenti? | almeno **C** |
| 4 | Si trattano dati particolari (salute, minori, opinioni) o documenti d'identità? | **D** |
| 5 | Ci sono contenuti generati dagli utenti (commenti, upload, recensioni)? | aggiungi modulo **UGC** |
| 6 | C'è un'API usata da app o terze parti? | aggiungi modulo **API** |
| 7 | C'è un chatbot, una ricerca AI o un agente? | aggiungi modulo **AI** |
| 8 | Si distribuisce software (app, plugin, libreria) a terzi? | aggiungi modulo **Prodotto (CRA)** |
| 9 | L'organizzazione è soggetto NIS2? | aggiungi modulo **NIS2** |

## 2. Profili di base

| | **A — Vetrina** | **B — Area utenti** | **C — E-commerce** | **D — Dati sensibili** |
|---|---|---|---|---|
| Esempi | Sito istituzionale, catalogo, blog, landing | Newsletter con profilo, area riservata, community | Negozio online, prenotazioni a pagamento | Sanità, formazione minori, documenti |
| Livello ASVS 5.0 | L1 | L2 | L2 | L2 pieno + parti L3 |
| Architettura consigliata | **Statica** o CMS headless | CMS/framework con auth standard | Piattaforma e-commerce o PSP esterno | Framework con auth dedicata, isolamento dati |
| Autenticazione | Solo admin, MFA | Passkey + password NIST, MFA admin | come B + step-up su dati di pagamento | Passkey/MFA per tutti |
| Pagamenti | — | — | **Solo via PSP** (redirect o campi ospitati), mai dati carta sul server | — |
| Header/CSP | Set comune | Set comune + CSP strict | CSP strict **obbligatoria** sul checkout | CSP strict + Trusted Types |
| Pen test | Facoltativo | Prima del lancio | Prima del lancio + annuale | Prima del lancio + annuale + a ogni rilascio rilevante |
| Backup | Settimanale | Giornaliero | Giornaliero + immutabile | Continuo + immutabile, cifrato |
| Log | Accessi admin | Eventi di autenticazione | + ordini e pagamenti | Audit completo |
| GDPR | Informativa, cookie | + registro, DPA fornitori | + conservazione dati ordini | + DPIA (art. 35) |

## 3. Moduli aggiuntivi

| Modulo | Requisiti chiave | File |
|---|---|---|
| **UGC** | Sanitizzazione HTML, upload sicuri su dominio separato, moderazione, anti-spam | [upload-file](../03-input-e-output/upload-file.md), [xss](../03-input-e-output/xss.md) |
| **API** | OWASP API Top 10, schema OpenAPI validato, rate limit, inventario | [owasp-api-top10](../07-api/owasp-api-top10.md) |
| **AI** | OWASP LLM Top 10, output non fidato, RAG con permessi, limiti di costo | [owasp-llm-top10](../08-ai-llm/owasp-llm-top10.md) |
| **Prodotto (CRA)** | Processo di segnalazione 24 h, SBOM, VDP, aggiornamenti firmati | [cyber-resilience-act](../12-normativa-ue/cyber-resilience-act.md) |
| **NIS2** | Misure ACN di base, notifica incidenti, governance documentata | [nis2-italia](../12-normativa-ue/nis2-italia.md) |

## 4. Scelte architetturali che riducono il rischio

- **Il codice che non scrivi non ha bug tuoi.** Per login, pagamenti, newsletter e moduli preferisci servizi maturi (identity provider, PSP, piattaforme) a soluzioni artigianali, verificandoli con il [questionario fornitori](../15-modelli/questionario-fornitori.md).
- **Statico quando possibile.** Un sito generato staticamente (Astro, Hugo, Eleventy, Next.js export) non ha database né pannello esposto: per il profilo A è la scelta più sicura ed economica.
- **Separa il pubblico dall'amministrazione.** Pannello di gestione su dominio separato e protetto (VPN, accesso zero trust, IP allowlist).
- **Proprietà degli asset.** Domini, hosting e account intestati all'organizzazione fin dal primo giorno.

## 5. Scheda di progetto (da compilare)

```markdown
Progetto: [NOME]           Data: [DATA]          Responsabile: [NOME]
Profilo base: [A/B/C/D]    Moduli: [UGC, API, AI, CRA, NIS2]
Livello ASVS: [L1/L2/L3]
Dati trattati: [...]
Fornitori coinvolti: [...] → questionario inviato il [DATA]
Threat model: [link]       Pen test previsto: [DATA]
Decisioni di sicurezza e rischi accettati:
- [...]
```
