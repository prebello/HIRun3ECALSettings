from CRABClient.UserUtilities import config
config = config()

inputList='QCDEMEnrichedInputprebello.txt'

config.General.requestName = 'QCDEMEnriched_DIGI_Run2'
config.General.workArea = 'QCD_pThat-30_EMEnrichedDijet_HS_TuneCP5_HydjetDrumMB_5p02TeV_pythia8_DIGI_ECAL_ZS_Run2'
config.General.transferOutputs = True

config.JobType.pluginName = 'Analysis'
config.JobType.psetName = 'step2_DIGI_QCDEMEnriched.py'
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000
config.JobType.inputFiles = ["EcalSRSettings_beam2018_option1_v00_mc.db"]


config.Data.userInputFiles = open(inputList).readlines()
config.Data.outputPrimaryDataset = 'QCD_pThat-30_EMEnrichedDijet_HS_TuneCP5_HydjetDrumMB_5p02TeV_pythia8_DIGI_ECAL_ZS_Run2'
config.Data.splitting = 'FileBased'
config.Data.unitsPerJob = 1
#NJOBS = 5000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line                            
#config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.Data.totalUnits = len(config.Data.userInputFiles)

config.Data.publication = True
config.Data.outputDatasetTag ='QCD_pThat-30_EMEnrichedDijet_HS_TuneCP5_HydjetDrumMB_5p02TeV_pythia8_DIGI_ECAL_ZS_Run2'
config.Data.outLFNDirBase = '/store/user/prebello/'
config.Site.storageSite ='T2_US_Vanderbilt'
