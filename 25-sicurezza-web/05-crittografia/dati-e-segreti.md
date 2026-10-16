---
titolo: Cifratura dei dati e gestione dei segreti
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, crittografia]
prossima_revisione: 2027-04-15
owasp: [A04:2025, A02:2025]
asvs: [V11, V13, V14]
---

# Cifratura dei dati e gestione dei segreti

> **In sintesi.** Non inventare crittografia, usa librerie di alto livello. I segreti (chiavi API, password del DB, chiavi di firma) non stanno mai nel codice né nel repository: stanno in un vault, con rotazione e privilegi minimi.

## Dati a riposo

- 🔴 Classifica i dati: personali, particolari (salute, ecc.), di pagamento, credenziali. La protezione si calibra sulla classe.
- 🔴 Cifratura del disco/volume e dei backup (di solito offerta dal provider: attivala e verificala).
- 🟠 Cifratura a livello di campo per dati molto sensibili (documenti d'identità, IBAN), con chiavi gestite da KMS.
- 🔴 Primitive moderne: **AES-256-GCM** o **ChaCha20-Poly1305** per la cifratura simmetrica; **Ed25519** o ECDSA P-256 per le firme; **Argon2id** per le password (vedi [password-nist](../01-autenticazione/password-nist.md)).
- 🔴 Usa librerie ad alto livello (libsodium, Tink, `cryptography` di Python, Web Crypto API) che scelgono nonce e modalità corrette.
- ❌ Mai: ECB, MD5/SHA-1 per sicurezza, chiavi o IV fissi, `Math.random()` per token.
- 🔴 Pagamenti: non conservare i dati della carta; usa un PSP con tokenizzazione (riduce drasticamente l'ambito PCI DSS).

## Segreti

### 🔴 Obbligatorio

- Nessun segreto nel codice, nei file di configurazione versionati, nelle immagini Docker o nel bundle JavaScript del frontend.
- `.env` escluso da git; `.env.example` senza valori reali.
- **Secret scanning** su repository e CI (GitHub secret scanning con push protection, Gitleaks, TruffleHog).
- Se un segreto finisce in un commit: **ruotalo subito**; riscrivere la storia di git non basta.

### 🟠 Raccomandato

- Secret manager: HashiCorp Vault / OpenBao, AWS Secrets Manager, GCP Secret Manager, Azure Key Vault, Doppler, Infisical.
- Credenziali **a breve scadenza** e federate (OIDC) al posto di chiavi statiche, soprattutto in CI (vedi [ci-cd](../06-supply-chain/ci-cd.md)).
- Rotazione programmata e un **runbook** di rotazione d'emergenza per ogni segreto critico.
- Segreti diversi per ogni ambiente (dev, staging, produzione).

### 🟢 Avanzato

- HSM o KMS per le chiavi di firma (JWT, firme documenti).
- Envelope encryption: dati cifrati con chiave dati, chiave dati cifrata con chiave master nel KMS.

## Lezione da Shai-Hulud

Il worm npm del 2025 cercava proprio i segreti sulle macchine degli sviluppatori e nelle pipeline (token GitHub, npm, chiavi cloud). La difesa migliore è che quei segreti **non esistano** a lungo: token effimeri e federati. Vedi [npm-dopo-shai-hulud](../06-supply-chain/npm-dopo-shai-hulud.md).

## Fonti

- [DEEPWATCH-BRIEF], [THN-GITHUB] — vedi [fonti.md](../fonti.md)
