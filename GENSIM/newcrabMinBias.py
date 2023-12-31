from CRABClient.UserUtilities import config
config = config()

config.General.requestName = 'MinBiasGENSIMv8'
config.General.workArea = 'MinBias_Hydjet_Drum5F_2018_5p02TeV'
config.General.transferOutputs = True

config.JobType.pluginName = 'PrivateMC'
config.JobType.psetName = 'HIN-HINPbPbAutumn18GS-00033_1_cfg.py'

config.Data.outputPrimaryDataset = 'MinBias_Hydjet_Drum5F_2018_5p02TeV'
config.Data.splitting = 'EventBased'
config.Data.unitsPerJob = 100
NJOBS = 10000  # This is not a configuration parameter, but an auxiliary variable that we use in the next line\                                                                    
config.Data.totalUnits = config.Data.unitsPerJob * NJOBS
config.JobType.numCores = 8
config.JobType.maxMemoryMB = 20000

config.Data.publication = True
config.Data.outputDatasetTag ='MinBias_Hydjet_Drum5F_2018_5p02TeV'
config.Data.outLFNDirBase = '/store/user/prebello/'
config.Site.storageSite ='T2_US_Vanderbilt'
