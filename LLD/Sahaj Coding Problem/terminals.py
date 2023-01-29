import abc
from math import floor
from payment_processor import CashProcessor, CreditCardProcessor

class Terminal(abc.ABC):
    def __init__(self, id) -> None:
        self.__terminal_id = id
    
    @property
    def terminal_id(self):
        return self.__terminal_id

class EntryTerminal(Terminal):
    def __init__(self, id, parking_spot_strategy) -> None:
        super().__init__(id)
        self.parking_spot_strategy = parking_spot_strategy
    def get_ticket(self, spot_type, parking_ticket_factory, parking_lot):
        spot =  self.parking_spot_strategy.get_parking_spot(spot_type, parking_lot)
        if spot is None:
            print("Parking spot is full")
            return None
        return parking_ticket_factory.get_ticket(spot)

class ExitTerminal(Terminal):
    def __init__(self, id, tarrif_caculator) -> None:
        super().__init__(id)
        self.__tarrif_calculator = tarrif_caculator
        self.payment_switcher = {
            "Cash": CashProcessor(),
            "CreditCard": CreditCardProcessor()
        }

    def accept_ticket(self, parking_lot, parking_ticket, payment_type):
        amount = self.__tarrif_calculator.calculate(parking_ticket)
        self.process_payment(payment_type, amount)
        spot = parking_ticket.spot
        self.unreserve_spot(spot, parking_lot)
        return
    def process_payment(self, payment_type, amount):
        payment_processor = self.payment_switcher.get(payment_type)
        payment_processor.process(amount)
    
    def unreserve_spot(self, spot, parking_lot):
        reserved_spots = parking_lot.reserved_spots
        for floor_number in reserved_spots:
            if spot in reserved_spots[floor_number]:
                parking_lot.floors[floor_number].parking_spots[spot.get_type()].append(spot)
                reserved_spots[floor_number].discard(spot)
                break


class TerminalFactory:
    def __init__(self) -> None:
        self.id = 0
    def get_entry_terminal(self, parking_assignment_strategy):
        self.id += 1
        return EntryTerminal(self.id, parking_assignment_strategy)
    def get_exit_terminal(self, tarrif_calculator):
        self.id += 1
        return ExitTerminal(self.id, tarrif_calculator)