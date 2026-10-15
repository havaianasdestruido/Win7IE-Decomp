#!/usr/bin/env python3
"""Verify Phase 0 inventory coverage against the live bin/ corpus."""
from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
BIN = ROOT / "bin"
GEN = ROOT / "analysis" / "report" / "generated"


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1 << 20), b""):
            digest.update(chunk)
    return digest.hexdigest()


def index_by_path(rows: list[dict], label: str, failures: list[str]) -> dict[str, dict]:
    mapping: dict[str, dict] = {}
    for item in rows:
        path = item.get("path")
        if not path:
            failures.append(f"{label} row missing path")
            continue
        if path in mapping:
            failures.append(f"{label} duplicate path: {path}")
            continue
        mapping[path] = item
    return mapping


def expect_hashes(mapping: dict[str, dict], live_hashes: dict[str, str], label: str, failures: list[str], required: set[str] | None = None) -> None:
    paths = set(mapping)
    if required is not None and paths != required:
        missing = sorted(required - paths)
        extra = sorted(paths - required)
        if missing:
            failures.append(f"{label} missing paths: {missing[:5]}")
        if extra:
            failures.append(f"{label} extra paths: {extra[:5]}")
    for rel, rec in mapping.items():
        digest = rec.get("sha256")
        if digest is None:
            failures.append(f"{label} missing sha256: {rel}")
            continue
        live = live_hashes.get(rel)
        if live is None:
            failures.append(f"{label} path not in bin/: {rel}")
        elif digest != live:
            failures.append(f"{label} hash mismatch: {rel}")


def main() -> int:
    files = sorted(path for path in BIN.rglob("*") if path.is_file())
    hashes = json.loads((GEN / "hashes.json").read_text(encoding="utf-8"))
    inventory = json.loads((GEN / "inventory.json").read_text(encoding="utf-8"))
    pe_struct = json.loads((GEN / "pe-struct.json").read_text(encoding="utf-8"))
    rsds = json.loads((GEN / "debug-rsds.json").read_text(encoding="utf-8"))
    failures: list[str] = []

    if len(files) != 57:
        failures.append(f"bin/ contains {len(files)} files, expected 57")
    total = sum(path.stat().st_size for path in files)
    if total != 30_617_822:
        failures.append(f"bin/ totals {total} bytes, expected 30617822")

    live = {path.relative_to(ROOT).as_posix(): path for path in files}
    live_hashes = {rel: sha256_file(path) for rel, path in live.items()}
    pe_paths = {rel for rel, path in live.items() if path.read_bytes()[:2] == b"MZ"}
    code_paths = {rel for rel in pe_paths if not rel.endswith(".mui")}

    lock = index_by_path(hashes, "hashes.json", failures)
    expect_hashes(lock, live_hashes, "hashes.json", failures, set(live))

    inv_map = index_by_path(inventory, "inventory.json", failures)
    expect_hashes(inv_map, live_hashes, "inventory.json", failures, set(live))

    pe_map = index_by_path(pe_struct, "pe-struct.json", failures)
    expect_hashes(pe_map, live_hashes, "pe-struct.json", failures, pe_paths)

    rsds_map = index_by_path(rsds, "debug-rsds.json", failures)
    expect_hashes(rsds_map, live_hashes, "debug-rsds.json", failures, code_paths)

    if len(pe_paths) != 49:
        failures.append(f"PE/COFF count {len(pe_paths)}, expected 49")
    kinds = {item["kind"] for item in inventory}
    expected_kinds = {"PE/COFF", "XML", "RTF", "ICO", "UTF-16LE text", "text"}
    if kinds != expected_kinds:
        failures.append(f"inventory kinds {sorted(kinds)} != {sorted(expected_kinds)}")

    src_dirs = [path for path in (ROOT / "src").iterdir() if path.is_dir()]
    if len(src_dirs) != 49:
        failures.append(f"src/ has {len(src_dirs)} module dirs, expected 49")
    for directory in src_dirs:
        if not (directory / "README.md").is_file() or not (directory / "interfaces.h").is_file():
            failures.append(f"incomplete ledger: {directory.name}")

    if failures:
        print("FAIL")
        for item in failures:
            print(f"  - {item}")
        return 1
    print("ok: Phase 0 coverage 57/57 files, 49/49 PE images, generated records match live hashes, ledgers present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
