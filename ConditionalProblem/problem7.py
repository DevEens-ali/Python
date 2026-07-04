password = input("Enter the password")

if len(password) < 6:
    print("Weak")
elif len(password) < 10:
    print("Medium")
elif len(password) > 10:
    print("Strong")
else:
    print("NO password Entr")