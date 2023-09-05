from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'QCDEnrichedGENSIM'
config.General.workArea = 'QCD_pThat-30_EMEnrichedDijet_TuneCP5_HydjetDrumMB_5p02TeV_pythia8'
config.General.transferOutputs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'HIN-HINPbPbAutumn18GSHIMix-00057_1_cfg.py'

config.Data.outputPrimaryDataset = 'QCD_pThat-30_EMEnrichedDijet_TuneCP5_HydjetDrumMB_5p02TeV_pythia8'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 10000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line\                                                                    
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000

config.Data.publication = True
config.Data.outputDatasetTag ='QCD_pThat-30_EMEnrichedDijet_TuneCP5_HydjetDrumMB_5p02TeV_pythia8'
config.Data.outLFNDirBase = '/store/user/prebello/'
config.Site.storageSite ='T2_US_Vanderbilt'
