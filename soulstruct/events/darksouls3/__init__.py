from .core import EMEVD, convert_events, compare_events
import soulstruct.maps.darksouls3.maps as constants
from soulstruct.maps.darksouls3.maps import *
from . import instructions
from .instructions import *
from . import tests
from .tests import *
from . import enums
from .enums import *
from . import decompiler

name = "darksouls3"

__all__ = [
    # EMEVD class
    "EMEVD",
    # Sub-packages / package attributes (contents of constants, instructions, and tests are also in this namespace)
    "constants",
    "instructions",
    "tests",
    "enums",
    "name",
    "decompiler",
    # File utilities
    "convert_events",
    "compare_events",
    # Dark Souls 3 map constants
    "COMMON",
    "COMMON_FUNC",
    "HIGH_WALL_OF_LOTHRIC",
    "LOTHRIC_CASTLE",
    "UNDEAD_SETTLEMENT",
    "ARCHDRAGON_PEAK",
    "FARRON_KEEP",
    "GRAND_ARCHIVES",
    "CATHEDRAL_OF_THE_DEEP",
    "IRITHYLL",
    "CATACOMBS_OF_CARTHUS",
    "PROFANED_CAPITAL",
    "FIRELINK_SHRINE",
    "KILN_OF_THE_FIRST_FLAME",
    "PAINTED_WORLD_OF_ARIANDEL",
    "ARENA_GRAND_ROOF",
    "ARENA_KILN_OF_FLAME",
    "DREG_HEAP",
    "RINGED_CITY",
    "ARENA_DRAGON_RUINS",
    "ARENA_ROUND_PLAZA",
    # Shared instructions
    "RunEvent",
    "Wait",
    "WaitFrames",
    "WaitRandomSeconds",
    "WaitRandomFrames",
    "WaitForNetworkApproval",
    "SetCharacterState",
    "EnableCharacter",
    "DisableCharacter",
    "SetAIState",
    "EnableAI",
    "DisableAI",
    "SetTeamType",
    "Kill",
    "EzstateAIRequest",
    "CancelSpecialEffect",
    "ResetStandbyAnimationSettings",
    "SetStandbyAnimationSettings",
    "SetGravityState",
    "EnableGravity",
    "DisableGravity",
    "SetCharacterEventTarget",
    "SetImmortalityState",
    "EnableImmortality",
    "DisableImmortality",
    "SetNest",
    "SetInvincibilityState",
    "EnableInvincibility",
    "DisableInvincibility",
    "ClearTargetList",
    "AICommand",
    "SetEventPoint",
    "SetAIParamID",
    "ReplanAI",
    "CreateNPCPart",
    "SetNPCPartHealth",
    "SetNPCPartEffects",
    "SetNPCPartBulletDamageScaling",
    "SetDisplayMask",
    "SetCollisionMask",
    "SetNetworkUpdateAuthority",
    "SetBackreadState",
    "EnableBackread",
    "DisableBackread",
    "SetHealthBarState",
    "EnableHealthBar",
    "DisableHealthBar",
    "SetCharacterCollisionState",
    "EnableCharacterCollision",
    "DisableCharacterCollision",
    "AIEvent",
    "ReferDamageToEntity",
    "SetNetworkUpdateRate",
    "SetBackreadStateAlternate",
    "DropMandatoryTreasure",
    "SetTeamTypeAndExitStandbyAnimation",
    "HumanityRegistration",
    "ResetAnimation",
    "ActivateMultiplayerBuffs",
    "SetObjectState",
    "EnableObject",
    "DisableObject",
    "DestroyObject",
    "RestoreObject",
    "SetTreasureState",
    "EnableTreasure",
    "DisableTreasure",
    "ActivateObject",
    "SetObjectActivation",
    "SetObjectActivationWithIdx",
    "EnableObjectActivation",
    "DisableObjectActivation",
    "PostDestruction",
    "CreateHazard",
    "RegisterStatue",
    "RemoveObjectFlag",
    "SetObjectInvulnerability",
    "EnableObjectInvulnerability",
    "DisableObjectInvulnerability",
    "EnableTreasureCollection",
    "SetFlagState",
    "EnableFlag",
    "DisableFlag",
    "ToggleFlag",
    "SetRandomFlagInRange",
    "EnableRandomFlagInRange",
    "DisableRandomFlagInRange",
    "ToggleRandomFlagInRange",
    "SetFlagRangeState",
    "EnableFlagRange",
    "DisableFlagRange",
    "ChangeFlagRange",
    "IncrementEventValue",
    "ClearEventValue",
    "EnableThisFlag",
    "DisableThisFlag",
    "SetEventState",
    "StopEvent",
    "RestartEvent",
    "SetCollisionState",
    "EnableCollision",
    "DisableCollision",
    "SetCollisionBackreadMaskState",
    "EnableCollisionBackreadMask",
    "DisableCollisionBackreadMask",
    "AwardItemLot",
    "AwardItemLotToHostOnly",
    "RemoveItemFromPlayer",
    "RemoveWeaponFromPlayer",
    "RemoveArmorFromPlayer",
    "RemoveRingFromPlayer",
    "RemoveGoodFromPlayer",
    "SnugglyItemDrop",
    "SetNextSnugglyTrade",
    "RequestAnimation",
    "ForceAnimation",
    "SetAnimationsState",
    "EnableAnimations",
    "DisableAnimations",
    "EndOfAnimation",
    "CreateFX",
    "DeleteFX",
    "CreateTemporaryFX",
    "CreateObjectFX",
    "DeleteObjectFX",
    "SetBackgroundMusic",
    "PlaySoundEffect",
    "SetSoundEventState",
    "EnableSoundEvent",
    "DisableSoundEvent",
    "RegisterLadder",
    "RegisterBonfire",
    "SetMapPieceState",
    "DisableMapPiece",
    "EnableMapPiece",
    "PlaceSummonSign",
    "SetDeveloperMessageState",
    "EnableSoapstoneMessage",
    "DisableSoapstoneMessage",
    "DisplayDialog",
    "DisplayBanner",
    "DisplayStatus",
    "DisplayBattlefieldMessage",
    "PlayCutscene",
    "PlayCutsceneAndMovePlayer",
    "PlayCutsceneToPlayer",
    "PlayCutsceneAndMoveSpecificPlayer",
    "PlayCutsceneAndRotatePlayer",
    "SetNavmeshType",
    "EnableNavmeshType",
    "DisableNavmeshType",
    "ToggleNavmeshType",
    "SetNetworkSync",
    "EnableNetworkSync",
    "DisableNetworkSync",
    "ClearMainCondition",
    "IssuePrefetchRequest",
    "SaveRequest",
    "TriggerMultiplayerEvent",
    "SetVagrantSpawning",
    "EnableVagrantSpawning",
    "DisableVagrantSpawning",
    "IncrementPvPSin",
    "NotifyBossBattleStart",
    "SetSpawnerState",
    "EnableSpawner",
    "DisableSpawner",
    "ShootProjectile",
    "CreateProjectileOwner",
    "WarpToMap",
    "MoveRemains",
    "Move",
    "MoveToEntity",
    "MoveAndSetDrawParent",
    "ShortMove",
    "MoveAndCopyDrawParent",
    "MoveObjectToCharacter",
    "SetRespawnPoint",
    "KillBoss",
    "IncrementNewGameCycle",
    "AwardAchievement",
    "BetrayCurrentCovenant",
    "EqualRecovery",
    "ChangeCamera",
    "SetCameraVibration",
    "SetLockedCameraSlot",
    "HellkiteBreathControl",
    "SetMapDrawParamSlot",
    # Line-for-line control flow instructions (high-level Python blocks are recommended instead)
    "SkipLines",
    "Terminate",
    "End",
    "Restart",
    "IfValueComparison",
    "AwaitConditionState",
    "AwaitConditionTrue",
    "AwaitConditionFalse",
    "SkipLinesIfConditionState",
    "SkipLinesIfConditionTrue",
    "SkipLinesIfConditionFalse",
    "SkipLinesIfFinishedConditionState",
    "SkipLinesIfFinishedConditionTrue",
    "SkipLinesIfFinishedConditionFalse",
    "TerminateIfConditionState",
    "EndIfConditionTrue",
    "EndIfConditionFalse",
    "RestartIfConditionTrue",
    "RestartIfConditionFalse",
    "TerminateIfFinishedConditionState",
    "EndIfFinishedConditionTrue",
    "EndIfFinishedConditionFalse",
    "RestartIfFinishedConditionTrue",
    "RestartIfFinishedConditionFalse",
    "IfConditionState",
    "IfConditionTrue",
    "IfConditionFalse",
    "IfTimeElapsed",
    "IfFramesElapsed",
    "IfRandomTimeElapsed",
    "IfRandomFramesElapsed",
    "SkipLinesIfMapPresenceState",
    "SkipLinesIfInsideMap",
    "SkipLinesIfOutsideMap",
    "TerminateIfMapPresenceState",
    "EndIfInsideMap",
    "EndIfOutsideMap",
    "RestartIfInsideMap",
    "RestartIfOutsideMap",
    "IfMapPresenceState",
    "IfInsideMap",
    "IfOutsideMap",
    "IfMultiplayerEvent",
    "AwaitFlagState",
    "AwaitThisEventOn",
    "AwaitThisEventOff",
    "AwaitThisEventSlotOn",
    "AwaitThisEventSlotOff",
    "AwaitFlagOn",
    "AwaitFlagOff",
    "AwaitFlagChange",
    "SkipLinesIfFlagState",
    "SkipLinesIfThisEventOn",
    "SkipLinesIfThisEventOff",
    "SkipLinesIfThisEventSlotOn",
    "SkipLinesIfThisEventSlotOff",
    "SkipLinesIfFlagOn",
    "SkipLinesIfFlagOff",
    "TerminateIfFlagState",
    "EndIfThisEventOn",
    "EndIfThisEventOff",
    "EndIfThisEventSlotOn",
    "EndIfThisEventSlotOff",
    "EndIfFlagOn",
    "EndIfFlagOff",
    "RestartIfThisEventOn",
    "RestartIfThisEventOff",
    "RestartIfThisEventSlotOn",
    "RestartIfThisEventSlotOff",
    "RestartIfFlagOn",
    "RestartIfFlagOff",
    "IfFlagState",
    "IfThisEventOn",
    "IfThisEventOff",
    "IfThisEventSlotOn",
    "IfThisEventSlotOff",
    "IfFlagOn",
    "IfFlagOff",
    "IfFlagChange",
    "SkipLinesIfFlagRangeState",
    "SkipLinesIfFlagRangeAllOn",
    "SkipLinesIfFlagRangeAllOff",
    "SkipLinesIfFlagRangeAnyOn",
    "SkipLinesIfFlagRangeAnyOff",
    "TerminateIfFlagRangeState",
    "EndIfFlagRangeAllOn",
    "EndIfFlagRangeAllOff",
    "EndIfFlagRangeAnyOn",
    "EndIfFlagRangeAnyOff",
    "RestartIfFlagRangeAllOn",
    "RestartIfFlagRangeAllOff",
    "RestartIfFlagRangeAnyOn",
    "RestartIfFlagRangeAnyOff",
    "IfFlagRangeState",
    "IfFlagRangeAllOn",
    "IfFlagRangeAllOff",
    "IfFlagRangeAnyOn",
    "IfFlagRangeAnyOff",
    "IfTrueFlagCountComparison",
    "IfTrueFlagCountEqual",
    "IfTrueFlagCountNotEqual",
    "IfTrueFlagCountGreaterThan",
    "IfTrueFlagCountLessThan",
    "IfTrueFlagCountGreaterThanOrEqual",
    "IfTrueFlagCountLessThanOrEqual",
    "IfEventValueComparison",
    "IfEventValueEqual",
    "IfEventValueNotEqual",
    "IfEventValueGreaterThan",
    "IfEventValueLessThan",
    "IfEventValueGreaterThanOrEqual",
    "IfEventValueLessThanOrEqual",
    "IfEventsComparison",
    "IfCharacterRegionState",
    "IfCharacterInsideRegion",
    "IfCharacterOutsideRegion",
    "IfPlayerInsideRegion",
    "IfPlayerOutsideRegion",
    "IfAllPlayersRegionState",
    "IfAllPlayersInsideRegion",
    "IfAllPlayersOutsideRegion",
    "IfEntityDistanceState",
    "IfEntityWithinDistance",
    "IfEntityBeyondDistance",
    "IfPlayerWithinDistance",
    "IfPlayerBeyondDistance",
    "IfPlayerItemStateNoBox",
    "IfPlayerItemStateBox",
    "IfPlayerItemState",
    "IfPlayerHasItem",
    "IfPlayerHasWeapon",
    "IfPlayerHasArmor",
    "IfPlayerHasRing",
    "IfPlayerHasGood",
    "IfPlayerDoesNotHaveItem",
    "IfPlayerDoesNotHaveWeapon",
    "IfPlayerDoesNotHaveArmor",
    "IfPlayerDoesNotHaveRing",
    "IfPlayerDoesNotHaveGood",
    "IfAnyItemDroppedInRegion",
    "IfItemDropped",
    "AwaitObjectDestructionState",
    "AwaitObjectDestroyed",
    "AwaitObjectNotDestroyed",
    "SkipLinesIfObjectDestructionState",
    "SkipLinesIfObjectDestroyed",
    "SkipLinesIfObjectNotDestroyed",
    "TerminateIfObjectDestructionState",
    "EndIfObjectDestroyed",
    "EndIfObjectNotDestroyed",
    "RestartIfObjectDestroyed",
    "RestartIfObjectNotDestroyed",
    "IfObjectDestructionState",
    "IfObjectDestroyed",
    "IfObjectNotDestroyed",
    "IfObjectDamagedBy",
    "IfObjectActivated",
    "IfObjectHealthValueComparison",
    "IfMovingOnCollision",
    "IfRunningOnCollision",
    "IfStandingOnCollision",
    "SkipLinesIfComparison",
    "SkipLinesIfEqual",
    "SkipLinesIfNotEqual",
    "SkipLinesIfGreaterThan",
    "SkipLinesIfLessThan",
    "SkipLinesIfGreaterThanOrEqual",
    "SkipLinesIfLessThanOrEqual",
    "TerminateIfComparison",
    "EndIfEqual",
    "EndIfNotEqual",
    "EndIfGreaterThan",
    "EndIfLessThan",
    "EndIfGreaterThanOrEqual",
    "EndIfLessThanOrEqual",
    "RestartIfEqual",
    "RestartIfNotEqual",
    "RestartIfGreaterThan",
    "RestartIfLessThan",
    "RestartIfGreaterThanOrEqual",
    "RestartIfLessThanOrEqual",
    "IfActionButton",
    "IfWorldTendencyComparison",
    "IfWhiteWorldTendencyComparison",
    "IfBlackWorldTendencyComparison",
    "IfWhiteWorldTendencyGreaterThanOrEqual",
    "IfBlackWorldTendencyGreaterThanOrEqual",
    "IfNewGameCycleComparison",
    "IfNewGameCycleEqual",
    "IfNewGameCycleGreaterThanOrEqual",
    "IfDLCState",
    "IfDLCOwned",
    "IfDLCNotOwned",
    "IfOnlineState",
    "IfOnline",
    "IfOffline",
    "IfCharacterDeathState",
    "IfCharacterDead",
    "IfCharacterAlive",
    "IfAttacked",
    "IfHealthComparison",
    "IfHealthEqual",
    "IfHealthNotEqual",
    "IfHealthGreaterThan",
    "IfHealthLessThan",
    "IfHealthGreaterThanOrEqual",
    "IfHealthLessThanOrEqual",
    "IfCharacterType",
    "IfCharacterHollow",
    "IfCharacterHuman",
    "IfCharacterTargetingState",
    "IfCharacterTargeting",
    "IfCharacterNotTargeting",
    "IfCharacterSpecialEffectState",
    "IfCharacterHasSpecialEffect",
    "IfCharacterDoesNotHaveSpecialEffect",
    "IfCharacterPartHealthComparison",
    "IfCharacterPartHealthLessThanOrEqual",
    "IfCharacterBackreadState",
    "IfCharacterBackreadEnabled",
    "IfCharacterBackreadDisabled",
    "IfTAEEventState",
    "IfHasTAEEvent",
    "IfDoesNotHaveTAEEvent",
    "IfHasAIStatus",
    "IfSkullLanternState",
    "IfSkullLanternActive",
    "IfSkullLanternInactive",
    "IfPlayerClass",
    "IfPlayerCovenant",
    "IfPlayerSoulLevelComparison",
    "IfPlayerSoulLevelGreaterThanOrEqual",
    "IfPlayerSoulLevelLessThanOrEqual",
    "IfHealthValueComparison",
    "IfHealthValueEqual",
    "IfHealthValueNotEqual",
    "IfHealthValueGreaterThan",
    "IfHealthValueLessThan",
    "IfHealthValueGreaterThanOrEqual",
    "IfHealthValueLessThanOrEqual",
    "ArenaRankingRequest1v1",
    "ArenaRankingRequest2v2",
    "ArenaRankingRequestFFA",
    "ArenaExitRequest",
    "ArenaSetNametag1",
    "ArenaSetNametag2",
    "ArenaSetNametag3",
    "ArenaSetNametag4",
    "DisplayArenaDissolutionMessage",
    "ArenaSetNametag5",
    "ArenaSetNametag6",
    # Dark Souls 3 instructions
    "RunCommonEvent",
    "IfMultiplayerState",
    "IfHost",
    "IfClient",
    "IfTryingToCreateSession",
    "IfTryingToJoinSession",
    "IfLeavingSession",
    "IfFailedToCreateSession",
    "IfDamageType",
    "IfActionButtonInRegion",
    "IfPlayerOwnWorldState",
    "IfPlayerInOwnWorld",
    "IfPlayerNotInOwnWorld",
    "IfMapCeremonyState",
    "IfMapInCeremony",
    "IfMapNotInCeremony",
    "IfMultiplayerNetworkPenalized",
    "IfPlayerGender",
    "IfOngoingCutsceneFinished",
    "IfHollowArenaMatchReadyState",
    "IfHollowArenaSoloResults",
    "IfHollowArenaSoloScoreComparison",
    "IfHollowArenaTeamResults",
    "IfSteamDisconnected",
    "IfAllyPhantomCountComparison",
    "IfPlayerHasSpecialEffect",
    "IfPlayerDoesNotHaveSpecialEffect",
    "IfCharacterDrawGroupState",
    "IfCharacterDrawGroupActive",
    "IfCharacterDrawGroupInactive",
    "IfPlayerRemainingYoelLevelComparison",
    "IfCharacterInvadeType",
    "IfCharacterChameleonState",
    "IfObjectBurnState",
    "IfObjectBackreadState",
    "IfObjectBackreadEnabled",
    "IfObjectBackreadDisabled",
    "IfObjectBackreadState_Alternate",
    "IfObjectBackreadEnabled_Alternate",
    "IfObjectBackreadDisabled_Alternate",
    "GotoIfConditionState",
    "GotoIfConditionTrue",
    "GotoIfConditionFalse",
    "Goto",
    "GotoIfValueComparison",
    "GotoIfFinishedConditionState",
    "GotoIfFinishedConditionTrue",
    "GotoIfFinishedConditionFalse",
    "WaitHollowArenaHalftime",
    "SkipLinesIfMultiplayerState",
    "SkipLinesIfHost",
    "SkipLinesIfClient",
    "SkipLinesIfTryingToCreateSession",
    "SkipLinesIfTryingToJoinSession",
    "SkipLinesIfLeavingSession",
    "SkipLinesIfFailedToCreateSession",
    "TerminateIfMultiplayerState",
    "EndIfHost",
    "EndIfClient",
    "EndIfTryingToCreateSession",
    "EndIfTryingToJoinSession",
    "EndIfLeavingSession",
    "EndIfFailedToCreateSession",
    "RestartIfHost",
    "RestartIfClient",
    "RestartIfTryingToCreateSession",
    "RestartIfTryingToJoinSession",
    "RestartIfLeavingSession",
    "RestartIfFailedToCreateSession",
    "SkipLinesIfCoopClientCountComparison",
    "TerminateIfCoopClientCountComparison",
    "EndIfCoopClientCountComparison",
    "RestartIfCoopClientCountComparison",
    "GotoIfCharacterSpecialEffectState",
    "GotoIfCharacterHasSpecialEffect",
    "GotoIfCharacterDoesNotHaveSpecialEffect",
    "GotoIfPlayerOwnWorldState",
    "GotoIfPlayerInOwnWorld",
    "GotoIfPlayerNotInOwnWorld",
    "TerminateIfPlayerOwnWorldState",
    "EndIfPlayerOwnWorldState",
    "EndIfPlayerInOwnWorld",
    "EndIfPlayerNotInOwnWorld",
    "RestartIfPlayerOwnWorldState",
    "RestartIfPlayerInOwnWorld",
    "RestartIfPlayerNotInOwnWorld",
    "SkipLinesIfClientTypeCountComparison",
    "GotoIfClientTypeCountComparison",
    "TerminateIfClientTypeCountComparison",
    "EndIfClientTypeCountComparison",
    "RestartIfClientTypeCountComparison",
    "GotoIfFlagState",
    "GotoIfThisEventOn",
    "GotoIfThisEventOff",
    "GotoIfThisEventSlotOn",
    "GotoIfThisEventSlotOff",
    "GotoIfFlagOn",
    "GotoIfFlagOff",
    "GotoIfFlagRangeState",
    "GotoIfFlagRangeAllOn",
    "GotoIfFlagRangeAllOff",
    "GotoIfFlagRangeAnyOn",
    "GotoIfFlagRangeAnyOff",
    "GotoIfMultiplayerState",
    "GotoIfHost",
    "GotoIfClient",
    "GotoIfTryingToCreateSession",
    "GotoIfTryingToJoinSession",
    "GotoIfLeavingSession",
    "GotoIfFailedToCreateSession",
    "GotoIfMapPresenceState",
    "GotoIfInsideMap",
    "GotoIfOutsideMap",
    "GotoIfCoopClientCountComparison",
    "TerminateIfCharacterSpecialEffectState",
    "EndIfCharacterSpecialEffectState",
    "EndIfCharacterHasSpecialEffect",
    "EndIfCharacterDoesNotHaveSpecialEffect",
    "RestartIfCharacterSpecialEffectState",
    "RestartIfCharacterHasSpecialEffect",
    "RestartIfCharacterDoesNotHaveSpecialEffect",
    "EndIfPlayerHasSpecialEffect",
    "EndIfPlayerDoesNotHaveSpecialEffect",
    "RestartIfPlayerHasSpecialEffect",
    "RestartIfPlayerDoesNotHaveSpecialEffect",
    "SkipLinesIfCharacterSpecialEffectState",
    "SkipLinesIfCharacterHasSpecialEffect",
    "SkipLinesIfCharacterDoesNotHaveSpecialEffect",
    "SkipLinesIfPlayerHasSpecialEffect",
    "SkipLinesIfPlayerDoesNotHaveSpecialEffect",
    "GotoIfCharacterRegionState",
    "GotoIfCharacterInsideRegion",
    "GotoIfCharacterOutsideRegion",
    "TerminateIfCharacterRegionState",
    "EndIfCharacterRegionState",
    "EndIfCharacterInsideRegion",
    "EndIfCharacterOutsideRegion",
    "RestartIfCharacterRegionState",
    "RestartIfCharacterInsideRegion",
    "RestartIfCharacterOutsideRegion",
    "SkipLinesIfCharacterRegionState",
    "SkipLinesIfCharacterInsideRegion",
    "SkipLinesIfCharacterOutsideRegion",
    "GotoIfHollowArenaMatchType",
    "GotoIfObjectDestructionState",
    "GotoIfObjectDestroyed",
    "GotoIfObjectNotDestroyed",
    "DefineLabel",
    "PlayCutsceneAndMovePlayerAndSetTimePeriod",
    "PlayCutsceneAndSetTimePeriod",
    "PlayCutsceneAndMovePlayer_Dummy",
    "PlayCutsceneAndMovePlayerAndSetMapCeremony",
    "PlayCutsceneAndSetMapCeremony",
    "PlayCutsceneAndMovePlayer_WithUnknowns",
    "PlayCutsceneAndMovePlayer_WithSecondRegion",
    "SetBossHealthBarState",
    "EnableBossHealthBar",
    "DisableBossHealthBar",
    "HandleMinibossDefeat",
    "Unknown_2003_27",
    "EventValueOperation",
    "StoreItemAmountSpecifiedByFlagValue",
    "GivePlayerItemAmountSpecifiedByFlagValue",
    "SetDirectionDisplayState",
    "EnableDirectionDisplay",
    "DisableDirectionDisplay",
    "SetMapHitGridCorrespondence",
    "EnableMapHitGridCorrespondence",
    "DisableMapHitGridCorrespondence",
    "SetMapContentImageDisplayState",
    "SetMapBoundariesDisplay",
    "SetAreaWind",
    "WarpPlayerToRespawnPoint",
    "StartEnemySpawner",
    "SummonNPC",
    "InitializeWarpObject",
    "MakeEnemyAppear",
    "SetCurrentMapCeremony",
    "SetMapCeremony",
    "DisplayEpitaphMessage",
    "SetNetworkConnectedFlagState",
    "SetNetworkConnectedFlagRangeState",
    "SetOmissionModeCounts",
    "ResetOmissionModeCountsToDefault",
    "InitializeCrowTrade",
    "InitializeCrowTradeRegion",
    "SetNetworkInteractionState",
    "SetHUDVisibility",
    "EnableHUDVisibility",
    "DisableHUDVisibility",
    "SetBonfireWarpingState",
    "EnableBonfireWarping",
    "DisableBonfireWarping",
    "SetAutogeneratedEventSpecificFlag_1",
    "HandleBossDefeatAndDisplayBanner",
    "SetAutogeneratedEventSpecificFlag_2",
    "SetLoadingScreenTipsState",
    "EnableLoadingScreenTips",
    "DisableLoadingScreenTips",
    "AwardGestureItem",
    "SendNPCSummonHome",
    "Unknown_2003_79",
    "SetDecoratedBossHealthBarState",
    "EnableDecoratedBossHealthBar",
    "DisableDecoratedBossHealthBar",
    "PlaceNPCSummonSign_WithoutEmber",
    "AddSpecialEffect",
    "RotateToFaceEntity",
    "ChangeCharacterCloth",
    "ChangePatrolBehavior",
    "SetLockOnPoint",
    "Test_RequestRagdollRestraint",
    "ChangePlayerCharacterInitParam",
    "AdaptSpecialEffectHealthChangeToNPCPart",
    "ImmediateActivate",
    "SetCharacterTalkRange",
    "IncrementCharacterNewGameCycle",
    "SetMultiplayerBuffs_NonBoss",
    "Unknown_2004_59",
    "SetPlayerRemainingYoelLevels",
    "ExtinguishBurningObjects",
    "ShowObjectByMapCeremony",
    "DestroyObject_NoSlot",
    "DisplayDialogAndSetFlags",
    "DisplayAreaWelcomeMessage",
    "DisplayHollowArenaMessage",
    "RegisterHealingFountain",
    "BanishInvaders",
    "BanishPhantomsAndUpdateServerPvPStats",
    "BanishPhantoms",
    "SetBossMusicState",
    "EnableBossMusic",
    "DisableBossMusic",
    "NotifyDoorEventSoundDampening",
    "SetMapSoundWithFade",
    "EnableSoundEventWithFade",
    "DisableSoundEventWithFade",
    "Unknown_2010_07",
    "SetCollisionResState",
    "ActivateCollisionAndCreateNavmesh",
    "SetAreaWelcomeMessageState",
    "EnableAreaWelcomeMessage",
    "DisableAreaWelcomeMessage",
    "CreatePlayLog",
    "StartPlayLogMeasurement",
    "StopPlayLogMeasurement",
    "PlayLogParameterOutput",
    # Names processed directly by EVS parser
    "NeverRestart",
    "RestartOnRest",
    "UnknownRestart",
    "EVENTS",
    "Condition",
    "END",
    "RESTART",
    "Await",
    # Shared tests
    "THIS_FLAG",
    "THIS_SLOT_FLAG",
    "ONLINE",
    "OFFLINE",
    "DLC_OWNED",
    "SKULL_LANTERN_ACTIVE",
    "WHITE_WORLD_TENDENCY",
    "BLACK_WORLD_TENDENCY",
    "NEW_GAME_CYCLE",
    "SOUL_LEVEL",
    "FlagEnabled",
    "FlagDisabled",
    "SecondsElapsed",
    "FramesElapsed",
    "CharacterInsideRegion",
    "CharacterOutsideRegion",
    "PlayerInsideRegion",
    "PlayerOutsideRegion",
    "AllPlayersInsideRegion",
    "AllPlayersOutsideRegion",
    "InsideMap",
    "OutsideMap",
    "EntityWithinDistance",
    "EntityBeyondDistance",
    "PlayerWithinDistance",
    "PlayerBeyondDistance",
    "HasItem",
    "HasWeapon",
    "HasArmor",
    "HasRing",
    "HasGood",
    "ActionButton",
    "MultiplayerEvent",
    "TrueFlagCount",
    "EventValue",
    "EventFlagValue",
    "AnyItemDroppedInRegion",
    "ItemDropped",
    "OwnsItem",
    "OwnsWeapon",
    "OwnsArmor",
    "OwnsRing",
    "OwnsGood",
    "IsAlive",
    "IsDead",
    "IsAttacked",
    "HealthRatio",
    "HealthValue",
    "PartHealthValue",
    "IsCharacterType",
    "IsHollow",
    "IsHuman",
    "IsInvader",
    "IsBlackPhantom",
    "IsWhitePhantom",
    "HasSpecialEffect",
    "BackreadEnabled",
    "BackreadDisabled",
    "HasTaeEvent",
    "IsTargeting",
    "HasAiStatus",
    "AiStatusIsNormal",
    "AiStatusIsRecognition",
    "AiStatusIsAlert",
    "AiStatusIsBattle",
    "PlayerIsClass",
    "PlayerInCovenant",
    "IsDamaged",
    "IsDestroyed",
    "IsActivated",
    "PlayerStandingOnCollision",
    "PlayerMovingOnCollision",
    "PlayerRunningOnCollision",
    # Dark Souls 3 tests
    "HOST",
    "CLIENT",
    "IN_OWN_WORLD",
    "ActionButtonInRegion",
    "IsAttackedWithDamageType",
    "CharacterDrawGroupActive",
    "CharacterDrawGroupInactive",
    # Basic enums
    "RestartType",
    "uint",
    "short",
    "ushort",
    "char",
    "uchar",
    "PLAYER",
    "CLIENT_PLAYER_1",
    "CLIENT_PLAYER_2",
    "CLIENT_PLAYER_3",
    "CLIENT_PLAYER_4",
    "CLIENT_PLAYER_5",
    # Enums identical in all games
    "AIStatusType",
    "BitOperation",
    "ButtonType",
    "CharacterType",
    "CharacterUpdateRate",
    "ClassType",
    "ComparisonType",
    "CutsceneType",
    "DamageTargetType",
    "EventEndType",
    "FlagState",
    "FlagType",
    "InterpolationState",
    "ItemType",
    "RangeState",
    "CoordEntityType",
    "NavmeshType",
    "NumberButtons",
    "OnOffChange",
    "RestartType",
    "SoundType",
    "StatueType",
    "SummonSignType",
    "TriggerAttribute",
    "WorldTendencyType",
    "UpdateAuthority",
    # Enums in Dark Souls 3 only
    "ArmorType",
    "BannerType",
    "CalculationType",
    "ClientType",
    "ConditionGroup",
    "Covenant",
    "DamageType",
    "DeleteOrAdd",
    "DialogResult",
    "DisplayState",
    "DoorState",
    "Gender",
    "Label",
    "MultiplayerState",
    "NPCPartType",
    "PlayGoState",
    "PlayLogMultiplayerType",
    "PlayerPlayLogParameter",
    "SingleplayerSummonSignType",
    "TeamType",
    "HollowArenaMatchType",
    "HollowArenaResult",
]
