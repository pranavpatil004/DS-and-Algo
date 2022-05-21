from delta_airlines import DeltaAirlinesSeat
from seats.economy import EconomySeat

seat = EconomySeat()

seat = DeltaAirlinesSeat(seat)

print(seat.seat_price)
print(seat.aminities)