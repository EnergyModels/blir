# Class to hold details of the solar power plant
class VariableRenewableEnergy:

    # ----------
    # Instantiate
    # ----------
    def __init__(self, plant_type='PV', capacity=32.3, cost_install=2004., cost_OM_fix=22.02, cost_OM_var=0.0):
        # Properties:
        self.plant_type = plant_type  # (string) Technology type
        self.capacity = capacity  # (MW) capacity
        self.cost_install = cost_install  # ($/kW)
        self.cost_OM_fix = cost_OM_fix  # ($/kW/year)
        self.cost_OM_var = cost_OM_var  # ($/MWh)


# Class to hold details of the wind power plant
class Wind(VariableRenewableEnergy):
    def __init__(self, capacity=0.0, cost_install=2004., cost_OM_fix=22.02, cost_OM_var=0.0):
        VariableRenewableEnergy.__init__(self, plant_type='Wind', capacity=capacity, cost_install=cost_install,
                                         cost_OM_fix=cost_OM_fix, cost_OM_var=cost_OM_var)


# Class to hold details of the solar power plant
class Solar(VariableRenewableEnergy):
    def __init__(self, capacity=0.0, cost_install=2004., cost_OM_fix=22.02, cost_OM_var=0.0):
        VariableRenewableEnergy.__init__(self, plant_type='Solar', capacity=capacity, cost_install=cost_install,
                                         cost_OM_fix=cost_OM_fix, cost_OM_var=cost_OM_var)
