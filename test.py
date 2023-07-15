# def my_decorator(func):
#     def wrapper():
#         print('befor')
#         func()
#         print('after')
#     return wrapper

# @my_decorator
# def my_function():
#     print("insi")

# my_function()

# def outer(func):
#     def inner(*args, **kwargs):
#         print("@@@@@@@@@@@@@@@@")
#         func(*args, **kwargs)
#         print("@@@@@@@@@@@@@@@@")
#     return inner
# def say_hello(a, b):
#     return 'salam'

# say_hello1 = outer(say_hello)
# print(say_hello.__name__)
# print(say_hello1.__name__)
# say_hello1(2, 3)
# @property
# def decorator(f):
#     def new_function():
#         print("Extra Functionality")
#         f()
#     return new_function

# @decorator
# def initial_function():
#     print("Initial Functionality")

# initial_function()


import logging
logging.basicConfig(filename='app.log',
                    filemode='a',
                    level=logging.DEBUG,
                    format='%(name)s - %(levelname)s - %(message)s',
                    )


# logger=logging.getLogger(__name__)


# def t(a,b):
#     namefun=t.__name__
#     logger.info(f'user get me this arf `{a}`, and use this function `{namefun}`')
#     return a+b
# z=0
# # while z<6:
# #     z+=1
# #     a=10
# #     b=10
# #     print(t(a,b))
# #     a+=10
# #     b+=10
# print(t(10,20))

# def makeـlocation(dimensions: int) -> list:
#     function_name=makeـlocation.__name__
#     # logger.info(f'user use this function_name `{function_name}`')
#     places = list()
#     for x in range(0, dimensions):
#         for y in range(0, dimensions):
#             coordinates = (x, y)
#             places.append(coordinates)
#     return places


# print(makeـlocation(10))
from colorama import Fore

# def get_help(location: tuple):
#     function_name=get_help.__name__
#     # logger.info(f'user use this function_name `{function_name}`')
#     x, y = location
#     help = f'''At the beginning of history,
#     if you moves forward {x} years and climb {y} steps on the ladder of destiny
#     , you will go to the other side of history.'''
#     print(Fore.RED,help)
# get_help((2,3))
# def writeـmap(dimensions: int, user: tuple):
#     function_name=writeـmap.__name__
#     # logger.info(f'user use this function_name `{function_name}`')
#     x, y = user
#     print(Fore.YELLOW,'_ '*dimensions,end='\n')
#     for j in range(0, dimensions):
#         if j == y:
#             for i in range(0, dimensions):
#                 if i == x:
#                     print(Fore.RESET ,'|*',Fore.YELLOW, end='')
#                 else:
#                     print('|_', end='')
#             print('|')
#         else:
#             print('|_'*dimensions, end="|\n")


# writeـmap(10,(2,2))
# import time
# from asciiquarium import Aquarium, Dino

# # ایجاد یک آکواریوم جدید
# aquarium = Aquarium()

# # ایجاد یک دایناسور در آکواریوم
# dino = Dino(aquarium)

# # افزودن دایناسور به آکواریوم
# aquarium.add_object(dino)

# # نمایش آکواریوم
# aquarium.start()

# # حرکت دایناسور تا زمانی که کاربر کلید "q" را فشار دهد
# while True:
#     dino.move()
#     time.sleep(0.1)
#     if aquarium.is_key_pressed('q'):
#         break

# # خاتمه نمایش آکواریوم
# aquarium.stop()


from art import *

animal_name = input("Enter the name of an animal: ")
animal_art = text2art(animal_name)
print(animal_art)
