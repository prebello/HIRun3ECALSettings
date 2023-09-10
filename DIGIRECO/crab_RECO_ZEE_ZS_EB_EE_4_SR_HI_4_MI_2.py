from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'ZEE_RECO_ZS_EB_EE_4_SR_HI_4_MI_2'
config.General.workArea = 'Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_RECO_ECAL_ZS_EB_EE_4_SR_HI_4_MI_2'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_RECO_ZEE.py'
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000
config.JobType.inputFiles = ["EcalSRSettings_beam2018_option1_v00_mc_ZS_EB_EE_4_SR_HI_4_MI_2.db"]


config.Data.userInputFiles = "/Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_ZS_EB_EE_4_SR_HI_4_MI_2/prebello-Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_ZS_EB_EE_4_SR_HI_4_MI_2-cacfd8c0139675428c1918cae9c21a85/USER"
config.Data.inputDBS = "phys03"
config.Data.outputPrimaryDataset = 'Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_RECO_ECAL_ZS_EB_EE_4_SR_HI_4_MI_2'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1

config.Data.publication = True
config.Data.outputDatasetTag ='Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_RECO_ECAL_ZS_EB_EE_4_SR_HI_4_MI_2'
config.Data.outLFNDirBase = '/store/user/prebello/'
config.Site.storageSite ='T2_US_Vanderbilt'
