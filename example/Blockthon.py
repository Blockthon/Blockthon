# //////////////////////////////////////////////////
# // Github : github.com/Pymmdrza                 //
# // official Page : https://github.com/Blockthon //
# //////////////////////////////////////////////////

import codecs, ecdsa, hashlib, hmac, pbkdf2, os, base58
from bit import Key
from bit.format import bytes_to_wif
from binascii import hexlify as _decode
from binascii import unhexlify as _encode
from mnemonic import Mnemonic
import requests, json, re, random
from hdwallet import HDWallet
from hdwallet.symbols import BTC, ETH, TRX, LTC, DOGE, DGB, RVN, DASH, BTG, VIA, QTUM, ZEC
from bip32utils import BIP32Key
from bip32utils import BIP32_HARDEN
from bip32utils import Base58
import binascii


def PrivateKey():
    return os.urandom(32).hex()


# --------------------------------------------------------------------------------

def base58_(hashaddr_):
    a_ = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'
    b58_ = ''
    _lz = len(hashaddr_) - len(hashaddr_.lstrip('0'))
    _addrNum = int(hashaddr_, 16)
    while _addrNum > 0:
        dg_ = _addrNum % 58
        cdg_ = a_[dg_]
        b58_ = cdg_ + b58_
        _addrNum //= 58
    on_ = _lz // 2
    for one in range(on_):
        b58_ = '1' + b58_
    return b58_


# --------------------------------------------------------------------------------

