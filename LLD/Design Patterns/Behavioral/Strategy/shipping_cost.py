from cost_strategy import CostStrategy
class ShippingCost:
    def __init__(self, shipping_strategy: CostStrategy) -> None:
        self.__shipping_strategy = shipping_strategy
    def calculate_cost(self):
        return self.__shipping_strategy.calculate_cost()