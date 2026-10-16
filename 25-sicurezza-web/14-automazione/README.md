---
titolo: Automazione dei controlli
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-16
tag: [sicurezza-web, automazione]
prossima_revisione: 2027-01-15
owasp: [A02:2025, A03:2025, A09:2025]
---

# Automazione dei controlli

> **In sintesi.** Strumenti pronti da copiare in qualunque progetto futuro, indipendenti dal linguaggio. Trasformano le regole delle altre cartelle in controlli che girano da soli.

## Contenuto

```text
14-automazione/
├── scripts/
│   ├── check-headers.py        ← verifica header, cookie, TLS, redirect, file esposti
│   └── kb-revisioni.py         ← elenca i file di questa base da rivedere
├── github/
│   ├── workflows/security.yml  ← pipeline CI: segreti, dipendenze, workflow, header, DAST
│   ├── dependabot.yml          ← aggiornamenti automatici (con cooldown)
│   └── renovate.json           ← alternativa a Dependabot
└── config/
    ├── npmrc                   ← .npmrc che disattiva gli script di installazione
    ├── pre-commit-config.yaml  ← blocca i segreti prima del commit
    └── gitignore-sicurezza     ← righe da aggiungere al .gitignore
```

## check-headers.py

Controlla un sito in pochi secondi, solo con la libreria standard di Python 3.

```bash
python3 check-headers.py https://example.it
python3 check-headers.py https://example.it --json > risultato.json
```

Verifica: HSTS, CSP (e se è strict), `nosniff`, `Referrer-Policy`, COOP, `Permissions-Policy`, protezione dal clickjacking, header che rivelano versioni, attributi dei cookie, versione TLS e rifiuto di TLS 1.0/1.1, redirect HTTP→HTTPS, presenza di `security.txt`, esposizione di `.git/`, `.env` e backup comuni.

Esce con codice 1 se trova errori bloccanti: si può usare in CI.

> Usalo solo su siti di cui sei responsabile o con autorizzazione. Le richieste sono normali GET, ma la ricerca di file esposti può comparire nei log di sicurezza altrui.

**Testato** su due server locali (uno configurato correttamente, uno vulnerabile): rileva correttamente tutti i problemi del secondo. Non sostituisce SSL Labs (cifrari, catena di certificati, post-quantum) né un DAST.

## kb-revisioni.py

```bash
python3 25-sicurezza-web/14-automazione/scripts/kb-revisioni.py --radice 25-sicurezza-web --giorni 30
python3 25-sicurezza-web/14-automazione/scripts/kb-revisioni.py --radice 25-sicurezza-web --markdown > revisioni.md
```

Elenca i file con `prossima_revisione` scaduta o in scadenza e i marcatori `⚠️ da verificare` aperti. Pensato per la revisione trimestrale (vedi [CONTRIBUIRE](../contribuire.md)).

## Pipeline CI (GitHub Actions)

1. Copia `github/workflows/security.yml` in `.github/workflows/` e `scripts/check-headers.py` in `security/` del repository.
2. Imposta la variabile di repository `STAGING_URL` (Settings → Secrets and variables → Actions → Variables) per attivare i job su header e DAST.
3. **Fissa le action per SHA** prima dell'uso (`pinact run` o `npx pin-github-action .github/workflows/security.yml`): nel file sono indicate per tag solo per leggibilità. Vedi [ci-cd](../06-supply-chain/ci-cd.md).
4. Copia `dependabot.yml` (oppure `renovate.json`, non entrambi).

**Verifica eseguita:** YAML e JSON validi. ⚠️ Non eseguito su GitHub da qui: lancia il workflow con *Run workflow* e controlla il primo esito. Se usi GitLab o altre piattaforme, i comandi `docker run` dei job si riportano quasi identici.

## Per chi non usa un repository

Anche un sito WordPress su hosting condiviso può avere un controllo periodico: esegui `check-headers.py` da un qualunque computer una volta al mese (o da un'attività programmata) e confronta i risultati.