# Generated Mnemonic Random
def getMnemonic(size=12):
    """ Size for Generated words 12 or 24 default 12 """
    ml = ''
    words = "AbandonAbilityAbleAboutAboveAbsentAbsorbAbstractAbsurdAbuseAccessAccidentAccountAccuseAchieveAcidAcousticAcquireAcrossActActionActorActressActualAdaptAddAddictAddressAdjustAdmitAdultAdvanceAdviceAerobicAffairAffordAfraidAgainAgeAgentAgreeAheadAimAirAirportAisleAlarmAlbumAlcoholAlertAlienAllAlleyAllowAlmostAloneAlphaAlreadyAlsoAlterAlwaysAmateurAmazingAmongAmountAmusedAnalystAnchorAncientAngerAngleAngryAnimalAnkleAnnounceAnnualAnotherAnswerAntennaAntiqueAnxietyAnyApartApologyAppearAppleApproveAprilArchArcticAreaArenaArgueArmArmedArmorArmyAroundArrangeArrestArriveArrowArtArtefactArtistArtworkAskAspectAssaultAssetAssistAssumeAsthmaAthleteAtomAttackAttendAttitudeAttractAuctionAuditAugustAuntAuthorAutoAutumnAverageAvocadoAvoidAwakeAwareAwayAwesomeAwfulAwkwardAxisBabyBachelorBaconBadgeBagBalanceBalconyBallBambooBananaBannerBarBarelyBargainBarrelBaseBasicBasketBattleBeachBeanBeautyBecauseBecomeBeefBeforeBeginBehaveBehindBelieveBelowBeltBenchBenefitBestBetrayBetterBetweenBeyondBicycleBidBikeBindBiologyBirdBirthBitterBlackBladeBlameBlanketBlastBleakBlessBlindBloodBlossomBlouseBlueBlurBlushBoardBoatBodyBoilBombBoneBonusBookBoostBorderBoringBorrowBossBottomBounceBoxBoyBracketBrainBrandBrassBraveBreadBreezeBrickBridgeBriefBrightBringBriskBroccoliBrokenBronzeBroomBrotherBrownBrushBubbleBuddyBudgetBuffaloBuildBulbBulkBulletBundleBunkerBurdenBurgerBurstBusBusinessBusyButterBuyerBuzzCabbageCabinCableCactusCageCakeCallCalmCameraCampCanCanalCancelCandyCannonCanoeCanvasCanyonCapableCapitalCaptainCarCarbonCardCargoCarpetCarryCartCaseCashCasinoCastleCasualCatCatalogCatchCategoryCattleCaughtCauseCautionCaveCeilingCeleryCementCensusCenturyCerealCertainChairChalkChampionChangeChaosChapterChargeChaseChatCheapCheckCheeseChefCherryChestChickenChiefChildChimneyChoiceChooseChronicChuckleChunkChurnCigarCinnamonCircleCitizenCityCivilClaimClapClarifyClawClayCleanClerkCleverClickClientCliffClimbClinicClipClockClogCloseClothCloudClownClubClumpClusterClutchCoachCoastCoconutCodeCoffeeCoilCoinCollectColorColumnCombineComeComfortComicCommonCompanyConcertConductConfirmCongressConnectConsiderControlConvinceCookCoolCopperCopyCoralCoreCornCorrectCostCottonCouchCountryCoupleCourseCousinCoverCoyoteCrackCradleCraftCramCraneCrashCraterCrawlCrazyCreamCreditCreekCrewCricketCrimeCrispCriticCropCrossCrouchCrowdCrucialCruelCruiseCrumbleCrunchCrushCryCrystalCubeCultureCupCupboardCuriousCurrentCurtainCurveCushionCustomCuteCycleDadDamageDampDanceDangerDaringDashDaughterDawnDayDealDebateDebrisDecadeDecemberDecideDeclineDecorateDecreaseDeerDefenseDefineDefyDegreeDelayDeliverDemandDemiseDenialDentistDenyDepartDependDepositDepthDeputyDeriveDescribeDesertDesignDeskDespairDestroyDetailDetectDevelopDeviceDevoteDiagramDialDiamondDiaryDiceDieselDietDifferDigitalDignityDilemmaDinnerDinosaurDirectDirtDisagreeDiscoverDiseaseDishDismissDisorderDisplayDistanceDivertDivideDivorceDizzyDoctorDocumentDogDollDolphinDomainDonateDonkeyDonorDoorDoseDoubleDoveDraftDragonDramaDrasticDrawDreamDressDriftDrillDrinkDripDriveDropDrumDryDuckDumbDuneDuringDustDutchDutyDwarfDynamicEagerEagleEarlyEarnEarthEasilyEastEasyEchoEcologyEconomyEdgeEditEducateEffortEggEightEitherElbowElderElectricElegantElementElephantElevatorEliteElseEmbarkEmbodyEmbraceEmergeEmotionEmployEmpowerEmptyEnableEnactEndEndlessEndorseEnemyEnergyEnforceEngageEngineEnhanceEnjoyEnlistEnoughEnrichEnrollEnsureEnterEntireEntryEnvelopeEpisodeEqualEquipEraEraseErodeErosionErrorEruptEscapeEssayEssenceEstateEternalEthicsEvidenceEvilEvokeEvolveExactExampleExcessExchangeExciteExcludeExcuseExecuteExerciseExhaustExhibitExileExistExitExoticExpandExpectExpireExplainExposeExpressExtendExtraEyeEyebrowFabricFaceFacultyFadeFaintFaithFallFalseFameFamilyFamousFanFancyFantasyFarmFashionFatFatalFatherFatigueFaultFavoriteFeatureFebruaryFederalFeeFeedFeelFemaleFenceFestivalFetchFeverFewFiberFictionFieldFigureFileFilmFilterFinalFindFineFingerFinishFireFirmFirstFiscalFishFitFitnessFixFlagFlameFlashFlatFlavorFleeFlightFlipFloatFlockFloorFlowerFluidFlushFlyFoamFocusFogFoilFoldFollowFoodFootForceForestForgetForkFortuneForumForwardFossilFosterFoundFoxFragileFrameFrequentFreshFriendFringeFrogFrontFrostFrownFrozenFruitFuelFunFunnyFurnaceFuryFutureGadgetGainGalaxyGalleryGameGapGarageGarbageGardenGarlicGarmentGasGaspGateGatherGaugeGazeGeneralGeniusGenreGentleGenuineGestureGhostGiantGiftGiggleGingerGiraffeGirlGiveGladGlanceGlareGlassGlideGlimpseGlobeGloomGloryGloveGlowGlueGoatGoddessGoldGoodGooseGorillaGospelGossipGovernGownGrabGraceGrainGrantGrapeGrassGravityGreatGreenGridGriefGritGroceryGroupGrowGruntGuardGuessGuideGuiltGuitarGunGymHabitHairHalfHammerHamsterHandHappyHarborHardHarshHarvestHatHaveHawkHazardHeadHealthHeartHeavyHedgehogHeightHelloHelmetHelpHenHeroHiddenHighHillHintHipHireHistoryHobbyHockeyHoldHoleHolidayHollowHomeHoneyHoodHopeHornHorrorHorseHospitalHostHotelHourHoverHubHugeHumanHumbleHumorHundredHungryHuntHurdleHurryHurtHusbandHybridIceIconIdeaIdentifyIdleIgnoreIllIllegalIllnessImageImitateImmenseImmuneImpactImposeImproveImpulseInchIncludeIncomeIncreaseIndexIndicateIndoorIndustryInfantInflictInformInhaleInheritInitialInjectInjuryInmateInnerInnocentInputInquiryInsaneInsectInsideInspireInstallIntactInterestIntoInvestInviteInvolveIronIslandIsolateIssueItemIvoryJacketJaguarJarJazzJealousJeansJellyJewelJobJoinJokeJourneyJoyJudgeJuiceJumpJungleJuniorJunkJustKangarooKeenKeepKetchupKeyKickKidKidneyKindKingdomKissKitKitchenKiteKittenKiwiKneeKnifeKnockKnowLabLabelLaborLadderLadyLakeLampLanguageLaptopLargeLaterLatinLaughLaundryLavaLawLawnLawsuitLayerLazyLeaderLeafLearnLeaveLectureLeftLegLegalLegendLeisureLemonLendLengthLensLeopardLessonLetterLevelLiarLibertyLibraryLicenseLifeLiftLightLikeLimbLimitLinkLionLiquidListLittleLiveLizardLoadLoanLobsterLocalLockLogicLonelyLongLoopLotteryLoudLoungeLoveLoyalLuckyLuggageLumberLunarLunchLuxuryLyricsMachineMadMagicMagnetMaidMailMainMajorMakeMammalManManageMandateMangoMansionManualMapleMarbleMarchMarginMarineMarketMarriageMaskMassMasterMatchMaterialMathMatrixMatterMaximumMazeMeadowMeanMeasureMeatMechanicMedalMediaMelodyMeltMemberMemoryMentionMenuMercyMergeMeritMerryMeshMessageMetalMethodMiddleMidnightMilkMillionMimicMindMinimumMinorMinuteMiracleMirrorMiseryMissMistakeMixMixedMixtureMobileModelModifyMomMomentMonitorMonkeyMonsterMonthMoonMoralMoreMorningMosquitoMotherMotionMotorMountainMouseMoveMovieMuchMuffinMuleMultiplyMuscleMuseumMushroomMusicMustMutualMyselfMysteryMythNaiveNameNapkinNarrowNastyNationNatureNearNeckNeedNegativeNeglectNeitherNephewNerveNestNetNetworkNeutralNeverNewsNextNiceNightNobleNoiseNomineeNoodleNormalNorthNoseNotableNoteNothingNoticeNovelNowNuclearNumberNurseNutOakObeyObjectObligeObscureObserveObtainObviousOccurOceanOctoberOdorOffOfferOfficeOftenOilOkayOldOliveOlympicOmitOnceOneOnionOnlineOnlyOpenOperaOpinionOpposeOptionOrangeOrbitOrchardOrderOrdinaryOrganOrientOriginalOrphanOstrichOtherOutdoorOuterOutputOutsideOvalOvenOverOwnOwnerOxygenOysterOzonePactPaddlePagePairPalacePalmPandaPanelPanicPantherPaperParadeParentParkParrotPartyPassPatchPathPatientPatrolPatternPausePavePaymentPeacePeanutPearPeasantPelicanPenPenaltyPencilPeoplePepperPerfectPermitPersonPetPhonePhotoPhrasePhysicalPianoPicnicPicturePiecePigPigeonPillPilotPinkPioneerPipePistolPitchPizzaPlacePlanetPlasticPlatePlayPleasePledgePluckPlugPlungePoemPoetPointPolarPolePolicePondPonyPoolPopularPortionPositionPossiblePostPotatoPotteryPovertyPowderPowerPracticePraisePredictPreferPreparePresentPrettyPreventPricePridePrimaryPrintPriorityPrisonPrivatePrizeProblemProcessProduceProfitProgramProjectPromoteProofPropertyProsperProtectProudProvidePublicPuddingPullPulpPulsePumpkinPunchPupilPuppyPurchasePurityPurposePursePushPutPuzzlePyramidQualityQuantumQuarterQuestionQuickQuitQuizQuoteRabbitRaccoonRaceRackRadarRadioRailRainRaiseRallyRampRanchRandomRangeRapidRareRateRatherRavenRawRazorReadyRealReasonRebelRebuildRecallReceiveRecipeRecordRecycleReduceReflectReformRefuseRegionRegretRegularRejectRelaxReleaseReliefRelyRemainRememberRemindRemoveRenderRenewRentReopenRepairRepeatReplaceReportRequireRescueResembleResistResourceResponseResultRetireRetreatReturnReunionRevealReviewRewardRhythmRibRibbonRiceRichRideRidgeRifleRightRigidRingRiotRippleRiskRitualRivalRiverRoadRoastRobotRobustRocketRomanceRoofRookieRoomRoseRotateRoughRoundRouteRoyalRubberRudeRugRuleRunRunwayRuralSadSaddleSadnessSafeSailSaladSalmonSalonSaltSaluteSameSampleSandSatisfySatoshiSauceSausageSaveSayScaleScanScareScatterSceneSchemeSchoolScienceScissorsScorpionScoutScrapScreenScriptScrubSeaSearchSeasonSeatSecondSecretSectionSecuritySeedSeekSegmentSelectSellSeminarSeniorSenseSentenceSeriesServiceSessionSettleSetupSevenShadowShaftShallowShareShedShellSheriffShieldShiftShineShipShiverShockShoeShootShopShortShoulderShoveShrimpShrugShuffleShySiblingSickSideSiegeSightSignSilentSilkSillySilverSimilarSimpleSinceSingSirenSisterSituateSixSizeSkateSketchSkiSkillSkinSkirtSkullSlabSlamSleepSlenderSliceSlideSlightSlimSloganSlotSlowSlushSmallSmartSmileSmokeSmoothSnackSnakeSnapSniffSnowSoapSoccerSocialSockSodaSoftSolarSoldierSolidSolutionSolveSomeoneSongSoonSorrySortSoulSoundSoupSourceSouthSpaceSpareSpatialSpawnSpeakSpecialSpeedSpellSpendSphereSpiceSpiderSpikeSpinSpiritSplitSpoilSponsorSpoonSportSpotSpraySpreadSpringSpySquareSqueezeSquirrelStableStadiumStaffStageStairsStampStandStartStateStaySteakSteelStemStepStereoStickStillStingStockStomachStoneStoolStoryStoveStrategyStreetStrikeStrongStruggleStudentStuffStumbleStyleSubjectSubmitSubwaySuccessSuchSuddenSufferSugarSuggestSuitSummerSunSunnySunsetSuperSupplySupremeSureSurfaceSurgeSurpriseSurroundSurveySuspectSustainSwallowSwampSwapSwarmSwearSweetSwiftSwimSwingSwitchSwordSymbolSymptomSyrupSystemTableTackleTagTailTalentTalkTankTapeTargetTaskTasteTattooTaxiTeachTeamTellTenTenantTennisTentTermTestTextThankThatThemeThenTheoryThereTheyThingThisThoughtThreeThriveThrowThumbThunderTicketTideTigerTiltTimberTimeTinyTipTiredTissueTitleToastTobaccoTodayToddlerToeTogetherToiletTokenTomatoTomorrowToneTongueTonightToolToothTopTopicToppleTorchTornadoTortoiseTossTotalTouristTowardTowerTownToyTrackTradeTrafficTragicTrainTransferTrapTrashTravelTrayTreatTreeTrendTrialTribeTrickTriggerTrimTripTrophyTroubleTruckTrueTrulyTrumpetTrustTruthTryTubeTuitionTumbleTunaTunnelTurkeyTurnTurtleTwelveTwentyTwiceTwinTwistTwoTypeTypicalUglyUmbrellaUnableUnawareUncleUncoverUnderUndoUnfairUnfoldUnhappyUniformUniqueUnitUniverseUnknownUnlockUntilUnusualUnveilUpdateUpgradeUpholdUponUpperUpsetUrbanUrgeUsageUseUsedUsefulUselessUsualUtilityVacantVacuumVagueValidValleyValveVanVanishVaporVariousVastVaultVehicleVelvetVendorVentureVenueVerbVerifyVersionVeryVesselVeteranViableVibrantViciousVictoryVideoViewVillageVintageViolinVirtualVirusVisaVisitVisualVitalVividVocalVoiceVoidVolcanoVolumeVoteVoyageWageWagonWaitWalkWallWalnutWantWarfareWarmWarriorWashWaspWasteWaterWaveWayWealthWeaponWearWeaselWeatherWebWeddingWeekendWeirdWelcomeWestWetWhaleWhatWheatWheelWhenWhereWhipWhisperWideWidthWifeWildWillWinWindowWineWingWinkWinnerWinterWireWisdomWiseWishWitnessWolfWomanWonderWoodWoolWordWorkWorldWorryWorthWrapWreckWrestleWristWriteWrongYardYearYellowYouYoungYouthZebraZeroZoneZoo"
    mnemonics = re.findall('[A-Z][a-z]+', words)
    z = 0
    c = 0
    for r in range(size):
        lx = random.choice(mnemonics)
        ml += f" {lx}"

    return str(ml).lower()


