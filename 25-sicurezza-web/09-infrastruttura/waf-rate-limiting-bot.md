---
titolo: WAF, rate limiting, bot e DDoS
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, infrastruttura]
prossima_revisione: 2027-04-15
owasp: [A07:2025, A02:2025]
---

# WAF, rate limiting, bot e DDoS

> **In sintesi.** Sono controlli **perimetrali** che riducono il rumore e comprano tempo. Non correggono le vulnerabilità del codice: sono un livello in più della difesa in profondità.

## WAF

- 🟠 WAF gestito davanti al sito (Cloudflare, AWS WAF, Fastly, Akamai, Azure Front Door) o ModSecurity/Coraza con **OWASP Core Rule Set**.
- 🟠 Parti in modalità *log/monitor*, analizza i falsi positivi, poi passa in blocco.
- 🟠 Usa il WAF per *virtual patching* in attesa della correzione reale di una CVE.
- ❌ Non disattivare controlli applicativi "perché tanto c'è il WAF".

## Rate limiting

| Endpoint | Limite indicativo |
|---|---|
| Login, verifica OTP | pochi tentativi/minuto per account **e** per IP, con blocco progressivo |
| Reset password, registrazione | pochi/ora per IP ed email |
| API pubbliche | quota per chiave/utente |
| Ricerca, export, generazione PDF/AI | limite di costo, non solo di numero |

- 🔴 Applica i limiti anche lato applicazione (non solo al CDN), con risposta `429` e `Retry-After`.
- 🟠 Algoritmi token bucket o sliding window su archivio condiviso (Redis) se hai più istanze.

## Bot e abuso dei flussi

- 🟠 Protezione da credential stuffing, scraping, scalping, creazione massiva di account.
- 🟠 CAPTCHA a basso attrito o challenge invisibili (Cloudflare Turnstile, hCaptcha, reCAPTCHA) solo dove serve, valutandone l'impatto su accessibilità e privacy.
- 🟢 Segnali comportamentali e reputazione IP per i flussi critici (checkout, prenotazioni).

## DDoS

- 🟠 CDN/anti-DDoS di livello 3/4 e 7 davanti all'origine.
- 🟠 **Nascondi l'IP dell'origine** e accetta traffico solo dal CDN (allowlist IP o tunnel tipo Cloudflare Tunnel).
- 🟠 Cache aggressiva per i contenuti pubblici; autoscaling con limiti di spesa.

## Fonti

- [OLIGO-BP], [RADWARE-21BP], [A10-WEBSEC] — vedi [fonti.md](../fonti.md)
