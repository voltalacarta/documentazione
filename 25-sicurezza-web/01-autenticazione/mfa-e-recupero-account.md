---
titolo: MFA, SSO e recupero account
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, autenticazione]
prossima_revisione: 2027-04-15
owasp: [A07:2025]
asvs: [V6, V10]
---

# MFA, SSO e recupero dell'account

> **In sintesi.** Non tutti i secondi fattori si equivalgono. La gerarchia va da quelli resistenti al phishing (passkey, chiavi FIDO2) a quelli da evitare (SMS). Il recupero account va progettato con la stessa cura del login.

## Gerarchia dei fattori

| Livello | Fattore | Resistente al phishing | Uso consigliato |
|---|---|---|---|
| 1 | Chiave hardware FIDO2 / passkey legata al dispositivo | ✅ | Admin, accessi privilegiati |
| 2 | Passkey sincronizzata | ✅ | Tutti gli utenti |
| 3 | App TOTP (Authenticator) | ❌ | Fallback accettabile |
| 4 | Notifica push con *number matching* | ❌ (parzialmente mitigato) | Fallback |
| 5 | OTP via email | ❌ | Solo recupero, con limiti |
| 6 | OTP via SMS | ❌ | Da evitare; vulnerabile a SIM swap |

NIST SP 800-63B-4 e CISA collocano gli autenticatori crittografici hardware (FIDO2/WebAuthn, smart card PKI) nella fascia più alta.

## Pratiche MFA

- 🔴 MFA obbligatoria per tutti gli account amministrativi, inclusi pannelli CMS, hosting, DNS, registrar, repository e CI.
- 🟠 MFA disponibile per tutti gli utenti, fortemente incoraggiata.
- 🟠 Contro la *MFA fatigue*: limita le richieste push e usa il number matching.
- 🔴 Codici di backup monouso, mostrati una sola volta e conservati come hash.

## SSO (OAuth 2.x / OpenID Connect)

- 🔴 Usa **Authorization Code + PKCE** per tutti i client, anche server-side. L'*implicit flow* e il *password grant* sono deprecati.
- 🔴 Valida `state` (o usa PKCE) contro CSRF, `nonce` contro replay, `iss`, `aud`, scadenza e firma del token.
- 🔴 Redirect URI registrate in modo esatto, niente wildcard.
- 🟠 Segui le raccomandazioni di OAuth 2.0 Security Best Current Practice (RFC 9700) e, se possibile, OAuth 2.1.

## Recupero account

- 🔴 Token di reset: casuali (≥ 128 bit), monouso, scadenza breve (≤ 30 minuti), conservati come hash.
- 🔴 Risposta identica sia che l'email esista sia che no (anti-enumerazione).
- 🔴 Invalida tutte le sessioni attive dopo un reset.
- 🟠 Notifica l'utente su tutti i canali noti quando cambia password, email o metodi MFA.
- 🟠 Periodo di attesa o verifica aggiuntiva per la sostituzione dell'email principale.
- 🟢 Per account di alto valore: recupero assistito con verifica d'identità, mai solo via email.

## Fonti

- [OPTRO-NIST], [AUTHSIGNAL-NIST] — vedi [fonti.md](../fonti.md)
