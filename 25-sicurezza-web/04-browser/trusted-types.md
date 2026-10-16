---
titolo: Trusted Types
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, browser]
prossima_revisione: 2027-04-15
owasp: [A05:2025]
asvs: [V3]
---

# Trusted Types

> **In sintesi.** Trusted Types rende il codice JavaScript sicuro per default contro la DOM XSS: i sink pericolosi (`innerHTML`, `eval`, `script.src`…) smettono di accettare stringhe e accettano solo oggetti creati da una *policy* che hai revisionato.

## Attivazione

```http
Content-Security-Policy: require-trusted-types-for 'script'; trusted-types app-sanitizer
```

`trusted-types` limita i nomi delle policy che il codice può creare.

## Esempio di policy

```js
const policy = trustedTypes.createPolicy('app-sanitizer', {
  createHTML: (input) => DOMPurify.sanitize(input, { RETURN_TRUSTED_TYPE: false }),
});

el.innerHTML = policy.createHTML(userContent); // accettato
el.innerHTML = userContent;                    // bloccato dal browser
```

## Percorso di adozione

1. 🟢 Avvia in **report-only** (`Content-Security-Policy-Report-Only`) per inventariare tutte le violazioni.
2. 🟢 Sostituisci le assegnazioni dirette con API sicure (`textContent`, `setAttribute` su attributi innocui) o con una policy unica e centralizzata.
3. 🟢 Verifica la compatibilità delle librerie di terze parti; molte (Angular, Lit, DOMPurify) supportano Trusted Types nativamente.
4. 🟢 Passa in enforce.

## Note

- È raccomandato da web.dev per i siti che trattano dati sensibili, insieme alla CSP.
- **Supporto (verificato il 2026-10-15):** Chrome ed Edge dalla versione 83 (2020), Safari dalla 26 (settembre 2025), Firefox da febbraio 2026. Con l'arrivo di Firefox, Trusted Types è diventato **Baseline** a febbraio 2026: oggi protegge su tutti i browser principali. Su browser più vecchi l'header viene ignorato senza rompere nulla.
- Conseguenza pratica: da opzione "avanzata" è diventata una misura realisticamente adottabile per ogni sito con dati sensibili.

## Fonti

- [WEBDEV-HEADERS], [URIPORTS-TT], [ALERT-HEADERS] — vedi [fonti.md](../fonti.md)
