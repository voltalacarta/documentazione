---
titolo: Gestione degli errori e delle condizioni eccezionali
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, operazioni]
prossima_revisione: 2027-04-15
owasp: [A10:2025]
asvs: [V16]
---

# Gestione degli errori e delle condizioni eccezionali

> **In sintesi.** Nuova categoria della OWASP Top 10:2025 (A10). Il problema non è solo l'errore che rivela troppo, ma il sistema che, davanti a un caso imprevisto (timeout, valore nullo, eccezione non gestita, risorsa esaurita), **apre** invece di chiudere.

## Due facce del problema

1. **Fuga di informazioni**: stack trace, query SQL, percorsi di file, versioni software mostrati all'utente.
2. **Fail-open**: un controllo che va in eccezione e lascia passare la richiesta.

```python
# ❌ fail-open
try:
    autorizzato = policy.check(utente, risorsa)
except Exception:
    autorizzato = True   # "per non bloccare l'utente"

# ✅ fail-closed
try:
    autorizzato = policy.check(utente, risorsa)
except Exception:
    log.exception("errore nel controllo di autorizzazione")
    autorizzato = False
```

## Pratiche

### 🔴 Obbligatorio

- **Gestore globale** delle eccezioni che restituisce un messaggio generico con un ID di riferimento e registra i dettagli solo nei log.
- Pagine d'errore personalizzate per 4xx/5xx, senza informazioni tecniche.
- Ogni controllo di sicurezza **fallisce in modo chiuso**: errore → accesso negato.
- Transazioni atomiche per operazioni multi-step (pagamento + ordine + magazzino): un errore a metà non deve lasciare stati incoerenti sfruttabili.

### 🟠 Raccomandato

- Timeout espliciti su tutte le chiamate esterne, con comportamento definito al superamento.
- Gestione di casi limite: valori nulli, numeri negativi, overflow, stringhe vuote, Unicode, richieste concorrenti (*race condition* su coupon, saldi, voti).
- Limiti di risorse (memoria, dimensione richieste, profondità di ricorsione/JSON) per evitare crash sfruttabili.
- Test di *fault injection*: cosa succede se il database, la cache o il servizio di autenticazione non rispondono?

### 🟢 Avanzato

- Fuzzing degli endpoint e dei parser (vedi [testing-di-sicurezza](../11-sdlc/testing-di-sicurezza.md)).

## Fonti

- [OWASP-T10], [FASTLY-T10], [REDHOT-T10], [RADWARE-15BP] — vedi [fonti.md](../fonti.md)
