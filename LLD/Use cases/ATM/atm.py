


"""
ATM:
    Card reader
    Screen    
    Keypad
    cash dispener
    printer to print receipts
    deposit slot

Requirements:  
    User can withdraw money
    User can deposit money using cash or cheques
    Admin can add cash to the ATM
    User can check balance
    ATM should support savings and current account
    ATM should multiple banks
    User can transfer fund to another account


class Card:
    def __init__(self, card_number, card_holder_name, account_number, cvv, card_type) -> None:
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.account_number = account_number
        self.cvv = cvv
        self.card_type = card_type
        

class CardReader:
    def read_card(self, card: Card):
        return card.account_number, card.card_holder_name

class Screen:
    def display(message):
        print(message)


"""



"""
Requirements:
    withdraw money
    deposit money - cheque, cash
    check balance
    transfer funds to different account
    print receipt
    send notification
    -- admin can add cash in ATM

"""
import abc


class Card:
    def __init__(self, card_number, card_holder_name, account_number, cvv, card_type) -> None:
        self.card_number = card_number
        self.card_holder_name = card_holder_name
        self.account_number = account_number
        self.cvv = cvv
        self.card_type = card_type


class CardReader:
    @staticmethod
    def read_card(card: Card):
        return card.account_number, card.card_holder_name

class Display:
    @staticmethod
    def show(message):
        print(message)

class Verification(abc.ABC):
    @abc.abstractmethod
    def verify(account_number, pin):
        pass

class Bank:
    def __init__(self, accounts_info) -> None:
        self.__accounts_info = accounts_info
    
    def pin_verification_api(self, account_number, pin):
        return pin == self.__accounts_info[account_number].pin

class PinVerification(Verification):
    def verify(account_number, pin, bank: Bank):
        return bank.pin_verification_api(account_number, pin)

class Account:
    def __init__(self, account_number, account_owner_name, pin, balance) -> None:
        self.__account_number = account_number
        self.__account_owner_name = account_owner_name
        self.__pin = pin
        self.__balance = balance
    
    @property
    def balance(self):
        return self.__balance
    
    @balance.setter
    def set_balance(self, new_balance):
        self.__balance = new_balance


class AccountOperations:
    def withdraw_money(self, account: Account, amount):
        if amount > account.balance:
            raise Exception("Not enough money in the account")
        account.balance -= amount
        return True
    
    def deposit_money(self, account: Account, amount):
        account.balance += amount
        return True

class ATM:
    def __init__(self, cash) -> None:
        self.__cash_reserve = cash
    def withdraw_money(self, card: Card, pin_number):
        user_account, user_name  = CardReader.read_card(card)
        Display.show(f"Welcome {user_name} account {user_account}")
        


        # card swipe
        # pin verification
        # select account type
        # enter amount
        # select transaction type
        # verify ATM and user account balance
        # complete transaction
        # dispense money
        # print receipt
        # send notification
        pass
    def deposit_money(self):
        # card swipe
        # pin verification
        # select account type
        # enter amount
        # add cash to depositor
        # verify cash
        # display message
        # display balance
        pass
    
    def check_balance(self):
        # card swipe
        # pin verification
        # select account type
        # contact bank API
        # display account details
        pass
    
    def transfer_money(self):
        # card swipe
        # pin verification
        # enter destination account details
        # transfer money from origin account to destination account
        # display message
        pass

