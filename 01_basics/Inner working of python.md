Jitna b data ka type ka hey wo memory mn rehta hey kabhi b variable mn nahi jata hey python mn

Actually there is no datatype in python
hum variable mn kabhi b koi datatype assign he nahi krty hey

memory k andar jo reference hey os ka datatype hota hey 
for example there is 10 store in memory the type is Number 
if "xyz" store there memory ref is String

________________________________________

1. Python Mein Variable Kya Hota Hai?

Sab se pehle ye baat yaad rakho:

Python mein variable ke andar data store nahi hota. Variable sirf object ka reference (address) store karta hai.

Example:

a = 10

Memory:

Variable          Memory

a  ----------->   10

10 memory mein object hai.

a sirf us object ko point kar raha hai.

2. Reference Count Kya Hota Hai?

Reference Count ka matlab hai:

Kitne variables ya references ek hi object ko point kar rahe hain.

Example:

score = 10
a_score = 10

Memory:

score --------\
               \
                ---> 10
               /
a_score ------/

Ab object 10 ko do variables point kar rahe hain.

Isliye us object ka Reference Count = 2 (internally Python ke temporary references ki wajah se actual count zyada ho sakta hai).

Example
a = 5
b = a

Memory:

a ------\
         \
          ---> 5
         /
b ------/

Reference Count:

Object 5

Reference Count = 2
3. sys.getrefcount()

Python reference count dekhne ke liye:

import sys

a = 10

sys.getrefcount(a)

Example:

>>> import sys
>>> x = 100
>>> y = x
>>> sys.getrefcount(x)

Ye actual count se 1 zyada return karta hai.

Kyun?

Kyunkay jab tum function call karte ho:

sys.getrefcount(x)

to x temporarily function ke parameter ke through bhi reference ban jata hai.

Isliye count 1 extra hota hai.

4. Ye Strange Numbers Kyun Aa Rahe Hain?

Tum ne likha:

sys.getrefcount(1)

3221225472

Ye normal nahi hai.

Python 3.12 aur us ke baad kuch immutable objects (integers, strings, booleans) ko Immortal Objects bana diya gaya hai.

Matlab:

unka reference count practically kabhi zero nahi hota.
Python unko delete nahi karta.

Isliye bohat bara number show hota hai.

Ye CPython ki optimization hai.

5. Mutable Example

Tumhara example:

l1 = [1,2,3,4]
l2 = l1

Memory:

l1 --------\
            \
             ---> [1,2,3,4]
            /
l2 --------/

Dono same list ko point kar rahe hain.

Ab:

l1[0] = 55

Memory:

[55,2,3,4]

Kyunkay list mutable hai.

Object change hua.

Isliye:

l1

Output:

[55,2,3,4]

Aur

l2

Output bhi:

[55,2,3,4]

Kyunkay dono same object ko point kar rahe hain.

6. Dusra Example
myl1 = [5,6,7,8]
myl2 = myl1

Memory:

myl1 -------\
              \
               ---> [5,6,7,8]
              /
myl2 -------/

Ab tum ne likha:

myl1 = [11,12,13,14]

Ab kya hua?

Python ne purani list ko modify nahi kiya.

Nayi list bana di.

Memory:

myl1 --------> [11,12,13,14]

myl2 --------> [5,6,7,8]

Ab dono alag objects ko point kar rahe hain.

Isliye:

myl1[2] = 22

sirf

[11,12,22,14]

ko change karega.

Purani list bilkul waise hi rahegi.

7. Kya Data Variable Mein Store Hota Hai?

Tum ne likha:

Jitna bhi datatype ka data hai wo memory mein rehta hai, variable mein nahi.

✅ 100% Correct.

Example:

name = "Ali"

Memory:

Variable

name ---------> "Ali"

Variable ke andar "Ali" nahi gaya.

Sirf us ka reference gaya.

8. "Actually There is No Datatype in Variable"

Tum ne likha:

hum variable mn kabhi datatype assign nahi karte.

✅ Bilkul sahi.

Example:

a = 10

Ab

a = "Ali"

Phir

a = [1,2,3]

Ek hi variable alag alag objects ko point kar sakta hai.

Isliye Python ko kehte hain:

Dynamically Typed Language

Variable ka koi fixed datatype nahi hota.

Datatype object ka hota hai.

9. Datatype Kis Ka Hota Hai?

Example:

x = 10

Memory:

Variable

x ---------> Object

             10
            Type=int

Example:

x = "Ali"

Memory:

Variable

x ---------> Object

            "Ali"
          Type=str

Datatype object ke sath attached hota hai.

Variable ke sath nahi.

10. Easy Rule

Kabhi bhi yaad rakhna:

Variable
    ↓
Reference
    ↓
Object in Memory
    ↓
Object has Type

Ya phir aur bhi simple:

Variable
     │
     ▼
Object
(Type is inside the object)
Final Summary (Exam Notes)
Python mein variable data store nahi karta, sirf object ka reference store karta hai.
Har value (Integer, String, List, Tuple, Dictionary, etc.) memory mein object ki form mein rehti hai.
Har object ka apna datatype hota hai.
Variable ka koi permanent datatype nahi hota.
Reference Count batata hai ke kitne references ek hi object ko point kar rahe hain.
Immutable objects (String, Integer, Tuple) ko change nahi kiya ja sakta; modification par naya object create hota hai.
Mutable objects (List, Dictionary, Set) ko directly modify kiya ja sakta hai.
Jab kisi object ko koi reference point nahi karta, to Python ka Garbage Collector uski memory free kar deta hai (except kuch optimized/immortal objects in modern CPython).