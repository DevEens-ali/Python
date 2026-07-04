numbers = [1,-2,-3,-7,-4,-6,3,-9,-2,-0,-2,-3,6,-4,2,-0,-0,-2,-0,-7,4,-4,-6,2,-2,3]
positive_number_counts = 0
for num in numbers:
    if num > 0:
        positive_number_counts +=1
print("Total Positive numbers are",positive_number_counts)
