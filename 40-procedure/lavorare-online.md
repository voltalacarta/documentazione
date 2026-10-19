---
titolo: Lavorare online
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-15
tag: [procedure, codespaces, cloud-shell, github-dev]
sintesi: "Usare github.dev, Codespaces e Cloud Shell"
collegati: [0003, 0005]
---

# Lavorare online

## Scopo

Aprire un editor nel browser su un repository GitHub, lavorare e salvare il lavoro su GitHub.

## Quale strumento scegliere

| Situazione | Strumento |
| --- | --- |
| Correggere un refuso, scrivere una nota | **github.dev** |
| Lavoro lungo, serve il terminale, estensioni complete | **Codespaces** |
| Quota di Codespaces finita | **Cloud Shell** |

## Prerequisiti (una volta sola)

1. Impostazioni di costo applicate (vedi [ambiente cloud](../20-infrastruttura/ambiente-cloud.md#impostazioni-consigliate)).
2. Per Cloud Shell: un account Google.

## A · github.dev

1. Apri il repository su github.com e premi `.` (punto).
2. Se compare l'avviso, accetta le **estensioni consigliate**.
3. Modifica i file.
4. Pannello **Source Control** (icona dei rami, a sinistra) → scrivi il messaggio → **Commit & Push**.

## B · Codespaces

1. Repository → **Code** → scheda **Codespaces** → **Create codespace on main**.
2. Attendi l'avvio: estensioni e strumenti si installano da soli.
3. Lavora; il terminale si apre con `` Ctrl+` ``.
4. A fine lavoro: **Source Control** → messaggio → **Commit** → **Sync Changes**.
5. Chiudi la scheda. Il Codespace si spegne da solo dopo il timeout di inattività.

Per riaprirlo: [github.com/codespaces](https://github.com/codespaces) elenca tutti i Codespace esistenti.

## C · Cloud Shell (riserva)

1. Apri [shell.cloud.google.com](https://shell.cloud.google.com) e accedi con l'account Google.
2. La prima volta, nel terminale:

   ```bash
   gh auth login        # scegli GitHub.com → HTTPS → Login with a web browser
   gh repo clone voltalacarta/documentazione
   ```

3. Pulsante **Open Editor** per l'editor grafico.
4. A fine lavoro, nel terminale:

   ```bash
   git add -A && git commit -m "docs: descrizione" && git push
   ```

## Verifica

Su github.com il repository mostra l'ultimo commit con il tuo messaggio. Se non c'è, il lavoro **non** è salvato.

## Problemi frequenti

| Problema | Soluzione |
| --- | --- |
| Codespaces non si avvia: quota esaurita | Usa github.dev o Cloud Shell fino al mese successivo |
| Push rifiutato perché il ramo è indietro | **Sync Changes** (o `git pull --rebase`) e poi di nuovo push |
| Estensioni Foam non attive | Pannello Estensioni → filtro *Recommended* → installa |
| `gh: command not found` in Cloud Shell | Usa `git clone https://github.com/voltalacarta/documentazione` e accedi con un token |
