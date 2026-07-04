# tea_varieties = ["Black","Green","Oolong","Brown","Lemon","Coffee"]
# # print(tea_varieties[-4]) # Negative indexing in allowed in python
# print(tea_varieties[3])

# #Slicing dicing

# # print(tea_varieties[0:4]) # 1-3 print 4 is not included
# #because list is mutable we can change them
# tea_varieties[4] = "Herbal"
# # print(tea_varieties)

# #tea_varieties[1:2] = "white" # This create problem because it treat as a array and each chracter is treated as arrays
# #print(tea_varieties)

# # The solution of this problem is
# tea_varieties[1:2] = ["white"]
# # print(tea_varieties)


# another_varieties = ["Black","Green","Oolong","Brown","Lemon","Coffee"]
# another_varieties[1:1]

#>>> another_varieties = ["Black","Green","Oolong","Brown","Lemon","Coffee"]
#>>> another_varieties[1:1]
#[]
#>>> another_varieties[1:1] = ["test","test"]
#>>> another_varieties                       
#['Black', 'test', 'test', 'Green', 'Oolong', 'Brown', 'Lemon', 'Coffee']
#>>> another_varieties[1:3]
#['test', 'test']
#>>> another_varieties[1:3]=[]
#>>> another_varieties        
#['Black', 'Green', 'Oolong', 'Brown', 'Lemon', 'Coffee']
#>>> 

# looping in List


#>>> for tea in another_varieties:
#...     print(tea)
#... 
#Black
#Green
#Oolong
#Brown
#Lemon
#Coffee
#>>> for tea in another_varieties:
#...     print(tea , end="-")
#... 
#Black-Green-Oolong-Brown-Lemon-Coffee->>>  
#>>> if "Oolong" in another_varieties:
#...     print("I have Oolong")
#... 
#I have Oolong
#>>> if "Herbal" in another_varieties:
#...     print("I don't have Herbal tea")
#... 
#>>> another_varieties.append("Herbal")
#>>> print(another_varieties)            
#['Black', 'Green', 'Oolong', 'Brown', 'Lemon', 'Coffee', 'Herbal']


#______________________________________________________________________________
#>>> another_varieties.append("Herbal")
#>>> print(another_varieties)            
#['Black', 'Green', 'Oolong', 'Brown', 'Lemon', 'Coffee', 'Herbal']
#>>> another_varieties.pop()           
#'Herbal'
#>>> another_varieties      
#['Black', 'Green', 'Oolong', 'Brown', 'Lemon', 'Coffee']
#>>> another_varieties.remove("Brown")
#>#>> another_varieties     
#['Black', 'Green', 'Oolong', 'Lemon', 'Coffee']
#>>> another_varieties.insert(2,"Oolong")
#>>> another_varieties                   
#['Black', 'Green', 'Oolong', 'Oolong', 'Lemon', 'Coffee']
#>>> another_varieties.insert(2,"Black Coffee")
#>>> another_varieties                                                      
#['Black', 'Green', 'Black Coffee', 'Oolong', 'Oolong', 'Lemon', 'Coffee']
#>>> 

# >>> tea_varieties_copies = another_varieties # is trah copies banany mn // is mn same reference 2 variables mn divide hogya hey
# >>> tea_varieties_copies
# ['Black', 'Green', 'Black Coffee', 'Oolong', 'Oolong', 'Lemon', 'Coffee']
# # >>> tea_varieties_copies = another_varieties.copy() # or is trah copy banany mn kya difference hey or is mn actual copy bani hey memory mn


# list comprehension

#>>> squared_num = [x**2 for x in range(10)]
#>>> squared_num                            
#[0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

#>>> range(10)
#range(0, 10)
#>>> 

#range is method that takes parameter and gives the range between 0 to given value but last value is not included
#>>> cube_number = [y**3 for y in range(5)] 
#>>> cube_number
#[0, 1, 8, 27, 64]
#>>> 

#List is Mutable, isliye items change, add aur remove kiye ja sakte hain.
#Indexing 0 se start hoti hai aur negative indexing bhi supported hai.
#Slicing mein end index include nahi hota.
#append() end mein item add karta hai.
#pop() default last item remove karta hai aur usay return bhi karta hai.
#remove() value ko remove karta hai.
#insert(index, value) given index par item insert karta hai.
#list1 = list2 sirf reference copy banata hai (same object).
#list1 = list2.copy() new list object create karta hai.
#List Comprehension ek concise (short) syntax hai jo loop aur append() ka shortcut hai.