---
titolo: Cross-Site Request Forgery (CSRF)
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, input-e-output]
prossima_revisione: 2027-04-15
owasp: [A01:2025, A08:2025]
asvs: [V3, V7]
---

# Cross-Site Request Forgery (CSRF)

> **In sintesi.** Un sito esterno fa inviare al browser della vittima una richiesta autenticata al tuo sito. Oggi la difesa combina cookie `SameSite`, token anti-CSRF del framework e controllo degli header di provenienza.

## Pratiche

### 🔴 Obbligatorio

- Le richieste con effetti (`POST`, `PUT`, `PATCH`, `DELETE`) non devono mai essere `GET`.
- Cookie di sessione con `SameSite=Lax` o `Strict`.
- **Token anti-CSRF** del framework (synchronizer token o double-submit firmato) su tutti i form e le chiamate che modificano stato. Non disattivarli "perché danno fastidio".

### 🟠 Raccomandato

- Verifica di **`Origin`** (o `Referer` come ripiego) sulle richieste che cambiano stato.
- **Fetch Metadata**: rifiuta lato server richieste con `Sec-Fetch-Site: cross-site` verso endpoint non pensati per essere chiamati da altri siti.

  ```text
  se Sec-Fetch-Site in {cross-site} e metodo != GET e endpoint non pubblico → 403
  ```

- Per API usate solo dal tuo frontend: richiedi un header personalizzato (es. `X-Requested-With`) e un `Content-Type: application/json`, che forzano un preflight CORS.

### 🟢 Avanzato

- Riautenticazione per azioni ad alto impatto (anche contro CSRF residui).

## Errori comuni

- Pensare che `SameSite=Lax` basti da solo: non copre sottodomini compromessi né richieste `GET` con effetti.
- CORS con `Access-Control-Allow-Credentials: true` e origine riflessa: annulla le difese (vedi [cors](../04-browser/cors.md)).

## Fonti

- [RADWARE-15BP], [ALERT-HEADERS] — vedi [fonti.md](../fonti.md)
