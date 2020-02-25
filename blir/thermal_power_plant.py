# ========================================================================
# Instantiate PowerPlant
# ========================================================================
class ThermalPowerPlant:

    def __init__(self, plantType="CCGT",
                 capacity=51.3,
                 maxEfficiency=53.44,
                 rampRate=64.94,
                 minRange=36.43,
                 startTime=33.13,
                 stopTime=5.0,
                 Eff_A=-6.94E-03,
                 Eff_B=1.28E+00,
                 Eff_C=4.08E+01,
                 cost_install=1260.0,
                 cost_OM_fix=11.11,
                 cost_OM_var=3.54,
                 co2CaptureEff=0.0)

        # Define Plant Characteristics
        self.type = plantType  # Technology type (string)
        self.capacity = capacity  # MW
        self.maxEfficiency = maxEfficiency  # %
        self.rampRate = rampRate  # MW/min
        self.minRange = minRange  # %
        self.startTime = startTime  # min
        self.stopTime = stopTime  # min
        self.Eff_A = Eff_A  # Efficiency Curve Ax^2 + Bx + C
        self.Eff_B = Eff_B  # -
        self.Eff_C = Eff_C  # -
        self.cost_install = cost_install  # ($/kW)
        self.cost_OM_fix = cost_OM_fix  # ($/kW/year)
        self.cost_OM_var = cost_OM_var  # ($/MWh)
        self.co2CaptureEff = co2CaptureEff  # Carbon Capture Efficiency (%)


class CCGT(ThermalPowerPlant):
    def __init__(self, capacity=51.3,  # MW
                 maxEfficiency=53.44,  # %
                 rampRate=64.94,  # MW/min
                 minRange=36.43,  # %
                 startTime=33.13,  # min
                 stopTime=5.0,  # min
                 Eff_A=-6.94E-03,  # Efficiency Curve Ax^2 + Bx + C
                 Eff_B=1.28E+00,
                 Eff_C=4.08E+01,
                 cost_install=1260.0,  # ($/kW)
                 cost_OM_fix=11.11,  # ($/kW/year)
                 cost_OM_var=3.54,  # ($/MWh)
                 co2CaptureEff=0.0):  # Carbon Capture Efficiency (%)
        ThermalPowerPlant.__init__(self, plantType="CCGT",
                                   capacity=capacity,
                                   maxEfficiency=maxEfficiency,
                                   rampRate=rampRate,
                                   minRange=minRange,
                                   startTime=startTime,
                                   stopTime=stopTime,
                                   Eff_A=Eff_A,
                                   Eff_B=Eff_B,
                                   Eff_C=Eff_C,
                                   cost_install=cost_install,
                                   cost_OM_fix=cost_OM_fix,
                                   cost_OM_var=cost_OM_var,
                                   co2CaptureEff=co2CaptureEff)


class OCGT(ThermalPowerPlant):
    def __init__(self, capacity=51.3,  # MW
                 maxEfficiency=38.33,  # %
                 rampRate=72.77,  # MW/min
                 minRange=46.11,  # %
                 startTime=10.0,
                 stopTime=5.0,
                 Eff_A=-1.09E-02,
                 Eff_B=2.03E+00,
                 Eff_C=5.44E+00,
                 cost_install=750.0,
                 cost_OM_fix=17.67,
                 cost_OM_var=3.54,
                 co2CaptureEff=0.0):
        ThermalPowerPlant.__init__(self, plantType="OCGT",
                                   capacity=capacity,
                                   maxEfficiency=maxEfficiency,
                                   rampRate=rampRate,
                                   minRange=minRange,
                                   startTime=startTime,
                                   stopTime=stopTime,
                                   Eff_A=Eff_A,
                                   Eff_B=Eff_B,
                                   Eff_C=Eff_C,
                                   cost_install=cost_install,
                                   cost_OM_fix=cost_OM_fix,
                                   cost_OM_var=cost_OM_var,
                                   co2CaptureEff=co2CaptureEff)
# ========================================================================
# Method for calculating efficiency at a given power output
# Does not set efficiency, thus it could be used by a control scheme to determine where to operate
# ========================================================================
# eff_fr = self.Eff_A * load_fr ** 2 + self.Eff_B * load_fr + self.Eff_C


class Fuel:

    def __init__(self, fuelType='NATGAS', cost=10.58, emissions=0.18):
        self.fuelType = fuelType  # name of fuel
        self.cost = cost  # cost [$] per MWh thermal
        self.emissions = emissions  # CO2 emissions [tons] per MWh thermals

