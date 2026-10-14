# Analysis tools

## `inventory.py`

Recursively inventories `bin/`, computes SHA-256, classifies `MZ` inputs, invokes caller-supplied GNU `objdump -x`, conservatively extracts PE architecture/entrypoint/sections/imports/exports, and generates reports plus per-image ledgers.

```sh
python3 analysis/tools/inventory.py
```

Dependencies: Python 3.11+ and GNU objdump (validated with 2.40). Inputs are read-only. Outputs are overwritten under `analysis/report/generated/`, `analysis/report/inventory.md`, `analysis/report/api-map.md`, and matching `src/` module ledgers. Limitations: GNU textual output is not stable across versions; raw output is retained as authority; this is structural inspection, not decompilation; imports do not establish prototypes or executed paths.

REA is invoked directly with the reproducible commands in `analysis/report/methodology.md`; no redundant wrapper was created.