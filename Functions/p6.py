# def sum_all(*args):
#     print(args)
#     for i in args:
#         print(i * 2)
#     return sum(args)
    

    

# print(sum_all(1,2,3))
# # print(sum_all(1,2,3,4,5))
# # print(sum_all(1,2,3,4,5,6,7))


# def print_kwargs(**kwargs):
#     for key , value in kwargs.items():
#         print(f"{key} : {value}")
# print_kwargs(name = "Shaktimaan",power="Lazer_power",enemy="Dr.jackel")



# def even_generator(limit):
#     for i in range(2, limit + 1, 2):
#         yield i

# for num in even_generator(10):
#     print(num)


# def greet():
#     message = "Hello Bro!"

#     def display():
#         print(message)

#     display()

# greet()


def greet():
    message = "Hello bro"
    def display():
        print(message)
    
    return display
result = greet()
print(result)