---
titolo: Server-Side Request Forgery (SSRF)
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, autorizzazione]
prossima_revisione: 2027-04-15
owasp: [A01:2025]
---

# Server-Side Request Forgery (SSRF)

> **In sintesi.** Quando il server scarica un URL fornito dall'utente (anteprime link, webhook, import da URL, generazione PDF, agenti AI che navigano), un attaccante può fargli raggiungere risorse interne. Nel 2025 OWASP l'ha accorpata al Broken Access Control: è di fatto un aggiramento dei confini di accesso.

## Bersagli tipici

- Metadata dei cloud: `http://169.254.169.254/` (credenziali IAM).
- Servizi interni: `localhost:6379` (Redis), pannelli admin, database.
- Schemi alternativi: `file://`, `gopher://`, `dict://`.

## Pratiche

### 🔴 Obbligatorio

- Se possibile, **evita** di accettare URL arbitrari: usa ID di risorse note o un'allowlist di domini.
- Accetta solo `https` (ed eventualmente `http`), mai altri schemi.
- **Risolvi il DNS e verifica l'IP** prima della connessione; blocca intervalli privati, loopback, link-local, IPv6 equivalenti (`::1`, `fc00::/7`, `fe80::/10`) e IPv4 mappati in IPv6.
- Collegati **all'IP verificato**, non di nuovo al nome (contro il *DNS rebinding*).
- Non seguire i redirect, oppure rivalida ogni salto.
- Su AWS imponi **IMDSv2** (token obbligatorio); su GCP/Azure usa gli header richiesti dai metadata service.

### 🟠 Raccomandato

- Esegui le richieste in uscita da un servizio o proxy dedicato (egress proxy) senza accesso alla rete interna.
- Regole firewall di egress: il server web non deve poter aprire connessioni arbitrarie.
- Timeout brevi e limite di dimensione delle risposte.
- Non restituire all'utente la risposta grezza né gli errori di connessione dettagliati.

## Attenzione agli agenti AI

Un agente LLM con uno strumento "fetch URL" è un generatore di SSRF guidato da testo: applica le stesse regole e vedi [agenti-e-strumenti](../08-ai-llm/agenti-e-strumenti.md).

## Fonti

- [FASTLY-T10], [HCL-T10] — vedi [fonti.md](../fonti.md)
