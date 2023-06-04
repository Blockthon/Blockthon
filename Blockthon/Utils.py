from binascii import hexlify as _decode
from bip32utils import BIP32Key
from .Base58 import b58_decode, b58check_decode, b58check_encode, b58_encode, Base58_
from hdwallet import HDWallet as Wallet_
from hdwallet.symbols import BTC, ETH, BTG, TRX, LTC, DASH, DGB, DOGE, ZEC, QTUM, RVN
from mnemonic import Mnemonic
from bit.format import bytes_to_wif as Bytes_To_Wif
from bit import Key as Wallet
from hashlib import sha256 as _SHA256, new as New_, sha512 as _SHA512
import codecs, os, re, random, pbkdf2, requests, json, hmac


def SHA256(bytestring): return _SHA256(bytestring).digest()


def Double_SHA256(bytestring): return _SHA256(_SHA256(bytestring).digest()).digest()


def Double_SHA256_Checksum(bytestring): return Double_SHA256(bytestring)[:4]


def RIPEMD160_SHA256(bytestring): return New_('ripemd160', _SHA256(bytestring)).digest()


def PrivateKey(): return os.urandom(32).hex()


def PrivateKey_To_Wif(privatekey, compress=False):
    byte_string = PrivateKey_To_Bytes(privatekey)
    if compress:
        wif = Bytes_To_Wif(byte_string, compressed=True)
    else:
        wif = Bytes_To_Wif(byte_string, compressed=False)

    return wif


def PrivateKey_To_Addr(privatekey, compress=False):
    if compress:
        wif = PrivateKey_To_Wif(privatekey, compress=True)
        bits = Wallet(wif)
        return bits.address
    else:
        wif = PrivateKey_To_Wif(privatekey)
        bitu = Wallet(wif)
        return bitu.address


def PrivateKey_To_Bytes(privatekey): return codecs.decode(privatekey, 'hex')


def PrivateKey_To_Mnemonics(privatekey):
    """
    Convert HEX To Bytes , after converting , convert to Mnemonic (WORD)
    PrivateKey: str --> Bytes (seed) --> Mnemonic(Word): str

    @param privatekey: (hex):
    @return: Mnemonic [string]
    """
    byte_string = PrivateKey_To_Bytes(privatekey)
    valid_lengths = [16, 20, 24, 28, 32]
    nearest_length = min(valid_lengths, key=lambda x: abs(x - len(byte_string)))
    if len(byte_string) != nearest_length:
        byte_string = byte_string[:nearest_length]
    return Mnemonic('english').to_mnemonic(byte_string)


def PrivateKey_To_Binary(privatekey): return bin(int(privatekey, 16))[2:].zfill(256)


def PrivateKey_To_Dec(privatekey): return int(privatekey, 16)


def PrivateKey_To_PublicHash(privatekey):
    w: Wallet_ = Wallet_(symbol=BTC)
    return w.hash(privatekey)


def PrivateKey_To_PublicKey(privatekey, compress=False):
    hd: Wallet_ = Wallet_(symbol=BTC)
    hd.from_private_key(privatekey)
    if compress:
        return hd.public_key(True, privatekey)
    else:
        return hd.public_key(False, privatekey)


def PrivateKey_To_RootKey(privatekey): return Mnemonic_To_RootKey(PrivateKey_To_Mnemonics(privatekey))


def PrivateKey_From_Passphrase(passphrase): return str(_SHA256(passphrase.encode('utf-8')).hexdigest())


def PrivateKey_From_RootKey(xprv):
    deco_ = b58check_decode(xprv)
    pvk_b_ = deco_[46:78]
    return pvk_b_.hex()


def PrivateKey_From_Binary(Bin_string): return hex(int(Bin_string, 2))[2:].zfill(32)


def PrivateKey_From_Dec(dec): return "%064x" % dec


def PrivateKey_To_Compress_Addr(privatekey): return PrivateKey_To_Addr(privatekey, compress=True)


