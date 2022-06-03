from shipping_cost import ShippingCost
from cost_strategy import Fedex, PostOffice, Amazon
sc = ShippingCost(Fedex())
print(sc.calculate_cost())
sc = ShippingCost(PostOffice())
print(sc.calculate_cost())
sc = ShippingCost(Amazon())
print(sc.calculate_cost())
