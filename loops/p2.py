n = int(input("Enter the number"))
even_numer_sum = 0

for i in range(1, n + 1):
    if i %2 ==0:
        even_numer_sum +=1
print("Total Even number count",even_numer_sum)