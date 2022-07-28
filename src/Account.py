class Bank_Account:
    __balance = 0
    __name = None

    def __init__(self, bal, nm):
        self.__balance = bal
        self.__name = nm

    def deposit(self, amount):
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if self.__balance >= amount:
            self.__balance -= amount
            return self.__balance
        else:
            raise Exception("Insufficient balance")

    def interest(self,rate_computer):
        return rate_computer.getRate() * self.__balance
    
    def balance(self):
        return(self.__balance)

    def name(self):
        return (self.__name)
           
    #def __eq__(self, other):
        #if not isinstance(other, Bank_Account):
            # don't attempt to compare against unrelated types
           # return NotImplemented
        #print(self.__balance, other.__balance)
        #return self.__balance == other.__balance and self.__name == other.__name