def PrivateKey_To_UnCompress_Addr(privatekey): return PrivateKey_To_Addr(privatekey)


HASH160 = RIPEMD160_SHA256


def PublicKey_To_Addr(public_key):
    PublicKeyByte = codecs.decode(public_key, 'hex')
    sha256_bpk = _SHA256(PublicKeyByte)
    sha256_bpk_digest = sha256_bpk.digest()
    ripemd160_bpk = New_('ripemd160')
    ripemd160_bpk.update(sha256_bpk_digest)
    ripemd160_bpk_digest = ripemd160_bpk.digest()
    ripemd160_bpk_hex = codecs.encode(ripemd160_bpk_digest, 'hex')
    NetByte = b'00'
    NetBTCBytePubKey = NetByte + ripemd160_bpk_hex
    NetBTCPubKeyByte = codecs.decode(
        NetBTCBytePubKey, 'hex')
    Hash256N = _SHA256(NetBTCPubKeyByte)
    Hash256N_digest = Hash256N.digest()
    sha256_2_nbpk = _SHA256(Hash256N_digest)
    sha256_2_nbpk_digest = sha256_2_nbpk.digest()
    sha256_2_hex = codecs.encode(sha256_2_nbpk_digest, 'hex')
    checksum = sha256_2_hex[:8]
    addrHex = (NetBTCBytePubKey + checksum).decode('utf-8')
    return Base58_(addrHex)


# ==========================================================

