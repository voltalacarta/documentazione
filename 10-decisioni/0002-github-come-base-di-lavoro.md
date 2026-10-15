---
titolo: GitHub come base unica di lavoro
stato: accettato
creato: 2026-10-15
aggiornato: 2026-10-15
tag: [decisioni, github, infrastruttura]
collegati: [0003, 0004]
---

# 0002 · GitHub come base unica di lavoro

## Contesto

Si vuole un'unica base per codice, documentazione e note, accessibile da qualsiasi dispositivo e su cui anche l'assistente AI (Claude) possa lavorare direttamente.

## Decisione

- **GitHub** è la piattaforma di riferimento per codice, documentazione e second brain.
- L'organizzazione/account di riferimento è [`voltalacarta`](https://github.com/voltalacarta).
- Claude è collegato a GitHub e lavora sui repository autorizzati: legge, modifica, fa commit e apre pull request.

## Conseguenze

- ✅ Un solo posto per tutto, accessibile dal browser.
- ✅ Versionamento, revisione e automazioni (GitHub Actions) disponibili ovunque.
- ⚠️ L'account GitHub diventa critico: va protetto (vedi [sicurezza](../20-infrastruttura/sicurezza.md)).
- ⚠️ GitHub non è un backup: serve una copia esterna (vedi [sicurezza](../20-infrastruttura/sicurezza.md#backup)).

## Dettagli

- [Organizzazione GitHub](../20-infrastruttura/github.md)