# --------------------------------------------------------------------------------
# Convert Mnemonic to Hex (Private Key)
def Mnemonic_To_PrivateKey(MnemonicWord):
    return PrivateKey_From_RootKey(Mnemonic_To_RootKey(MnemonicWord))


# --------------------------------------------------------------------------------

# Convert Mnemonic to Root (xprv) Private key Hex From Root Key : return [str]
def Mnemonic_To_RootPrivateKey(Mnemonic_Words):
    """ Convert Mnemonic to Private key Hex From Root Key : return [str] """
    return RootPrivateKey_From_RootKey(Mnemonic_To_RootKey(Mnemonic_Words))


# --------------------------------------------------------------------------------

# Generated root key to private key hex SHA256
def PrivateKey_From_RootKey(xprv):
    deco_ = base58.b58decode_check(xprv)
    pvk_b_ = deco_[46:78]
    return pvk_b_.hex()


# --------------------------------------------------------------------------------

# Generated Root Key Wallet From Mnemonic's with BIP39
def Mnemonic_To_RootKey(mnemonic_words):
    mnemonic_ = ''.join(c for c in mnemonic_words if c.isalnum())
    mnemonic_ = mnemonic_.split(' ')
    seed_ = pbkdf2.PBKDF2(' '.join(mnemonic_), 'mnemonic' + '', iterations=2048, macmodule=hmac,
                          digestmodule=hashlib.sha512).read(64)
    xprv_ = BIP32Key.fromEntropy(seed_)
    return xprv_.ExtendedKey()


