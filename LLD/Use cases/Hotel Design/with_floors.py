"""
    Hotel:
        check_in: number_of_rooms
        check_out: room_numbers
    Allocation:
        top_to_bottom: 
        bottom_to_top: 
"""

import abc
import enum
from heapq import heappush, heappop


class Hotel:
    def __init__(self, hotel_name, address, floors, rooms_count_per_floor, allocation_strategy) -> None:
        self.__hotel_name = hotel_name
        self.__address = address
        self.__allocation_strategy = AllocationStrategyFactory.get_allocation_strategy(allocation_strategy)
        self.__floors = FloorFactory.get_floor(floors, rooms_count_per_floor)
        
    def check_in(self, room_count):
        rooms = self.__allocation_strategy.allocate_rooms(self.__floors, room_count)
        return rooms
    
    def check_out(self, rooms):
        for floor in self.__floors.values():
            floor.checkout_rooms(rooms)

class Room:
    def __init__(self, room_id, floor_id) -> None:
        self.__room_id = room_id
        self.__floor_id = floor_id

    @property
    def room_id(self):
        return self.__room_id

class Floor:
    def __init__(self, floor_id, rooms_count_per_floor) -> None:
        self.__rooms, self.__available_rooms = RoomFactory.get_room(rooms_count_per_floor, floor_id)
        self.__room_reserved = set()
    
    def get_rooms(self, count):
        rooms = []
        while count > 0 and self.__available_rooms:
            room_id = heappop(self.__available_rooms)
            self.__room_reserved.add(room_id)
            rooms.append(room_id)
            count -= 1
        return rooms

    def checkout_rooms(self, rooms):
        for room_id in rooms:
            if str(room_id) in self.__room_reserved:
                self.__room_reserved.remove(str(room_id))
                heappush(self.__available_rooms, str(room_id))


class FloorFactory:
    @staticmethod
    def get_floor(floor_cnt, rooms_count_per_floor):
        floors = {}
        for floor_id in range(1, floor_cnt+1):
            floor = Floor(floor_id, rooms_count_per_floor)
            floors[floor_id] = floor
        return floors

class AllocationStrategy(abc.ABC):
    @abc.abstractmethod
    def allocate_rooms(self, floors, room_count):
        pass

class TopToBottomAllocationStrategy(AllocationStrategy):
    
    def allocate_rooms(self, floors, room_count):
        rooms = []
        floor_cnt = len(floors)
        while room_count > 0 and floor_cnt > 0:
            floor_rooms = floors[floor_cnt].get_rooms(room_count)
            rooms.extend(floor_rooms)
            room_count -= len(floor_rooms)
            floor_cnt -= 1
        if room_count > 0:
            raise Exception("Rooms unavailable")
        return rooms

class BottomToTopAllocationStrategy(AllocationStrategy):

    def allocate_rooms(self, floors, room_count):
        rooms = []
        floor_cnt = 1
        while room_count > 0 and floor_cnt <= len(floors):
            floor_rooms = floors[floor_cnt].get_rooms(room_count)
            rooms.extend(floor_rooms)
            room_count -= len(floor_rooms)
            floor_cnt += 1
        if room_count > 0:
            raise Exception("Rooms unavailable")
        return rooms

class AllocationStrategyFactory:
    @staticmethod
    def get_allocation_strategy(allocation_strategy):
        switcher = {
            StrategyType.TOPTOBOTTOM: TopToBottomAllocationStrategy(),
            StrategyType.BOTTOMTOTOP: BottomToTopAllocationStrategy()
        }
        return switcher.get(allocation_strategy, "Invalid strategy")

class RoomFactory:
    @staticmethod
    def get_room(rooms_count_per_floor , floor_id):
        __rooms, __available_rooms = {}, []
        for id in range(1, rooms_count_per_floor+1):
            room_id = str(floor_id) + str(id).zfill(2)
            room = Room(room_id, floor_id)
            __rooms[room_id] = room
            __available_rooms.append(room.room_id)
        return __rooms, __available_rooms


class StrategyType(enum.Enum):
    TOPTOBOTTOM, BOTTOMTOTOP = 1, 2

hotel = Hotel("Treebo", "Goa", 5, 4, StrategyType.BOTTOMTOTOP)

print(hotel.check_in(5))
hotel.check_out([104])
print(hotel.check_in(4))