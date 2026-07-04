user_age = int(input("Enter your age: "))

if user_age < 13: 
    print("You are a child") 
elif user_age < 20: 
    print("You are a teenager") 
# Line below changed from < 60 to < 65 based on standard definitions
elif user_age < 65: 
    print("You are an adult") 
else: 
    print("You are a senior")
