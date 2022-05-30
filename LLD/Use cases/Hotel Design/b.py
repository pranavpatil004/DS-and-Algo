"""
    Hotel:
        check_in: number_of_rooms
        check_out: room_numbers
    Allocation:
        top_to_bottom: 
        bottom_to_top: 
"""

import abc
from heapq import heapify, heappush, heappop


class Hotel:
    def __init__(self, hotel_name, address, floors, rooms_count_per_floor, allocation_strategy) -> None:
        self.__hotel_name = hotel_name
        self.__address = address
        self.__allocation_strategy_factory = AllocationStrategyFactory()
        self.__allocation_strategy = self.__allocation_strategy_factory.get_allocation_strategy(allocation_strategy)
        self.__room_factory = RoomFactory()
        
        self.__rooms = {}
        self.__available_rooms = []
        for floor_id in range(1, floors+1):
            for id in range(1, rooms_count_per_floor+1):
                room_id = str(floor_id) + str(id).zfill(2)
                room = self.__room_factory.get_room(room_id, floor_id)
                self.__rooms[room_id] = room
                self.__allocation_strategy.add_room(self.__available_rooms, room)
        self.__room_reserved = set()
    
    @property
    def available_rooms(self):
        return self.__available_rooms
        
    def check_in(self, room_count):
        rooms = self.__allocation_strategy.allocate_rooms(self.__available_rooms, room_count)
        for room_id in rooms:
            self.__room_reserved.add(room_id)
        return rooms
    
    def check_out(self, rooms):
        for room_id in rooms:
            self.__room_reserved.remove(room_id)
            self.__allocation_strategy.add_room(self.__available_rooms, self.__rooms[str(room_id)])

class Room:
    def __init__(self, room_id, floor_id) -> None:
        self.__room_id = room_id
        self.__floor_id = floor_id

    @property
    def room_id(self):
        return self.__room_id

class Floor:
    def __init__(self, floor_id, rooms) -> None:
        self.__floor_id = floor_id
        self.__rooms = rooms


class AllocationStrategy(abc.ABC):
    @abc.abstractmethod
    def allocate_rooms(self, rooms_available, room_count):
        pass
    
    @abc.abstractmethod
    def add_room(self, rooms_available, room: Room):
        pass

class TopToBottomAllocationStrategy(AllocationStrategy):

    def add_room(self, rooms_available, room: Room):
        heappush(rooms_available, -int(room.room_id))
    
    def allocate_rooms(self, rooms_available, room_count):
        if len(rooms_available) < room_count:
            raise Exception("Rooms not available")
        rooms = []
        while room_count > 0:
            rooms.append(-heappop(rooms_available))
            room_count -= 1
        return rooms

class BottomToTopAllocationStrategy(AllocationStrategy):
    def add_room(self, rooms_available, room: Room):
        heappush(rooms_available, int(room.room_id))

    def allocate_rooms(self, rooms_available, room_count):
        if len(rooms_available) < room_count:
            raise Exception("Rooms not available")
        rooms = []
        while room_count > 0:
            rooms.append(heappop(rooms_available))
            room_count -= 1
        return rooms

class AllocationStrategyFactory:
    def get_allocation_strategy(self, allocation_strategy):
        switcher = {
            "TopToBottom": TopToBottomAllocationStrategy(),
            "BottomToTop": BottomToTopAllocationStrategy()
        }
        return switcher.get(allocation_strategy, "Invalid strategy")

class RoomFactory:
    def get_room(self, room_id, floor_id):
        room = Room(room_id, floor_id)
        return room



hotel = Hotel("Treebo", "Goa", 5, 10, "BottomToTop")

print(hotel.check_in(5))
hotel.check_out([104])
print(hotel.available_rooms)
print(hotel.check_in(4))
print(hotel.available_rooms)