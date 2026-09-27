from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
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

for file_name in required_files:
    if not (ROOT / file_name).is_file():
        errors.append(f"missing file: {file_name}")

for directory_name in required_dirs:
    if not (ROOT / directory_name).is_dir():
        errors.append(f"missing directory: {directory_name}")

for meta in (ROOT / "templates").rglob("template.yml"):
    text = meta.read_text(encoding="utf-8")

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

    if not (meta.parent / "README.md").exists():
        errors.append(f"{meta.parent}: missing README.md")

    match = re.search(
        r"^difficulty:\s*(\S+)",
        text,
        re.MULTILINE,
    )

    if match and match.group(1) not in {
        "beginner",
        "intermediate",
        "advanced",
        "professional",
    }:
        errors.append(f"{meta}: invalid difficulty")


private_key_pattern = re.compile(
    r"-----BEGIN .*PRIVATE KEY-----"
)

github_token_prefix = "gh" + "p_"
github_token_pattern = re.compile(
    rf"\b{re.escape(github_token_prefix)}[A-Za-z0-9]{{30,}}\b"
)

api_key_prefix = "sk" + "-"
api_key_pattern = re.compile(
    rf"\b{re.escape(api_key_prefix)}[A-Za-z0-9]{{30,}}\b"
)

bad_patterns = [
    private_key_pattern,
    github_token_pattern,
    api_key_pattern,
]

for path in ROOT.rglob("*"):
    if not path.is_file() or ".git" in path.parts:
        continue

    if path.suffix.lower() not in {
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
        text = path.read_text(encoding="utf-8")
    except (UnicodeDecodeError, OSError):
        continue

    for pattern in bad_patterns:
        if pattern.search(text):
            errors.append(f"possible secret in {path}")
            break

if errors:
    print("Validation failed:")
    print("\n".join(f"- {error}" for error in errors))
    raise SystemExit(1)

print("Validation passed.")
