---
titolo: Injection (SQL, NoSQL, comandi, template)
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, input-e-output]
prossima_revisione: 2027-04-15
owasp: [A05:2025]
asvs: [V1, V2]
---

# Injection

> **In sintesi.** Succede quando dati non fidati diventano parte di un comando o di una query. La difesa non è "filtrare i caratteri pericolosi", ma **tenere separati dati e codice** con API parametrizzate.

## Le varianti

| Tipo | Esempio di sink | Difesa primaria |
|---|---|---|
| SQL | `query("... WHERE id=" + id)` | Prepared statement / ORM |
| NoSQL | `find({ user: req.body.user })` con oggetto `{ $ne: null }` | Validazione del tipo, sanitizzazione degli operatori |
| Comandi OS | `exec("convert " + file)` | API native senza shell; `execFile` con argomenti separati |
| Template (SSTI) | `render(userInput)` | Mai compilare template forniti dall'utente |
| LDAP / XPath | filtri costruiti a stringa | Escape specifico della libreria |
| Header / log | `\r\n` nei valori | Validazione e encoding |
| XSS | output HTML | vedi [xss](xss.md) |
| Prompt injection | input verso LLM | vedi [owasp-llm-top10](../08-ai-llm/owasp-llm-top10.md) |

## Pratiche

### 🔴 Obbligatorio

- **Query parametrizzate** ovunque, anche per gli ID numerici.

  ```python
  cur.execute("SELECT * FROM utenti WHERE email = %s", (email,))
  ```

- Per parti non parametrizzabili (nome colonna in `ORDER BY`), usa un'**allowlist**.
- **Validazione dell'input** per tipo, lunghezza, formato e intervallo, preferibilmente con uno schema (Zod, Pydantic, JSON Schema, Bean Validation).
- Nessuna `eval`, `Function()`, deserializzazione nativa (`pickle`, `unserialize`, `BinaryFormatter`) di dati non fidati.

### 🟠 Raccomandato

- Account database con privilegi minimi: l'applicazione non deve poter fare `DROP` o leggere tabelle di altri servizi.
- SAST in CI per individuare concatenazioni nei sink (vedi [testing-di-sicurezza](../11-sdlc/testing-di-sicurezza.md)).
- Code review mirate su query raw e chiamate a processi esterni.

### 🟢 Avanzato

- Regole SAST personalizzate (Semgrep/CodeQL) per i pattern del tuo codice.

## Errori comuni

- Credere che l'ORM protegga sempre: i metodi `raw()` / `whereRaw()` no.
- Validare solo lato client.
- Usare l'escape manuale al posto della parametrizzazione.

## Fonti

- [OWASP-T10], [RADWARE-15BP] — vedi [fonti.md](../fonti.md)
