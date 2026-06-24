from abc import ABC, abstractmethod
class BankAccount(ABC):
    def __init__(self,balance,num):
        self.__balance=balance
        self.__acc_no=num
    @abstractmethod
    def calculate_interest(self):
     pass
    def deposit(self,amt):
      self. __balance +=amt
    def withdraw(self,amt):
      self.__balance -=amt
    def get_balance(self):
       return self.__balance
class SavingsACC(BankAccount):
    def __init__(self,balance,num):
         super().__init__(balance,num)
    def calculate_interest(self):
       return self.get_balance()*5/100
    def display(self):
       print(self.__balance)
     
    
class currentACC(BankAccount):
    def __init__(self,balance,num):
       super().__init__(balance,num)
    def calculate_interest(self):
       return self.get_balance()*2/100
    def display(self):
       print(self.__balance)

objectsaving=SavingsACC(1000,123)
objectsaving.deposit(500)
print(objectsaving.calculate_interest())
print(objectsaving.get_balance())
    