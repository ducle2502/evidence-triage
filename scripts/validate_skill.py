#!/usr/bin/env python3
"""Validate the evidence-triage skill package.

Checks:
- SKILL.md frontmatter (name, description, version)
- Reference table parity between SKILL.md and references/
- Required docs and assets
- Unreplaced template placeholders
- Common secret patterns

Uses only the Python standard library.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
SKILL = ROOT / "SKILL.md"
REFERENCE_DIR = ROOT / "references"

REQUIRED_FILES = [
    ROOT / "README.md",
    ROOT / "README.vi.md",
    ROOT / "LICENSE",
    ROOT / "CONTRIBUTING.md",
    ROOT / "SECURITY.md",
    ROOT / "CODE_OF_CONDUCT.md",
    ROOT / "VISION.md",
    ROOT / "CHANGELOG.md",
    ROOT / "docs" / "ARCHITECTURE.md",
    ROOT / "docs" / "GITHUB_SETUP.md",
    ROOT / "assets" / "banner.svg",
    ROOT / "assets" / "banner-dark.svg",
    ROOT / "assets" / "social-preview.png",
]

SECRET_PATTERNS = [
    re.compile(r"ghp_[A-Za-z0-9]{20,}"),
    re.compile(r"sk-[A-Za-z0-9]{20,}"),
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
]

PLACEHOLDER_PATTERNS = [
    re.compile(r"OWNER/REPO"),
    re.compile(r"PROJECT_NAME"),
    re.compile(r"OWNER_USERNAME"),
]

SCAN_SUFFIXES = {".md", ".py", ".yml", ".yaml", ".json", ".jsonc", ".toml"}
SKIP_PARTS = {".git", "node_modules", "__pycache__"}
SKIP_FILES = {Path(__file__).resolve()}

errors: list[str] = []


def fail(message: str) -> None:
    errors.append(message)
    print(f"FAIL {message}")


def ok(message: str) -> None:
    print(f"OK   {message}")


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def check_frontmatter() -> str:
    if not SKILL.is_file():
        fail("SKILL.md is missing")
        sys.exit(1)

    text = read(SKILL)
    if not text.startswith("---\n"):
        fail("SKILL.md does not start with YAML frontmatter")
        return text

    parts = text.split("---", 2)
    if len(parts) < 3:
        fail("SKILL.md frontmatter is not closed with ---")
        return text

    front: dict[str, str] = {}
    for line in parts[1].splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            front[key.strip()] = value.strip()

    for key in ("name", "description", "version"):
        if not front.get(key):
            fail(f"SKILL.md frontmatter is missing '{key}'")

    if front.get("name") and front["name"] != "evidence-triage":
        fail(f"SKILL.md name is '{front['name']}', expected 'evidence-triage'")

    version = front.get("version", "")
    if version and not re.fullmatch(r"\d+\.\d+\.\d+", version):
        fail(f"SKILL.md version '{version}' is not semver")

    if front.get("description") and len(front["description"]) < 80:
        fail("SKILL.md description is too short to trigger reliably")

    ok("SKILL.md frontmatter")
    return text


def check_references(text: str) -> int:
    if not REFERENCE_DIR.is_dir():
        fail("references/ directory is missing")
        return 0

    files = sorted(path.name for path in REFERENCE_DIR.glob("*.md"))
    if not files:
        fail("references/ contains no Markdown files")
        return 0

    english = [name for name in files if not name.endswith(".vi.md")]
    vietnamese = [name for name in files if name.endswith(".vi.md")]

    for name in english:
        if name not in text:
            fail(f"references/{name} is not listed in SKILL.md")

    for name in vietnamese:
        base = name[: -len(".vi.md")] + ".md"
        if not (REFERENCE_DIR / base).is_file():
            fail(f"references/{name} has no English source {base}")
        if base not in text:
            fail(f"references/{name} has no listed English source {base}")

    listed = set(re.findall(r"references/([A-Za-z0-9._-]+\.md)", text))
    for name in sorted(listed):
        if not (REFERENCE_DIR / name).is_file():
            fail(f"SKILL.md lists references/{name}, which does not exist")

    ok(
        "reference table parity "
        f"({len(english)} English files, {len(vietnamese)} Vietnamese translations)"
    )
    return len(files)


def check_required_files() -> None:
    missing = [str(path.relative_to(ROOT)) for path in REQUIRED_FILES if not path.is_file()]
    for name in missing:
        fail(f"required file is missing: {name}")
    if not missing:
        ok(f"required files ({len(REQUIRED_FILES)})")


def check_license() -> None:
    license_path = ROOT / "LICENSE"
    if not license_path.is_file():
        return
    text = read(license_path)
    for marker in ("MIT License", "Finic", "duke2502"):
        if marker not in text:
            fail(f"LICENSE is missing '{marker}'")
    ok("LICENSE attribution")


def check_public_hygiene() -> None:
    problems = 0
    for path in ROOT.rglob("*"):
        if not path.is_file():
            continue
        if path.resolve() in SKIP_FILES:
            continue
        if any(part in SKIP_PARTS for part in path.parts):
            continue
        if path.suffix.lower() not in SCAN_SUFFIXES:
            continue

        try:
            content = read(path)
        except UnicodeDecodeError:
            continue

        relative = path.relative_to(ROOT)
        for pattern in SECRET_PATTERNS:
            if pattern.search(content):
                fail(f"possible secret in {relative}")
                problems += 1
        for pattern in PLACEHOLDER_PATTERNS:
            if pattern.search(content):
                fail(f"unreplaced placeholder in {relative}")
                problems += 1

    if problems == 0:
        ok("public hygiene scan")


def main() -> int:
    text = check_frontmatter()
    reference_count = check_references(text)
    check_required_files()
    check_license()
    check_public_hygiene()

    if errors:
        print(f"\n{len(errors)} error(s).")
        return 1

    print(f"\nValidation passed: {reference_count} reference files.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
