number = int(input("enter the number :"))
square = number * number
square = str(square)
last = square[-1]
last = int(last)
if last == number:
    print(number,"is a automorphic number")
else:
    print(number,"is not a automorphic number")
