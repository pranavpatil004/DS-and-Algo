"""Module with central driver code"""
import abc
from collections import defaultdict
from parking_spots import ParkingSpotType
from terminals import EntryTerminal, TerminalFactory
from parking_ticket import SimpleAssignment, ParkingTicketFactory
from tarrif_calculator import MallStrategy, AirportStrategy, StadiumStrategy
from datetime import datetime

class ParkingSpot(abc.ABC):
    """Parking spot abstract class"""
    def __init__(self, spot_id):
        self.__spot_id = spot_id

    @abc.abstractproperty
    def is_reserved(self):
        pass

    @property
    def spot_id(self):
        return self.__spot_id
    @property
    def get_type(self):
        pass

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
    
    def get_type(self):
        return ParkingSpotType.SMALL_SPOT

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
    
    def get_type(self):
        return ParkingSpotType.MEDIUM_SPOT

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
    
    def get_type(self):
        return ParkingSpotType.LARGE_SPOT


class ParkingSpotFactory:
    _instance = {}
    def __init__(self) -> None:
        self.current_id = 0
        self.spot_dic = {
            ParkingSpotType.SMALL_SPOT: SmallSpot,
            ParkingSpotType.MEDIUM_SPOT: MediumSpot,
            ParkingSpotType.LARGE_SPOT: LargeSpot
        }
    def __new__(cls, *args, **kwargs):
        if cls not in ParkingSpotFactory._instance:
            new_instance = super().__new__(cls)
            new_instance.__init__(*args, **kwargs)
            ParkingSpotFactory._instance[cls] = new_instance
        return ParkingSpotFactory._instance[cls]
        
    def get_parking_spot(self, parking_spot_type):
        self.current_id += 1
        return self.spot_dic[parking_spot_type](self.current_id)


class ParkingFloorFactory:
    @staticmethod
    def get_parking_floor(floor_count, small_spots, medium_spots, large_spots):
        parking_floors = []
        parking_spot_factory = ParkingSpotFactory()
        for floor in range(floor_count):
            parking_spots = {
                ParkingSpotType.SMALL_SPOT: [parking_spot_factory.get_parking_spot(ParkingSpotType.SMALL_SPOT) for _ in range(small_spots)],
                ParkingSpotType.MEDIUM_SPOT: [parking_spot_factory.get_parking_spot(ParkingSpotType.MEDIUM_SPOT) for _ in range(medium_spots)],
                ParkingSpotType.LARGE_SPOT: [parking_spot_factory.get_parking_spot(ParkingSpotType.LARGE_SPOT) for _ in range(large_spots)]
            }
            parking_floors.append(ParkingFloor(parking_spots))
        return parking_floors


class ParkingFloor:
    def __init__(self, parking_spots) -> None:
        self.__parking_spots = parking_spots

    def add_parking_spot(self, spot: ParkingSpot):
        switcher = {
            SmallSpot: self.__parking_spots[ParkingSpotType.SMALL_SPOT].put(spot.get_number(), spot),
            MediumSpot: self.__parking_spots[ParkingSpotType.MEDIUM_SPOT].put(spot.get_number(), spot),
            LargeSpot: self.__parking_spots[ParkingSpotType.LARGE_SPOT].put(spot.get_number(), spot),
        }
        switcher.get(spot.get_type(), 'Wrong parking spot type')
    
    @property
    def parking_spots(self):
        return self.__parking_spots

class ParkingLot:
    # _instance = {}
    # def __new__(cls, *args, **kwargs):
    #     if cls not in ParkingLot._instance:
    #         instance = super().__new__(cls)
    #         instance.__init__(*args, **kwargs)
    #         ParkingLot._instance[cls] = instance
    #     return ParkingLot._instance[cls]
    
    def __init__(self, entry_terminals, exit_terminals, floors: list) -> None:
        self.__entrances = entry_terminals
        self.__exits = exit_terminals
        self.__reserved_spots = defaultdict(set)
        self.__floors = floors
        self.__parking_ticket_factory = ParkingTicketFactory()
    
    @property
    def entrances(self):
        return self.__entrances
    
    @property
    def exits(self):
        return self.__exits

    @property
    def reserved_spots(self):
        return self.__reserved_spots

    @property
    def floors(self):
        return self.__floors

    def get_ticket(self, entry_terminal: EntryTerminal, spot_type):
        return entry_terminal.get_ticket(spot_type=spot_type,parking_ticket_factory=self.__parking_ticket_factory, parking_lot=self) 
        

if __name__ == "__main__":
    parking_floors = ParkingFloorFactory.get_parking_floor(2, 40, 50, 80)
    terminal_factory = TerminalFactory()
    parking_assignment = SimpleAssignment()
    tarrif_strategy = StadiumStrategy()
    entry_terminals = [terminal_factory.get_entry_terminal(parking_assignment) for _ in range(2)]
    exit_terminals = [terminal_factory.get_exit_terminal(tarrif_strategy) for _ in range(2)]
    parking_lot = ParkingLot(entry_terminals, exit_terminals, parking_floors)
    tickets = []
    for i in range(4000):
        ticket = parking_lot.get_ticket(entry_terminals[0], ParkingSpotType.MEDIUM_SPOT)
        if ticket:
            tickets.append(ticket)
    print(len(tickets))
    ticket = tickets.pop(4)
    date_1 = '15/6/2022 01:14:18.333338'
    date_format_str = '%d/%m/%Y %H:%M:%S.%f'
    ticket.issue_time = datetime.strptime(date_1, date_format_str)
    exit_terminals[0].accept_ticket(parking_lot, ticket, "CreditCard")
    print(len(parking_lot.reserved_spots))
    ticket = parking_lot.get_ticket(entry_terminals[0], ParkingSpotType.MEDIUM_SPOT)
    print(len(parking_lot.reserved_spots))

