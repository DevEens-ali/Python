Number = int(input("Enter the number"))
factorial = 1

while Number > 0:
    factorial = factorial * Number
    Number -=1
    print(factorial)