"""
for number in range(1, 41):
    if number % 3 != 0 and number % 5 != 0:
        print(number)
"""
"""
p= float(input("Please enter the Value of Principle :"))
r=0.09
t=int(input("Please enter the time :"))
interest = p * (1+ r) ** t
compound = interest - p
print(interest)
print(compound)
"""
"""
for num in range(2,40):
  count=0
for i in range ( 1,num+1 ):
    if num % i == 0:
count = 1  
    if count == 2:
       print(num)
"""

#function
"""
def summation(a,b):
    return a+b
print(summation(80,100))
"""
"""
def substract(a,b,c):
    return a-b-c
print(substract(100,30,20))
"""
"""
def multiple(x,y=2):
    return x*y
print(multiple(6))
"""
"""
def operation(a,b):
    return a+b,a-b,a*b,a//b,a%b

print(operation(20,10))
"""
#lambda function
"""
squarerootofnumber=lambda x: x**2
print(squarerootofnumber(6))
"""
"""
age=lambda a:f" you are {a} old"

print(age(70))
"""
"""
# recursive function is one that call itself
def factorial(n):
    if n == 0:
        return 1
    else:
        return n* factorial(n-1)
print(factorial(5))
"""
#Fibonacci series
"""
def fibonaccinumber(n):
    if n==0:
        return 0
    elif n==1:
        return 1
    else:
        return fibonaccinumber(n-2)+fibonaccinumber(n-1)
n=int(input("Enter the stop number:"))
for i in range (n):
        print(fibonaccinumber(i))
"""
#Question 1
"""