# --------------------------------------------------------------------------------

# Generated Private Key From Root Key (xprv)
def RootPrivateKey_From_RootKey(xprv):
    decoded = base58.b58decode_check(xprv)
    return decoded.hex()


# --------------------------------------------------------------------------------


# Generated Random Binary : return [str]
def getBin(size):
    """ Generated Random Binary : return [str] """
    bs_ = ''
    for _ in range(size):
        bs_ += random.choice(['0', '1'])
    return bs_


# --------------------------------------------------------------------------------


# Generated Bitcoin Address P2PKH From Private Key (HEX)
def P2PKH_From_PrivateKey(privatekey):
    """ Generated Bitcoin Address P2PKH From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=BTC)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# --------------------------------------------------------------------------------


# Generated Bitcoin Address P2SH From Private Key (HEX)
def P2SH_From_PrivateKey(privatekey):
    """ Generated Bitcoin Address P2SH From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=BTC)
    wallet.from_private_key(privatekey)
    return wallet.p2sh_address()


# --------------------------------------------------------------------------------


# Generated Bitcoin Address P2WSH From Private Key (HEX)
def P2WSH_From_PrivateKey(privatekey):
    """ Generated Bitcoin Address P2WSH From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=BTC)
    wallet.from_private_key(privatekey)
    return wallet.p2wsh_address()


# --------------------------------------------------------------------------------


# Generated Bitcoin Address P2WPKH From Private Key (HEX)
def P2WPKH_From_PrivateKey(privatekey):
    """ Generated Bitcoin Address P2WPKH From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=BTC)
    wallet.from_private_key(privatekey)
    return wallet.p2wpkh_address()


