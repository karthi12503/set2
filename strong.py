import math
def factorial(digit):
    return (math.factorial(digit))
number = int(input("enter the number"))
sum = 0
temp = number
while temp > 0:
    digit = temp % 10
    fact = factorial(digit)
    sum = sum + fact
    temp = temp // 10
if sum == number:
    print(number," is a STRONG number")
else:
    print(number,"is NOT a STRONG number")
