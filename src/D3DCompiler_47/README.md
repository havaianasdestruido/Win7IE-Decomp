# D3DCompiler_47.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `f5fb4ba15e86d47f708d2ef2876de09400ab2e84d0e06df224134f178dbe870f` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/D3DCompiler_47.dll`
- Bytes: 4,158,464
- SHA-256: `f5fb4ba15e86d47f708d2ef2876de09400ab2e84d0e06df224134f178dbe870f`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x18038f360` (RVA `0x38f360`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_CUI`
- Linker: `11.0`; OS version: `6.3`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `HIGH_ENTROPY_VA`, `DYNAMIC_BASE`, `NX_COMPAT`
- Timestamp field: `2013-10-14T06:30:36Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `D3DCompiler_47.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x3bdb15 | 0x3bdc00 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0x11768 | 0x8e00 | `0x1803bf000` | 0x3be000 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x1d2f8 | 0x1d400 | `0x1803d1000` | 0x3c6e00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x1840 | 0x1a00 | `0x1803ef000` | 0x3e4200 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x440 | 0x600 | `0x1803f1000` | 0x3e5c00 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x111d6 | 0x11200 | `0x1803f2000` | 0x3e6200 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | RVA | Size |
|---|---|---:|
| `Export` | `0x3be7a0` | 0x375 |
| `Import` | `0x3ef650` | 0x64 |
| `Resource` | `0x3f1000` | 0x440 |
| `Exception` | `0x3d1000` | 0x1d2f8 |
| `BaseReloc` | `0x3f2000` | 0x7b90 |
| `Debug` | `0x10d0` | 0x1c |
| `LoadConfig` | `0xa6140` | 0x94 |
| `IAT` | `0x3ef000` | 0x650 |

## Static imports

- `ADVAPI32.dll`: 12 imports
- `KERNEL32.dll`: 68 imports
- `msvcrt.dll`: 117 imports
- `RPCRT4.dll`: 1 imports

## Delay-load imports

- None recovered.

## Exports

`D3DAssemble`, `D3DCompile`, `D3DCompile2`, `D3DCompileFromFile`, `D3DCompressShaders`, `D3DCreateBlob`, `D3DCreateFunctionLinkingGraph`, `D3DCreateLinker`, `D3DDecompressShaders`, `D3DDisassemble`, `D3DDisassemble10Effect`, `D3DDisassemble11Trace`, `D3DDisassembleRegion`, `D3DGetBlobPart`, `D3DGetDebugInfo`, `D3DGetInputAndOutputSignatureBlob`, `D3DGetInputSignatureBlob`, `D3DGetOutputSignatureBlob`, `D3DGetTraceInstructionOffsets`, `D3DLoadModule`, `D3DPreprocess`, `D3DReadFileToBlob`, `D3DReflect`, `D3DReflectLibrary`, `D3DReturnFailure1`, `D3DSetBlobPart`, `D3DStripShader`, `D3DWriteBlobToFile`, `DebugSetMute`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/D3DCompiler_47.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
