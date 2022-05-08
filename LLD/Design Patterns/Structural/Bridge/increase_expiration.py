import abc

class IncreaseExpirationAbstract(abc.ABC):
    @abc.abstractproperty
    def enhance_expiration(self):
        pass


class StudentEnhancedExpiration(IncreaseExpirationAbstract):
    @property
    def enhance_expiration(self):
        return 2

class AnnualEnhancedExpiration(IncreaseExpirationAbstract):
    @property
    def enhance_expiration(self):
        return 5