# --------------------------------------------------------------------------------


# Generated Bitcoin Address P2WSH in P2sh From Private Key (HEX)
def P2WSH_in_P2SH_From_PrivateKey(privatekey):
    """ Generated Bitcoin Address P2wsh in P2sh From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=BTC)
    wallet.from_private_key(privatekey)
    return wallet.p2wsh_in_p2sh_address()


# --------------------------------------------------------------------------------


# Generated Bitcoin Address P2wpkh in P2sh From Private Key (HEX)
def P2WPKH_in_P2SH_From_PrivateKey(privatekey):
    """ Generated Bitcoin Address P2wpkh in P2sh From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=BTC)
    wallet.from_private_key(privatekey)
    return wallet.p2wpkh_in_p2sh_address()


# --------------------------------------------------------------------------------


# Generated and convert Ethereum Address Wallet From Private Key (HEX)
def ETH_From_PrivateKey(privatekey):
    """ Generated and convert Ethereum Address Wallet From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=ETH)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# --------------------------------------------------------------------------------


# Generated and convert TRON Address Wallet From Private Key (HEX)
def TRX_From_PrivateKey(privatekey):
    """ Generated and convert TRON Address Wallet From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=TRX)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# --------------------------------------------------------------------------------


# Generated and convert Dogecoin Address Wallet From Private Key (HEX)
def DOGE_From_PrivateKey(privatekey):
    """ Generated and convert Dogecoin Address Wallet From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=DOGE)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# --------------------------------------------------------------------------------


# Generated and convert Dash Address Wallet From Private Key (HEX)
def DASH_From_PrivateKey(privatekey):
    """ Generated and convert Dash Address Wallet From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=DASH)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# --------------------------------------------------------------------------------


