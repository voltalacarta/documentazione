---
titolo: Cross-Site Scripting (XSS)
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, input-e-output]
prossima_revisione: 2027-04-15
owasp: [A05:2025]
asvs: [V1, V3]
---

# Cross-Site Scripting (XSS)

> **In sintesi.** Tre livelli di difesa che si sommano: **encoding contestuale** dell'output, **CSP strict** che impedisce l'esecuzione di script non autorizzati, **Trusted Types** che blocca i sink DOM pericolosi.

## Tipi

- **Riflessa**: l'input torna nella risposta (`?q=<script>`).
- **Memorizzata**: l'input viene salvato e mostrato ad altri (commenti, profili).
- **DOM-based**: il JavaScript del client inserisce dati non fidati in sink come `innerHTML`, `document.write`, `location`, `eval`.

## Pratiche

### 🔴 Obbligatorio

- Usa template ed framework con **escape automatico** (React, Vue, Angular, Twig, Jinja2 con autoescape, Blade). Evita le vie di fuga: `dangerouslySetInnerHTML`, `v-html`, `|safe`, `{!! !!}`, `[innerHTML]`.
- **Encoding per contesto**: HTML body, attributo, URL, JavaScript, CSS richiedono encoding diversi.
- Se devi accettare HTML (editor rich text), sanitizzalo con **DOMPurify** (client) o equivalenti server (es. `nh3`/`bleach` in Python, HTML Purifier in PHP). Mantieni la libreria aggiornata.
- Valida gli URL inseriti dall'utente: solo `https:` / `http:` / `mailto:`, mai `javascript:` o `data:`.
- Cookie di sessione `HttpOnly` (vedi [sessioni-e-cookie](../01-autenticazione/sessioni-e-cookie.md)).

### 🟠 Raccomandato

- **CSP strict** con nonce o hash: vedi [content-security-policy](../04-browser/content-security-policy.md).
- `X-Content-Type-Options: nosniff` e `Content-Type` corretto su ogni risposta.
- Upload serviti da un dominio separato (vedi [upload-file](upload-file.md)).

### 🟢 Avanzato

- **Trusted Types** per eliminare la DOM XSS: vedi [trusted-types](../04-browser/trusted-types.md). Dal febbraio 2026 è supportato da tutti i browser principali, quindi per siti con dati sensibili va considerato 🟠 raccomandato.
- **Sanitizer API** nativa (`element.setHTML(input)`): inserisce HTML rimuovendo per default ciò che può eseguire script. Disponibile in Firefox 148 (febbraio 2026) e Chrome/Edge 146 (marzo 2026); **non ancora in Safari**. Usala con un fallback (DOMPurify) finché non è supportata ovunque. Attenzione a non confonderla con `setHTMLUnsafe()`, che **non** sanitizza.

## Output generato da AI

L'output di un LLM va trattato come input utente non fidato: un modello manipolato può generare markup o link malevoli. Vedi [owasp-llm-top10](../08-ai-llm/owasp-llm-top10.md) (LLM05).

## Fonti

- [WEBDEV-HEADERS], [OWASP-T10], [LILTING-SETHTML] — vedi [fonti.md](../fonti.md)
