from autos import economy
from decorators import V6

car = economy.Economy()

print(car.description)
print(car.price)

car = V6.V6(car)

print(car.description)
print(car.price)