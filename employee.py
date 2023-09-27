"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Wage:
    
    def __init__(self, pay, hours=-1) -> None:
        self.pay = pay
        self.hours = hours

    def __is_monthly(self) -> bool:
        return self.hours < 0
    
    def calculate_pay(self) -> float:
        return self.pay * (self.hours if not self.__is_monthly() else 1)
    
    def __str__(self) -> str:
        if self.__is_monthly():
            return f"monthly salary of {self.pay}"
        else:
            return f"contract of {self.hours} hours at {self.pay}/hour"
        
class Commision:
    
    def __init__(self, commision, contracts=-1) -> None:
        self.commision = commision
        self.contracts = contracts

    def __is_bonus(self) -> bool:
        return self.contracts < 0
    
    def calculate_commision(self) -> float:
        return self.commision * (self.contracts if not self.__is_bonus() else 1)
    
    def __str__(self) -> str:
        if self.__is_bonus():
            return f"bonus commission of {self.commision}"
        else:
            return f"commission for {self.contracts} contract(s) at {self.commision}/contract"
class Employee:
    def __init__(self, name, wage:Wage, commision:Commision=None):
        self.name = name
        self.wage = wage
        self.commision = commision

    def get_pay(self):
        pay = 0
        if self.wage is not None:
            pay += self.wage.calculate_pay()
        if self.commision is not None:
            pay += self.commision.calculate_commision()
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
