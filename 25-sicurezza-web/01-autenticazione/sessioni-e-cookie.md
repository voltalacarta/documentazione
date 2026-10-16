---
titolo: Sessioni, cookie e token
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, autenticazione]
prossima_revisione: 2027-04-15
owasp: [A07:2025, A01:2025]
asvs: [V7, V9]
---

# Sessioni, cookie e token

> **In sintesi.** Una sessione rubata vale quanto una password rubata, e aggira anche la MFA. I cookie devono avere tutti gli attributi di sicurezza, le sessioni devono scadere e ruotare.

## Cookie di sessione

```http
Set-Cookie: __Host-session=<id-casuale>; Path=/; Secure; HttpOnly; SameSite=Lax; Max-Age=28800
```

| Attributo | Scopo | Livello |
|---|---|---|
| `Secure` | Solo su HTTPS | 🔴 |
| `HttpOnly` | Non leggibile da JavaScript (limita i danni di una XSS) | 🔴 |
| `SameSite=Lax` (o `Strict`) | Mitigazione CSRF | 🔴 |
| Prefisso `__Host-` | Impone `Secure`, `Path=/` e nessun `Domain`: impedisce che sottodomini sovrascrivano il cookie | 🟠 |
| `Max-Age` / `Expires` | Durata limitata | 🔴 |

## Gestione della sessione

- 🔴 ID di sessione casuale crittograficamente sicuro (≥ 128 bit di entropia), generato dal framework.
- 🔴 **Rigenera l'ID** al login, al cambio di privilegi e al logout (contro *session fixation*).
- 🔴 Logout che invalida la sessione **lato server**, non solo il cookie.
- 🔴 Timeout di inattività (es. 15–30 min per aree sensibili) e timeout assoluto (es. 8–24 h).
- 🟠 Pagina "dispositivi connessi" con revoca delle singole sessioni.
- 🟠 Riautenticazione (step-up) per azioni critiche: cambio email, password, MFA, dati di pagamento.
- 🟢 **Device Bound Session Credentials (DBSC)**: la sessione è legata a una chiave conservata nel chip di sicurezza del dispositivo, quindi un cookie rubato non funziona su un'altra macchina. Stato a ottobre 2026: Chrome lo ha rilasciato ad aprile 2026 ed è generalmente disponibile **solo su Windows** (rollout da maggio 2026); gli altri browser non lo supportano ancora. Va usato come protezione **aggiuntiva**, non come unica difesa.

## JWT e token autocontenuti

Preferisci **sessioni server-side** per le applicazioni web tradizionali. Se usi JWT:

- 🔴 Imponi l'algoritmo atteso lato server; rifiuta `alg: none` e la confusione HS/RS.
- 🔴 Valida firma, `exp`, `nbf`, `iss`, `aud`.
- 🔴 Scadenza breve (5–15 min) per gli access token; refresh token ruotati e revocabili.
- 🔴 Non mettere dati sensibili nel payload: è solo codificato in Base64, non cifrato.
- 🟠 Non conservare token in `localStorage`: qualunque XSS li legge. Preferisci cookie `HttpOnly` o il pattern BFF (*Backend for Frontend*).

## Vedi anche

- [csrf](../03-input-e-output/csrf.md)
- [xss](../03-input-e-output/xss.md)

## Fonti

- [HNS-DBSC], [GWS-DBSC] — vedi [fonti.md](../fonti.md)
