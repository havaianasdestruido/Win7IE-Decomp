#pragma once
/*
 * Evidence ledger for sqmapi.dll
 * SHA-256: ab65e97c8405660a881163957ef1fc29df0e1627eef04b282b3f6825eb78e4c2
 *
 * Observed exports (names/ordinals only; types and calling
 * conventions are not asserted in Phase 0):
 *   SqmAddToAverage  @ ordinal 12
 *   SqmAddToStream  @ ordinal 13
 *   SqmAddToStreamDWord  @ ordinal 14
 *   SqmAddToStreamDWord64  @ ordinal 15
 *   SqmAddToStreamString  @ ordinal 16
 *   SqmAddToStreamV  @ ordinal 17
 *   SqmCheckEscalationAddToStreamDWord  @ ordinal 2
 *   SqmCheckEscalationAddToStreamDWord64  @ ordinal 1
 *   SqmCheckEscalationAddToStreamString  @ ordinal 3
 *   SqmCheckEscalationSetDWord  @ ordinal 5
 *   SqmCheckEscalationSetDWord64  @ ordinal 4
 *   SqmCheckEscalationSetString  @ ordinal 6
 *   SqmCleanup  @ ordinal 18
 *   SqmClearFlags  @ ordinal 19
 *   SqmCreateNewId  @ ordinal 20
 *   SqmEndSession  @ ordinal 21
 *   SqmEndSessionEx  @ ordinal 22
 *   SqmFlushSession  @ ordinal 23
 *   SqmGetEnabled  @ ordinal 24
 *   SqmGetEscalationRuleStatus  @ ordinal 7
 *   SqmGetFlags  @ ordinal 25
 *   SqmGetInstrumentationProperty  @ ordinal 8
 *   SqmGetLastUploadTime  @ ordinal 26
 *   SqmGetMachineId  @ ordinal 27
 *   SqmGetSession  @ ordinal 28
 *   SqmGetSessionStartTime  @ ordinal 29
 *   SqmGetUserId  @ ordinal 30
 *   SqmIncrement  @ ordinal 31
 *   SqmIsNamespaceEnabled  @ ordinal 32
 *   SqmIsWindowsOptedIn  @ ordinal 33
 *   SqmLoadEscalationManifest  @ ordinal 9
 *   SqmReadSharedMachineId  @ ordinal 34
 *   SqmReadSharedUserId  @ ordinal 35
 *   SqmSet  @ ordinal 36
 *   SqmSetAppId  @ ordinal 37
 *   SqmSetAppVersion  @ ordinal 38
 *   SqmSetBits  @ ordinal 39
 *   SqmSetBool  @ ordinal 40
 *   SqmSetCurrentTimeAsUploadTime  @ ordinal 41
 *   SqmSetDWord64  @ ordinal 42
 *   SqmSetEnabled  @ ordinal 43
 *   SqmSetEscalationInfo  @ ordinal 10
 *   SqmSetFlags  @ ordinal 44
 *   SqmSetIfMax  @ ordinal 45
 *   SqmSetIfMin  @ ordinal 46
 *   SqmSetMachineId  @ ordinal 47
 *   SqmSetString  @ ordinal 48
 *   SqmSetUserId  @ ordinal 49
 *   SqmStartSession  @ ordinal 50
 *   SqmStartUpload  @ ordinal 51
 *   SqmStartUploadEx  @ ordinal 52
 *   SqmSysprepCleanup  @ ordinal 53
 *   SqmSysprepGeneralize  @ ordinal 54
 *   SqmSysprepSpecialize  @ ordinal 55
 *   SqmTimerAccumulate  @ ordinal 56
 *   SqmTimerAddToAverage  @ ordinal 57
 *   SqmTimerRecord  @ ordinal 58
 *   SqmTimerStart  @ ordinal 59
 *   SqmUnattendedSetup  @ ordinal 60
 *   SqmUnloadEscalationManifest  @ ordinal 11
 *   SqmWaitForUploadComplete  @ ordinal 61
 *   SqmWriteSharedMachineId  @ ordinal 62
 *   SqmWriteSharedUserId  @ ordinal 63
 *
 * No callable declarations are emitted until signatures are recovered.
 */

