from datetime import datetime

class InterestRateComputer:
    def get_rate():
        pass


class BankAccount:
    def __init__(self, balance=0, name=''):
        self.balance = balance
        self.name = name

    def deposit(self, amount):
        self.balance += amount
        # recording the time of transaction for future implementation of reporting feature
        now = datetime.now()
        print("now =", now)
        # dd/mm/YY H:M:S
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print("Transaction:", amount, "-", dt_string)	



    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
            # recording the time of transaction for future implementation of reporting feature
            now = datetime.now()
            print("now =", now)
            # dd/mm/YY H:M:S
            dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            print("Transaction:", amount, "-", dt_string)

        #TODO: Write code to handle the insufficient balance case here

    def interest(self, rate_computer):
        return rate_computer.get_rate() * self.balance

