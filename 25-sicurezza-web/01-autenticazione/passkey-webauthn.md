---
titolo: Passkey e WebAuthn
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, autenticazione]
prossima_revisione: 2027-04-15
owasp: [A07:2025]
asvs: [V6]
---

# Passkey e WebAuthn

> **In sintesi.** Nel 2026 le passkey sono il metodo di login da offrire per primo: sono resistenti al phishing per costruzione e NIST le riconosce nelle sue linee guida di identità digitale.

## Perché resistono al phishing

Una passkey è una coppia di chiavi crittografiche legata al dominio del sito. Il server conserva solo la chiave pubblica; il browser firma una sfida solo per l'origine corretta. Non esiste un segreto riutilizzabile che un sito falso possa farsi consegnare: è questa la proprietà che NIST indica come base della resistenza al phishing.

## Posizione di NIST (SP 800-63B-4)

- La revisione 4, finalizzata a luglio 2025, sostituisce l'edizione precedente e integra la guida supplementare del 2024 sugli autenticatori sincronizzabili.
- **Passkey sincronizzate** (iCloud Keychain, Google Password Manager, password manager) → possono raggiungere **AAL2** se implementate correttamente. Le chiavi private devono essere conservate cifrate e l'account che le sincronizza deve essere a sua volta protetto con MFA.
- **Passkey vincolate al dispositivo** (chiavi hardware FIDO2) → livello più alto, adatte ad **AAL3**.
- La **condivisione** di passkey, proposta da alcuni prodotti come funzione, è considerata da NIST un rischio da gestire, non una caratteristica di sicurezza.

## Pratiche

### 🔴 Obbligatorio (se hai account utente)

- Usa una libreria WebAuthn mantenuta (es. SimpleWebAuthn per Node, `webauthn4j`, `py_webauthn`, `web-auth/webauthn-lib` per PHP) — non implementare il protocollo a mano.
- Verifica lato server origine, `rpId`, challenge monouso e contatore di firma.
- Mantieni almeno un metodo di **recupero** sicuro (vedi [mfa-e-recupero-account](mfa-e-recupero-account.md)).

### 🟠 Raccomandato

- Offri la passkey come opzione predefinita in registrazione e proponi la creazione dopo un login con password.
- Supporta l'**autofill condizionale** (`autocomplete="username webauthn"`) per una UX senza attrito.
- Consenti più passkey per account e una pagina per gestirle (nome, data di creazione, revoca).
- Per gli **amministratori**: richiedi passkey o chiave hardware, niente fallback via SMS.

### 🟢 Avanzato

- Policy di attestazione per ambienti che richiedono autenticatori specifici (AAL3).
- Segnali di rischio al login (nuovo dispositivo, geografia anomala) per richiedere step-up.

## Errori comuni

- Lasciare la password come fallback debole e permanente: l'account resta forte quanto il metodo più debole.
- Recupero account via email senza ulteriori controlli: diventa la porta d'ingresso preferita.

## Fonti

- [NIST-800-63B-4], [TECHWALLA-PASSKEY], [YUBICO-NIST], [CORBADO-NIST] — vedi [fonti.md](../fonti.md)
