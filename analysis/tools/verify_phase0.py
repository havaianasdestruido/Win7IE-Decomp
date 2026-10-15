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


def main() -> int:
    files = sorted(path for path in BIN.rglob("*") if path.is_file())
    hashes = json.loads((GEN / "hashes.json").read_text(encoding="utf-8"))
    inventory = json.loads((GEN / "inventory.json").read_text(encoding="utf-8"))
    pe_struct = json.loads((GEN / "pe-struct.json").read_text(encoding="utf-8"))
    failures: list[str] = []

    if len(files) != 57:
        failures.append(f"bin/ contains {len(files)} files, expected 57")
    total = sum(path.stat().st_size for path in files)
    if total != 30_617_822:
        failures.append(f"bin/ totals {total} bytes, expected 30617822")

    lock = {item["path"]: item for item in hashes}
    live = {path.relative_to(ROOT).as_posix(): path for path in files}
    if set(lock) != set(live):
        failures.append("hashes.json path set does not match bin/")

    pe_count = 0
    for rel, path in live.items():
        digest = sha256_file(path)
        rec = lock.get(rel)
        if rec is None:
            continue
        if rec["sha256"] != digest:
            failures.append(f"hash mismatch: {rel}")
        if rec["size"] != path.stat().st_size:
            failures.append(f"size mismatch: {rel}")
        if path.read_bytes()[:2] == b"MZ":
            pe_count += 1

    if pe_count != 49:
        failures.append(f"PE/COFF count {pe_count}, expected 49")
    if len(pe_struct) != 49:
        failures.append(f"pe-struct.json has {len(pe_struct)} images, expected 49")
    if len(inventory) != 57:
        failures.append(f"inventory.json has {len(inventory)} rows, expected 57")

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
    print("ok: Phase 0 coverage 57/57 files, 49/49 PE images, hashes match, ledgers present")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
