"""Stage the repository's existing content for MkDocs without editing it."""

from pathlib import Path
import shutil


ROOT = Path(__file__).resolve().parents[1]
STAGING = ROOT / ".mkdocs"


def copy_tree(name: str) -> None:
    source = ROOT / name
    if source.exists():
        shutil.copytree(source, STAGING / name)


if STAGING.exists():
    shutil.rmtree(STAGING)

STAGING.mkdir()
shutil.copy2(ROOT / "README.md", STAGING / "index.md")

for directory in ("publication", "sources", "notes", "assets", "stylesheets"):
    copy_tree(directory)

# Publication Markdown uses paths relative to its original publishing context.
# Mirror the assets in staging so those paths work without source-file edits.
shutil.copytree(STAGING / "assets", STAGING / "publication" / "assets")
