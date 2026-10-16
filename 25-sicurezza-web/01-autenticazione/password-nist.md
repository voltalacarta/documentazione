---
titolo: Politica delle password (NIST SP 800-63B-4)
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, autenticazione]
prossima_revisione: 2027-04-15
owasp: [A07:2025, A04:2025]
asvs: [V6, V11]
---

# Politica delle password secondo NIST SP 800-63B-4

> **In sintesi.** Lunghezza conta più della complessità, niente scadenze forzate, controllo contro le password compromesse, pieno supporto ai password manager. Chi applica ancora rotazioni a 90 giorni e regole "maiuscola + numero + simbolo" è fuori linea rispetto a NIST.

## Regole

| Regola | Indicazione | Note |
|---|---|---|
| Lunghezza minima | **≥ 15 caratteri** se la password è l'unico fattore; ≥ 8 se usata con MFA | La soglia 15 è la raccomandazione NIST corrente |
| Lunghezza massima | Accetta **almeno 64 caratteri** | Non troncare mai in silenzio |
| Composizione | **Nessuna regola** di composizione obbligatoria | Le regole spingono verso schemi prevedibili |
| Scadenza | **Nessuna rotazione periodica** | Cambio solo in caso di sospetta compromissione |
| Blocklist | **Obbligatoria**: password comuni, compromesse, legate al servizio o all'utente | Es. API k-anonymity di Have I Been Pwned |
| Suggerimenti / domande segrete | **Vietati** | |
| Incolla / password manager | **Consentiti** e supportati | Non bloccare il paste |
| Mostra password | Offri il pulsante "mostra" | Riduce errori di battitura |
| Caratteri | Accetta Unicode e spazi | Normalizza (NFKC) prima dell'hash |

## Conservazione

- 🔴 Algoritmi in ordine di preferenza (OWASP Password Storage Cheat Sheet, verificato il 2026-10-15). Mai hash veloci (MD5, SHA-1, SHA-256 semplice).

  | Algoritmo | Configurazione minima OWASP | Note |
  |---|---|---|
  | **Argon2id** | m=19 MiB (19456 KiB), t=2, p=1 | Preferito. Equivalenti: 46 MiB/t=1, 12 MiB/t=3, 9 MiB/t=4, 7 MiB/t=5 |
  | scrypt | N=2^17 (128 MiB), r=8, p=1 | Se Argon2id non è disponibile |
  | bcrypt | work factor ≥ 10 | Solo sistemi legacy; la maggior parte delle implementazioni ignora i byte oltre il 72° |
  | PBKDF2-HMAC-SHA256 | 600.000 iterazioni | Quando serve conformità FIPS-140 |

- 🔴 Salt unico per utente (gestito dalla libreria).
- 🟠 Parti dai minimi e aumenta finché l'hash richiede circa 100–500 ms sul tuo server.
- 🟢 **Pepper**: segreto aggiuntivo conservato separatamente dal database (in un vault o HSM).
- 🟠 Ri-hash trasparente al login quando aggiorni algoritmo o parametri.

## Protezione dagli attacchi

- 🔴 Rate limiting e blocco progressivo per account e per IP (vedi [waf-rate-limiting-bot](../09-infrastruttura/waf-rate-limiting-bot.md)).
- 🔴 Messaggi d'errore generici: "credenziali non valide", non "utente inesistente".
- 🟠 Rilevamento di credential stuffing (molti account diversi da pochi IP).
- 🟠 Notifica all'utente di login da nuovi dispositivi.

## Vedi anche

- [passkey-webauthn](passkey-webauthn.md) — l'alternativa da privilegiare
- [mfa-e-recupero-account](mfa-e-recupero-account.md)

## Fonti

- [NIST-800-63B-4], [OWASP-CS-PASSWORD], [OPTRO-NIST], [SAKIMURA-NIST], [AUTHSIGNAL-NIST] — vedi [fonti.md](../fonti.md)
