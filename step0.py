import random

def move(dimensions: int, move: str, x: int, y: int):
    if move == 'Right':
        x += 1
    elif move == 'Left':
        x -= 1
    elif move == 'Down':
        y += 1
    elif move == 'Up':
        y -= 1
    return x, y


def moveـcontrol(dimensions: int, x: int, y: int) -> int:
    max_y, max_x = dimensions, dimensions
    min_x, min_y = 0, 0
    if x > max_x:
        x -= 1
    elif x < min_x:
        x += 1
    elif y > max_y:
        y -= 1
    elif y < min_y:
        y += 1

    return x, y


def say_move(dimensions: int, x: int, y: int) -> list:
    move1, move2, move3, move4 = 'Down', 'Right', 'Up', 'Left'
    max_y, max_x = dimensions, dimensions
    min_x, min_y = 0, 0
    can_move = list()
    if min_x < x < max_x and min_y < y < max_y:
        can_move.append(move1)
        can_move.append(move2)
        can_move.append(move3)
        can_move.append(move4)
    elif x == min_x:
        can_move.append(move2)
        if y == min_y:
            can_move.append(move1)
        elif y == max_y:
            can_move.append(move3)
        else:
            can_move.append(move1)
            can_move.append(move3)
    elif x == max_x:
        can_move.append(move4)
        if y == min_y:
            can_move.append(move1)
        elif y == max_y:
            can_move.append(move3)
        else:
            can_move.append(move1)
            can_move.append(move3)
    elif min_x < x < max_x:
        can_move.append(move4)
        can_move.append(move2)
        if y == min_y:
            can_move.append(move1)
        elif y == max_y:
            can_move.append(move3)
    return can_move


def art(dimensions: int, x: int, y: int):
    print(' _'*dimensions, end='\n')
    for j in range(0, dimensions):
        if j == y:
            for i in range(0, dimensions):
                if i == x:
                    print('|*', end='')
                else:
                    print('|_', end='')
            print('|')
        else:
            print('|_'*dimensions, end="|\n")


def locationـrandom(dimensions: int) -> int:
    
    y_list = list()
    x_list = list()
    for i in range(0, dimensions):
        x_list.append(i)
        y_list.append(i)
    x_D = random.choice(x_list)
    y_D = random.choice(y_list)
    x_list.remove(x_D)
    y_list.remove(y_D)
    x_H = random.choice(x_list)
    y_H = random.choice(y_list)
    x_list.remove(x_H)
    y_list.remove(y_H)
    x_P = random.choice(x_list)
    y_p = random.choice(y_list)
    return x_D, y_D, x_H, y_H, x_P, y_p


def Matchـlocation(x_user: int, y_user: int, x_place: int, y_place: int) -> bool:  # noqa
    flage = False
    if x_user == x_place and y_user == y_place:
        flage = True
    return flage


def help(x, y):
    help = f'''At the beginning of history,
    if you move forward {x} years and climb {y} steps on the ladder of destiny
    , you will go to the other side of history.'''
    print(help)


def clera():
    import os
    return os.system('cls')











dimensions = int(input())
x_D, y_D, x_H, y_H, x_P, y_P = locationـrandom(dimensions)
x_U, y_U = 0, 0
while True:
    art(dimensions, x_U, y_U)
    print(f'derago :{(x_D, y_D)}')
    print(f'hole :{x_H, y_H}')
    print(f'help :{x_P, y_P}')
    print(x_U, y_U)
    print(say_move(dimensions, x_U, y_U))
    x_U, y_U = move(dimensions, input().capitalize(), x_U, y_U)
    x_U, y_U = moveـcontrol(dimensions, x_U, y_U)
    art(dimensions, x_U, y_U)
    if Matchـlocation(x_U, y_U, x_H, y_H):
        Gameـstatus = 'win'
        break
    elif Matchـlocation(x_U, y_U, x_D, y_D):
        Gameـstatus = 'lose'
        break
    elif Matchـlocation(x_U, y_U, x_P, y_P):
        help(x_H, y_H)
    else:
        Gameـstatus = None

    print(x_U, y_U)
    clera()
print(f'You are {Gameـstatus}')