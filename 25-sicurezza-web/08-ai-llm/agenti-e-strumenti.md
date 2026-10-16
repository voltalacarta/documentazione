---
titolo: Agenti AI, strumenti e MCP
stato: bozza
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, ai-llm]
prossima_revisione: 2027-01-15
---

# Agenti AI, strumenti e MCP

> **In sintesi.** Un agente che può navigare, leggere email o chiamare API è un utente privilegiato manovrabile da chiunque riesca a fargli leggere un testo. Progettalo come se l'attaccante controllasse il prompt.

## Il problema in una frase

Un agente che combina (1) accesso a dati privati, (2) esposizione a contenuti non fidati e (3) capacità di comunicare verso l'esterno può essere indotto a esfiltrare dati. Se le tre condizioni sono presenti insieme, il rischio è strutturale.

## Pratiche

### 🔴 Obbligatorio

- **Minimo privilegio per gli strumenti** (LLM06 *Excessive Agency*): ogni tool espone solo le operazioni indispensabili, con le credenziali dell'utente e non di un account di servizio onnipotente.
- **Conferma umana** per azioni irreversibili o con effetti esterni: pagamenti, invio email, cancellazioni, pubblicazioni.
- Gli strumenti che scaricano URL applicano le regole anti-[SSRF](../02-autorizzazione/ssrf.md).
- Parametri degli strumenti validati con schema, come qualunque API.

### 🟠 Raccomandato

- Allowlist di domini per la navigazione e per l'invio di dati in uscita.
- Separazione tra agenti/contesti che leggono contenuti esterni e quelli che hanno accesso a dati sensibili.
- **Server MCP** (Model Context Protocol): installa solo server da fonti verificate, fissane le versioni, verifica descrizioni e permessi degli strumenti (le descrizioni stesse possono contenere injection — *tool poisoning*), usa OAuth con scope minimi.
- Log di audit di ogni chiamata a strumento, con utente, parametri e risultato.

### 🟢 Avanzato

- Sandbox per l'esecuzione di codice generato (container effimeri, nessuna rete o rete filtrata).
- Rate limit e budget per sessione agentica.

> ⚠️ Area in rapida evoluzione: rivedere questo file ogni 3 mesi.

## Fonti

- [CORALOGIX-LLM], [GUPTA-LLM01], [PREAMBLE-LLM] — vedi [fonti.md](../fonti.md)
