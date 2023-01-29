import abc
class PaymentProcessor(abc.ABC):
    @abc.abstractmethod
    def process(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount):
        print("Amount processed by credit card", amount)
        return amount

class CashProcessor(PaymentProcessor):
    def process(self, amount):
        print("Amount processed by cash", amount)
        return amount