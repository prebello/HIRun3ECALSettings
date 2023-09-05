# HIRun3ECALSettings
HI Object Validation acc ECAL ZS/SR settings

Following instructions from the Twiki [link](https://twiki.cern.ch/twiki/bin/view/CMS/HiEcalStudies2021#Job_submission)

in srCondWrite_cfg.py change "LowInterestChannelZS" and "HighInterestChannelZS":

srpBarrelLowInterestChannelZS = cms.double(X*0.035)

srpBarrelHighInterestChannelZS = cms.double(Y*0.035)

srpEndcapLowInterestChannelZS = cms.double(X*0.06)

srpEndcapHighInterestChannelZS = cms.double(Y*0.06)

as well as "trigPrimBypass*" values 
