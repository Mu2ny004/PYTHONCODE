#Inhertance class
"""""
class Staff:
    def __init__(self,name,Staff_id,Department):
        self.name=name
        self.Staff_id=Staff_id
        self.Department=Department
    def display_Detail(self):
        print(f"\n Name :{self.name}")
        print(f"Staff ID: {self.Staff_id}")
        print(f"Department : {self.Department}")
class Teacher(Staff):
    def __init__(self, name, Staff_id, Department, Subject, Teaching_Hours):
        super().__init__(name, Staff_id, Department)
        self.Subject=Subject
        self.Teaching_Hours= int (Teaching_Hours)

    def display_Detail(self):
        super().display_Detail()
        print(f"Subject: {self.Subject}")
        print(f"Teaching Hours: {self.Teaching_Hours}")
        print(f"Overloading: {'Yes' if self.in_overloading() else 'No'}")

    def in_overloading(self):

        return self.Teaching_Hours>20
class Administrator(Staff):
    def __init__(self, name, Staff_id, Department, Position, Office_Hours):
        super().__init__(name, Staff_id, Department)
        self.Position=Position
        self.Office_Hours=int (Office_Hours)
    def display_Detail(self):
        super().display_Detail()
        print(f"Position : {self.Position}")
        print(f"Office_Hours : {self.Office_Hours}")
        print(f"Senior : {'yes' if self.Senior() else 'No'}")

    def Senior(self):
        return self.Office_Hours > 40

teacher=Teacher("James","T001","Math","Teacher of Math","20")
Admin=Administrator("Robert","Dept 002","Academic Register","Register","41")

print("Teacher Deatail")
teacher.display_Detail()

print("Administrator Deatail")
Admin.display_Detail()
"""""
#Input the value
"""""
length=float(input("Enter the Lengeth: "))
width=float(input("Enter the Width: "))
Perimeter=2*length+width
Area=length*width
print(f"Value of Perimeter: {Perimeter}")
print(f"Area of Rectangle: {Area}")
"""""
#class inhertance ranking
"""""
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
"""""
#even number
"""""
count=1
while count<=20:
    print(count)
    count*=2
"""""
#list
"""""
# Initial list
animals = ["Goat", "Chicken", "Sheep", "Lion", "Hare"]

# Step 2: Sort alphabetically
animals.sort()

# Step 3: Add Elephant
animals.append("Elephant")

# Step 4: Separate wild and domestic
domestic = []
wild = []
for animal in animals:
    if animal in ["Lion", "Elephant"]:
        wild.append(animal)
    else:
        domestic.append(animal)
# Step 5: Add Tiger in the middle of wild animals
middle_index = len(wild) // 2
wild.insert(middle_index, "Tiger")
# Print results
print("Domestic animals:", domestic)
print("Wild animals:", wild)
"""""
"""""
#Check if password is correct
while True:
    password = input("Enter your password: ")
    if password == "python123":
        print("Access granted!")
        break
    else:
        print("Incorrect password. Try again.")
"""
#vowel
"""""
text = input("Enter a string: ")

vowels = "aeiouAEIOU"

print("Vowels in the string:")
for char in text:
    if char in vowels:
        print(char)
"""""
#interest
"""""
principal = float(input("Enter the initial deposit amount (Rwf): "))
rate = float(input("Enter the interest rate (%): "))
years = int(input("Enter number of years: "))

final_amount = principal * (1 + rate / 100) ** years

print(f"After {years} years at {rate}% interest, the amount grows to: {final_amount:.2f} Rwf")
"""""
#Pattern
"""""
for i in range(1,6):
    print("*"* i)
    """""
# sinnnn
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

import math

# Input two sides and the angle between them (in degrees)
a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))
angle_deg = float(input("Enter the angle between them (in degrees): "))

# Convert angle to radians
angle_rad = math.radians(angle_deg)

# Compute the area
area = 0.5 * a * b * math.sin(angle_rad)

# Display the result
print(f"The area of the triangle is: {area:.2f}")

