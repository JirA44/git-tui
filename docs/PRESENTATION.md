# git-tui — Présentation

**One-liner:** `git log` devient une table Rich lisible en 1 commande.

## À quoi ça sert ?
- **Rétro sprint** → `git-tui .` montre qui a commité quoi sans `git shortlog` illisible.
- **Audit onboarding** → vérifier qu'un repo a bien 3 auteurs actifs, pas 1.
- **Portfolio** → screenshot du tableau pour slide "contribution".

## Exemple
```
$ git-tui D:/Code/forge-cli
Commits: 1  Fichiers: 12  Auteurs: 1
┌─────────────────┬─────────┐
│ Auteur          │ Commits │
├─────────────────┼─────────┤
│ Forge           │       1 │
└─────────────────┴─────────┘
```

## Public
Devs qui vivent en terminal, enseignants qui notent des projets Git.

## Étendre
`git-tui --since 2026-01-01 --by-file` (prochaine V1.01)
