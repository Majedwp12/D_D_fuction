from funcs import *
Gameـstatus = None
dimensions = int(input())
deragon, user, door, hint = locations_game(dimensions)

while True:
        writeـmap(dimensions, user)
        print(f'derago :{deragon}')
        print(f'Door :{door}')
        print(f'help :{hint}')
        valid_moves = get_moves(dimensions, user)
        print(f"your are in room {user}")
        print(f"valid moves are: {valid_moves}")
        move = input("please enter your move: ").capitalize()
        if move in valid_moves:
            user = move_player(user, move)
        writeـmap(dimensions, user)
        if checkـmatchـlocation(user, door):
            Gameـstatus = 'win'
            break
        elif checkـmatchـlocation(user, deragon):
            Gameـstatus = 'lose'
            break
        elif checkـmatchـlocation(user, hint):
            help(door)
        else:
            Gameـstatus = None

        print(user)
        clera()
print(f'You are {Gameـstatus}')
