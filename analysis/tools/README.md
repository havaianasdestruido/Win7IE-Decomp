# Analysis tools

Phase 0 tooling inventories the read-only `bin/` corpus, parses PE/COFF structure, and emits evidence ledgers. Nothing in this directory writes inside `bin/`.

## `pe.py`

Stdlib PE32/PE32+ parser. Extracts COFF/optional headers, section table, data directories, static IAT, delay-load IAT, EAT, and CodeView `RSDS` debug records.

```sh
python3 analysis/tools/pe.py bin/iexplore.exe
```

## `test_pe.py`

Locks known structural facts (hashes, entry RVA, sections, delay-load, CLR, export names) against representative corpus images.

```sh
python3 analysis/tools/test_pe.py
```

## `inventory.py`

Recursively inventories `bin/`, computes SHA-256, classifies files by magic bytes, invokes GNU `objdump -x` (raw output retained), parses PE images with `pe.py`, and regenerates reports plus per-image ledgers.

```sh
python3 analysis/tools/inventory.py
```

Outputs (all outside `bin/`):

- `analysis/report/generated/hashes.json` — compact cryptographic lock
- `analysis/report/generated/inventory.json` — per-file identity + PE summary
- `analysis/report/generated/pe-struct.json` — full parsed PE structure
- `analysis/report/generated/dependencies.json` — static and delay-load edges
- `analysis/report/generated/debug-rsds.json` — CodeView RSDS PDB filename/GUID/Age tuples
- `analysis/report/generated/*.objdump.txt` — authoritative GNU objdump `-x` text
- `analysis/report/inventory.md`, `api-map.md`, `dependencies.md`
- `src/<module>/README.md` and `src/<module>/interfaces.h`

Dependencies: Python 3.11+ and GNU objdump (validated with 2.40). GNU textual output is version-sensitive; raw objdump text remains authoritative when a parser field is disputed.

## `verify_phase0.py`

Re-hashes `bin/`, checks 57/49 coverage, and confirms generated lock files still match the corpus.

```sh
python3 analysis/tools/verify_phase0.py
```

## REA baseline

REA 6.5.0 commands used for Phase 0.4 are recorded in `analysis/report/methodology.md` and can be reproduced with:

```sh
python3 analysis/tools/rea_baseline.py
```

REA is not a substitute for the stdlib parser: it binds GNU objdump observations and artifact hashes. Typed native decompilation still requires a Hopper/Ghidra/IDA provider (Phase 1).
