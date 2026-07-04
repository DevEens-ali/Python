Python Numbers Ko Itna Achi Tarah Handle Kyun Karta Hai?

Python ek high-level aur dynamically typed language hai jo scientific computing, data science, AI, machine learning, finance aur general programming ke liye design ki gayi hai. In tamam fields mein numbers ka bohat zyada use hota hai. Isi liye Python numbers ko bohat efficiently aur intelligently handle karta hai.

Real-Life Example

Socho tum aik AI model bana rahe ho.

Us mein millions of calculations hongi.

Jaise:

Addition
Multiplication
Division
Statistics
Matrix calculations
Probability

Agar language numbers ko achi tarah handle na kare to AI ya Data Science jaisi fields mein kaam karna mushkil ho jaye.

Isi liye Python ka number system bohat powerful hai.

Python Numbers Objects Hote Hain

Python mein number sirf ek value nahi hota.

Har number memory mein ek object hota hai.

Example:

a = 10

Memory:

a
 │
 ▼
+---------+
|   10    |
| Type=int|
+---------+

Yahan:

a sirf reference hai.
10 ek object hai.
Us object ka datatype int hai.
Python Numbers Immutable Hote Hain

Ye bohat important point hai.

a = 10

Phir:

a = a + 5

Python 10 ko change nahi karta.

Wo naya object banata hai:

Pehle

a ---> 10

Baad mein

10  (purana object)

a ---> 15 (naya object)

Isi liye integers immutable hote hain.

Python Automatically Datatype Decide Karta Hai

Tum datatype nahi batatay.

Python khud decide karta hai.

a = 10

Python samajh gaya:

int
a = 3.14

Python samajh gaya:

float
a = 4 + 5j

Python samajh gaya:

complex

Is process ko Dynamic Typing kehte hain.

Python Ke Main Number Types

Python mein mainly 3 numeric data types hain.

1. Integer (int)

Puri numbers.

10
100
-25
0
2. Float (float)

Decimal numbers.

10.5
3.14
-2.75
3. Complex (complex)

Scientific aur mathematical calculations ke liye.

4 + 5j

Yahan

4 = Real Part

5j = Imaginary Part
Python Numbers Powerful Kyun Hain?

Python numbers ke sath bohat sari built-in facilities deta hai.

Example:

abs(-20)

Output:

20
pow(2,5)

Output:

32
round(3.14159,2)

Output:

3.14

Aur math module use karke:

import math

math.sqrt(25)

math.factorial(5)

math.pi

math.sin(0)

Ye sab ready-made functions Python provide karta hai.

Python Ki Sab Se Bari Power

Dusri languages mein integer ki limit hoti hai.

Example:

32-bit Integer

Maximum:

2,147,483,647

Lekin Python mein integers practically unlimited size ke ho sakte hain (sirf available memory ki limit tak).

Example:

a = 999999999999999999999999999999999999999999999999999

Ye bhi Python asani se handle kar leta hai.

Isi wajah se Python scientific computing aur cryptography mein bhi use hota hai.

________________________________________

Sab se Pehle Ek Short Difference
Function	Purpose	Kis ke liye?
str()	Human-readable string banata hai	User
repr()	Developer-friendly representation deta hai	Programmer
print()	Screen par output dikhata hai	Display
1. str()

str() kisi object ko simple aur readable string mein convert karta hai.

Is ka maqsad hota hai ke user asani se output parh sake.

Example:

name = "Ali"

print(str(name))

Output:

Ali

Yahan str() ne sirf readable form return ki.

Example 2
num = 100

print(str(num))

Output:

100

Yahan integer ko string bana diya.

Check karo:

num = 100

print(type(num))
print(type(str(num)))

Output:

<class 'int'>
<class 'str'>
2. repr()

repr() object ki official representation return karta hai.

Ye developers ke liye hoti hai.

Is ka goal hota hai ke object ko clearly represent kare.

Example:

name = "Ali"

repr(name)

Output:

"'Ali'"

Ya agar print() use karo:

print(repr(name))

Output:

'Ali'

Notice karo quotes bhi aa gayi.

Kyun?

Kyunkay Python batana chahta hai ke ye string object hai.

Example
text = "Hello\nWorld"

Ab:

print(str(text))

Output:

Hello
World

Lekin

print(repr(text))

Output:

'Hello\nWorld'

Yahan repr() ne newline ko actual line break nahi banaya.

Us ne escape sequence bhi show kar diya.

Developer ko asli data dikhana hota hai.

3. print()

print() koi conversion function nahi hai.

Ye sirf output screen par dikhata hai.

Example:

name = "Ali"

print(name)

Output:

Ali

Internally:

print(name)

lagbhag aisa behave karta hai:

print(str(name))

Matlab print() normally str() ko use karta hai.

Example
x = 50

print(x)

Output:

50

Yahan:

print() output show kar raha hai.
str() internally use hui.
Ek Zabardast Example
text = "Hello\nWorld"

Ab teenon compare karo.

repr()
repr(text)

Output:

'Hello\nWorld'
str()
str(text)

Agar print karo:

print(str(text))

Output:

Hello
World
print()
print(text)

Output:

Hello
World
Custom Class Example
class Student:
    pass

s = Student()

print(s)

Output:

<__main__.Student object at 0x7f8...>

Ye actually repr() use kar raha hota hai.

Agar tum class mein __str__() bana do:

class Student:
    def __str__(self):
        return "Student Object"

s = Student()

print(s)

Output:

Student Object

Aur agar __repr__() bana do:

class Student:
    def __repr__(self):
        return "Student(id=1)"

s = Student()

print(repr(s))

Output:

Student(id=1)
Easy Analogy

Socho tumhara aik dost hai.

Us ka naam hai:

Ali
str()

User se introduce karwana:

Ali
repr()

Police record ya database mein:

Person(name='Ali')

Zyada detail.

print()

Sirf screen par jo dikhana hai wo dikha do.

Ali
Interview Question
repr() aur str() mein difference?
str()	repr()
Human-readable	Developer-readable
Simple output	Detailed representation
Users ke liye	Programmers ke liye
print() normally isi ko use karta hai	Debugging mein useful
Golden Rule ⭐

Yaad rakhna:

str() = User ko dikhane wali representation
repr() = Programmer ko dikhane wali representation
print() = Screen par output dikhane ka function (jo aam tor par str() use karta hai)