# git-tui

## Français — présentation

**git-tui** transforme l’historique Git d’un dépôt en tableau lisible dans le terminal. Il affiche des totaux de commits, fichiers et auteurs, avec une vue synthétique utile pour une rétrospective ou un audit rapide.

### À quoi ça sert, et pourquoi ?

`git shortlog` donne une sortie brute ; git-tui facilite la lecture et la comparaison sans devoir reformater les résultats à la main.

### Exemples

```bash
pip install -e .
git-tui .
git-tui D:/Code/forge-cli --since 2026-01-01
```

## English — overview

**git-tui** turns a Git repository’s history into a readable terminal table with commit, file and author totals. It is useful for quick project reviews, contribution summaries and onboarding checks.

### What is it for, and why use it?

Compared with raw `git shortlog` output, git-tui provides a compact view that is easier to scan and reuse in a report.

### Examples

```bash
pip install -e .
git-tui .
git-tui D:/Code/forge-cli --since 2026-01-01
```

## Installation et utilisation (français)



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
