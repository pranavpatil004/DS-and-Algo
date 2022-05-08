import abc
class PriceDiscountAbstract(abc.ABC):
    @abc.abstractproperty
    def discount_amount(self):
        pass

class PriceDiscountStudent(PriceDiscountAbstract):
    @property
    def discount_amount(self):
        return 0.1

class PriceDiscountCorporate(PriceDiscountAbstract):
    @property
    def discount_amount(self):
        return 0.3


    