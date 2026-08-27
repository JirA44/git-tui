# git-tui

> **Analyseur Git en terminal** — `git log` devient une table lisible en 1 commande.

[![Python 3.10+](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![TUI](https://img.shields.io/badge/TUI-Rich%20%2B%20Click-purple)](#)

### En 1 ligne
```bash
pip install -e .
git-tui .
git-tui D:/Code/forge-cli --since 2026-01-01
```

---

## Présentation

| Besoin | Résultat |
|---|---|
| **Rétro sprint** | Table des auteurs triée par commits, sans `git shortlog` illisible |
| **Audit onboarding** | Vérifie en 1s si un repo a 4 auteurs actifs ou 1 seul |
| **Portfolio / soutenance** | Screenshot du tableau pour slide “contribution” |

### Exemple
```
$ git-tui D:/Code/forge-cli
╭──────────────────────────────╮
│ Commits: 3  Fichiers: 12  Auteurs: 1 │
╰──────────────────────────────╯
┌─────────────────┬─────────┐
│ Auteur          │ Commits │
├─────────────────┼─────────┤
│ Forge           │       3 │
└─────────────────┴─────────┘
```

---

## Installation

```bash
git clone https://github.com/JirA44/git-tui
cd git-tui
pip install -e .
git-tui --help
```

## Utilisation

```bash
# Repo courant
git-tui .

# Autre repo
git-tui D:/Code/share-list

# Dans un script
git-tui . > audit.txt
```

## À quoi ça sert vs `git shortlog` ?

`git shortlog -sn` donne une ligne brute. `git-tui` donne un **panel Rich** avec totaux (commits / fichiers / auteurs) + table triée, prêt à coller dans une doc.

---

## Roadmap
- [ ] `--since 1.month` / `--until`
- [ ] `--by-file` (top fichiers modifiés)
- [ ] Export `--json` / `--csv`

MIT — PRs bienvenues.
