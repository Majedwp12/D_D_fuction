# # # dim = 5
# # # y =4
# # # x = 4


# # # def art(dimensions: int):
# # #     print(' _'*dimensions, end='\n')
# # #     for j in range(0, dimensions):
# # #         print('|_'*dimensions, end="|\n")

# # # def art(dimensions: int, x: int, y: int):
# # #     print(' _'*dimensions, end='\n')
# # #     for j in range(0, dimensions):
# # #         if j == y:
# # #             for i in range(0, dimensions):
# # #                 if i == x:
# # #                     print('|*', end='')
# # #                 else:
# # #                     print('|_', end='')
# # #             print('|')
# # #         else:
# # #             print('|_'*dimensions, end="|\n")


# # import random  # art(dim, x, y)


# # def locationـrandom(dimensions: int) -> int:

# #     x_D = random.randint(1, dimensions)
# #     y_D = random.randint(1, dimensions)
# #     x_H = random.randint(1, dimensions)
# #     y_H = random.randint(1, dimensions)
# #     return x_D, y_D, x_H, y_H


# # # print(locationـrandom(5))
# # def locationـrandom(dimensions: int) -> int:
# #     y_list = list()
# #     x_list = list()
# #     for i in range(0, dimensions):
# #         x_list.append(i)
# #         y_list.append(i)
# #     x_D = random.choice(x_list)
# #     y_D = random.choice(y_list)
# #     x_list.remove(x_D)
# #     y_list.remove(y_D)
# #     x_H = random.choice(x_list)
# #     y_H = random.choice(y_list)
# #     return x_D, y_D, x_H, y_H


# # def Matchـlocation(x_user: int, y_user: int, x_place: int, y_place: int) -> bool:
# #     flage = False
# #     if x_user == x_place and y_user == y_place:
# #         flage = True
# #     return flage


# # def move(dimensions: int, move: str, x: int, y: int):
# #     if move == 'Right':
# #         x += 1
# #     elif move == 'Left':
# #         x -= 1
# #     elif move == 'Down':
# #         y += 1
# #     elif move == 'Up':
# #         y -= 1
# #     return x, y


# # def help(x, y):
# #     help = f'''At the beginning of history, 
# #     if you move forward {x} years and climb {y} steps on the ladder of destiny
# #     , you will go to the other side of history.'''
# #     print(help)


# # # تعریف تابع بررسی عدد زوج بودن
# # def is_even(num):
# #     return num % 2 == 0

# # # ایجاد یک لیست از اعداد
# # numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# # # استفاده از تابع filter() برای فیلتر کردن اعداد زوج از لیست
# # even_numbers = list(filter(is_even, numbers))

# # for i  in numbers:
# #     print(is_even(i))



# # def get_moves(dimensions: int,player:tuple)->list:
# #     moves=['Up','Down','Left','Right']
# #     x_max,y_max=dimensions,dimensions
# #     x,y=player
# #     if x==0:
# #         move.remove('Left')
# #     if x==dimensions:
# #         move.remove('Right')
# #     if y==0:
# #         move.remove('Up')
# #     if y==dimensions:
# #         move.remove('Down')
# #     return moves


# dim=10
# loc=list()
# for i in range(0,dim):
#     for j in range(0,dim):
#         x=(i,j)
#         loc.append(x)
# print(loc)




# def makeـlocation(dimensions: int)->list:
#     places=list()
#     for x in range(0,dimensions):
#         for y in range(0,dimensions):
#             coordinates=(i,j)
#             places.append(coordinates)
#     return places
























# import random


# def get_moves(player):
#     moves = ['right', 'left', 'up', 'down']
#     x, y = player

#     if x == 0:
#         moves.remove('left')
#     if x == 3:
#         moves.remove('right')
#     if y == 0:
#         moves.remove('up')
#     if y == 3:
#         moves.remove('down')

#     return moves


# def get_locations(coordinations):
#     return random.sample(coordinations, 3)




# def move_user(dimensions: int, moves: str, x: int, y: int):
#     if moves == 'Right':
#         x += 1
#     elif moves == 'Left':
#         x -= 1
#     elif moves == 'Down':
#         y += 1
#     elif moves == 'Up':
#         y -= 1
#     return x, y



# # def say_move(dimensions: int, x: int, y: int) -> list:
# #     move1, move2, move3, move4 = 'Down', 'Right', 'Up', 'Left'
# #     max_y, max_x = dimensions, dimensions
# #     min_x, min_y = 0, 0
# #     can_move = list()
# #     if min_x < x < max_x and min_y < y < max_y:
# #         can_move.append(move1)
# #         can_move.append(move2)
# #         can_move.append(move3)
# #         can_move.append(move4)
# #     elif x == min_x:
# #         can_move.append(move2)
# #         if y == min_y:
# #             can_move.append(move1)
# #         elif y == max_y:
# #             can_move.append(move3)
# #         else:
# #             can_move.append(move1)
# #             can_move.append(move3)
# #     elif x == max_x:
# #         can_move.append(move4)
# #         if y == min_y:
# #             can_move.append(move1)
# #         elif y == max_y:
# #             can_move.append(move3)
# #         else:
# #             can_move.append(move1)
# #             can_move.append(move3)
# #     elif min_x < x < max_x:
# #         can_move.append(move4)
# #         can_move.append(move2)
# #         if y == min_y:
# #             can_move.append(move1)
# #         elif y == max_y:
# #             can_move.append(move3)
# #     return can_move



# import random


# def makeـlocation(dimensions: int) -> list:
#     places = list()
#     for x in range(0, dimensions):
#         for y in range(0, dimensions):
#             coordinates = (x, y)
#             places.append(coordinates)
#     return places


# def get_locations(coordinations, Numberـlocations: int):
#     return random.sample(coordinations, Numberـlocations)


# def delit_arond_derago(locat: list, detloc: tuple) -> list:
#     x, y = detloc
#     for i in range(x-1, x+2):
#         for j in range(y-1, y+2):
#             not_ok_lac = (i, j)
#             if not_ok_lac not in locat:
#                 continue
#             locat.remove(not_ok_lac)
#     return locat

# def locations_game(dimensions: int)->list:
#     map_cell = makeـlocation(dimensions)
#     derago_locations = get_locations(map_cell, 1)
#     derago_locations = derago_locations[0]
#     new_map_cell = delit_arond_derago(map_cell, derago_locations)
#     user, door, hint = get_locations(new_map_cell, 3)
#     return [derago_locations, user, door, hint]

# print(locations_game(10))

# def move_player(player:tuple, move:str):
#     x, y = player
#     if move == 'up':
#         y -= 1
#     if move == 'down':
#         y += 1
#     if move == 'left':
#         x -= 1
#     if move == 'right':
#         x += 1

#     return x, y


# print(move_player((1,0),'up'))