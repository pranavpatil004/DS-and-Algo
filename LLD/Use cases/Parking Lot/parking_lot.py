from collections import OrderedDict
import enum
import abc

class VehicleType(enum.Enum):
    BIKE, THREE_WHEELER, CAR, BUS = 1, 2, 3, 4

class Vehicle(abc.ABC):
    @abc.abstractproperty
    def vehicle_number(self):
        pass

class Bike(Vehicle):
    def __init__(self, vehicle_number) -> None:
        self.__vehicle_number = vehicle_number
    
    @property
    def vehicle_number(self):
        return self.__vehicle_number

class Car(Vehicle):
    def __init__(self, vehicle_number) -> None:
        self.__vehicle_number = vehicle_number
    
    @property
    def vehicle_number(self):
        return self.__vehicle_number

class Bus(Vehicle):
    def __init__(self, vehicle_number) -> None:
        self.__vehicle_number = vehicle_number
    
    @property
    def vehicle_number(self):
        return self.__vehicle_number

class ParkingTicket:
    def __init__(self, id: int, vehicle: Vehicle, amount: int, paid: bool) -> None:
        self.__id = id
        self.__vehicle = vehicle
        self.__amount = amount
        self.__paid = paid

    @property
    def id(self):
        return self.__id
    
    @property
    def vehicle(self):
        return self.__vehicle
    
    @property
    def amount(self):
        return self.__amount

    @property
    def paid(self):
        return self.__paid
    
    @paid.setter
    def paid(self, is_paid):
        self.__paid = is_paid

class ParkingTicketBuilder():
    def __init__(self) -> None:
        self.car_ticket_mapping = {
            Bike: 100,
            Car: 200,
            Bus: 500
        }
    def generate_parking_ticket(self, vehicle):
        parking_ticket = ParkingTicket(ParkingTicketManager.get_next_id(), vehicle, self.car_ticket_mapping[type(vehicle)], False)
        return parking_ticket

class ParkingTicketManager(object):
    instance = {}
    def __new__(cls, *args, **kwargs):
        if cls not in ParkingTicketManager.instance:
            new_instance = super().__new__(cls, args, kwargs)
            ParkingTicketManager.instance[cls] = new_instance
        return ParkingTicketManager.instance[cls]
    
    def __init__(self) -> None:
        self.__parking_tickets = OrderedDict()
        self.__parking_ticket_builder = ParkingTicketBuilder()
        self.__exit_vehicles = {}
    
    def get_next_id(self):
        id = 0
        if self.__parking_tickets:
            id = self.__parking_tickets.keys()[-1] + 1
        return id
    
    def entry(self, vehicle):
        parking_ticket = self.__parking_ticket_builder.generate_parking_ticket(vehicle)
        self.__parking_tickets[parking_ticket.id] = parking_ticket
        return parking_ticket

    def pay_and_exit(self, parking_ticket: ParkingTicket, amount):
        if amount == parking_ticket.amount:
            parking_ticket.paid = True
            self.__exit_vehicles[parking_ticket.id] = parking_ticket
            del self.__parking_tickets[parking_ticket.id]
        else:
            raise Exception("Invalid amount")
        
class ParkingLot:
    def __init__(self, parking_floors_count: int, parking_spots_count: int) -> None:
        self.parking_floors = [ParkingFloor(parking_spots_count)]*parking_floors_count

class ParkingFloor:
    def __init__(self, parking_spots_count: int) -> None:
        self.parking_spots = [ParkingSpot()]*parking_spots_count
        self.is_full = False

class ParkingSpot:
    def __init__(self) -> None:
        self.occupied = False
