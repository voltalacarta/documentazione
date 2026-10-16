---
titolo: Controllo degli accessi
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, autorizzazione]
prossima_revisione: 2027-04-15
owasp: [A01:2025]
asvs: [V8, V2]
---

# Controllo degli accessi

> **In sintesi.** È il rischio n.1 della OWASP Top 10:2025 ed è stato trovato in tutte le applicazioni testate. La regola è una: **ogni richiesta viene autorizzata sul server, per quella specifica risorsa, per quell'utente**.

## Forme tipiche del difetto

- **IDOR / BOLA**: `GET /fatture/1043` restituisce la fattura di un altro cliente cambiando il numero.
- **Forced browsing**: pagine `/admin` protette solo perché "nessuno conosce l'URL".
- **Escalation verticale**: un utente invia `role=admin` in un form o modifica un claim del token.
- **Mass assignment**: l'API accetta campi non previsti (`isVerified`, `price`) e li salva.
- **Manipolazione dei token di accesso**: JWT non verificati, cookie con il ruolo in chiaro.
- **CORS permissivo** che espone API autenticate a qualunque origine (vedi [cors](../04-browser/cors.md)).
- **SSRF** (dal 2025 parte di questa categoria): vedi [ssrf](ssrf.md).

## Pratiche

### 🔴 Obbligatorio

- **Nega per default**: ogni route richiede autenticazione e autorizzazione esplicite; le eccezioni pubbliche sono elencate.
- Controllo **centralizzato** (middleware, policy, decorator), non sparso in ogni controller.
- Verifica di **proprietà** a livello di oggetto: la query include sempre il proprietario o il tenant.

  ```sql
  SELECT * FROM fatture WHERE id = $1 AND cliente_id = $2;
  ```

- Allowlist dei campi aggiornabili (DTO/schema) contro il mass assignment.
- Le stesse regole valgono per **tutte** le interfacce: pagine, API, GraphQL, websocket, export, job asincroni.

### 🟠 Raccomandato

- Modello esplicito: RBAC per casi semplici, ABAC/ReBAC (es. OpenFGA, Cedar, Oso) per permessi complessi o multi-tenant.
- Identificatori non sequenziali (UUIDv4/v7) come difesa aggiuntiva — **non** come sostituto del controllo.
- Rate limiting su endpoint che enumerano risorse.
- Log di ogni accesso negato, con alert su picchi (vedi [logging-e-alert](../10-operazioni/logging-e-alert.md)).

### 🟢 Avanzato

- Test automatici di autorizzazione: matrice ruoli × endpoint eseguita in CI (es. con due utenti di test che provano ad accedere uno alle risorse dell'altro).
- Row-Level Security nel database (es. PostgreSQL RLS) come seconda linea per il multi-tenant.

## Come verificarlo

- Test manuale con due account dello stesso livello e di livelli diversi; estensioni come Autorize (Burp) automatizzano la ripetizione delle richieste.
- Requisiti ASVS 5.0 capitolo V8.

## Fonti

- [OWASP-T10], [RADWARE-T10] — vedi [fonti.md](../fonti.md)
