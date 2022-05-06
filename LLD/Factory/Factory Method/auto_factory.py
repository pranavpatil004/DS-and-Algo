import autos

class AutoFactory:
    def get_auto(self, vehical_type):
        if vehical_type == "Ford":
            return autos.ford_fusion.FordFusion()
        elif vehical_type == "Chevy":
            return autos.chevy_volt.ChevyVolt()
        elif vehical_type == "Jeep":
            return autos.jeep_sahara.JeepSahara()
        else:
            raise NotImplementedError("Vehical type not recognized", vehical_type)