def getMnemonic(size=12):
    """
Generate random mnemonic (word's) with size . size default= 12
    @param size: [integer]
    @return: Mnemonic Words [string]
    """
    ml = ''
    words = "AbandonAbilityAbleAboutAboveAbsentAbsorbAbstractAbsurdAbuseAccessAccidentAccountAccuseAchieveAcidAcousticAcquireAcrossActActionActorActressActualAdaptAddAddictAddressAdjustAdmitAdultAdvanceAdviceAerobicAffairAffordAfraidAgainAgeAgentAgreeAheadAimAirAirportAisleAlarmAlbumAlcoholAlertAlienAllAlleyAllowAlmostAloneAlphaAlreadyAlsoAlterAlwaysAmateurAmazingAmongAmountAmusedAnalystAnchorAncientAngerAngleAngryAnimalAnkleAnnounceAnnualAnotherAnswerAntennaAntiqueAnxietyAnyApartApologyAppearAppleApproveAprilArchArcticAreaArenaArgueArmArmedArmorArmyAroundArrangeArrestArriveArrowArtArtefactArtistArtworkAskAspectAssaultAssetAssistAssumeAsthmaAthleteAtomAttackAttendAttitudeAttractAuctionAuditAugustAuntAuthorAutoAutumnAverageAvocadoAvoidAwakeAwareAwayAwesomeAwfulAwkwardAxisBabyBachelorBaconBadgeBagBalanceBalconyBallBambooBananaBannerBarBarelyBargainBarrelBaseBasicBasketBattleBeachBeanBeautyBecauseBecomeBeefBeforeBeginBehaveBehindBelieveBelowBeltBenchBenefitBestBetrayBetterBetweenBeyondBicycleBidBikeBindBiologyBirdBirthBitterBlackBladeBlameBlanketBlastBleakBlessBlindBloodBlossomBlouseBlueBlurBlushBoardBoatBodyBoilBombBoneBonusBookBoostBorderBoringBorrowBossBottomBounceBoxBoyBracketBrainBrandBrassBraveBreadBreezeBrickBridgeBriefBrightBringBriskBroccoliBrokenBronzeBroomBrotherBrownBrushBubbleBuddyBudgetBuffaloBuildBulbBulkBulletBundleBunkerBurdenBurgerBurstBusBusinessBusyButterBuyerBuzzCabbageCabinCableCactusCageCakeCallCalmCameraCampCanCanalCancelCandyCannonCanoeCanvasCanyonCapableCapitalCaptainCarCarbonCardCargoCarpetCarryCartCaseCashCasinoCastleCasualCatCatalogCatchCategoryCattleCaughtCauseCautionCaveCeilingCeleryCementCensusCenturyCerealCertainChairChalkChampionChangeChaosChapterChargeChaseChatCheapCheckCheeseChefCherryChestChickenChiefChildChimneyChoiceChooseChronicChuckleChunkChurnCigarCinnamonCircleCitizenCityCivilClaimClapClarifyClawClayCleanClerkCleverClickClientCliffClimbClinicClipClockClogCloseClothCloudClownClubClumpClusterClutchCoachCoastCoconutCodeCoffeeCoilCoinCollectColorColumnCombineComeComfortComicCommonCompanyConcertConductConfirmCongressConnectConsiderControlConvinceCookCoolCopperCopyCoralCoreCornCorrectCostCottonCouchCountryCoupleCourseCousinCoverCoyoteCrackCradleCraftCramCraneCrashCraterCrawlCrazyCreamCreditCreekCrewCricketCrimeCrispCriticCropCrossCrouchCrowdCrucialCruelCruiseCrumbleCrunchCrushCryCrystalCubeCultureCupCupboardCuriousCurrentCurtainCurveCushionCustomCuteCycleDadDamageDampDanceDangerDaringDashDaughterDawnDayDealDebateDebrisDecadeDecemberDecideDeclineDecorateDecreaseDeerDefenseDefineDefyDegreeDelayDeliverDemandDemiseDenialDentistDenyDepartDependDepositDepthDeputyDeriveDescribeDesertDesignDeskDespairDestroyDetailDetectDevelopDeviceDevoteDiagramDialDiamondDiaryDiceDieselDietDifferDigitalDignityDilemmaDinnerDinosaurDirectDirtDisagreeDiscoverDiseaseDishDismissDisorderDisplayDistanceDivertDivideDivorceDizzyDoctorDocumentDogDollDolphinDomainDonateDonkeyDonorDoorDoseDoubleDoveDraftDragonDramaDrasticDrawDreamDressDriftDrillDrinkDripDriveDropDrumDryDuckDumbDuneDuringDustDutchDutyDwarfDynamicEagerEagleEarlyEarnEarthEasilyEastEasyEchoEcologyEconomyEdgeEditEducateEffortEggEightEitherElbowElderElectricElegantElementElephantElevatorEliteElseEmbarkEmbodyEmbraceEmergeEmotionEmployEmpowerEmptyEnableEnactEndEndlessEndorseEnemyEnergyEnforceEngageEngineEnhanceEnjoyEnlistEnoughEnrichEnrollEnsureEnterEntireEntryEnvelopeEpisodeEqualEquipEraEraseErodeErosionErrorEruptEscapeEssayEssenceEstateEternalEthicsEvidenceEvilEvokeEvolveExactExampleExcessExchangeExciteExcludeExcuseExecuteExerciseExhaustExhibitExileExistExitExoticExpandExpectExpireExplainExposeExpressExtendExtraEyeEyebrowFabricFaceFacultyFadeFaintFaithFallFalseFameFamilyFamousFanFancyFantasyFarmFashionFatFatalFatherFatigueFaultFavoriteFeatureFebruaryFederalFeeFeedFeelFemaleFenceFestivalFetchFeverFewFiberFictionFieldFigureFileFilmFilterFinalFindFineFingerFinishFireFirmFirstFiscalFishFitFitnessFixFlagFlameFlashFlatFlavorFleeFlightFlipFloatFlockFloorFlowerFluidFlushFlyFoamFocusFogFoilFoldFollowFoodFootForceForestForgetForkFortuneForumForwardFossilFosterFoundFoxFragileFrameFrequentFreshFriendFringeFrogFrontFrostFrownFrozenFruitFuelFunFunnyFurnaceFuryFutureGadgetGainGalaxyGalleryGameGapGarageGarbageGardenGarlicGarmentGasGaspGateGatherGaugeGazeGeneralGeniusGenreGentleGenuineGestureGhostGiantGiftGiggleGingerGiraffeGirlGiveGladGlanceGlareGlassGlideGlimpseGlobeGloomGloryGloveGlowGlueGoatGoddessGoldGoodGooseGorillaGospelGossipGovernGownGrabGraceGrainGrantGrapeGrassGravityGreatGreenGridGriefGritGroceryGroupGrowGruntGuardGuessGuideGuiltGuitarGunGymHabitHairHalfHammerHamsterHandHappyHarborHardHarshHarvestHatHaveHawkHazardHeadHealthHeartHeavyHedgehogHeightHelloHelmetHelpHenHeroHiddenHighHillHintHipHireHistoryHobbyHockeyHoldHoleHolidayHollowHomeHoneyHoodHopeHornHorrorHorseHospitalHostHotelHourHoverHubHugeHumanHumbleHumorHundredHungryHuntHurdleHurryHurtHusbandHybridIceIconIdeaIdentifyIdleIgnoreIllIllegalIllnessImageImitateImmenseImmuneImpactImposeImproveImpulseInchIncludeIncomeIncreaseIndexIndicateIndoorIndustryInfantInflictInformInhaleInheritInitialInjectInjuryInmateInnerInnocentInputInquiryInsaneInsectInsideInspireInstallIntactInterestIntoInvestInviteInvolveIronIslandIsolateIssueItemIvoryJacketJaguarJarJazzJealousJeansJellyJewelJobJoinJokeJourneyJoyJudgeJuiceJumpJungleJuniorJunkJustKangarooKeenKeepKetchupKeyKickKidKidneyKindKingdomKissKitKitchenKiteKittenKiwiKneeKnifeKnockKnowLabLabelLaborLadderLadyLakeLampLanguageLaptopLargeLaterLatinLaughLaundryLavaLawLawnLawsuitLayerLazyLeaderLeafLearnLeaveLectureLeftLegLegalLegendLeisureLemonLendLengthLensLeopardLessonLetterLevelLiarLibertyLibraryLicenseLifeLiftLightLikeLimbLimitLinkLionLiquidListLittleLiveLizardLoadLoanLobsterLocalLockLogicLonelyLongLoopLotteryLoudLoungeLoveLoyalLuckyLuggageLumberLunarLunchLuxuryLyricsMachineMadMagicMagnetMaidMailMainMajorMakeMammalManManageMandateMangoMansionManualMapleMarbleMarchMarginMarineMarketMarriageMaskMassMasterMatchMaterialMathMatrixMatterMaximumMazeMeadowMeanMeasureMeatMechanicMedalMediaMelodyMeltMemberMemoryMentionMenuMercyMergeMeritMerryMeshMessageMetalMethodMiddleMidnightMilkMillionMimicMindMinimumMinorMinuteMiracleMirrorMiseryMissMistakeMixMixedMixtureMobileModelModifyMomMomentMonitorMonkeyMonsterMonthMoonMoralMoreMorningMosquitoMotherMotionMotorMountainMouseMoveMovieMuchMuffinMuleMultiplyMuscleMuseumMushroomMusicMustMutualMyselfMysteryMythNaiveNameNapkinNarrowNastyNationNatureNearNeckNeedNegativeNeglectNeitherNephewNerveNestNetNetworkNeutralNeverNewsNextNiceNightNobleNoiseNomineeNoodleNormalNorthNoseNotableNoteNothingNoticeNovelNowNuclearNumberNurseNutOakObeyObjectObligeObscureObserveObtainObviousOccurOceanOctoberOdorOffOfferOfficeOftenOilOkayOldOliveOlympicOmitOnceOneOnionOnlineOnlyOpenOperaOpinionOpposeOptionOrangeOrbitOrchardOrderOrdinaryOrganOrientOriginalOrphanOstrichOtherOutdoorOuterOutputOutsideOvalOvenOverOwnOwnerOxygenOysterOzonePactPaddlePagePairPalacePalmPandaPanelPanicPantherPaperParadeParentParkParrotPartyPassPatchPathPatientPatrolPatternPausePavePaymentPeacePeanutPearPeasantPelicanPenPenaltyPencilPeoplePepperPerfectPermitPersonPetPhonePhotoPhrasePhysicalPianoPicnicPicturePiecePigPigeonPillPilotPinkPioneerPipePistolPitchPizzaPlacePlanetPlasticPlatePlayPleasePledgePluckPlugPlungePoemPoetPointPolarPolePolicePondPonyPoolPopularPortionPositionPossiblePostPotatoPotteryPovertyPowderPowerPracticePraisePredictPreferPreparePresentPrettyPreventPricePridePrimaryPrintPriorityPrisonPrivatePrizeProblemProcessProduceProfitProgramProjectPromoteProofPropertyProsperProtectProudProvidePublicPuddingPullPulpPulsePumpkinPunchPupilPuppyPurchasePurityPurposePursePushPutPuzzlePyramidQualityQuantumQuarterQuestionQuickQuitQuizQuoteRabbitRaccoonRaceRackRadarRadioRailRainRaiseRallyRampRanchRandomRangeRapidRareRateRatherRavenRawRazorReadyRealReasonRebelRebuildRecallReceiveRecipeRecordRecycleReduceReflectReformRefuseRegionRegretRegularRejectRelaxReleaseReliefRelyRemainRememberRemindRemoveRenderRenewRentReopenRepairRepeatReplaceReportRequireRescueResembleResistResourceResponseResultRetireRetreatReturnReunionRevealReviewRewardRhythmRibRibbonRiceRichRideRidgeRifleRightRigidRingRiotRippleRiskRitualRivalRiverRoadRoastRobotRobustRocketRomanceRoofRookieRoomRoseRotateRoughRoundRouteRoyalRubberRudeRugRuleRunRunwayRuralSadSaddleSadnessSafeSailSaladSalmonSalonSaltSaluteSameSampleSandSatisfySatoshiSauceSausageSaveSayScaleScanScareScatterSceneSchemeSchoolScienceScissorsScorpionScoutScrapScreenScriptScrubSeaSearchSeasonSeatSecondSecretSectionSecuritySeedSeekSegmentSelectSellSeminarSeniorSenseSentenceSeriesServiceSessionSettleSetupSevenShadowShaftShallowShareShedShellSheriffShieldShiftShineShipShiverShockShoeShootShopShortShoulderShoveShrimpShrugShuffleShySiblingSickSideSiegeSightSignSilentSilkSillySilverSimilarSimpleSinceSingSirenSisterSituateSixSizeSkateSketchSkiSkillSkinSkirtSkullSlabSlamSleepSlenderSliceSlideSlightSlimSloganSlotSlowSlushSmallSmartSmileSmokeSmoothSnackSnakeSnapSniffSnowSoapSoccerSocialSockSodaSoftSolarSoldierSolidSolutionSolveSomeoneSongSoonSorrySortSoulSoundSoupSourceSouthSpaceSpareSpatialSpawnSpeakSpecialSpeedSpellSpendSphereSpiceSpiderSpikeSpinSpiritSplitSpoilSponsorSpoonSportSpotSpraySpreadSpringSpySquareSqueezeSquirrelStableStadiumStaffStageStairsStampStandStartStateStaySteakSteelStemStepStereoStickStillStingStockStomachStoneStoolStoryStoveStrategyStreetStrikeStrongStruggleStudentStuffStumbleStyleSubjectSubmitSubwaySuccessSuchSuddenSufferSugarSuggestSuitSummerSunSunnySunsetSuperSupplySupremeSureSurfaceSurgeSurpriseSurroundSurveySuspectSustainSwallowSwampSwapSwarmSwearSweetSwiftSwimSwingSwitchSwordSymbolSymptomSyrupSystemTableTackleTagTailTalentTalkTankTapeTargetTaskTasteTattooTaxiTeachTeamTellTenTenantTennisTentTermTestTextThankThatThemeThenTheoryThereTheyThingThisThoughtThreeThriveThrowThumbThunderTicketTideTigerTiltTimberTimeTinyTipTiredTissueTitleToastTobaccoTodayToddlerToeTogetherToiletTokenTomatoTomorrowToneTongueTonightToolToothTopTopicToppleTorchTornadoTortoiseTossTotalTouristTowardTowerTownToyTrackTradeTrafficTragicTrainTransferTrapTrashTravelTrayTreatTreeTrendTrialTribeTrickTriggerTrimTripTrophyTroubleTruckTrueTrulyTrumpetTrustTruthTryTubeTuitionTumbleTunaTunnelTurkeyTurnTurtleTwelveTwentyTwiceTwinTwistTwoTypeTypicalUglyUmbrellaUnableUnawareUncleUncoverUnderUndoUnfairUnfoldUnhappyUniformUniqueUnitUniverseUnknownUnlockUntilUnusualUnveilUpdateUpgradeUpholdUponUpperUpsetUrbanUrgeUsageUseUsedUsefulUselessUsualUtilityVacantVacuumVagueValidValleyValveVanVanishVaporVariousVastVaultVehicleVelvetVendorVentureVenueVerbVerifyVersionVeryVesselVeteranViableVibrantViciousVictoryVideoViewVillageVintageViolinVirtualVirusVisaVisitVisualVitalVividVocalVoiceVoidVolcanoVolumeVoteVoyageWageWagonWaitWalkWallWalnutWantWarfareWarmWarriorWashWaspWasteWaterWaveWayWealthWeaponWearWeaselWeatherWebWeddingWeekendWeirdWelcomeWestWetWhaleWhatWheatWheelWhenWhereWhipWhisperWideWidthWifeWildWillWinWindowWineWingWinkWinnerWinterWireWisdomWiseWishWitnessWolfWomanWonderWoodWoolWordWorkWorldWorryWorthWrapWreckWrestleWristWriteWrongYardYearYellowYouYoungYouthZebraZeroZoneZoo"
    mnemonics = re.findall('[A-Z][a-z]+', words)
    for r in range(size):
        lx = random.choice(mnemonics)
        ml += f" {lx}"
    return str(ml).lower()


