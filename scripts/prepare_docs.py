"""Stage the repository's existing content for MkDocs without editing it."""

from pathlib import Path
import re
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
for directory in ("publication", "stylesheets"):
    copy_tree(directory)

# Use the repository README as the landing page. No project-source document is
# included in the published artifact.
shutil.copy2(ROOT / "README.md", STAGING / "index.md")

# Copy only images referenced by publication Markdown. Mirror them beside the
# publication pages so their existing paths work without source-file edits.
image_pattern = re.compile(r"!\[[^\]]*\]\((assets/[^)]+)\)")
for document in (ROOT / "publication").glob("*.md"):
    for relative_path in image_pattern.findall(document.read_text(encoding="utf-8")):
        source = ROOT / relative_path
        if not source.is_file():
            continue
        for prefix in (STAGING, STAGING / "publication"):
            destination = prefix / relative_path
            destination.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(source, destination)
