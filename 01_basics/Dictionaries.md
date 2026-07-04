what are Dictionaries and how it is different from list

Ans : One difference is that when we looping on a list it return values.
but when we looping on Dict it return keys instead of values.

>>> chai_types = {}
>>> chai_types = {"Lemon":"Bitter taste","Ginger":"Zasty","Green":"Mild","Masala":"spicy"}
>>> chai_types     
{'Lemon': 'Bitter taste', 'Ginger': 'Zasty', 'Green': 'Mild', 'Masala': 'spicy'}
>>> chai_types["Green"]
'Mild'
>>> chai_types.get("Ginger")
'Zasty'
>>> chai_types.get("Gingery")
>>> chai_types.get("Masalaa")
>>> chai_types.get("lemonade")
>>> 

>> chai_types.get("Masalaa") --> jab menay is trah masala likha toh mujy error nahi mila
>>> chai_types.get("lemonade")
>>> chai_types["Masalaa"] --> or jab is trah likha toh mujy error mila [ye qn ??]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types["Masalaa"]
    ~~~~~~~~~~^^^^^^^^^^^
KeyError: 'Masalaa'
>>> 

_________________________________________________________________________

changing values

>>> chai_types
{'Lemon': 'Bitter taste', 'Ginger': 'Zasty', 'Green': 'Mild', 'Masala': 'spicy'}
>>> chai_types["Green"] = "Fresh"
>>> chai_types                   
{'Lemon': 'Bitter taste', 'Ginger': 'Zasty', 'Green': 'Fresh', 'Masala': 'spicy'}
>>> 

>>> chai_types
{'Lemon': 'Bitter taste', 'Ginger': 'Zasty', 'Green': 'Fresh', 'Masala': 'spicy'}
>>> for chay in chai_types:
...     print(chay)
... 
Lemon
Ginger
Green
Masala
>>> for chay in chai_types:
...     print(chay, chai_types[chay])
... 
Lemon Bitter taste
Ginger Zasty
Green Fresh
Masala spicy
>>> for key, value in chai_types.item():
...     print(key, value)
... 
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    for key, value in chai_types.item():
                      ^^^^^^^^^^^^^^^
AttributeError: 'dict' object has no attribute 'item'. Did you mean: 'items'?
>>> for key, value in chai_types.items():
...     print(key, value)
... 
Lemon Bitter taste
Ginger Zasty
Green Fresh
Masala spicy
>>> 
>>> chai_types
{'Lemon': 'Bitter taste', 'Ginger': 'Zasty', 'Green': 'Fresh', 'Masala': 'spicy'}
>>> #adding new chai types
>>> chai_types["Earl grey"] = "citrus"
>>> chai_types                        
{'Lemon': 'Bitter taste', 'Ginger': 'Zasty', 'Green': 'Fresh', 'Masala': 'spicy', 'Earl grey': 'citrus'}
>>> 

What is the difference between pop() in list and dict and popitem() 
>>> chai_types.pop("Ginger")
'Zasty'
>>> chai_types.popitem()         
('Earl grey', 'citrus')
>>> chai_types
{'Lemon': 'Bitter taste', 'Green': 'Fresh', 'Masala': 'spicy'}
>>> chai_types.pop()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    chai_types.pop()
    ~~~~~~~~~~~~~~^^
TypeError: pop expected at least 1 argument, got 0
>>> 

Nested Dictionaries
>>> tea_shop = {
... "chai": {"Masala":"spicy","Earl_grey":"Citurs":"lemon":"bitter"}
  File "<stdin>", line 2
    "chai": {"Masala":"spicy","Earl_grey":"Citurs":"lemon":"bitter"}
                                                  ^
SyntaxError: invalid syntax
>>> tea_shop = {
... "chai": {"Masala":"spicy","Earl_grey":"Citurs","lemon":"bitter"},
... "Tea":{"Green":"Mild","Brown":"Sweet","Black":"Strong"},
... }
>>> tea_shop
{'chai': {'Masala': 'spicy', 'Earl_grey': 'Citurs', 'lemon': 'bitter'}, 'Tea': {'Green': 'Mild', 'Brown': 'Sweet', 'Black': 'Strong'}}
>>> tea_shop["Chai"]["lemon"]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
    tea_shop["Chai"]["lemon"]
    ~~~~~~~~^^^^^^^^
KeyError: 'Chai'
>>> tea_shop["chai"]["lemon"]
'bitter'

list comprehension in dictionaries
_________________________________________________________________________
>>> squared_num = [x:x**2 for x in range(6)]
  File "<stdin>", line 1
    squared_num = [x:x**2 for x in range(6)]
                    ^
SyntaxError: invalid syntax
>>> squared_num = {x:x**2 for x in range(6)}
>>> squared_num                             
{0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
>>> cube_of_num = {y:y**3 for y in range(7)}
>>> cube_of_num                             
{0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216}
>>> 
>>> cube_of_num.clear() // clear all the values inside the dictionarie
>>> cube_of_num        
{}
>>> 
>>> keys = ["Masala","Lemon","Ginger","Brown","White"]
>>> default_value = "Delicious"
>>> new_dict = dict.fromkeys(keys,default_value)
>>> new_dict
{'Masala': 'Delicious', 'Lemon': 'Delicious', 'Ginger': 'Delicious', 'Brown': 'Delicious', 'White': 'Delicious'}
>>> 

⭐ Dictionary Methods Summary

Method	         Purpose
dict["key"]  	Key se value access kare (key na mile to KeyError)
get(key)	    Safe access, key na mile to None return
keys()	        Sirf keys return karta hai
values()	    Sirf values return karta hai
items()	        Key aur value dono return karta hai
pop(key)	    Given key ko remove karta hai
popitem()	    Last inserted key-value pair remove karta hai
clear()      	Dictionary ke tamam items remove kar deta hai
fromkeys()	    Di hui keys se nayi dictionary banata hai aur sab ko same default value assign karta hai


⭐ Interview Point (List vs Dictionary)


List data ko index ki madad se store aur access karti hai.
Dictionary data ko key-value pairs ki form mein store karti hai aur keys ki madad se access karti hai.
List par loop lagane se values milti hain.
Dictionary par loop lagane se by default keys milti hain.
List mein pop() index ya last item remove karta hai, jabke Dictionary mein pop() ko key deni padti hai kyun ke dictionary mein indexing hoti hi nahi.