def Mnemonic_To_Bytes(mnemonicWords):
    return _SHA256(mnemonicWords.encode('utf-8')).digest()


def Mnemonic_To_RootKey(mnemonic_words):
    mnemonic_ = ''.join(c for c in mnemonic_words if c.isalnum())
    mnemonic_ = mnemonic_.split(' ')
    seed_ = pbkdf2.PBKDF2(' '.join(mnemonic_), 'mnemonic' + '', iterations=2048, macmodule=hmac,
                          digestmodule=_SHA512).read(64)
    xprv_ = BIP32Key.fromEntropy(seed_)
    return xprv_.ExtendedKey()


# ===========================================================
def rxd_():
    se_ = []
    se_.clear()
    for m in range(256):
        se_.append(m)
    return random.sample(se_, len(se_))


# generated random bytes
def getBytes():
    """
Generate random bytes (seed)
    @return: bytes
    """
    bts = [b'\x00', b'\x01', b'\x02', b'\x03', b'\x04', b'\x05', b'\x06', b'\x07', b'\x08', b'\t', b'\n', b'\x0b',
           b'\x0c',
           b'\r', b'\x0e', b'\x0f', b'\x10', b'\x11', b'\x12', b'\x13', b'\x14', b'\x15', b'\x16', b'\x17', b'\x18',
           b'\x19', b'\x1a', b'\x1b', b'\x1c', b'\x1d', b'\x1e', b'\x1f', b' ', b'!', b'"', b'#', b'$', b'%', b'&',
           b"'",
           b'(', b')', b'*', b'+', b',', b'-', b'.', b'/', b'0', b'1', b'2', b'3', b'4', b'5', b'6', b'7', b'8', b'9',
           b':',
           b';', b'<', b'=', b'>', b'?', b'@', b'A', b'B', b'C', b'D', b'E', b'F', b'G', b'H', b'I', b'J', b'K', b'L',
           b'M',
           b'N', b'O', b'P', b'Q', b'R', b'S', b'T', b'U', b'V', b'W', b'X', b'Y', b'Z', b'[', b'\\', b']', b'^', b'_',
           b'`', b'a', b'b', b'c', b'd', b'e', b'f', b'g', b'h', b'i', b'j', b'k', b'l', b'm', b'n', b'o', b'p', b'q',
           b'r',
           b's', b't', b'u', b'v', b'w', b'x', b'y', b'z', b'{', b'|', b'}', b'~', b'\x7f', b'\x80', b'\x81', b'\x82',
           b'\x83', b'\x84', b'\x85', b'\x86', b'\x87', b'\x88', b'\x89', b'\x8a', b'\x8b', b'\x8c', b'\x8d', b'\x8e',
           b'\x8f', b'\x90', b'\x91', b'\x92', b'\x93', b'\x94', b'\x95', b'\x96', b'\x97', b'\x98', b'\x99', b'\x9a',
           b'\x9b', b'\x9c', b'\x9d', b'\x9e', b'\x9f', b'\xa0', b'\xa1', b'\xa2', b'\xa3', b'\xa4', b'\xa5', b'\xa6',
           b'\xa7', b'\xa8', b'\xa9', b'\xaa', b'\xab', b'\xac', b'\xad', b'\xae', b'\xaf', b'\xb0', b'\xb1', b'\xb2',
           b'\xb3', b'\xb4', b'\xb5', b'\xb6', b'\xb7', b'\xb8', b'\xb9', b'\xba', b'\xbb', b'\xbc', b'\xbd', b'\xbe',
           b'\xbf', b'\xc0', b'\xc1', b'\xc2', b'\xc3', b'\xc4', b'\xc5', b'\xc6', b'\xc7', b'\xc8', b'\xc9', b'\xca',
           b'\xcb', b'\xcc', b'\xcd', b'\xce', b'\xcf', b'\xd0', b'\xd1', b'\xd2', b'\xd3', b'\xd4', b'\xd5', b'\xd6',
           b'\xd7', b'\xd8', b'\xd9', b'\xda', b'\xdb', b'\xdc', b'\xdd', b'\xde', b'\xdf', b'\xe0', b'\xe1', b'\xe2',
           b'\xe3', b'\xe4', b'\xe5', b'\xe6', b'\xe7', b'\xe8', b'\xe9', b'\xea', b'\xeb', b'\xec', b'\xed', b'\xee',
           b'\xef', b'\xf0', b'\xf1', b'\xf2', b'\xf3', b'\xf4', b'\xf5', b'\xf6', b'\xf7', b'\xf8', b'\xf9', b'\xfa',
           b'\xfb', b'\xfc', b'\xfd', b'\xfe', b'\xff']
    plus = [rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(),
            rxd_(), rxd_(),
            rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(), rxd_(),
            rxd_(), rxd_(),
            rxd_(), rxd_()]
    for i in range(256):
        byte_ = bts[plus[0][i]] + bts[plus[1][i]] + bts[plus[2][i]] + bts[plus[3][i]] + bts[plus[4][i]] + bts[
            plus[5][i]] + bts[
                    plus[6][i]] + bts[plus[7][i]] + bts[plus[8][i]] + bts[plus[9][i]] + bts[plus[10][i]] + bts[
                    plus[11][i]] + bts[
                    plus[12][i]] + bts[plus[13][i]] + bts[plus[14][i]] + bts[plus[15][i]] + bts[plus[16][i]] + bts[
                    plus[17][i]] + \
                bts[
                    plus[18][i]] + bts[plus[19][i]] + bts[plus[20][i]] + bts[plus[21][i]] + bts[plus[22][i]] + bts[
                    plus[23][i]] + \
                bts[
                    plus[24][i]] + bts[plus[25][i]] + bts[plus[26][i]] + bts[plus[27][i]] + bts[plus[28][i]] + bts[
                    plus[29][i]] + \
                bts[
                    plus[30][i]] + bts[plus[31][i]]
        return byte_


