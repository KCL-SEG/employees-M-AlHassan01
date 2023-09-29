"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Work:
    """"""

    def __init__(self, money:int, interval:int=-1) -> None:
        self.money = money
        self.interval = interval

    def on_interval(self) -> bool:
        return self.interval > 0

    def calculate_pay(self) -> int:
        return self.money*(self.interval if self.on_interval() else 1)

class Wage(Work):
    """"""
    
    def __init__(self, pay:int, hours:int=-1) -> None:
        super().__init__(pay, hours)

    @property
    def pay(self) -> int:
        return self.money
    
    @property
    def hours(self) -> int:
        return self.interval
    

    def __str__(self) -> str:
        if not self.on_interval():
            return f"monthly salary of {self.pay}"
        else:
            return f"contract of {self.hours} hours at {self.pay}/hour"
        
class Commision(Work):
    """"""
    
    def __init__(self, commision:int, contracts:int=-1) -> None:
        super().__init__(commision, contracts)

    @property
    def commision(self) -> int:
        return self.money
    
    @property
    def contracts(self) -> int:
        return self.interval
    
    def __str__(self) -> str:
        if not self.on_interval():
            return f"bonus commission of {self.commision}"
        else:
            return f"commission for {self.contracts} contract(s) at {self.commision}/contract"
        

class Employee:
    """"""
    
    def __init__(self, name, wage:Wage, commision:Commision=None):
        self.name = name
        self.wage = wage
        self.commision = commision

    def get_pay(self):
        pay = 0
        if self.wage is not None:
            pay += self.wage.calculate_pay()
        if self.commision is not None:
            pay += self.commision.calculate_pay()
        return pay

    def __str__(self):
        return (f"{self.name} works on a {self.wage}" + 
                f"{'. ' if self.commision is None else f' and receives a {self.commision}. '}" +
                f"Their total pay is {self.get_pay()}.")







# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', Wage(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', Wage(25, 100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', Wage(3000), Commision(200, 4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', Wage(25, 150), Commision(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', Wage(2000), Commision(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', Wage(30, 120), Commision(600))
