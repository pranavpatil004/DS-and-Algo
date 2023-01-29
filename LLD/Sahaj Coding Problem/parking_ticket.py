import abc
from datetime import datetime

class ParkingTicket:
    def __init__(self, id, spot, issue_time) -> None:
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
    
    @issue_time.setter
    def issue_time(self, issue_time):
        self.__issue_time = issue_time

class ParkingTicketFactory:
    def __init__(self):
        self.current_id = 0
    def get_ticket(self, spot):
        self.current_id += 1
        return ParkingTicket(self.current_id, spot, datetime.now())

class ParkingSpotAssignmentStrategy(abc.ABC):
    @abc.abstractmethod
    def get_parking_spot(self, parking_spot_type, parking_lot):
        pass

class SimpleAssignment(ParkingSpotAssignmentStrategy):
    def get_parking_spot(self, parking_spot_type, parking_lot):
        for floor_num, floor in enumerate(parking_lot.floors):
            parking_spots = floor.parking_spots
            if parking_spots[parking_spot_type]:
                reserved_spot = parking_spots[parking_spot_type].pop()
                parking_lot.reserved_spots[floor_num].add(reserved_spot)
                return reserved_spot
        return None
        