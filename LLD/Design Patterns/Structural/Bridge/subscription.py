import abc
from dateutil.relativedelta import relativedelta
class SubscriptionAbstract(abc.ABC):
    def __init__(self, username, enrolled_date, price_discount, enhanced_expiration):
        self.__username = username
        self.__enrolled_date = enrolled_date
        self.__price_discount = price_discount
        self.__enhanced_expiration = enhanced_expiration
    
    @property
    def username(self):
        return self.__username
    
    @property
    def enrolled_date(self):
        return self.__enrolled_date
    
    @abc.abstractproperty
    def base_price(self):
        pass

    @abc.abstractproperty
    def base_expiration(self):
        pass

    @property
    def price(self):
        return self.base_price * (1-self.__price_discount.discount)
    
    @abc.abstractproperty
    def expiration(self):
        pass

