import abc
from collections import defaultdict
from sys import last_traceback
import enum
class ParkingSpotType(enum.Enum):
    SmallSpot, MediumSpot, LargeSpot = 1, 2, 3

class ParkingSpot(abc.ABC):
    def __init__(self, spot_id):
        self.__spot_id = spot_id
    
    @abc.abstractproperty
    def is_reserved(self):
        pass

    @property
    def spot_id(self):
        return self.__spot_id
    
    def get_type(self):
        return type(self)

class SmallSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id)
        self.__is_reserved = False
    
    @property
    def is_reserved(self):
        return self.__is_reserved

    @is_reserved.setter
    def set_is_reserved(self, is_reserved):
        self.__is_reserved = is_reserved

class MediumSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id)
        self.__is_reserved = False
    
    @property
    def is_reserved(self):
        return self.__is_reserved

    @is_reserved.setter
    def set_is_reserved(self, is_reserved):
        self.__is_reserved = is_reserved

class LargeSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id)
        self.__is_reserved = False

    @property
    def is_reserved(self):
        return self.__is_reserved

    @is_reserved.setter
    def set_is_reserved(self, is_reserved):
        self.__is_reserved = is_reserved

class ParkingTicket:
    def __init__(self, id, spot: ParkingSpot, issue_time) -> None:
        self.__ticket_id = id
        self.__spot = spot
        self.__issue_time = issue_time
    
    @property
    def ticket_id(self):
        return self.__ticket_id
    
    @property
    def spot(self):
        return self.__spot
    
    @property
    def issue_time(self):
        return self.__issue_time

class Terminal(abc.ABC):
    def __init__(self, id) -> None:
        self.__terminal_id = id
    
    @property
    def terminal_id(self):
        return self.__terminal_id

class EntryTerminal(Terminal):
    def __init__(self, id) -> None:
        super().__init__(id)
        self.parking_spot_strategy = ParkingTicketAssignmentStrategy()
    
    def get_ticket(self, spot_type):
        return self.parking_spot_strategy.get_parking_spot(spot_type, self)

class TarrifCalculator:
    def __init__(self, hourly_rate) -> None:
        self.__hourly_rate = hourly_rate
    def calculate(self, ticket: ParkingTicket):
        # calculate difference between current time and issue time
        current_time = 1
        tarrif = (current_time - ticket.issue_time)*self.__hourly_rate
        return tarrif

class ExitTerminal(Terminal):
    def __init__(self, id, tarrif_calculator: TarrifCalculator) -> None:
        super().__init__(id)
        self.__tarrif_calculator = tarrif_calculator
        self.__parking_lot = ParkingLot()
    
    def accept_ticket(self, parking_ticket: ParkingTicket, paymentType):
        amount = self.__tarrif_calculator.calculate(parking_ticket)
        payment_switcher = {
            "Cash": CashProcessor(),
            "CreditCard": CreditCardProcessor()
        }
        payment_processor = payment_switcher.get(paymentType)
        payment_processor.process(amount)
        spot = parking_ticket.spot
        self.__parking_lot.reserved_spots.discard(spot)
        self.__parking_lot.add_parking_spot(spot)
        return

class ParkingSpotFactory:
    _instance = []
    def __init__(self) -> None:
        self.current_id = 0
        self.spot_dic = {
            ParkingSpotType.SmallSpot: SmallSpot,
            ParkingSpotType.MediumSpot: MediumSpot,
            ParkingSpotType.LargeSpot: LargeSpot
        }
    def __new__(cls, *args, **kwargs):
        if cls not in ParkingSpotFactory._instance:
            new_instance = super().__new__(cls, args, kwargs)
            ParkingSpotFactory._instance[cls] = new_instance
        return ParkingSpotFactory._instance[cls]
        
    def get_parking_spot(self, parking_spot_type):
        self.current_id += 1
        return self.spot_dic[parking_spot_type](self.current_id)


class ParkingTicketFactory:
    def __init__(self):
        self.current_id = 0
    def get_ticket(self, spot):
        self.current_id += 1
        return ParkingTicket(self.current_id, spot, "current_time")

class ParkingLot:
    _instance = {}
    def __new__(cls, *args, **kwargs):
        if cls not in ParkingLot._instance:
            instance = super().__new__(cls, args, kwargs)
            ParkingLot._instance[cls] = instance
        return ParkingLot._instance[cls]
    
    def __init__(self, entry_terminals, exit_terminals, floors) -> None:
        self.__entrances = [EntryTerminal() for _ in range(entry_terminals)]
        self.__exits = [ExitTerminal() for _ in range(exit_terminals)]
        self.__reserved_spots = defaultdict(set)
        self.floors = floors
    
    @property
    def entrances(self):
        return self.__entrances
    
    @property
    def exits(self):
        return self.__exits

    @property
    def reserved_spots(self):
        return self.__reserved_spots

    def get_ticket(entry_terminal: EntryTerminal, spot_type):
        return entry_terminal.get_ticket(spot_type)

class ParkingFloorFactory:
    @staticmethod
    def get_parking_floor(floor_count, small_spots, medium_spots, large_spots):
        parking_floors = []
        parking_spot_factory = ParkingSpotFactory()
        for floor in floor_count:
            parking_spots = {
                ParkingSpotType.SmallSpot: [parking_spot_factory.get_parking_spot(ParkingSpotType.SmallSpot) for _ in small_spots],
                ParkingSpotType.MediumSpot: [parking_spot_factory.get_parking_spot(ParkingSpotType.MediumSpot) for _ in medium_spots],
                ParkingSpotType.LargeSpot: [parking_spot_factory.get_parking_spot(ParkingSpotType.LargeSpot) for _ in large_spots]
            }
            parking_floors.append(ParkingFloor(parking_spots))
        return parking_floors


class ParkingFloor:
    def __init__(self, parking_spots) -> None:
        self.__parking_spots = parking_spots

    def add_parking_spot(self, spot: ParkingSpot):
        switcher = {
            SmallSpot: self.__parking_spots[ParkingSpotType.SmallSpot].put(spot.get_number(), spot),
            MediumSpot: self.__parking_spots[ParkingSpotType.MediumSpot].put(spot.get_number(), spot),
            LargeSpot: self.__parking_spots[ParkingSpotType.LargeSpot].put(spot.get_number(), spot),
        }
        switcher.get(spot.get_type(), 'Wrong parking spot type')
    
    @property
    def parking_spots(self):
        return self.__parking_spots
 
class ParkingTicketAssignmentStrategy:
    def __init__(self) -> None:
        self.__parking_lot = ParkingLot()

    def get_parking_spot(self, parking_spot_type, terminal: Terminal):
        switcher = {
            "HandicapSpot": self.__parking_lot.handicap_spots,
            "CompactSpot": self.__parking_lot.compact_spots
        }
        spots = switcher.get(parking_spot_type, "Wrong parking spot type")
        if len(spots) == 0:
            return "Parking spots full"
        # find the closest one
        return spots.pop()

if __name__ == "__main__":
    parking_floors = ParkingFloorFactory.get_parking_floor
    parking_lot = ParkingLot(2, 2, parking_floors)
    print(parking_lot)


class PaymentProcessor(abc.ABC):
    @abc.abstractmethod
    def process(self, amount):
        pass

class CreditCardProcessor(PaymentProcessor):
    def process(self, amount):
        print("Amount processed by credit card")
        return amount

class CashProcessor(PaymentProcessor):
    def process(self, amount):
        print("Amount processed by cash")
        return amount