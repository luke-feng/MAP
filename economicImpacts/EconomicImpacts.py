def getLoss(cost_list):
    cost_list = list(cost_list)
    cost_name=['CostofRepair','CorporateIncomeLoss','OrganizationProductiveLoss','CostofEquipmentReplacement','SLALoss','IndirectLoss','TimetoRepair_without','TimetoDetect_without']
    cost_dict=dict(zip(cost_name,cost_list))
    L1 = cost_dict.get('CostofRepair') + cost_dict.get('CorporateIncomeLoss') +cost_dict.get('OrganizationProductiveLoss')
    L2 = cost_dict.get('CorporateIncomeLoss') + cost_dict.get('OrganizationProductiveLoss')
    L3 = cost_dict.get('CostofEquipmentReplacement') + cost_dict.get('SLALoss') + cost_dict.get('IndirectLoss')
    L = L1 * cost_dict.get('TimetoRepair_without') + L2 * cost_dict.get('TimetoDetect_without') + L3
    return L1,L2,L3,L

def getRisk(TimesofAttack,TimePeriod,VulnerabilityWithoutmeasure,L):
    T = TimesofAttack
    v = VulnerabilityWithoutmeasure
    R0 = T*v*L
    return R0

def getCost(InitialCost,AnnualUpgrade,AnnualMaintenance,TimePeriod):
    TotalCost = InitialCost+(AnnualUpgrade+AnnualMaintenance)*TimePeriod/12
    return TotalCost

def getMeasureTypeID(R0,R_min,R_max,L_max):
    if R0 < R_min:
        MeasureTypeID = 0
    elif R0 > R_max:
        MeasureTypeID = 3
    elif L > L_max:
        MeasureTypeID = 2
    else:
        MeasureTypeID = 1
    return MeasureTypeID

def calculateROSI(MeasureTypeID,TimesofAttack,TimePeriod,VulnerabilityWithoutmeasure,ReducedVulnerability,InsuranceAmount,TotalCost,R0,L1,L2,L3,TimetoRepair_with,TimetoDetect_with):
    T = TimesofAttack
    v = VulnerabilityWithoutmeasure
    vc = (1-ReducedVulnerability)*v
    if MeasureTypeID == 0:
        ROSI = -1.0
    elif MeasureTypeID == 3:
        ROSI = 0.0
    elif MeasureTypeID == 2:
        ROSI = (T*v*InsuranceAmount-TotalCost)/TotalCost
    else:
        RC = T*vc*(L1*TimetoRepair_with+L2*TimetoDetect_with+L3)
        ROSI = (R0-RC-TotalCost)/TotalCost
    return ROSI

def calculateNPV(MeasureTypeID,TimesofAttack,TimePeriod,VulnerabilityWithoutmeasure,ReducedVulnerability,InsuranceAmount,TotalCost,R0,L1,L2,L3,TimetoRepair_with,TimetoDetect_with,DiscountRate):
    T = TimesofAttack
    v = VulnerabilityWithoutmeasure
    vc = (1-ReducedVulnerability)*v
    year = int(TimePeriod/12)
    NPV=0.0
    if TimePeriod >= 12:
        if MeasureTypeID == 0 or MeasureTypeID == 3:
            NPV = 0.0
        elif MeasureTypeID == 2:
            for t in range(0,year): 
                NPV+= (T*v*InsuranceAmount-TotalCost)/(1+DiscountRate)**t
        else:
            RC = T*vc*(L1*TimetoRepair_with+L2*TimetoDetect_with+L3)
            for t in range(0,year): 
                NPV+= (R0-RC-TotalCost)/(1+DiscountRate)**t
    return NPV
