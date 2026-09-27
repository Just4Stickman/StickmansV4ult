from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SELF = Path(__file__).resolve()
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


# Repository structure validation
for file_name in required_files:
    if not (ROOT / file_name).is_file():
        errors.append(f"missing file: {file_name}")

for directory_name in required_dirs:
    if not (ROOT / directory_name).is_dir():
        errors.append(f"missing directory: {directory_name}")


# Template metadata validation
for meta in (ROOT / "templates").rglob("template.yml"):
    try:
        text = meta.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        errors.append(f"{meta}: unable to read file")
        continue

    required_keys = [
        "id:",
        "name:",
        "slug:",
        "version:",
        "status:",
        "difficulty:",
        "categories:",
        "languages:",
        "license:",
    ]

    for key in required_keys:
        if not re.search(rf"^{re.escape(key)}", text, re.MULTILINE):
            errors.append(f"{meta}: missing {key}")

    if not (meta.parent / "README.md").is_file():
        errors.append(f"{meta.parent}: missing README.md")

    difficulty = re.search(
        r"^difficulty:\s*(\S+)",
        text,
        re.MULTILINE,
    )

    if difficulty and difficulty.group(1) not in {
        "beginner",
        "intermediate",
        "advanced",
        "professional",
    }:
        errors.append(f"{meta}: invalid difficulty")


# Secret detection
#
# The patterns are deliberately assembled from parts so this validator
# does not contain complete token signatures that can trigger itself.
PRIVATE_KEY_HEADER = (
    "-----BEGIN "
    + r"[A-Z0-9 ]+"
    + " PRIVATE KEY-----"
)

GITHUB_PREFIX = "gh" + "p_"
OPENAI_PREFIX = "sk" + "-"

secret_patterns = [
    re.compile(PRIVATE_KEY_HEADER),
    re.compile(
        rf"\b{re.escape(GITHUB_PREFIX)}[A-Za-z0-9]{{30,}}\b"
    ),
    re.compile(
        rf"\b{re.escape(OPENAI_PREFIX)}[A-Za-z0-9]{{30,}}\b"
    ),
    re.compile(
        r"\bAKIA[0-9A-Z]{16}\b"
    ),
    re.compile(
        r"\bAIza[0-9A-Za-z_-]{35}\b"
    ),
]

scannable_extensions = {
    ".md",
    ".txt",
    ".yml",
    ".yaml",
    ".json",
    ".js",
    ".jsx",
    ".ts",
    ".tsx",
    ".py",
    ".sh",
    ".bash",
    ".zsh",
    ".env",
    ".ini",
    ".cfg",
    ".conf",
}

for path in ROOT.rglob("*"):
    if not path.is_file():
        continue

    if ".git" in path.parts:
        continue

    # Never scan this validator itself.
    try:
        if path.resolve() == SELF:
            continue
    except OSError:
        continue

    if path.suffix.lower() not in scannable_extensions:
        continue

    try:
        text = path.read_text(
            encoding="utf-8",
            errors="ignore",
        )
    except OSError:
        continue

    for pattern in secret_patterns:
        if pattern.search(text):
            errors.append(f"possible secret in {path}")
            break


# Final result
if errors:
    print("Validation failed:")
    for error in errors:
        print(f"- {error}")
    sys.exit(1)

print("Validation passed.")
