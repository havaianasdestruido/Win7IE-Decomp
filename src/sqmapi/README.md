# sqmapi.dll

> Evidence status: header, section, import/export, delay-load, and debug-directory facts below are verified against SHA-256 `ab65e97c8405660a881163957ef1fc29df0e1627eef04b282b3f6825eb78e4c2` using the stdlib PE parser and GNU objdump. Function types and behavior have not been guessed.

## Image

- Path: `bin/sqmapi.dll`
- Bytes: 286,088
- SHA-256: `ab65e97c8405660a881163957ef1fc29df0e1627eef04b282b3f6825eb78e4c2`
- Format: `PE32+`
- Machine: `IMAGE_FILE_MACHINE_AMD64`
- Entry point: `0x1800014d4` (RVA `0x14d4`)
- ImageBase: `0x180000000`
- Subsystem: `IMAGE_SUBSYSTEM_WINDOWS_GUI`
- Linker: `10.10`; OS version: `6.2`
- Characteristics: `EXECUTABLE_IMAGE`, `LARGE_ADDRESS_AWARE`, `DLL`
- DllCharacteristics: `DYNAMIC_BASE`, `NX_COMPAT`
- Timestamp field: `2012-07-26T01:32:17Z` (untrusted PE metadata)
- CLR header present: `False`
- CodeView PDB: `sqmapi.pdb`

## Sections

| Name | Virtual size | Raw size | VMA | File offset | Characteristics |
|---|---:|---:|---|---:|---|
| `.text` | 0x3e3d8 | 0x3e400 | `0x180001000` | 0x400 | CNT_CODE, MEM_EXECUTE, MEM_READ |
| `.data` | 0xce4 | 0xe00 | `0x180040000` | 0x3e800 | CNT_INITIALIZED_DATA, MEM_READ, MEM_WRITE |
| `.pdata` | 0x21d8 | 0x2200 | `0x180041000` | 0x3f600 | CNT_INITIALIZED_DATA, MEM_READ |
| `.idata` | 0x1b42 | 0x1c00 | `0x180044000` | 0x41800 | CNT_INITIALIZED_DATA, MEM_READ |
| `.rsrc` | 0x400 | 0x400 | `0x180046000` | 0x43400 | CNT_INITIALIZED_DATA, MEM_READ |
| `.reloc` | 0x204 | 0x400 | `0x180047000` | 0x43800 | CNT_INITIALIZED_DATA, MEM_DISCARDABLE, MEM_READ |

## Data directories (non-empty)

| Name | Address | Kind | Size |
|---|---|---|---:|
| `Export` | `0x7490` | RVA | 0x750 |
| `Import` | `0x44658` | RVA | 0x8c |
| `Resource` | `0x46000` | RVA | 0x400 |
| `Exception` | `0x41000` | RVA | 0x21d8 |
| `Security` | `0x43c00` | file offset | 0x2188 |
| `BaseReloc` | `0x47000` | RVA | 0x204 |
| `Debug` | `0x3b194` | RVA | 0x38 |
| `LoadConfig` | `0x3ab60` | RVA | 0x70 |
| `IAT` | `0x44000` | RVA | 0x658 |
| `DelayImport` | `0x3ac04` | RVA | 0xc0 |

## Static imports

- `ADVAPI32.dll`: 36 imports
- `KERNEL32.dll`: 97 imports
- `msvcrt.dll`: 52 imports
- `ntdll.dll`: 4 imports
- `RPCRT4.dll`: 3 imports
- `USER32.dll`: 5 imports

## Delay-load imports

- `Cabinet.dll`: 7 delay-load imports
- `CRYPT32.dll`: 4 delay-load imports
- `ole32.dll`: 6 delay-load imports
- `WINHTTP.dll`: 20 delay-load imports
- `XmlLite.dll`: 2 delay-load imports

## Exports

`SqmAddToAverage`, `SqmAddToStream`, `SqmAddToStreamDWord`, `SqmAddToStreamDWord64`, `SqmAddToStreamString`, `SqmAddToStreamV`, `SqmCheckEscalationAddToStreamDWord`, `SqmCheckEscalationAddToStreamDWord64`, `SqmCheckEscalationAddToStreamString`, `SqmCheckEscalationSetDWord`, `SqmCheckEscalationSetDWord64`, `SqmCheckEscalationSetString`, `SqmCleanup`, `SqmClearFlags`, `SqmCreateNewId`, `SqmEndSession`, `SqmEndSessionEx`, `SqmFlushSession`, `SqmGetEnabled`, `SqmGetEscalationRuleStatus`, `SqmGetFlags`, `SqmGetInstrumentationProperty`, `SqmGetLastUploadTime`, `SqmGetMachineId`, `SqmGetSession`, `SqmGetSessionStartTime`, `SqmGetUserId`, `SqmIncrement`, `SqmIsNamespaceEnabled`, `SqmIsWindowsOptedIn`, `SqmLoadEscalationManifest`, `SqmReadSharedMachineId`, `SqmReadSharedUserId`, `SqmSet`, `SqmSetAppId`, `SqmSetAppVersion`, `SqmSetBits`, `SqmSetBool`, `SqmSetCurrentTimeAsUploadTime`, `SqmSetDWord64`, `SqmSetEnabled`, `SqmSetEscalationInfo`, `SqmSetFlags`, `SqmSetIfMax`, `SqmSetIfMin`, `SqmSetMachineId`, `SqmSetString`, `SqmSetUserId`, `SqmStartSession`, `SqmStartUpload`, `SqmStartUploadEx`, `SqmSysprepCleanup`, `SqmSysprepGeneralize`, `SqmSysprepSpecialize`, `SqmTimerAccumulate`, `SqmTimerAddToAverage`, `SqmTimerRecord`, `SqmTimerStart`, `SqmUnattendedSetup`, `SqmUnloadEscalationManifest`, `SqmWaitForUploadComplete`, `SqmWriteSharedMachineId`, `SqmWriteSharedUserId`

## Reconstruction status

No compatibility implementation is emitted: available evidence is insufficient to assign semantics safely. Raw structural evidence is in `analysis/report/generated/sqmapi.dll.objdump.txt` and `analysis/report/generated/pe-struct.json`.
