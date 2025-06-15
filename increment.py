"""
Principle= 10000
Time=5
Rate=8

interest=Principle * Time * Rate/ 100
print(interest)
"""
#if statement
"""
a= int(input("Enter your age: "))
if a >= 18:
    print("You are Adult")
else:
    print("You are young")
"""
#else if statement
"""
marks= float(input("ENTER THE MARKS: "))
if marks >= 80:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
elif marks >= 60:
    print ("Grade C")
elif marks >= 50:
    print("Grade C")
else:
    print("Grade F")
"""
#logic statement
"""

average = float(input("Enter the average of marks :"))
lgrade = float(input("Enter the lower Grade in all modules :"))
if average>= 80 and lgrade >= 80:
    print("First Class")
elif average >= 80 and lgrade >= 70:
    print("Second Upper class A")
elif average >= 80 and lgrade<= 60:
    print("Second Lower class A")
elif average >=70 and lgrade >= 70:
    print("Second upper class B")
elif average >= 70 or lgrade <60:
    print("Second lower Class B")
elif average >= 60 and lgrade>=50:
    print("Second lower class C")
elif average>=60 and lgrade<= 50:
    print("pass A")
elif average >= 50:
    print("PASS B")
else:
    print("Fail")
"""
#loop statement
"""
for i in range(1,6):
    print(i)
"""
#while loop
"""
count = 1
while count <= 5:
    print(count)
    count +=2
"""
"""
#break statement
for i in range (1,10):
    if i == 5:
        break
    print(i)
    """
#continue statement
"""
for i in range(1, 10):
    if i == 5:
            continue
    print(i)
"""
# multiply statement
"""
for i in range(1,11):
    print(f"{4}*{i} = {8 * i}")
"""
#pattern statement
"""
for i in range(1,5):
    i += 5
    print(i)
"""
# Compound Interest Calculator
