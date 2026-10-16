---
titolo: Crittografia post-quantum per il web
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, crittografia]
prossima_revisione: 2027-01-15
owasp: [A04:2025]
---

# Crittografia post-quantum per il web

> **In sintesi.** Nel 2026 lo scambio di chiavi ibrido post-quantum è già lo standard di fatto del web lato browser. Abilitarlo sul server è semplice e protegge dal rischio *harvest now, decrypt later*. I certificati post-quantum invece **non** sono ancora disponibili.

## Perché ora

Un avversario può registrare oggi traffico cifrato e decifrarlo in futuro con un computer quantistico. Lo scambio di chiavi è il punto da proteggere per primo; l'autenticazione (firme dei certificati) è un problema solo nel momento in cui la connessione avviene.

## Stato a ottobre 2026

| Elemento | Stato |
|---|---|
| **ML-KEM** (FIPS 203) | Standard NIST finalizzato ad agosto 2024 |
| **X25519MLKEM768** | Gruppo ibrido (X25519 + ML-KEM-768): se uno dei due regge, la sessione è sicura |
| Standard IETF | **RFC 10024** (agosto 2026) definisce tre gruppi ibridi; solo X25519MLKEM768 è marcato *Recommended* |
| Browser | Chrome/Edge lo usano di default dalla versione 131 (nov. 2024) e da Chrome 138 non è più disattivabile; Firefox in gran parte delle build attuali |
| Adozione | Oltre due terzi del traffico TLS umano verso Cloudflare usava già lo scambio ibrido ad aprile 2026 |
| **Certificati ML-DSA** | Nessuna CA pubblica accettata dai trust store; ballot al CA/Browser Forum ancora in corso |

## Cosa fare

### 🟠 Raccomandato

- Aggiorna lo stack TLS: **OpenSSL 3.5+**, BoringSSL, oppure affidati a un CDN che lo abilita già.
- **Go 1.24+** abilita `X25519MLKEM768` **di default** quando non si impostano `CurvePreferences` (verificato sul sorgente di `crypto/tls`); `GODEBUG=tlsmlkem=0` lo disattiva. Da Go 1.26 sono abilitati di default anche gli ibridi su curve NIST. Lo stesso vale per i server scritti in Go, come Caddy e Traefik.
- Abilita il gruppo ibrido **in testa**, mantenendo i classici come fallback:

  ```nginx
  ssl_ecdh_curve X25519MLKEM768:X25519:secp256r1;
  ```

- Richiede **TLS 1.3**: un server fermo a TLS 1.2 non può offrirlo.
- Verifica che middlebox, WAF e load balancer non rompano ClientHello più grandi (circa +1,1 KB): esistono server *pq-intolerant* che rifiutano i client post-quantum pur accettando quelli classici.

### 🟢 Avanzato

- Inventario crittografico (*crypto-agility*): dove usi RSA/ECDSA/ECDH (TLS, firme JWT, VPN, SSH, cifratura a riposo), per pianificare la migrazione.
- Non configurare **solo** ML-KEM senza fallback: non è ancora in uso in produzione.

## Da monitorare

- Approvazione dei certificati ML-DSA da parte del CA/Browser Forum.
- Linee guida nazionali (ACN, ENISA) sulla roadmap di migrazione.

## Fonti

- [POSTQUANTUM-RFC10024], [ENCCONS-PQC], [UNVEIL-PQ], [PQPROBE], [GO-TLS-DEFAULTS] — vedi [fonti.md](../fonti.md)

> Nota di revisione 2026-10-15: la fonte [UNVEIL-PQ] indica che in Go il gruppo ibrido è disattivato di default; il sorgente ufficiale di Go mostra il contrario. Prevale il sorgente.
