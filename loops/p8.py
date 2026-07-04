check_number = int(input("Enter the number to check"))
is_prime = True

check_number > 1
for i in range(2,check_number):
    if(check_number %i)==0:
        is_prime = False
print(is_prime)
