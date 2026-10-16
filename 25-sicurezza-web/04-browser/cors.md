---
titolo: CORS (Cross-Origin Resource Sharing)
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, browser]
prossima_revisione: 2027-04-15
owasp: [A02:2025, A01:2025]
asvs: [V3, V4]
---

# CORS

> **In sintesi.** CORS non è una protezione: è un **allentamento** controllato della Same-Origin Policy. Ogni origine aggiunta è un sito a cui permetti di leggere le risposte delle tue API.

## Pratiche

### 🔴 Obbligatorio

- Se l'API è usata solo dal tuo sito sulla stessa origine, **non abilitare CORS**.
- **Allowlist esplicita** di origini, confrontate per uguaglianza esatta.
- **Mai riflettere** l'header `Origin` ricevuto in `Access-Control-Allow-Origin` senza confronto con l'allowlist.
- Mai `Access-Control-Allow-Origin: *` insieme a credenziali (i browser lo rifiutano, ma configurazioni che riflettono l'origine aggirano il limite).
- Non accettare l'origine `null` (inviata da iframe sandbox e file locali).

### 🟠 Raccomandato

- `Access-Control-Allow-Credentials: true` solo dove indispensabile.
- Limita metodi e header ammessi (`Access-Control-Allow-Methods`, `-Headers`).
- `Vary: Origin` sulle risposte, per non avvelenare le cache.
- `Access-Control-Max-Age` moderato (es. 600 s).

## Errori comuni

```text
❌ origin.endsWith("example.com")   → accetta "evilexample.com"
❌ origin.includes("example.com")   → accetta "example.com.attacker.net"
✅ ALLOWED.has(origin)              → Set di origini complete, con schema
```

## Fonti

- [AZION-HEADERS] — vedi [fonti.md](../fonti.md)