def Bytes_To_Mnemonic(bytestring): return Mnemonic('english').to_mnemonic(bytestring)


def Bytes_To_PrivateKey(bytestring): return _decode(bytestring).decode('utf-8')


def Bytes_To_PublicKey(bytestring, compress=False):
    if compress:
        return PrivateKey_To_PublicKey(Bytes_To_PrivateKey(bytestring), True)
    else:
        return PrivateKey_To_PublicKey(Bytes_To_PrivateKey(bytestring))

# --------------------------------------------------------------------------------
# Check Value Bitcoin Address Balance Return [str]
def Btc_Balance(addr):
    req = requests.get(f"https://bitcoin.atomicwallet.io/api/v2/address/{addr}").json()
    return dict(req)['balance']

# --------------------------------------------------------------------------------
# Check Value Ethereum Address Balance Return [str]
def Eth_Balance(addr):
    req = requests.get(f"https://ethereum.atomicwallet.io/api/v2/address/{addr}").json()
    return dict(req)['balance']

# --------------------------------------------------------------------------------
# Check Value Litecoin Address Balance Return [str]
def Ltc_Balance(address):
    """ Check Value Litecoin Address Balance Return [str] """
    req = requests.get(f"https://litecoin.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']

# --------------------------------------------------------------------------------
# Check Value TRON Address Balance Return [str]
def Trx_Balance(address):
    """ Check Value TRON Address Balance Return [str] """
    req = requests.get(f"https://apilist.tronscanapi.com/api/accountv2?address={address}&source=true").json()
    return dict(req)['balance']

# --------------------------------------------------------------------------------
# Check Value Dogecoin Address Balance Return [str]
def Doge_Balance(address):
    """ Check Value Dogecoin Address Balance Return [str] """
    req = requests.get(f"https://dogecoin.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']

# --------------------------------------------------------------------------------
# Check Value Bitcoin Gold Address Balance Return [str]
def Btg_Balance(address):
    """ Check Value Bitcoin Gold Address Balance Return [str] """
    req = requests.get(f"https://bgold.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']

# --------------------------------------------------------------------------------
# Check Value DigiByte Address Balance Return [str]
def Dgb_Balance(address):
    """ Check Value DigiByte Address Balance Return [str] """
    req = requests.get(f"https://digibyte.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']

# --------------------------------------------------------------------------------
# Check Value Ravencoin Address Balance Return [str]
def Rvn_Balance(address):
    """ Check Value Ravencoin Address Balance Return [str] """
    req = requests.get(f"https://ravencoin.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']

# --------------------------------------------------------------------------------
# Check Value Qtum Address Balance Return [str]
def Qtum_Balance(address):
    """ Check Value Qtum Address Balance Return [str] """
    req = requests.get(f"https://qtum.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']

# --------------------------------------------------------------------------------
# Check Value ZCASH Address Balance Return [str]
def Zec_Balance(address):
    """ Check Value ZCASH Address Balance Return [str] """
    req = requests.get(f"https://zcash.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']

# --------------------------------------------------------------------------------
# Check Value Dash Address Balance : return [str]
def Dash_Balance(address):
    """ # Check Value Dash Address Balance : return [str] """
    req = requests.get(f"https://dash.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']
