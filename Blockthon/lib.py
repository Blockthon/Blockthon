import hashlib, codecs, binascii, pbkdf2, hmac
import os, base58, random, ecdsa, re, base64
from hashlib import sha256, new, sha512
from typing import Type, Optional
from bip32utils import BIP32Key
from mnemonic import Mnemonic

BASE58_ALPHABET = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
GROUP_ORDER = (
    b'\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff\xff'
    b'\xfe\xba\xae\xdc\xe6\xafH\xa0;\xbf\xd2^\x8c\xd06AA'
)
GROUP_ORDER_INT = 0xFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFEBAAEDCE6AF48A03BBFD25E8CD0364141
KEY_SIZE = 32
ZERO = b'\x00'


def Base58Decode(v):
    if not isinstance(v, str):
        v = v.decode('ascii')
    dec = 0
    for char in v:
        dec = dec * 58 + BASE58_ALPHABET.index(char)
    return dec.to_bytes((dec.bit_length() + 7) // 8, 'big')


# Bytes To Hex
def Hexlify(data_str: bytes) -> str:
    return binascii.hexlify(data_str).decode()


# Converting Hex To Bytes
def unHexlify(data_str: str) -> bytes:
    return binascii.unhexlify(data_str)


def SH256(bytes_data: bytes) -> any:
    return hashlib.sha256(bytes_data)


def encrypt(data: str) -> str:
    return SH256(unHexlify(data)).hexdigest()


def B58enUnHex(hex_string: str) -> str:
    return base58.b58encode(unHexlify(hex_string)).decode('utf-8')


def getSec() -> str:
    char = 'abcdef1234567890'
    string = ''
    for _ in range(len(char)):
        adder = random.choice(char)
        if adder not in string:
            string += adder
    return string


def from_int(integer: int) -> str:
    return '{:02x}'.format(integer)


def PVK() -> str:
    key = ''
    for _ in range(6):
        norepeat = getSec()
        if norepeat not in key:
            key += norepeat
    if len(key) < 64:
        equal = (64 - len(key)) * '0'
        return equal + key
    else:
        return key[0:64]


def DecToHex(dec: int) -> str:
    decKey = from_int(dec)
    if len(decKey) < 64:
        return decKey.zfill(64)
    else:
        return decKey


def b58_encodec(data: str) -> str:
    return base58.b58encode(unHexlify(data)).decode('utf-8')


def HexToBin(hexed: str) -> str:
    return bin(int(hexed, 16))[2:].zfill(256)


def HexToMne(hex_string: str, size: int = 12) -> str:
    byte_string = unHexlify(hex_string)
    ValidLen = [12, 18, 24]
    if size in ValidLen:
        NearestLen = min(ValidLen, key=lambda x: abs(x - len(byte_string)))
        if len(byte_string) != NearestLen:
            byte_string = byte_string[:NearestLen]
        return Mnemonic('english').to_mnemonic(byte_string)
    else:
        return f"To create a mnemonic, you need to enter the size (number) of words"


def BytsToRIPEMD160(byte: bytes) -> bytes:
    RIPEMD160 = hashlib.new('ripemd160')
    RIPEMD160.update(byte)
    return RIPEMD160.digest()


def BytesToMne(bytes_string: bytes) -> str:
    return Mnemonic('english').to_mnemonic(bytes_string)


def BytesToMnemonic(bytes_string: bytes, size: int) -> str:
    mne = BytesToMne(bytes_string)
    if size == 12:
        return ' '.join(str(mne).split(' ')[0:12])
    elif size == 16:
        return ' '.join(str(mne).split(' ')[0:16])
    elif size == 18:
        return ' '.join(str(mne).split(' ')[0:18])
    elif size == 24:
        return ' '.join(str(mne).split(' ')[0:24])
    else:
        return ' '.join(str(mne).split(' ')[0:12])


def BytesToHex(bytes_string: bytes) -> str:
    return Hexlify(bytes_string)


def BytesToDec(bytestr: bytes) -> int:
    return int.from_bytes(bytestr, 'big')


def BytesToWif(byte, compress=False):
    from bit.format import bytes_to_wif
    if compress:
        return bytes_to_wif(byte, compressed=True)
    else:
        return bytes_to_wif(byte, compressed=False)


def BytesToAddr(bytes_data: bytes, compress=False) -> str:
    from bit import Key
    from bit.format import bytes_to_wif as btw
    if compress:
        wif = btw(bytes_data, compressed=True)
        bits = Key(wif)
        return bits.address
    else:
        wif = btw(bytes_data, compressed=False)
        bits = Key(wif)
        return bits.address


def BytesToPub(bytes_data: bytes, compress=False) -> str:
    from bit import Key
    from bit.format import bytes_to_wif as btw
    if compress:
        wif = btw(bytes_data, compressed=True)
        bits = Key(wif)
        pubbytes = bits.public_key
        return Hexlify(pubbytes)
    else:
        wif = btw(bytes_data, compressed=False)
        bits = Key(wif)
        pubbytes = bits.public_key
        return Hexlify(pubbytes)


def WifAddr(wif: str) -> str:
    from bit import Key
    bits = Key(wif)
    return bits.address


def WifToBytes(wif: str) -> bytes:
    wifbyte = base58.b58decode_check(wif)
    # wif_Bytes = Base58Decode_Check(wif)
    return wifbyte[1:]


def getMnemonic(size: int) -> Optional[str]:
    ml = ''
    words = "AbandonAbilityAbleAboutAboveAbsentAbsorbAbstractAbsurdAbuseAccessAccidentAccountAccuseAchieveAcidAcousticAcquireAcrossActActionActorActressActualAdaptAddAddictAddressAdjustAdmitAdultAdvanceAdviceAerobicAffairAffordAfraidAgainAgeAgentAgreeAheadAimAirAirportAisleAlarmAlbumAlcoholAlertAlienAllAlleyAllowAlmostAloneAlphaAlreadyAlsoAlterAlwaysAmateurAmazingAmongAmountAmusedAnalystAnchorAncientAngerAngleAngryAnimalAnkleAnnounceAnnualAnotherAnswerAntennaAntiqueAnxietyAnyApartApologyAppearAppleApproveAprilArchArcticAreaArenaArgueArmArmedArmorArmyAroundArrangeArrestArriveArrowArtArtefactArtistArtworkAskAspectAssaultAssetAssistAssumeAsthmaAthleteAtomAttackAttendAttitudeAttractAuctionAuditAugustAuntAuthorAutoAutumnAverageAvocadoAvoidAwakeAwareAwayAwesomeAwfulAwkwardAxisBabyBachelorBaconBadgeBagBalanceBalconyBallBambooBananaBannerBarBarelyBargainBarrelBaseBasicBasketBattleBeachBeanBeautyBecauseBecomeBeefBeforeBeginBehaveBehindBelieveBelowBeltBenchBenefitBestBetrayBetterBetweenBeyondBicycleBidBikeBindBiologyBirdBirthBitterBlackBladeBlameBlanketBlastBleakBlessBlindBloodBlossomBlouseBlueBlurBlushBoardBoatBodyBoilBombBoneBonusBookBoostBorderBoringBorrowBossBottomBounceBoxBoyBracketBrainBrandBrassBraveBreadBreezeBrickBridgeBriefBrightBringBriskBroccoliBrokenBronzeBroomBrotherBrownBrushBubbleBuddyBudgetBuffaloBuildBulbBulkBulletBundleBunkerBurdenBurgerBurstBusBusinessBusyButterBuyerBuzzCabbageCabinCableCactusCageCakeCallCalmCameraCampCanCanalCancelCandyCannonCanoeCanvasCanyonCapableCapitalCaptainCarCarbonCardCargoCarpetCarryCartCaseCashCasinoCastleCasualCatCatalogCatchCategoryCattleCaughtCauseCautionCaveCeilingCeleryCementCensusCenturyCerealCertainChairChalkChampionChangeChaosChapterChargeChaseChatCheapCheckCheeseChefCherryChestChickenChiefChildChimneyChoiceChooseChronicChuckleChunkChurnCigarCinnamonCircleCitizenCityCivilClaimClapClarifyClawClayCleanClerkCleverClickClientCliffClimbClinicClipClockClogCloseClothCloudClownClubClumpClusterClutchCoachCoastCoconutCodeCoffeeCoilCoinCollectColorColumnCombineComeComfortComicCommonCompanyConcertConductConfirmCongressConnectConsiderControlConvinceCookCoolCopperCopyCoralCoreCornCorrectCostCottonCouchCountryCoupleCourseCousinCoverCoyoteCrackCradleCraftCramCraneCrashCraterCrawlCrazyCreamCreditCreekCrewCricketCrimeCrispCriticCropCrossCrouchCrowdCrucialCruelCruiseCrumbleCrunchCrushCryCrystalCubeCultureCupCupboardCuriousCurrentCurtainCurveCushionCustomCuteCycleDadDamageDampDanceDangerDaringDashDaughterDawnDayDealDebateDebrisDecadeDecemberDecideDeclineDecorateDecreaseDeerDefenseDefineDefyDegreeDelayDeliverDemandDemiseDenialDentistDenyDepartDependDepositDepthDeputyDeriveDescribeDesertDesignDeskDespairDestroyDetailDetectDevelopDeviceDevoteDiagramDialDiamondDiaryDiceDieselDietDifferDigitalDignityDilemmaDinnerDinosaurDirectDirtDisagreeDiscoverDiseaseDishDismissDisorderDisplayDistanceDivertDivideDivorceDizzyDoctorDocumentDogDollDolphinDomainDonateDonkeyDonorDoorDoseDoubleDoveDraftDragonDramaDrasticDrawDreamDressDriftDrillDrinkDripDriveDropDrumDryDuckDumbDuneDuringDustDutchDutyDwarfDynamicEagerEagleEarlyEarnEarthEasilyEastEasyEchoEcologyEconomyEdgeEditEducateEffortEggEightEitherElbowElderElectricElegantElementElephantElevatorEliteElseEmbarkEmbodyEmbraceEmergeEmotionEmployEmpowerEmptyEnableEnactEndEndlessEndorseEnemyEnergyEnforceEngageEngineEnhanceEnjoyEnlistEnoughEnrichEnrollEnsureEnterEntireEntryEnvelopeEpisodeEqualEquipEraEraseErodeErosionErrorEruptEscapeEssayEssenceEstateEternalEthicsEvidenceEvilEvokeEvolveExactExampleExcessExchangeExciteExcludeExcuseExecuteExerciseExhaustExhibitExileExistExitExoticExpandExpectExpireExplainExposeExpressExtendExtraEyeEyebrowFabricFaceFacultyFadeFaintFaithFallFalseFameFamilyFamousFanFancyFantasyFarmFashionFatFatalFatherFatigueFaultFavoriteFeatureFebruaryFederalFeeFeedFeelFemaleFenceFestivalFetchFeverFewFiberFictionFieldFigureFileFilmFilterFinalFindFineFingerFinishFireFirmFirstFiscalFishFitFitnessFixFlagFlameFlashFlatFlavorFleeFlightFlipFloatFlockFloorFlowerFluidFlushFlyFoamFocusFogFoilFoldFollowFoodFootForceForestForgetForkFortuneForumForwardFossilFosterFoundFoxFragileFrameFrequentFreshFriendFringeFrogFrontFrostFrownFrozenFruitFuelFunFunnyFurnaceFuryFutureGadgetGainGalaxyGalleryGameGapGarageGarbageGardenGarlicGarmentGasGaspGateGatherGaugeGazeGeneralGeniusGenreGentleGenuineGestureGhostGiantGiftGiggleGingerGiraffeGirlGiveGladGlanceGlareGlassGlideGlimpseGlobeGloomGloryGloveGlowGlueGoatGoddessGoldGoodGooseGorillaGospelGossipGovernGownGrabGraceGrainGrantGrapeGrassGravityGreatGreenGridGriefGritGroceryGroupGrowGruntGuardGuessGuideGuiltGuitarGunGymHabitHairHalfHammerHamsterHandHappyHarborHardHarshHarvestHatHaveHawkHazardHeadHealthHeartHeavyHedgehogHeightHelloHelmetHelpHenHeroHiddenHighHillHintHipHireHistoryHobbyHockeyHoldHoleHolidayHollowHomeHoneyHoodHopeHornHorrorHorseHospitalHostHotelHourHoverHubHugeHumanHumbleHumorHundredHungryHuntHurdleHurryHurtHusbandHybridIceIconIdeaIdentifyIdleIgnoreIllIllegalIllnessImageImitateImmenseImmuneImpactImposeImproveImpulseInchIncludeIncomeIncreaseIndexIndicateIndoorIndustryInfantInflictInformInhaleInheritInitialInjectInjuryInmateInnerInnocentInputInquiryInsaneInsectInsideInspireInstallIntactInterestIntoInvestInviteInvolveIronIslandIsolateIssueItemIvoryJacketJaguarJarJazzJealousJeansJellyJewelJobJoinJokeJourneyJoyJudgeJuiceJumpJungleJuniorJunkJustKangarooKeenKeepKetchupKeyKickKidKidneyKindKingdomKissKitKitchenKiteKittenKiwiKneeKnifeKnockKnowLabLabelLaborLadderLadyLakeLampLanguageLaptopLargeLaterLatinLaughLaundryLavaLawLawnLawsuitLayerLazyLeaderLeafLearnLeaveLectureLeftLegLegalLegendLeisureLemonLendLengthLensLeopardLessonLetterLevelLiarLibertyLibraryLicenseLifeLiftLightLikeLimbLimitLinkLionLiquidListLittleLiveLizardLoadLoanLobsterLocalLockLogicLonelyLongLoopLotteryLoudLoungeLoveLoyalLuckyLuggageLumberLunarLunchLuxuryLyricsMachineMadMagicMagnetMaidMailMainMajorMakeMammalManManageMandateMangoMansionManualMapleMarbleMarchMarginMarineMarketMarriageMaskMassMasterMatchMaterialMathMatrixMatterMaximumMazeMeadowMeanMeasureMeatMechanicMedalMediaMelodyMeltMemberMemoryMentionMenuMercyMergeMeritMerryMeshMessageMetalMethodMiddleMidnightMilkMillionMimicMindMinimumMinorMinuteMiracleMirrorMiseryMissMistakeMixMixedMixtureMobileModelModifyMomMomentMonitorMonkeyMonsterMonthMoonMoralMoreMorningMosquitoMotherMotionMotorMountainMouseMoveMovieMuchMuffinMuleMultiplyMuscleMuseumMushroomMusicMustMutualMyselfMysteryMythNaiveNameNapkinNarrowNastyNationNatureNearNeckNeedNegativeNeglectNeitherNephewNerveNestNetNetworkNeutralNeverNewsNextNiceNightNobleNoiseNomineeNoodleNormalNorthNoseNotableNoteNothingNoticeNovelNowNuclearNumberNurseNutOakObeyObjectObligeObscureObserveObtainObviousOccurOceanOctoberOdorOffOfferOfficeOftenOilOkayOldOliveOlympicOmitOnceOneOnionOnlineOnlyOpenOperaOpinionOpposeOptionOrangeOrbitOrchardOrderOrdinaryOrganOrientOriginalOrphanOstrichOtherOutdoorOuterOutputOutsideOvalOvenOverOwnOwnerOxygenOysterOzonePactPaddlePagePairPalacePalmPandaPanelPanicPantherPaperParadeParentParkParrotPartyPassPatchPathPatientPatrolPatternPausePavePaymentPeacePeanutPearPeasantPelicanPenPenaltyPencilPeoplePepperPerfectPermitPersonPetPhonePhotoPhrasePhysicalPianoPicnicPicturePiecePigPigeonPillPilotPinkPioneerPipePistolPitchPizzaPlacePlanetPlasticPlatePlayPleasePledgePluckPlugPlungePoemPoetPointPolarPolePolicePondPonyPoolPopularPortionPositionPossiblePostPotatoPotteryPovertyPowderPowerPracticePraisePredictPreferPreparePresentPrettyPreventPricePridePrimaryPrintPriorityPrisonPrivatePrizeProblemProcessProduceProfitProgramProjectPromoteProofPropertyProsperProtectProudProvidePublicPuddingPullPulpPulsePumpkinPunchPupilPuppyPurchasePurityPurposePursePushPutPuzzlePyramidQualityQuantumQuarterQuestionQuickQuitQuizQuoteRabbitRaccoonRaceRackRadarRadioRailRainRaiseRallyRampRanchRandomRangeRapidRareRateRatherRavenRawRazorReadyRealReasonRebelRebuildRecallReceiveRecipeRecordRecycleReduceReflectReformRefuseRegionRegretRegularRejectRelaxReleaseReliefRelyRemainRememberRemindRemoveRenderRenewRentReopenRepairRepeatReplaceReportRequireRescueResembleResistResourceResponseResultRetireRetreatReturnReunionRevealReviewRewardRhythmRibRibbonRiceRichRideRidgeRifleRightRigidRingRiotRippleRiskRitualRivalRiverRoadRoastRobotRobustRocketRomanceRoofRookieRoomRoseRotateRoughRoundRouteRoyalRubberRudeRugRuleRunRunwayRuralSadSaddleSadnessSafeSailSaladSalmonSalonSaltSaluteSameSampleSandSatisfySatoshiSauceSausageSaveSayScaleScanScareScatterSceneSchemeSchoolScienceScissorsScorpionScoutScrapScreenScriptScrubSeaSearchSeasonSeatSecondSecretSectionSecuritySeedSeekSegmentSelectSellSeminarSeniorSenseSentenceSeriesServiceSessionSettleSetupSevenShadowShaftShallowShareShedShellSheriffShieldShiftShineShipShiverShockShoeShootShopShortShoulderShoveShrimpShrugShuffleShySiblingSickSideSiegeSightSignSilentSilkSillySilverSimilarSimpleSinceSingSirenSisterSituateSixSizeSkateSketchSkiSkillSkinSkirtSkullSlabSlamSleepSlenderSliceSlideSlightSlimSloganSlotSlowSlushSmallSmartSmileSmokeSmoothSnackSnakeSnapSniffSnowSoapSoccerSocialSockSodaSoftSolarSoldierSolidSolutionSolveSomeoneSongSoonSorrySortSoulSoundSoupSourceSouthSpaceSpareSpatialSpawnSpeakSpecialSpeedSpellSpendSphereSpiceSpiderSpikeSpinSpiritSplitSpoilSponsorSpoonSportSpotSpraySpreadSpringSpySquareSqueezeSquirrelStableStadiumStaffStageStairsStampStandStartStateStaySteakSteelStemStepStereoStickStillStingStockStomachStoneStoolStoryStoveStrategyStreetStrikeStrongStruggleStudentStuffStumbleStyleSubjectSubmitSubwaySuccessSuchSuddenSufferSugarSuggestSuitSummerSunSunnySunsetSuperSupplySupremeSureSurfaceSurgeSurpriseSurroundSurveySuspectSustainSwallowSwampSwapSwarmSwearSweetSwiftSwimSwingSwitchSwordSymbolSymptomSyrupSystemTableTackleTagTailTalentTalkTankTapeTargetTaskTasteTattooTaxiTeachTeamTellTenTenantTennisTentTermTestTextThankThatThemeThenTheoryThereTheyThingThisThoughtThreeThriveThrowThumbThunderTicketTideTigerTiltTimberTimeTinyTipTiredTissueTitleToastTobaccoTodayToddlerToeTogetherToiletTokenTomatoTomorrowToneTongueTonightToolToothTopTopicToppleTorchTornadoTortoiseTossTotalTouristTowardTowerTownToyTrackTradeTrafficTragicTrainTransferTrapTrashTravelTrayTreatTreeTrendTrialTribeTrickTriggerTrimTripTrophyTroubleTruckTrueTrulyTrumpetTrustTruthTryTubeTuitionTumbleTunaTunnelTurkeyTurnTurtleTwelveTwentyTwiceTwinTwistTwoTypeTypicalUglyUmbrellaUnableUnawareUncleUncoverUnderUndoUnfairUnfoldUnhappyUniformUniqueUnitUniverseUnknownUnlockUntilUnusualUnveilUpdateUpgradeUpholdUponUpperUpsetUrbanUrgeUsageUseUsedUsefulUselessUsualUtilityVacantVacuumVagueValidValleyValveVanVanishVaporVariousVastVaultVehicleVelvetVendorVentureVenueVerbVerifyVersionVeryVesselVeteranViableVibrantViciousVictoryVideoViewVillageVintageViolinVirtualVirusVisaVisitVisualVitalVividVocalVoiceVoidVolcanoVolumeVoteVoyageWageWagonWaitWalkWallWalnutWantWarfareWarmWarriorWashWaspWasteWaterWaveWayWealthWeaponWearWeaselWeatherWebWeddingWeekendWeirdWelcomeWestWetWhaleWhatWheatWheelWhenWhereWhipWhisperWideWidthWifeWildWillWinWindowWineWingWinkWinnerWinterWireWisdomWiseWishWitnessWolfWomanWonderWoodWoolWordWorkWorldWorryWorthWrapWreckWrestleWristWriteWrongYardYearYellowYouYoungYouthZebraZeroZoneZoo"
    mnemonics = re.findall('[A-Z][a-z]+', words)
    if size == 12:
        for r in range(size):
            lx = random.choice(mnemonics)
            ml += f" {lx}"
        return str(ml).lower()
    elif size == 18:
        for r in range(size):
            lx = random.choice(mnemonics)
            ml += f" {lx}"
        return str(ml).lower()
    else:
        return None


def MnemToRoot(mnem: str) -> str:
    mnemonic_ = ''.join(c for c in mnem if c.isalnum())
    mnemonic_ = mnemonic_.split(' ')
    seed_ = pbkdf2.PBKDF2(' '.join(mnemonic_), 'mnemonic' + '', iterations=2048, macmodule=hmac,
                          digestmodule=sha512).read(64)
    xprv_ = BIP32Key.fromEntropy(seed_)
    return xprv_.ExtendedKey()


def WordToBytes(mnem: str) -> bytes:
    return Mnemonic("english").to_seed(mnem)


def MnemonicToBytes(mnemonic_words: str) -> bytes:
    seed = BIP32Key.fromEntropy(WordToBytes(mnemonic_words))
    seed_bytes = seed.ChainCode()
    return ValidSecret(seed_bytes)


def PadScalar(scalar: bytes) -> bytes:
    return (ZERO * (KEY_SIZE - len(scalar))) + scalar


def DecToBytes(num: int) -> bytes:
    len_num = num.bit_length()
    return num.to_bytes((len_num + 7) // 8 or 1, 'big')


def DecBytePad(num: int) -> bytes:
    return PadScalar(num.to_bytes((num.bit_length() + 7) // 8 or 1, 'big'))


def ValidSecret(secret: bytes) -> bytes:
    if not 0 < BytesToDec(secret) < GROUP_ORDER_INT:
        raise ValueError(f'Secret scalar must be greater than 0 and less than {GROUP_ORDER_INT}.')
    return PadScalar(secret)


def getBytes(size: int = 32) -> bytes: return os.urandom(size)


def BinToHex(binString: str) -> str:
    return hex(int(binString, 2))[2:].zfill(32)


def getBin(size: int = 256) -> str:
    bin_str = ""
    for _ in range(size):
        bin_str += random.choice(['0', '1'])
    return bin_str


def AddrToH160(addr: str) -> str:
    decodeAddr = base58.b58decode(addr)
    hexAddr = Hexlify(decodeAddr)
    return hexAddr[2:-8]
