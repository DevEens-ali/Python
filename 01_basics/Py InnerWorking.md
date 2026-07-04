Python Code Execution Process

Jab hum Python file likhtay hain:

print("Hello World")

aur usay save kartay hain:

chai.py

to Python seedha CPU ko instructions nahi bhejta. Is k darmiyan kuch steps hotay hain.

Step 1: Python Source Code

Sab se pehle hum apna code likhtay hain.
 
print("Hello World")

Ye human-readable code hota hai.

Isay Source Code kehtay hain.

File extension:

.py

Example:

main.py
chai.py
app.py
Step 2: Compile to Byte Code

Jab hum file run kartay hain:

python chai.py

to Python pehle source code ko Byte Code mein convert karta hai.

Diagram mein yehi arrow dikhaya gaya hai:

.py  --->  Byte Code
Byte Code Kya Hota Hai?

Byte Code ek intermediate code hota hai.

Ye:

Machine code nahi hota
Human-readable bhi nahi hota
Python VM ke liye bana hota hai

Isay aap translator ki language samajh lo.

English -> Translator Language -> Urdu

Isi tarah:

Python Code -> Byte Code -> Machine Instructions
Byte Code Ki Advantages
1. Fast Execution

Python ko har dafa source code dobara analyze nahi karna parta.

Byte code pehle se ready hota hai.

Is liye execution thori fast ho jati hai.

2. Platform Independent

Byte code Windows, Linux aur Mac par chal sakta hai.

Kyunkay ye directly hardware se deal nahi karta.

Step 3: .pyc Files

Byte code ko Python save bhi kar sakta hai.

Extension hoti hai:

.pyc

Matlab:

Compiled Python File

Example:

main.pyc

Ye file Byte Code store karti hai.

pycache Folder

Jab Python Byte Code save karta hai to aksar ye folder create hota hai:

__pycache__

Example:

Project
│
├── main.py
│
└── __pycache__
     └── main.cpython-313.pyc

Is folder mein compiled byte code rakha jata hai.

Step 4: Python Virtual Machine (PVM)

Ab Byte Code ko kaun execute karega?

Answer:

Python Virtual Machine

ya

PVM

Diagram mein green box isi ko show kar raha hai.

Byte Code ---> Python VM
Python Virtual Machine Kya Hai?

Python VM ek software engine hai jo Byte Code ko read karta hai.

Aur phir operating system ko instructions deta hai.

Simple words mein:

Python VM = Python ka interpreter engine
Real Flow

Poora process:

Python Code (.py)

        ↓

Compile

        ↓

Byte Code (.pyc)

        ↓

Python Virtual Machine (PVM)

        ↓

Operating System

        ↓

CPU

        ↓

Output
Example

Hum ne likha:

print("Hello")

Python kya karega?

Step 1

Source Code

print("Hello")

↓

Step 2

Byte Code generate hoga

↓

Step 3

Python VM Byte Code ko execute karega

↓

Step 4

Screen par output ayega

Hello
________________________________________________________________________________________________________________________________________________________________________________________________________


Compile to Byte Code

Jab Python program run hota hai to sab se pehle Python source code (.py file) ko Byte Code mein convert karti hai. Byte Code ek low-level aur platform-independent code hota hai jo directly machine code nahi hota, balkeh Python Virtual Machine (PVM) ke samajhnay ke liye tayar kiya jata hai. Is process ko compilation kehte hain. Byte Code ki wajah se program ki execution thori fast ho jati hai kyunkay Python ko har baar source code ko dobara analyze nahi karna parta.

Important Points
Byte Code low-level aur platform-independent hota hai.
Byte Code source code se fast execute hota hai.
Compiled Python files ki extension .pyc hoti hai.
.pyc files ko compiled Python ya frozen binaries bhi kaha jata hai.
Python compiled files ko __pycache__ folder mein store karti hai.
pycache Folder

__pycache__ ek special folder hota hai jahan Python compiled Byte Code files (.pyc) save karti hai. Jab kisi module ko import kiya jata hai, Python uska compiled version yahan store kar deti hai taa ke agli dafa program zyada tezi se load ho sake.

Example:

hello_chai.cpython-312.pyc

Yahan:

hello_chai = original file ka naam
cpython = Python implementation
312 = Python version 3.12
.pyc = compiled Byte Code file
Important Points
Agar source code change ho jaye to Python nayi .pyc file generate karti hai.
Python version change honay par bhi nayi compiled file create hoti hai.
__pycache__ zyada tar imported modules ke liye use hota hai.
Top-level file (jo directly run ki jati hai) ke liye aam tor par .pyc file use nahi hoti.
Is mechanism ka maqsad program ki loading aur execution ko fast banana hai.


________________________________________________________________________________________________
________________________________________________________________________________________________

Python Virtual Machine (PVM)

Python Virtual Machine (PVM) Python ka runtime engine hota hai jo Byte Code ko execute karta hai. Jab Python source code ko Byte Code mein convert kar deti hai, to PVM us Byte Code ko line by line read aur execute karti hai. Isi wajah se PVM ko Python ka interpreter bhi kaha jata hai. PVM Python aur operating system ke darmiyan bridge ka kaam karti hai aur program ka output generate karti hai.

Important Points
PVM ka full form Python Virtual Machine hai.
Yeh Byte Code ko execute karti hai.
PVM Byte Code par loop chala kar instructions ko interpret karti hai.
Yeh Python ka runtime engine hoti hai.
PVM ko Python Interpreter bhi kaha jata hai.
Program ka actual execution PVM ke through hota hai.
Byte Code is Not Machine Code

Ek common misunderstanding yeh hoti hai ke Byte Code aur Machine Code same cheez hain, lekin aisa nahi hai. Byte Code machine code nahi hota. Machine code directly CPU samajhta hai, jabke Byte Code sirf Python Virtual Machine samajhti hai. Is liye Byte Code ko execute karne ke liye PVM ki zaroorat hoti hai.

Important Points
Byte Code machine code nahi hota.
CPU directly Byte Code ko execute nahi kar sakta.
Byte Code Python-specific instructions par mabni hota hai.
Byte Code ko samajhnay aur run karne ka kaam PVM karti hai.
Isi wajah se Python ko interpreted language kaha jata hai.
Python Implementations

Python ki sirf ek implementation nahi hai. Mukhtalif implementations available hain jo alag alag environments aur requirements ke liye banayi gayi hain.

Common Python Implementations
____________________
1:CPython
Python ki standard aur sab se zyada use honay wali implementation.
Official Python implementation hai.
C language mein likhi gayi hai.
____________________
2:Jython
Java platform ke liye Python implementation.
JVM (Java Virtual Machine) par run karti hai.
____________________
IronPython
Microsoft .NET framework ke liye banayi gayi implementation.
____________________
Stackless Python
High-performance concurrency aur multitasking ke liye use hoti hai.
____________________
PyPy
Fast execution ke liye optimized implementation.
JIT (Just-In-Time) compilation use karti hai.

:::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::