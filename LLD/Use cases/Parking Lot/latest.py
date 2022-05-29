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
        self.parking_ticket_builder = ParkingTicketFactory()
    
    def get_ticket(self, parkingTicketType):
        pass

class ExitTerminal(Terminal):
    def __init__(self, id) -> None:
        super().__init__(id)
    
    def accept_ticket(self, parking_ticket: ParkingTicket):
        # remove the spot from reserved array and add it in available
        pass

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

class ParkingAssignmentStrategy:
    def __init__(self) -> None:
        self.parking_spot_factory = ParkingSpotFactory()

    def get_parking_spot(self, parking_spot_type, terminal: Terminal):
        # algorithm to get nearest parking spot based on min heaps
        return self.parking_spot_factory.get_parking_spot(parking_spot_type)

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
    
    def __init__(self) -> None:
        pass

ParkingLot()