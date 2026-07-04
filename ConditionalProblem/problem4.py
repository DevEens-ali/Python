fruit = input("Enter the name of the fruit: ").lower()

if fruit == "banana":
    color = input("Enter the color of the fruit: ").lower()
    
    
    if color == "green":
        print("Your fruit is unripe.")
    elif color == "yellow":
        print("Your fruit is ripe.")
    elif color == "brown":
        print("Your fruit is overripe.")
    else:
        print("Unknown color entered.")
else:
    print("Expected food name was not entered.")


