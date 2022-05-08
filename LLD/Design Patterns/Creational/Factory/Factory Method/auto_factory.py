import autos
from inspect import isclass, isabstract, getmembers
class AutoFactory:
    def __init__(self):
        self.autos_dic = {}
        self.load_autos()
    def load_autos(self):
        classes = getmembers(autos, lambda m: isclass(m) and not isabstract(m))
        for name, _type in classes:
            if isclass(_type) and issubclass(_type, autos.AbstractAuto):
                self.autos_dic[name] = _type
    def get_auto(self, vehical_type):
        if vehical_type in self.autos_dic:
            return self.autos_dic[vehical_type]()
        else:
            raise NotImplementedError("Vehical type not recognized", vehical_type)
