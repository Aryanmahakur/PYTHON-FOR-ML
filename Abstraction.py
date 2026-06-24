from abc import ABC, abstractmethod

class Payment(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


class CreditCard(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Credit Card")


class UPI(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using UPI")


class NetBanking(Payment):

    def pay(self, amount):
        print(f"Paid ₹{amount} using Net Banking")


payments = [
    CreditCard(),
    UPI(),
    NetBanking()
]

for p in payments:
    p.pay(1000)