distance = int(input("Enter the distance"))
if distance < 3:
    print("Walk")
elif distance > 3 and distance < 15:
    print("Use a bike")
elif distance > 15:
    print("Use a car")
else:
    print("Invalid distance enter")