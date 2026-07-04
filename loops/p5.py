string = input("ENter the String")
for char in string:
    print(char)
    if string.count(char)==1:
        print("non repeated char is", char)