from datetime import datetime
import abc
from parking_spots import ParkingSpotType
import math

class TarrifCalculatorStrategy(abc.ABC):
    """Tarrif calculator abstract class"""
    @abc.abstractmethod
    def calculate(self, parking_ticket):
        """function to calculate amount to be paid for a ticket"""
        pass
    
    def get_total_hours_passed(self, parking_ticket):
        time_of_checkout = datetime.now()
        time_of_issue = parking_ticket.issue_time
        diff = time_of_checkout - time_of_issue
        diff_in_hours = math.ceil(diff.total_seconds() / 3600)
        return diff_in_hours

class MallStrategy(TarrifCalculatorStrategy):
    """Mall implmentation for tarrif calculator"""
    def __init__(self) -> None:
        self.rates = {
            ParkingSpotType.SMALL_SPOT: 10,
            ParkingSpotType.MEDIUM_SPOT: 20,
            ParkingSpotType.LARGE_SPOT: 50
        }
    def calculate(self, parking_ticket):
        diff_in_hours = self.get_total_hours_passed(parking_ticket)
        spot = parking_ticket.spot
        return self.rates[spot.get_type()] * diff_in_hours

class StadiumStrategy(TarrifCalculatorStrategy):
    def __init__(self) -> None:
        self.rates = {
            ParkingSpotType.SMALL_SPOT: {
                4: 30,
                8: 60
            },
            ParkingSpotType.MEDIUM_SPOT: {
                4: 60,
                8: 120
            }
        }
        self.hourly_rates = {
            ParkingSpotType.SMALL_SPOT: 100,
            ParkingSpotType.MEDIUM_SPOT: 200
        }
    def calculate(self, parking_ticket):
        diff = self.get_total_hours_passed(parking_ticket)
        spot = parking_ticket.spot
        total_amount = 0
        rate = self.rates[spot.get_type()]
        for hour, amount in rate.items():
            if diff > 0:
                total_amount += abs(diff-hour) * amount
                diff -= hour

        if diff > 0:
            total_amount += diff*self.hourly_rates[spot.get_type()]
        return total_amount

class AirportStrategy(TarrifCalculatorStrategy):
    def __init__(self) -> None:
        self.rates = {
            ParkingSpotType.SMALL_SPOT: {
                1: 0,
                8: 40,
                24: 60
            },
            ParkingSpotType.MEDIUM_SPOT: {
                1: 0,
                12: 60,
                24: 80
            }
        }
        self.daily_rates = {
            ParkingSpotType.SMALL_SPOT: 80,
            ParkingSpotType.MEDIUM_SPOT: 100
        }
    
    def calculate(self, parking_ticket):
        spot = parking_ticket.spot
        diff = self.get_total_hours_passed(parking_ticket)
        if diff <= 1:
            return 0
        if diff > 24:
            number_of_days = math.ceil(diff/24)
            return self.daily_rates[spot.get_type()] * number_of_days
        rate = self.rates[spot.get_type()]
        for hours, amount in rate.items():
            if hours >= diff:
                return amount * diff
        




