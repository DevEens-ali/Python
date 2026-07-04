customer_age = int(input("Enter Age: "))
day = input("Enter the day: ").lower() 


if customer_age >= 18:
    price = 12
    print(f"You are an adult. Your price will be ${price}")
elif 10 <= customer_age < 18:
    price = 10  
    print(f"You are a teenager. Your price will be ${price}")
else:
    price = 8
    print(f"You are a child. Your price will be ${price}")

if day == "wednesday":
    price = price - 2
    print(f"Hurrah! You have a discount. Final price: ${price}")
else:
    print(f"No discount. Final price: ${price}")
