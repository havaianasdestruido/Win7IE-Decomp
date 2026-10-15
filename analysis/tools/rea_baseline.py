#!/usr/bin/env python3
"""Reproduce the Phase 0.4 REA 6.5.0 objdump-adapter baseline.

Captures:
  - rea-agents version
  - file_headers for bin/iexplore.exe
  - disassemble for bin/iediagcmd.exe

Writes under analysis/report/rea/. Never writes bin/.
"""
from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
REA_DIR = ROOT / "analysis" / "report" / "rea"
NPX = ["npx", "-y", "rea-agents@6.5.0"]


def run(args: list[str], dest: Path | None = None) -> subprocess.CompletedProcess[str]:
    print("+", " ".join(args), flush=True)
    proc = subprocess.run(args, cwd=ROOT, text=True, capture_output=True)
    if dest is not None:
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_text(proc.stdout, encoding="utf-8")
        if proc.stderr:
            dest.with_suffix(dest.suffix + ".stderr").write_text(proc.stderr, encoding="utf-8")
    return proc


def main() -> int:
    version = run(NPX + ["--version"], REA_DIR / "version.txt")
    if version.returncode != 0:
        print(version.stderr, file=sys.stderr)
        return version.returncode

    headers = run(
        NPX + ["inspect-with-objdump", str(ROOT / "bin" / "iexplore.exe"), "file_headers", "--json"],
        REA_DIR / "iexplore-file-headers.json",
    )
    disasm = run(
        NPX + ["inspect-with-objdump", str(ROOT / "bin" / "iediagcmd.exe"), "disassemble", "--json"],
        REA_DIR / "iediagcmd-disassembly.json",
    )
    # Intentionally unsupported operation: keep the validation failure as evidence.
    bad = run(
        NPX + ["inspect-with-objdump", str(ROOT / "bin" / "iexplore.exe"), "headers", "--json"],
        REA_DIR / "iexplore-headers.json",
    )

    summary = {
        "version_exit": version.returncode,
        "file_headers_exit": headers.returncode,
        "disassemble_exit": disasm.returncode,
        "unsupported_headers_exit": bad.returncode,
        "version": (REA_DIR / "version.txt").read_text(encoding="utf-8").strip(),
    }
    print(json.dumps(summary, indent=2))
    return 0 if headers.returncode == 0 and disasm.returncode == 0 else 1


if __name__ == "__main__":
    raise SystemExit(main())
