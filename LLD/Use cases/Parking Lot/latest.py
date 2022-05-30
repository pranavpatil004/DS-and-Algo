import abc


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

class HandicapSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id)
        self.__is_reserved = False
    
    # x = hs.is_reserved
    @property
    def is_reserved(self):
        return self.__is_reserved

    # hs.is_reserved = False
    @is_reserved.setter
    def set_is_reserved(self, is_reserved):
        self.__is_reserved = is_reserved

class CompactSpot(ParkingSpot):
    def __init__(self, spot_id):
        super().__init__(spot_id)
        self.__is_reserved = False
    
    # x = hs.is_reserved
    @property
    def is_reserved(self):
        return self.__is_reserved

    # hs.is_reserved = False
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
    def __init__(self) -> None:
        self.current_id = 0
        self.spot_dic = {
            "HandicapSpot": HandicapSpot,
            "CompactSpot": CompactSpot
        }
    def get_parking_spot(self, parking_spot_type):
        self.current_id += 1
        return self.spot_dic[parking_spot_type](self.current_id)


class ParkingTicketFactory:
    def __init__(self):
        self.current_id = 0
    def get_ticket(self, spot):
        self.current_id += 1
        return ParkingTicket(self.current_id, spot, "current_time")

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

class ParkingLot:
    _instance = {}
    def __new__(cls, *args, **kwargs):
        if cls not in ParkingLot._instance:
            instance = super().__new__(cls, args, kwargs)
            ParkingLot._instance[cls] = instance
        return ParkingLot._instance[cls]
    
    def __init__(self, entry_terminals, exit_terminals) -> None:
        self.__entrances = [EntryTerminal() for _ in range(entry_terminals)]
        self.__exits = [ExitTerminal() for _ in range(exit_terminals)]
        self.__handicap_spots = {}
        self.__compact_spots = {}
        self.__reserved_spots = set()
    
    @property
    def entrances(self):
        return self.__entrances
    
    @property
    def exits(self):
        return self.__exits

    @property
    def handicap_spots(self):
        return self.__handicap_spots

    @property
    def reserved_spots(self):
        return self.__reserved_spots

    @property
    def compact_spots(self):
        return self.__compact_spots

    def add_parking_spot(self, spot: ParkingSpot):
        switcher = {
            HandicapSpot: self.__handicap_spots.put(spot.get_number(), spot),
            CompactSpot: self.__compact_spots.put(spot.get_number(), spot)
        }
        switcher.get(spot.get_type(), 'Wrong parking spot type')
    
    def get_ticket(entry_terminal: EntryTerminal, spot_type):
        return entry_terminal.get_ticket(spot_type)

 
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
