# Validation

## Performed

- Re-ran `analysis/tools/inventory.py`: all 57 inputs hashed and all 49 PE images parsed without modifying `bin/`.
- Cross-checked `iexplore.exe` using direct GNU objdump and REA's GNU objdump adapter. Both report `pei-x86-64`, architecture `i386:x86-64`, entry `0x1400019f0`; REA reports unchanged pre/post SHA-256 `cff801d6dc847bb832d0077ce38ddb66ef5b4637ff947bbdbc228eef10494f97`.
- REA's disassembly observation for `iediagcmd.exe` completed with captured artifact identity. Direct header inspection independently confirms the CLR runtime directory and `_CorExeMain` import.
- Original binaries remain unmodified according to Git status (all generated changes are outside `bin/`).

## Not performed

No reconstructed module was compiled because no evidence-supported compatibility implementation exists. No original executable was launched, and no behavioral equivalence, edge-case handling, or runtime success is claimed. No signing validation or symbol-server retrieval was performed.

## Known discrepancies and risks

GNU objdump textual parsing is version-sensitive; retained raw output is authoritative. Import names do not establish prototypes. PE timestamp values are not trusted. Resource-only classification is based on zero entrypoint/no imports and is therefore strongly supported but remains a structural characterization, not proof of every loader behavior.