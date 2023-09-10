from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'ZEE_RECO_highvalue'
config.General.workArea = 'Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_RECO_ECAL_ZS_highvalue'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step3_RECO_ZEE.py'
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000
config.JobType.inputFiles = ["EcalSRSettings_beam2018_option1_v00_mc_highvalue.db"]


config.Data.userInputFiles = "/Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_highvalue/prebello-Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_highvalue-72f762231a2e45f7b0201ffda2b1f691/USER"
config.Data.inputDBS = "phys03"
config.Data.outputPrimaryDataset = 'Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_RECO_ECAL_ZS_highvalue'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
config.Data.totalUnits = -1

config.Data.publication = True
config.Data.outputDatasetTag ='Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_RECO_ECAL_ZS_highvalue'
config.Data.outLFNDirBase = '/store/user/prebello/'
config.Site.storageSite ='T2_US_Vanderbilt'
