from CRABClient.UserUtilities import config
config = config()

inputList='ZEEInputprebello.txt'

config.General.requestName = 'ZEE_DIGI_ZS_EB_EE_12_SR_HI_4_MI_2'
config.General.workArea = 'Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_ZS_EB_EE_12_SR_HI_4_MI_2'
config.General.transferOutputs = True
config.JobType.inputFiles = ["EcalSRSettings_beam2018_option1_v00_mc_ZS_EB_EE_12_SR_HI_4_MI_2.db"]

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI_ZEE_ZS_EB_EE_12_SR_HI_4_MI_2.py'

config.Data.userInputFiles = open(inputList).readlines()
config.Data.outputPrimaryDataset = 'Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_ZS_EB_EE_12_SR_HI_4_MI_2'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#NJOBS = 5000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line                            
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.totalUnits = len(config.Data.userInputFiles)
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000

config.Data.publication = True
config.Data.outputDatasetTag ='Ze10e10_pThat-0_TuneCP5_HydjetDrumMB_5p02TeV_Pythia8_ZS_EB_EE_12_SR_HI_4_MI_2'
config.Data.outLFNDirBase = '/store/user/prebello/'
config.Site.storageSite ='T2_US_Vanderbilt'
