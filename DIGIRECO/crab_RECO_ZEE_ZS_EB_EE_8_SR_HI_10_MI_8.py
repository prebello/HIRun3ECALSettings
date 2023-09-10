from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'ZEE_RECO_ZS_EB_EE_8_SR_HI_10_MI_8'
config.General.workArea = 'Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_RECO_ECAL_ZS_EB_EE_8_SR_HI_10_MI_8'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_RECO_ZEE.py'
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000
config.JobType.inputFiles = ["EcalSRSettings_beam2018_option1_v00_mc_ZS_EB_EE_8_SR_HI_10_MI_8.db"]


config.Data.userInputFiles = "/Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_ZS_EB_EE_8_SR_HI_10_MI_8/prebello-Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_ZS_EB_EE_8_SR_HI_10_MI_8-1c530ebcb7c496442ad4e5508dfabddf/USER"
config.Data.inputDBS = "phys03"
config.Data.outputPrimaryDataset = 'Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_RECO_ECAL_ZS_EB_EE_8_SR_HI_10_MI_8'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1

config.Data.publication = True
config.Data.outputDatasetTag ='Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_RECO_ECAL_ZS_EB_EE_8_SR_HI_10_MI_8'
config.Data.outLFNDirBase = '/store/user/prebello/'
config.Site.storageSite ='T2_US_Vanderbilt'
