weather = input("Enter the weather: ").strip().lower()
if weather == "sunny":
    print("Go for a walk")
elif weather == "rainy":
    print("Read a book")
elif weather == "snowy":
    print("Build a snowman")
else:
    print("Invalid weather entered")