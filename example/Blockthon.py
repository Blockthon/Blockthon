# //////////////////////////////////////////////////
# // Github : github.com/Pymmdrza                 //
# // official Page : https://github.com/Blockthon //
# //////////////////////////////////////////////////

import codecs
from os import urandom
from bit import Key
from bit.format import bytes_to_wif
from binascii import hexlify
from mnemonic import Mnemonic
from codecs import decode as Decode
import requests, json, re, random
from assest.hdwallet import HDWallet
from assest.symbols import BTC, ETH, TRX, LTC, DOGE, DGB, RVN, DASH, BTG, VIA, QTUM, ZEC


def PrivateKey():
    return urandom(32).hex()


# Generated Mnemonic Random
def Get_Mnemonic(size=12):
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


# Generated and convert Ethereum Address Wallet From Private Key (HEX)
def ETH_From_PrivateKey(privatekey):
    wallet: HDWallet = HDWallet(symbol=ETH)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# Generated and convert TRON Address Wallet From Private Key (HEX)
def TRX_From_PrivateKey(privatekey):
    wallet: HDWallet = HDWallet(symbol=TRX)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# Generated and convert Dogecoin Address Wallet From Private Key (HEX)
def DOGE_From_PrivateKey(privatekey):
    wallet: HDWallet = HDWallet(symbol=DOGE)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# Generated and convert Dash Address Wallet From Private Key (HEX)
def DASH_From_PrivateKey(privatekey):
    wallet: HDWallet = HDWallet(symbol=DASH)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# Generated and convert Bitcoin Gold Address Wallet From Private Key (HEX)
def BTG_From_PrivateKey(privatekey):
    wallet: HDWallet = HDWallet(symbol=BTG)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# Generated and convert Litecoin Address Wallet From Private Key (HEX)
def LTC_From_PrivateKey(privatekey):
    wallet: HDWallet = HDWallet(symbol=LTC)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# Generated and convert DigiByte Address Wallet From Private Key (HEX)
def DigiByte_From_PrivateKey(privatekey):
    wallet: HDWallet = HDWallet(symbol=DGB)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# Generated and convert Rave Coin Address Wallet From Private Key (HEX)
def RVN_From_PrivateKey(privatekey):
    wallet: HDWallet = HDWallet(symbol=RVN)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# Generated and convert Via coin Address Wallet From Private Key (HEX)
def VIA_From_PrivateKey(privatekey):
    wallet: HDWallet = HDWallet(symbol=VIA)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# Generated and convert Qtum Address Wallet From Private Key (HEX)
def QTUM_From_PrivateKey(privatekey):
    wallet: HDWallet = HDWallet(symbol=QTUM)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# Generated and convert ZCash Address Wallet From Private Key (HEX)
def ZEC_From_PrivateKey(privatekey):
    wallet: HDWallet = HDWallet(symbol=ZEC)
    wallet.from_private_key(privatekey)
    return wallet.p2pkh_address()


# Convert Private Key to Dec
def PrivateKey_To_Dec(private_key):
    """ Convert Hex to Integer Return int [dec] """
    return int(private_key, 16)


# Convert Number (Dec) To Private Key (HEX)
def PrivateKey_From_int(int_):
    """ Convert Number (Integer) To Private key (HEX) Return str """
    return "%064x" % int_


# Convert Private Key (HEX) To Bytes
def PrivateKey_To_Bytes(private_key):
    """ Convert Hex to Bytes and Return binary [byte] """
    return Decode(private_key, 'hex')


# Convert Bytes (SEED) To Mnemonic
def Bytes_To_Mnemonic(Byte_String):
    """ Convert Bytes to Mnemonic Word with 256 bit Size and Return str [mnemonic] """
    return Mnemonic('english').to_mnemonic(Byte_String)


# Convert Bytes (Seed) To HEX (Private Key)
def Bytes_To_PrivateKey(Byte_String):
    """ convert bytes to hex for private key and return str [private_key] """
    return hexlify(Byte_String).decode('utf-8')


# Convert Private Key (HEX) To Mnemonic
def PrivateKey_To_Mnemonic(private_key):
    """Convert HEX To Bytes , after converting , convert to Mnemonic (WORD)
    PrivateKey: str --> Byte: Binary --> Mnemonic(Word): str"""
    Byte_String: str = PrivateKey_To_Bytes(private_key)
    return Mnemonic('english').to_mnemonic(Byte_String)


# Convert Byte To WIF Compressed and Un Compressed
def Bytes_To_WIF(Bytes_, compressed=False):
    """ convert bytes to wif and after compressed and uncompressed address """
    if compressed:
        wif = bytes_to_wif(Bytes_, compressed=True)
    else:
        wif = bytes_to_wif(Bytes_)
    return wif


# compressed and un compressed address from private key hex
def Addr_From_PrivateKey(private_key, compress=False):
    """ convert hex private key to compressed address and un compressed : return [str] """
    seed = codecs.decode(private_key, 'hex')
    if compress:
        _wc = bytes_to_wif(seed, compressed=True)
        bits = Key(_wc)
        return bits.address
    else:
        _wu = bytes_to_wif(seed, compressed=False)
        bitu = Key(_wu)
        return bitu.address


# Check Value Bitcoin Address Balance Return Value [str: '0']
def Balance(address):
    """check balance of value per address and return : str [balance]"""
    req = requests.get(f"https://bitcoin.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']


# Check Value Ethereum Address Balance Return [str]
def Balance_Ethereum(address):
    req = requests.get(f"https://ethereum.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']


# Check Value Litecoin Address Balance Return [str]
def Balance_Litecoin(address):
    req = requests.get(f"https://litecoin.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']


# Check Value TRON Address Balance Return [str]
def Balance_Tron(address):
    req = requests.get(f"https://apilist.tronscanapi.com/api/accountv2?address={address}&source=true").json()
    return dict(req)['balance']


# Check Value Dogecoin Address Balance Return [str]
def Balance_Dogecoin(address):
    req = requests.get(f"https://dogecoin.atomicwallet.io/api/v2/address/{address}").json()
    return dict(req)['balance']


# Check Value Bitcoin Gold Address Balance Return [str]
def Balance_BitcoinGold(address):
    req = requests.get(f"https://bgold.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']


# Check Value DigiByte Address Balance Return [str]
def Balance_DigiByte(address):
    req = requests.get(f"https://digibyte.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']


# Check Value Ravencoin Address Balance Return [str]
def Balance_Ravencoin(address):
    req = requests.get(f"https://ravencoin.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']


# Check Value Qtum Address Balance Return [str]
def Balance_Qtum(address):
    req = requests.get(f"https://qtum.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']


# Check Value ZCASH Address Balance Return [str]
def Balance_zCash(address):
    req = requests.get(f"https://zcash.atomicwallet.io/api/v1/address/{address}").json()
    return dict(req)['balance']
