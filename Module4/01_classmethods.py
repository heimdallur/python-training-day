"""Tutorial on classmethods"""

# Classes use methods inside them which take the self argument


from datetime import datetime


class Employee:
    # Classes should have an init dunder method
    def __init__(self,
                 firstname: str,
                 surname: str,
                 pay: int
                 ):
        # the "self" variable here is used
        # throughout to refer to the object itself
        self.firstname = firstname
        self.surname = surname
        self.pay = pay

    # This is a method inside the class
    def print_name(self):
        # here we can print my_var because it's part of self
        print(f"EMPLOYEE NAME: {self.firstname} {self.surname}")


# We can access the class by instantiating it and calling a method
emp = Employee("Micky", "Mouse", 10000)
emp.print_name()

# Classmethds are put inside the class with a decorator and take cls as
#   the first argument


class Employee:
    # This value is outside of init so it will apply to all
    #   instances of Employee
    annual_rise = 1.04

    def __init__(self,
                 firstname: str,
                 surname: str,
                 pay: int,
                 employee_annual_rise: float = annual_rise
                 ):
        self.firstname = firstname
        self.surname = surname
        self.pay = pay
        self.employee_annual_rise = employee_annual_rise

    def raise_pay(self):
        # Raise an emloyee's pay
        self.pay = self.pay * self.annual_rise

    def print_pay_rise_values(self):
        print(f"All employee pay rise is {self.annual_rise}")
        print(f"{self.firstname} {self.surname}'s pay rise is {self.employee_annual_rise}")

    # This is a method inside the class
    @classmethod
    def set_annual_rise(cls, new_value:float):
        # here we can print my_var because it's part of self
        cls.annual_rise = new_value


# You call it like this
emp1 = Employee("Elsa", "of Arendel", 10000)
emp1.print_pay_rise_values()
Employee.set_annual_rise(1.06)
emp2 = Employee("Anna", "of Arendel", 10000)
emp1.print_pay_rise_values()
emp2.print_pay_rise_values()

# Why do this? It keeps functions nicely organised into the space they're
#   associated with

# Another use is to actually create the class in different ways


class Employee:
    def __init__(self,
                 firstname: str,
                 surname: str,
                 pay: int,
                 annual_rise: float = 1.04
                 ):
        self.firstname = firstname
        self.surname = surname
        self.pay = pay
        self.annual_rise = annual_rise

    def raise_pay(self):
        # Raise an emloyee's pay
        self.pay = self.pay * self.annual_rise

    def print_name(self):
        # here we can print my_var because it's part of self
        print(f"EMPLOYEE NAME: {self.firstname} {self.surname}")

    # This is a method inside the class
    @classmethod
    def create_from_str(cls, str):
        firstname, surname, pay = str.split(",")
        return cls(firstname, surname, pay)


# Now we cna use this to create a class
emp = Employee.create_from_str("Harry,Potter,100000")
emp.print_name()

# Some great examples of this is datetime
now = datetime.now()
today = datetime.today()
amazing_date = datetime.fromisoformat("2022-02-22T22:22:22.222222")