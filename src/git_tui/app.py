import subprocess, click
from pathlib import Path
from collections import Counter
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
console=Console()
def run(*a, cwd="."):
    return subprocess.check_output(a, cwd=cwd, text=True, errors="ignore")
@click.command()
@click.argument("path", default=".")
def main(path):
    p=Path(path)
    authors=Counter(run("git","log","--pretty=format:%an","--no-merges", cwd=p).splitlines())
    commits=len(list(authors.elements()))
    files=len(run("git","ls-files", cwd=p).splitlines())
    t=Table(title=f"Git TUI — {p.resolve().name}")
    t.add_column("Auteur"); t.add_column("Commits", justify="right")
    for a,n in authors.most_common(10): t.add_row(a,str(n))
    console.print(Panel(f"Commits: {commits}  Fichiers: {files}  Auteurs: {len(authors)}"))
    console.print(t)
if __name__=="__main__": main()
