---
titolo: TLS, certificati e HSTS
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, crittografia]
prossima_revisione: 2027-01-15
owasp: [A04:2025, A02:2025]
asvs: [V12]
---

# TLS, certificati e HSTS

> **In sintesi.** HTTPS ovunque, TLS 1.3 come preferenza, TLS 1.2 solo con cifrari moderni, nulla di più vecchio. HSTS con preload per impedire il downgrade. Certificati automatizzati.

## Configurazione

### 🔴 Obbligatorio

- **HTTPS su tutto il sito**, inclusi ambienti di staging pubblici, API e asset. Redirect 301 da HTTP.
- **TLS 1.3** abilitato; **TLS 1.2** ammesso solo con suite AEAD e forward secrecy (ECDHE + AES-GCM / ChaCha20-Poly1305). **Disabilita TLS 1.0, 1.1, SSLv3.**
- Certificati da CA pubblica con rinnovo **automatico** (ACME: Let's Encrypt, ZeroSSL, o la CA del CDN).
- **HSTS**: `max-age` di almeno 1 anno.

### 🟠 Raccomandato

- `includeSubDomains` e iscrizione alla **HSTS preload list** (hstspreload.org) — verifica prima che *tutti* i sottodomini supportino HTTPS: la rimozione dalla lista è lenta.
- Record DNS **CAA** per limitare quali CA possono emettere certificati per il dominio.
- Monitoraggio dei **Certificate Transparency log** (es. crt.sh, Cert Spotter) per accorgersi di certificati emessi a tua insaputa.
- **Key exchange ibrido post-quantum** `X25519MLKEM768`: vedi [post-quantum](post-quantum.md).
- **DNSSEC** sul dominio, se il registrar lo supporta.

### Evoluzioni in corso (certificati e revoca)

- 🔴 **Durata dei certificati in calo.** Il CA/Browser Forum ha approvato nel 2025 la riduzione progressiva della validità massima dei certificati pubblici (ballot SC-081):

  | Da | Validità massima | Riuso della validazione del dominio |
  |---|---|---|
  | prima di marzo 2026 | 398 giorni | 398 giorni |
  | **marzo 2026 (già in vigore)** | **200 giorni** | ridotto progressivamente |
  | marzo 2027 | 100 giorni | |
  | marzo 2028 | | 10 giorni |
  | marzo 2029 | **47 giorni** | |

  Conseguenza pratica: chi rinnova ancora a mano un certificato annuale deve passare **subito** al rinnovo automatico (ACME). Con 47 giorni il rinnovo manuale non è più gestibile.
- **OCSP non serve più.** Let's Encrypt ha spento i suoi responder OCSP il 6 agosto 2025, per ragioni di privacy (l'OCSP rivelava alla CA quali siti visitava l'utente) e semplicità. I browser verificano la revoca tramite **CRL**. Non configurare `OCSP Must-Staple`: è stato abbandonato e può causare interruzioni. `ssl_stapling` può restare attivo con CA che offrono ancora OCSP, ma non è più un requisito.

## Esempio nginx (base 2026)

```nginx
ssl_protocols TLSv1.2 TLSv1.3;
ssl_ecdh_curve X25519MLKEM768:X25519:secp256r1;   # richiede OpenSSL 3.5+
ssl_prefer_server_ciphers off;
ssl_session_tickets off;
add_header Strict-Transport-Security "max-age=63072000; includeSubDomains; preload" always;
```

Per i cifrari TLS 1.2 usa il generatore **Mozilla SSL Configuration Generator**, profilo *Intermediate*.

## Come verificarlo

- SSL Labs Server Test (obiettivo A/A+), `testssl.sh`, Mozilla Observatory.

## Fonti

- [UNVEIL-PQ], [APPVIEWX-SC081], [LE-OCSP] — vedi [fonti.md](../fonti.md)
