---
titolo: OWASP Top 10 for LLM Applications 2025
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, ai-llm]
prossima_revisione: 2027-01-15
---

# OWASP Top 10 for LLM Applications 2025

> **In sintesi.** Se il sito integra un chatbot, una ricerca semantica, un assistente o un agente, ai rischi web classici si aggiungono quelli specifici dei modelli linguistici. La lista è mantenuta dall'OWASP GenAI Security Project. La regola di fondo: **il modello non è un confine di sicurezza**.

## La lista

| # | Rischio | In pratica |
|---|---|---|
| LLM01 | **Prompt Injection** | Istruzioni malevole dirette (jailbreak) o **indirette**, nascoste in pagine, email, documenti che il modello legge |
| LLM02 | Sensitive Information Disclosure | Il modello rivela dati personali, segreti o documenti di altri utenti |
| LLM03 | Supply Chain | Modelli, dataset, plugin o librerie compromessi |
| LLM04 | Data and Model Poisoning | Dati di training, fine-tuning o embedding manipolati |
| LLM05 | Improper Output Handling | Output del modello usato senza validazione → XSS, SQLi, esecuzione di comandi |
| LLM06 | Excessive Agency | L'agente ha strumenti o permessi più ampi del necessario → vedi [agenti-e-strumenti](agenti-e-strumenti.md) |
| LLM07 | System Prompt Leakage | Il system prompt viene estratto: non deve contenere segreti né regole di sicurezza |
| LLM08 | Vector and Embedding Weaknesses | RAG che restituisce documenti a utenti non autorizzati, embedding avvelenati |
| LLM09 | Misinformation | Risposte false presentate come affidabili |
| LLM10 | Unbounded Consumption | Abuso dei costi e negazione del servizio tramite richieste costose |

Novità 2025 rispetto alla 2023/24: aggiunte *System Prompt Leakage* e *Vector and Embedding Weaknesses*; il poisoning è stato esteso a fine-tuning ed embedding. La prompt injection resta al primo posto.

## Un caso reale

**EchoLeak** (CVE-2025-32711): una injection indiretta *zero-click* in Microsoft 365 Copilot permetteva di esfiltrare contenuti interni con una singola email costruita ad arte. È l'esempio tipico di LLM01 + LLM02 + LLM06 insieme.

## Pratiche

### 🔴 Obbligatorio

- Tratta **ogni input** del modello (utente, pagine web, file, risultati RAG, output di strumenti) come non fidato.
- Tratta **ogni output** del modello come input utente: encoding prima di mostrarlo in HTML, mai passarlo direttamente a SQL, shell, `eval`.
- **Autorizzazione fuori dal modello**: il RAG filtra i documenti per permessi dell'utente *prima* di passarli al modello.
- Nessun segreto nel system prompt; le chiavi API restano lato server.
- Limiti di token, frequenza e budget per utente (LLM10).

### 🟠 Raccomandato

- Blocca il rendering automatico di immagini/link markdown nelle risposte, o limitalo a domini fidati: è un canale classico di esfiltrazione.
- Guardrail di input/output (classificatori di injection, filtri PII) come difesa aggiuntiva, non come unica difesa.
- Log delle conversazioni con attenzione a privacy e conservazione (vedi [gdpr](../12-normativa-ue/gdpr.md)).
- Red teaming periodico (es. strumenti open source come Promptfoo, garak).

### 🟢 Avanzato

- Separazione dei contesti (pattern *dual LLM* / *CaMeL*): il modello che legge dati non fidati non può invocare strumenti privilegiati.
- Allineamento con OWASP **AISVS** quando sarà stabile e con gli obblighi dell'**AI Act** se applicabili.

## Fonti

- [OPENSRC-LLM], [INDUSFACE-LLM], [CORALOGIX-LLM], [PREAMBLE-LLM], [GUPTA-LLM01] — vedi [fonti.md](../fonti.md)
