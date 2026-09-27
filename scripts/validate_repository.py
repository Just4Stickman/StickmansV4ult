from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
CURRENT_FILE = Path(__file__).resolve()
errors = []

required_files = [
    "README.md",
    "LICENSE",
    ".gitignore",
    ".editorconfig",
    "CONTRIBUTING.md",
    "SECURITY.md",
    "CODE_OF_CONDUCT.md",
]

required_dirs = [
    "templates",
    "tools",
    "snippets",
    "workflows",
    "configs",
    "docs",
    "scripts",
    ".github",
]

for f in required_files:
    if not (ROOT / f).is_file():
        errors.append(f"missing file: {f}")

for d in required_dirs:
    if not (ROOT / d).is_dir():
        errors.append(f"missing directory: {d}")

for meta in (ROOT / "templates").rglob("template.yml"):
    text = meta.read_text(encoding="utf-8")

    for key in [
        "id:",
        "name:",
        "slug:",
        "version:",
        "status:",
        "difficulty:",
        "categories:",
        "languages:",
        "license:",
    ]:
        if not re.search(rf"^{re.escape(key)}", text, re.MULTILINE):
            errors.append(f"{meta}: missing {key}")

    if not (meta.parent / "README.md").exists():
        errors.append(f"{meta.parent}: missing README.md")

    m = re.search(r"^difficulty:\s*(\S+)", text, re.MULTILINE)

    if m and m.group(1) not in {
        "beginner",
        "intermediate",
        "advanced",
        "professional",
    }:
        errors.append(f"{meta}: invalid difficulty")

bad_patterns = [
    re.compile(r"-----BEGIN .*PRIVATE KEY-----"),
    re.compile(r"\bghp_[A-Za-z0-9]{30,}\b"),
    re.compile(r"\bsk-[A-Za-z0-9]{30,}\b"),
]

for p in ROOT.rglob("*"):
    if not p.is_file() or ".git" in p.parts:
        continue

    # Never scan this validator itself.
    if p.name == "validate_repository.py" and p.parent.name == "scripts":
        continue

    if p.suffix.lower() not in {
        ".md",
        ".txt",
        ".yml",
        ".yaml",
        ".json",
        ".js",
        ".ts",
        ".py",
        ".sh",
        ".env",
    }:
        continue

    try:
        text = p.read_text(encoding="utf-8")
    except UnicodeDecodeError:
        continue

    for pattern in bad_patterns:
        if pattern.search(text):
            errors.append(f"possible secret in {p}")

if errors:
    print("Validation failed:")
    print("\n".join(f"- {e}" for e in errors))
    raise SystemExit(1)

print("Validation passed.")