# Generated and convert Bitcoin Gold Address Wallet From Private Key (HEX)
def BTG_From_PrivateKey(privatekey):
    """ Generated and convert Bitcoin Gold Address Wallet From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=BTG)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# --------------------------------------------------------------------------------


# Generated and convert Litecoin Address Wallet From Private Key (HEX)
def LTC_From_PrivateKey(privatekey):
    """ Generated and convert Litecoin Address Wallet From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=LTC)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# --------------------------------------------------------------------------------


# Generated and convert DigiByte Address Wallet From Private Key (HEX)
def DigiByte_From_PrivateKey(privatekey):
    """ Generated and convert DigiByte Address Wallet From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=DGB)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# --------------------------------------------------------------------------------


# Generated and convert Rave Coin Address Wallet From Private Key (HEX)
def RVN_From_PrivateKey(privatekey):
    """ Generated and convert Rave Coin Address Wallet From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=RVN)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# --------------------------------------------------------------------------------


# Generated and convert Via coin Address Wallet From Private Key (HEX)
def VIA_From_PrivateKey(privatekey):
    """ Generated and convert Via coin Address Wallet From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=VIA)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# --------------------------------------------------------------------------------


# Generated and convert Qtum Address Wallet From Private Key (HEX)
def QTUM_From_PrivateKey(privatekey):
    """ Generated and convert Qtum Address Wallet From Private Key (HEX) """
    wallet: HDWallet = HDWallet(symbol=QTUM)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# --------------------------------------------------------------------------------


# Generated and convert ZCash Address Wallet From Private Key (HEX)
def ZEC_From_PrivateKey(privatekey):
    """Generated and convert ZCash Address Wallet From Private Key (HEX)"""
    wallet: HDWallet = HDWallet(symbol=ZEC)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# --------------------------------------------------------------------------------


def PrivateKey_To_PublicKey(privatekey):
    key = ecdsa.SigningKey.from_string(codecs.decode(privatekey, 'hex'), curve=ecdsa.SECP256k1).verifying_key
    key_hex = key.hex()
    public_key = b'04' + key_hex
    return public_key


# --------------------------------------------------------------------------------


# Convert Private Key to Dec (Number - integer)
def PrivateKey_To_Dec(private_key):
    """ Convert Hex to Integer Return int [dec] """
    return int(private_key, 16)


# --------------------------------------------------------------------------------


# Convert Private Key (Hex) To decimal (Number)
def HEX_To_DEC(key):
    """ Convert Private Key (Hex) To Decimal (Number) return [int] """
    dec_number: int = 0
    for digit in key:
        dec_number: int = dec_number * 16
        if '0' <= digit <= '9':
            dec_number += ord(digit) - ord('0')
        elif 'A' <= digit <= 'F':
            dec_number += ord(digit) - ord('A') + 10
        elif 'a' <= digit <= 'f':
            dec_number += ord(digit) - ord('a') + 10
    return dec_number


# --------------------------------------------------------------------------------


# convert Binary to hex (Private key) : return [str]
def PrivateKey_From_Binary(Bin_string):
    """ convert binary to private key (hex) return [str] """
    return hex(int(Bin_string, 2))[2:].zfill(32)


# --------------------------------------------------------------------------------


# Convert Number (Dec) To Private Key (HEX)
def PrivateKey_From_int(int_):
    """ Convert Number (Integer) To Private key (HEX) [fast method] Return str """
    return "%064x" % int_


# --------------------------------------------------------------------------------


def PrivateKey_From_Passphrase(passphrase):
    return str(hashlib.sha256(passphrase.encode('utf-8')).hexdigest())


# --------------------------------------------------------------------------------


# convert Private Key (hex) to Binary : return [int]
def PrivateKey_To_Binary(hexString):
    """ convert Private Key (hex) to Binary : return [int] """
    return bin(int(hexString, 16))[2:].zfill(256)


# --------------------------------------------------------------------------------


# Convert Private Key (HEX) To Bytes
def PrivateKey_To_Bytes(private_key):
    """ Convert Hex to Bytes and Return binary [byte] """
    bs_ = codecs.decode(private_key, 'hex')
    return bs_


# --------------------------------------------------------------------------------


# Convert Binary 256 To HEX For Private Key : Return [str]
def Binary_To_PrivateKey(Bin_):
    """ Convert Binary 256 To HEX For Private Key : Return [str] """
    return hex(int(Bin_, 2))[2:].zfill(32)


# --------------------------------------------------------------------------------


# Convert Bytes (SEED) To Mnemonic
def Bytes_To_Mnemonic(Byte_String):
    """ Convert Bytes to Mnemonic Word with 256 bit Size and Return str [mnemonic] """
    return Mnemonic('english').to_mnemonic(Byte_String)


# --------------------------------------------------------------------------------


# Convert Bytes (Seed) To HEX (Private Key)
def Bytes_To_PrivateKey(Byte_String):
    """ convert bytes to hex for private key and return str [private_key] """
    return _decode(Byte_String).decode('utf-8')


# --------------------------------------------------------------------------------
# Convert Private Key (HEX) To Mnemonic
def PrivateKey_To_Mnemonic(private_key):
    """Convert HEX To Bytes , after converting , convert to Mnemonic (WORD)
    PrivateKey: str --> Bytes (seed) --> Mnemonic(Word): str"""
    byte_string = PrivateKey_To_Bytes(private_key)
    valid_lengths = [16, 20, 24, 28, 32]
    nearest_length = min(valid_lengths, key=lambda x: abs(x - len(byte_string)))
    if len(byte_string) != nearest_length:
        byte_string = byte_string[:nearest_length]
    return Mnemonic('english').to_mnemonic(byte_string)


# --------------------------------------------------------------------------------


# Convert Byte To WIF Compressed and Un Compressed
def Bytes_To_WIF(Bytes_, compressed=False):
    """ convert bytes to wif and after compressed and uncompressed address """
    if compressed:
        wif = bytes_to_wif(Bytes_, compressed=True)
    else:
        wif = bytes_to_wif(Bytes_)
    return wif


# --------------------------------------------------------------------------------
# Generated Bitcoin Address From Public Key
def PublicKey_To_Addr(public_key):
    PublicKeyByte = codecs.decode(public_key, 'hex')
    sha256_bpk = hashlib.sha256(PublicKeyByte)
    sha256_bpk_digest = sha256_bpk.digest()
    ripemd160_bpk = hashlib.new('ripemd160')
    ripemd160_bpk.update(sha256_bpk_digest)
    ripemd160_bpk_digest = ripemd160_bpk.digest()
    ripemd160_bpk_hex = codecs.encode(ripemd160_bpk_digest, 'hex')
    NetByte = b'00'
    NetBTCBytePubKey = NetByte + ripemd160_bpk_hex
    NetBTCPubKeyByte = codecs.decode(
        NetBTCBytePubKey, 'hex')
    Hash256N = hashlib.sha256(NetBTCPubKeyByte)
    Hash256N_digest = Hash256N.digest()
    sha256_2_nbpk = hashlib.sha256(Hash256N_digest)
    sha256_2_nbpk_digest = sha256_2_nbpk.digest()
    sha256_2_hex = codecs.encode(sha256_2_nbpk_digest, 'hex')
    checksum = sha256_2_hex[:8]
    addrHex = (NetBTCBytePubKey + checksum).decode('utf-8')
    return base58_(addrHex)


# --------------------------------------------------------------------------------


# compressed and un compressed address from private key hex
def Addr_From_PrivateKey(private_key, compress=False):
    """ convert hex private key to compressed address and un compressed : return [str] (for compressed address
    'compress=True' | for un compressed address 'compress=False')"""
    seed = codecs.decode(private_key, 'hex')
    if compress:
        _wc = bytes_to_wif(seed, compressed=True)
        bits = Key(_wc)
        return bits.address
    else:
        _wu = bytes_to_wif(seed, compressed=False)
        bitu = Key(_wu)
        return bitu.address


# --------------------------------------------------------------------------------


# Check Value Bitcoin Address Balance Return Value [str: '0']
def Balance(address):
    """check balance of value per Bitcoin address and return : str [balance]"""
    req = requests.get(f"https://bitcoin.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------


# Check Value Ethereum Address Balance Return [str]
def Balance_Ethereum(address):
    """ Check Value Ethereum Address Balance Return [str] """
    req = requests.get(f"https://ethereum.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------


# Check Value Litecoin Address Balance Return [str]
def Balance_Litecoin(address):
    """ Check Value Litecoin Address Balance Return [str] """
    req = requests.get(f"https://litecoin.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------


# Check Value TRON Address Balance Return [str]
def Balance_Tron(address):
    """ Check Value TRON Address Balance Return [str] """
    req = requests.get(f"https://apilist.tronscanapi.com/api/accountv2?address={address}&source=true").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------


# Check Value Dogecoin Address Balance Return [str]
def Balance_Dogecoin(address):
    """ Check Value Dogecoin Address Balance Return [str] """
    req = requests.get(f"https://dogecoin.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------


# Check Value Bitcoin Gold Address Balance Return [str]
def Balance_BitcoinGold(address):
    """ Check Value Bitcoin Gold Address Balance Return [str] """
    req = requests.get(f"https://bgold.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------


# Check Value DigiByte Address Balance Return [str]
def Balance_DigiByte(address):
    """ Check Value DigiByte Address Balance Return [str] """
    req = requests.get(f"https://digibyte.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------


# Check Value Ravencoin Address Balance Return [str]
def Balance_Ravencoin(address):
    """ Check Value Ravencoin Address Balance Return [str] """
    req = requests.get(f"https://ravencoin.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------


# Check Value Qtum Address Balance Return [str]
def Balance_Qtum(address):
    """ Check Value Qtum Address Balance Return [str] """
    req = requests.get(f"https://qtum.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------


# Check Value ZCASH Address Balance Return [str]
def Balance_zCash(address):
    """ Check Value ZCASH Address Balance Return [str] """
    req = requests.get(f"https://zcash.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']


# --------------------------------------------------------------------------------


# Check Value Dash Address Balance : return [str]
def Balance_Dash(address):
    """ # Check Value Dash Address Balance : return [str] """
    req = requests.get(f"https://dash.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']
# --------------------------------------------------------------------------------
