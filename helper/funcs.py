import random
import logging
from colorama import Fore
import logging
logging.basicConfig(filename='app.log',
                    filemode='w',
                    level=logging.DEBUG,
                    format='%(name)s - %(levelname)s - %(message)s',
                    )

logger=logging.getLogger(__name__)

def move_player(player: tuple, move: str):
    function_name=move_player.__name__
    logger.info(f'user use this function_name `{function_name}`')
    
    x, y = player
    if move == 'Up':
        y -= 1
    if move == 'Down':
        y += 1
    if move == 'Left':
        x -= 1
    if move == 'Right':
        x += 1
    return x, y


def get_moves(dimensions: int, player: tuple) -> list:
    function_name=get_moves.__name__
    logger.info(f'user use this function_name `{function_name}`')
    moves = ['Up', 'Down', 'Left', 'Right']
    
    x, y = player
    if x == 0:
        moves.remove('Left')
    if x == dimensions-1:
        moves.remove('Right')
    if y == 0:
        moves.remove('Up')
    if y == dimensions-1:
        moves.remove('Down')
    return moves


def writeـmap(dimensions: int, user: tuple):
    function_name=writeـmap.__name__
    logger.info(f'user use this function_name `{function_name}`')
    x, y = user
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


def checkـmatchـlocation(location1: tuple, location_2: tuple) -> bool:  # noqa
    function_name=checkـmatchـlocation.__name__
    logger.info(f'user use this function_name `{function_name}`')
    flage = False
    if location1 == location_2:
        flage = True
    return flage


def get_help(location: tuple):
    function_name=get_help.__name__
    logger.info(f'user use this function_name `{function_name}`')
    x, y = location
    help =Fore.RED, f'''At the beginning of history,
    if you moves forward {x} years and climb {y} steps on the ladder of destiny
    , you will go to the other side of history.'''
    print(Fore.RED,help)


def clera():
    function_name=clera.__name__
    logger.info(f'user use this function_name `{function_name}`')
    import os
    return os.system('cls')


def makeـlocation(dimensions: int) -> list:
    function_name=makeـlocation.__name__
    logger.info(f'user use this function_name `{function_name}`')
    places = list()
    for x in range(0, dimensions):
        for y in range(0, dimensions):
            coordinates = (x, y)
            places.append(coordinates)
    return places







def locations_game(dimensions: int) -> list:
    function_name=locations_game.__name__
    logger.info(f'user use this function_name `{function_name}`')
    def del_arond_derago(locat: list, detloc: tuple) -> list:
        x, y = detloc
        for i in range(x-1, x+2):
            for j in range(y-1, y+2):
                not_ok_lac = (i, j)
                if not_ok_lac not in locat:
                    continue
                locat.remove(not_ok_lac)
        return locat
    def get_locations(coordinations, Numberـlocations: int):
        return random.sample(coordinations, Numberـlocations)

    map_cell = makeـlocation(dimensions)
    derago_locations = get_locations(map_cell, 1)
    derago_locations = derago_locations[0]
    new_map_cell = del_arond_derago(map_cell, derago_locations)
    user, door, hint = get_locations(new_map_cell, 3)
    return [derago_locations, user, door, hint]
