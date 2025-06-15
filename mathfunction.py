"""""
import math

A_degree = 37
B_degree = 90
b = 4

C_degree = 180 - (A_degree + B_degree)

A_rad = math.radians(A_degree)
B_rad = math.radians(B_degree)
C_rad = math.radians(C_degree)

a = b * math.sin(A_rad) / math.sin(B_rad)

area = 0.5 * a * b * math.sin(C_rad)

print(f"Angle C: {C_degree} degrees")
print(f"Area of Triangle: {area:.2f}")
"""""
#Class Inhertance
"""""
class employee:
    pass
emp1=employee()
emp2=employee()
emp3=employee()

emp1.fristName="GANZA"
emp1.lastname="Levis"
emp1.empId=1001
emp2.fristName="MUGABE"
emp2.lastname="REMMY"
emp2.empId=2002
emp3.fristName="MUCYO"
emp3.lastname="PASSY"
emp3.empId=2004

print(f"First name: {emp1.fristName}")
print(f"Last Name: {emp1.lastname}")
print(f"Implyement ID: {emp1.empId}")
"""""
"""""
class employee:
    r=2
    def __init__(self,last,first,pay):
        self.last=last
        self.first=first
        self.pay=pay
        self.email=first+""+last+"@gmail.com"
    def fullname(self):
            return f"{self.last} {self.first}"
    def increase(self):
        self.pay = int(self.pay * self.r)
    def address(self):
        return f"{self.email},{self.pay}"
lect1 = employee("James", "hakizimana", 500)
lect1.increase()
print(f"New salary of{lect1.first} is {lect1.pay}Rwf")
print(lect1.fullname())
#lect1.increase()
print(lect1.pay)
lect1.address()
print(lect1.address())
"""""
#Sub class inheritance
class lecture:
    r=2
    def __init__(self,last,first,pay):
        self.last=last
        self.first=first
        self.pay=pay
        self.email=first+""+last+"@gmail.com"
    def fullname(self):
            return f"{self.last} {self.first}"
    def increase(self):
        self.pay = int(self.pay * self.r)
    def address(self):
        return f"{self.email},{self.pay}"
class ranking(lecture):
    def __init__(self,last,first,pay,working_experience):
        lecture.__init__(self,last,first,pay)
        self.working_experience=working_experience
    def promotion(self):
        if self.working_experience>5:
            print(f"you are a senior lecture and salary will be {self.pay*1.5}")
        else:
            print("keep working")
lect1=ranking("James","Hakizimana",500,7)
print(lect1.pay)
lect1.promotion()
print(lect1.promotion())
print()
lect1 =lecture("James", "hakizimana", 500)
lect1.increase()
print(f"New salary of{lect1.first} is {lect1.pay}Rwf")
print(lect1.fullname())
#lect1.increase()
print(lect1.pay)
lect1.address()
print(lect1.address())








































