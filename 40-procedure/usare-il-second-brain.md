---
titolo: Usare il second brain
stato: attivo
creato: 2026-10-15
aggiornato: 2026-10-20
tag: [procedure, second-brain, foam, obsidian]
sintesi: "App web (consigliata), Foam nel browser, Obsidian sul telefono, routine"
collegati: [0004, 0005, 0008]
---

# Usare il second brain

## Scopo

Scrivere, collegare e ritrovare note nel repository `second-brain`, dal browser o dal telefono.

## App web (consigliata)

Indirizzo: <https://voltalacarta.github.io/second-brain-app/>. Funziona su computer e telefono, e si può aggiungere alla schermata Home.

1. **Token, una volta ogni 90 giorni.** Il link «Come ottengo il token» nella schermata di accesso apre GitHub con quasi tutto già compilato.
   - **Resource owner:** `voltalacarta`.
   - **Repository access:** *Only select repositories* → `second-brain`.
   - **Permissions:** *Contents* **Read and write**; facoltativo *Actions* Read.
   - **Generate token**, poi copialo.
2. Incolla il token nell'app.
   - **Ricorda su questo dispositivo** solo sui tuoi dispositivi.
   - Senza, il token sparisce quando chiudi la scheda.
3. Uso:

   | Tasto | Effetto |
   | --- | --- |
   | `/` | Cerca note, concetti, idee |
   | `n` | Nuova nota da un modello di `_modelli/` |
   | `o` | Nota del giorno in `01-giornaliere/` |
   | `g` | Grafo completo (un tocco seleziona, il secondo apre) |
   | `e` | Modifica la nota aperta |
   | `Ctrl+S` | Salva: fa un commit; il grafo si aggiorna da solo dopo circa un minuto |

4. Scrivi `[[` per collegare un'altra nota. Le attività `- [ ]` si spuntano direttamente nella nota.
5. Per togliere una nota: menu **⋯ → Archivia**, che la sposta in `40-archivio/`.
6. Su un dispositivo che non è tuo: menu **⋯ → Esci e dimentica il token**.

Dettagli e motivi: [0008](../10-decisioni/0008-app-web-del-second-brain-su-github-pages.md).

## Nel browser (Foam)

1. Apri il repository `second-brain` in **Codespaces** (consigliato: si apre da sola la nota `inizia-qui.md`) o con **github.dev** (tasto `.`). Vedi [Lavorare online](lavorare-online.md).
2. Accetta le estensioni consigliate (Foam).
3. Usa la palette dei comandi (`Ctrl+Shift+P`, su Mac `Cmd+Shift+P`):

   | Comando | Effetto |
   | --- | --- |
   | `Foam: Open Today's Note` | Apre o crea la nota di oggi in `01-giornaliere/` (scrivi `today`) |
   | `Foam: Create New Note From Template` | Nuova nota da un modello (nota o progetto) |
   | `Foam: Show Graph` | Grafo dei collegamenti (scrivi `graph`) |

4. Scrivi `[[` per collegare un'altra nota: Foam suggerisce i nomi.
5. Il pannello **Connections** nella barra laterale mostra i backlink.
6. Fine sessione: **commit e push**.

## Sul telefono (Obsidian, facoltativo)

1. Installa **Obsidian** (gratuito).
2. Crea un vault vuoto chiamato `second-brain`.
3. *Impostazioni* → *Plugin della community* → attiva → cerca e installa **Git**.
4. Nelle impostazioni del plugin Git: URL `https://github.com/voltalacarta/second-brain`, nome utente GitHub e un **token personale** come password.
5. Comando *Git: Clone an existing remote repo* → incolla l'URL.
6. Per salvare: comando *Git: Commit-and-sync* (o attiva la sincronizzazione automatica a intervalli nelle impostazioni del plugin).

Il token si crea su **GitHub → Settings → Developer settings → Personal access tokens → Fine-grained**: accesso solo al repository `second-brain`, permesso *Contents: Read and write*, scadenza di un anno. Va conservato nel password manager.

Note giornaliere, modelli e cartella degli allegati sono già configurati nel repository (cartella `.obsidian/`).

## Routine consigliata

| Quando | Cosa |
| --- | --- |
| Ogni giorno | Nota giornaliera; le idee vanno in *Idee da smistare* o in `00-inbox/` |
| Ogni settimana | Svuota `00-inbox/`: sposta in progetti, aree o risorse e aggiungi almeno un collegamento |
| Ogni mese | Sposta in `40-archivio/` progetti chiusi e note che non servono più |

Lo smistamento settimanale si può chiedere a Claude.

## Problemi frequenti

| Problema | Soluzione |
| --- | --- |
| Conflitto tra telefono e browser | Prima di scrivere, sincronizza; a fine sessione, push. Non modificare la stessa nota in due posti insieme |
| Il grafo non compare in github.dev | Usa Codespaces, dove Foam funziona per intero |
| Il token del telefono è scaduto | Creane uno nuovo e aggiornalo nelle impostazioni del plugin Git |
