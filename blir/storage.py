# ========================================================================
# General class for energy storage
# ========================================================================
class Storage:

    # ----------
    # Instantiate
    # ----------
    def __init__(self, capacity=30.0, chargeRateMax=30.0, dischargeRateMax=30.0, roundTripEff=85.0, tau=30.0,
                 cost_install=2067., cost_OM_fix=35.6, initCharge=0.0):

        # Battery Properties:
        # Provided
        self.capacity = capacity  # (MWh) storage capacity
        self.chargeRateMax = chargeRateMax  # (MW) Max Discharge Rate
        self.dischargeRateMax = dischargeRateMax  # (MW) Max Discharge Rate
        self.roundTripEff = roundTripEff  # (%) Round trip efficiency, applied when energy is discharged
        self.cost_install = cost_install  # ($/kW)
        self.cost_OM_fix = cost_OM_fix  # ($/kW/year)
        self.initCharge = initCharge  # (%)

        # Derived
        self.chargeMin = 0.0  # (MW-min)
        self.chargeMax = capacity * 60.0  # convert from MWh (provided) to MW-min (working units)

        # Battery Performance
        self.ramp = 0.0  # MW
        self.dischargeRate = 0.0  # MW
        self.chargeRate = 0.0  # MW
        self.increase = 0.0  # MW-min
        self.decrease = 0.0  # MW-min
        self.charge = initCharge * self.chargeMax  # MW-min

    # ----------
    # Calculate Available Charge Rate (MW)
    # ----------
    def getChargeRateAvail(self, dt):

        if self.charge < self.chargeMax:
            chargeRateAvail = min((self.chargeMax - self.charge) / dt, self.chargeRateMax)
        else:
            chargeRateAvail = 0.0

        # Debugging        
        if debug:
            print("chargeRateAvail" + str(chargeRateAvail))

        return chargeRateAvail

    # ----------
    # Calculate Battery Discharge Rate Available (MW)
    # ----------
    def getDischargeRateAvail(self, dt):

        if self.charge > self.chargeMin:
            dischargeRateAvail = min((self.charge - self.chargeMin) / dt / self.tau, self.dischargeRateMax)
        else:
            dischargeRateAvail = 0.0

        # Debugging
        if debug:
            print("dischargeRateAvail" + str(dischargeRateAvail))

        return dischargeRateAvail

    # ----------
    # Update battery status
    # ----------
    def update(self, dt, increase, decrease):

        charge_old = self.charge

        # Dis/charge batteries
        # Power Going to and from battery
        self.dischargeRate = decrease  # MW
        self.chargeRate = increase  # MW
        # Power entering and exiting battery (apply efficiencies)
        self.decrease = decrease  # MW
        self.increase = increase * self.roundTripEff / 100.0  # MW (Only apply when storing)
        # Adjust battery charge
        self.charge = self.charge + self.increase * dt - self.decrease * dt  # MW-min

        # Ramp Rate
        self.ramp = (self.charge - charge_old) / dt  # MW


# ========================================================================
# Battery class, child of Storage
# Charge and discharge rates are set to be equal, otherwise classes are identical
# ========================================================================
class Battery(Storage):

    def __init__(self, capacity=30.0, rateMax=30.0, roundTripEff=90.0, cost_install=2067., cost_OM_fix=35.6,
                 initCharge=0.0):
        Storage.__init__(self, capacity=capacity, chargeRateMax=rateMax, dischargeRateMax=rateMax, roundTripEff=85.0,
                         cost_install=2067., cost_OM_fix=35.6, initCharge=initCharge)
