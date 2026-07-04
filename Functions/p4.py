import math

def cricle_stats(radius):
    return round(math.pi * radius **2)
area = cricle_stats(4)
print(area)

def circum_stats(radius):
    return round(2 * math.pi * radius)
circum = circum_stats(5)
print(circum)

