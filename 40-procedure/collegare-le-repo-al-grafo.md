---
titolo: Collegare le repo al grafo
stato: attivo
creato: 2026-10-19
aggiornato: 2026-10-19
tag: [procedure, second-brain, grafo, github-actions, segreti]
sintesi: "Come una repo entra nel grafo del second brain, e i due token facoltativi per le repo private e per l'aggiornamento immediato."
collegati: [0007]
---

# Collegare le repo al grafo

## Scopo

Fare in modo che ogni repo di voltalacarta compaia nel [grafo del second brain](https://github.com/voltalacarta/second-brain/blob/main/grafo.md), con i suoi documenti e i suoi concetti.

## Cosa succede da solo

- **Repo pubbliche:** entrano nel grafo **da sole**, entro 3 ore dalla creazione o dall'ultimo push. Non serve fare nulla.
- **Repo vuote:** compaiono come nodo, con la nota "ancora vuota".
- **Cosa viene letto:** solo i file `.md` (anche in una repo di codice), senza scaricare il resto.

## Repo private: il token di lettura (una volta sola)

Senza questo token il grafo vede solo le repo pubbliche e il second brain stesso.

1. Apri **GitHub → Settings → Developer settings → Personal access tokens → Fine-grained tokens → Generate new token**.
2. Compila:
   - *Token name:* `kg-lettura`
   - *Expiration:* 1 anno (segna la scadenza nel calendario)
   - *Resource owner:* `voltalacarta`
   - *Repository access:* **All repositories**
   - *Permissions → Repository → Contents:* **Read-only** (*Metadata* si aggiunge da sé)
3. **Generate token** e copia il valore (si vede una volta sola). Salvalo nel password manager.
4. Apri la repo **second-brain → Settings → Secrets and variables → Actions → New repository secret**:
   - *Name:* `KG_TOKEN`
   - *Secret:* il valore copiato
5. Avvia l'aggiornamento: **second-brain → Actions → Aggiorna il grafo → Run workflow**.

## Aggiornamento immediato dopo un push (facoltativo)

Di norma il grafo raccoglie le novità ogni 3 ore. Per averle subito:

1. Crea un secondo token fine-grained, `kg-avviso`: *Repository access:* **Only select repositories → second-brain**; *Contents:* **Read and write**.
2. In ogni repo che deve avvisare (per esempio `documentazione`): **Settings → Secrets and variables → Actions → New repository secret** → *Name:* `KG_AVVISO`.

L'Action *Aggiorna gli indici* di quella repo, a fine lavoro, chiederà al second brain di aggiornare il grafo.

## Regolare cosa entra nel grafo

| Voglio… | Dove |
| --- | --- |
| Escludere una repo | `second-brain/_config/grafo.yml` → `scoperta.escludi` |
| Solo il nodo della repo, senza i suoi file | `.kg.yml` nella repo → `livello: repo` |
| Escludere alcuni file o cartelle | `.kg.yml` nella repo → `escludi: ["cartella/**"]` |
| Far riconoscere un concetto nuovo in tutte le repo | `second-brain/_config/vocabolario.yml` |

## Verifica

Nella pagina [grafo.md](https://github.com/voltalacarta/second-brain/blob/main/grafo.md) la repo compare nella tabella **Repo**. Se ha ⚠️ *non leggibile*, è privata e manca `KG_TOKEN`, oppure il token è scaduto.

## Problemi frequenti

| Problema | Soluzione |
| --- | --- |
| La repo nuova non compare | Aspetta il giro successivo (3 ore) o avvia l'Action a mano |
| Una repo privata è "non leggibile" | Crea o rinnova `KG_TOKEN` |
| Il token è scaduto | Rigeneralo (*Regenerate token*) e aggiorna il segreto con lo stesso nome |
