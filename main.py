from myclass import Ship
from random import randrange
# import time


def field_print(_field):
    print(' ', end=' ')
    for i_ in range(0, len(_field[0])):  # range(1, len(_field[0]) + 1)
        print(i_, end=' ')
    print('\n', end='')
    for ny, y in enumerate(range(len(_field))):
        print(ny, end=' ')  # ny + 1
        for x in range(len(_field[y])):
            print(_field[y][x], end=' ')
        print('\n', end='')
    return ''


def ship_place_rnd(_ship, _field):
    check = 0
    while check == 0:
        check = 1
        _ship.y = randrange(6)
        y_start_check = _ship.y - 1
        if y_start_check < 0:
            y_start_check = 0
        y_end_check = _ship.y + 1
        if y_end_check > 5:
            y_end_check = 5
        _ship.x = randrange(6)
        if _ship.x + _ship.size > 6:
            _ship.x = _ship.x - (_ship.x + _ship.size - 6)
        x_start_check = _ship.x - 1
        if x_start_check < 0:
            x_start_check = 0
        x_end_check = _ship.x + _ship.size
        if x_end_check > 5:
            x_end_check = 5
        for y in range(y_start_check, y_end_check + 1):
            for x in range(x_start_check, x_end_check + 1):
                if _field[y][x] != '0':  # and _field[y][x] != '*':
                    check = 0
                # else:
                #    _field[y][x] = '*'
        if check == 1:
            for i in range(_ship.size):
                _field[_ship.y][_ship.x + i] = _ship.name
    return True


# army player
p_ship3_1 = Ship(0, 1, 3, 1)  # three-deck ship
p_ship2_1 = Ship(1, 1, 2, 2)  # two-deck ship
p_ship2_2 = Ship(2, 1, 2, 3)  # two-deck ship
p_ship1_1 = Ship(3, 1, 1, 4)  # one-deck ship
p_ship1_2 = Ship(4, 1, 1, 5)  # one-deck ship
p_ship1_3 = Ship(5, 1, 1, 6)  # one-deck ship
p_ship1_4 = Ship(5, 3, 1, 7)  # one-deck ship
ships_player = [p_ship3_1, p_ship2_1, p_ship2_2, p_ship1_1, p_ship1_2, p_ship1_3, p_ship1_4]
# army computer
c_ship3_1 = Ship(0, 0, 3, 1)  # three-deck ship
c_ship2_1 = Ship(1, 0, 2, 2)  # two-deck ship
c_ship2_2 = Ship(2, 0, 2, 3)  # two-deck ship
c_ship1_1 = Ship(3, 0, 1, 4)  # one-deck ship
c_ship1_2 = Ship(4, 0, 1, 5)  # one-deck ship
c_ship1_3 = Ship(5, 0, 1, 6)  # one-deck ship
c_ship1_4 = Ship(5, 2, 1, 7)  # one-deck ship
ships_computer = [c_ship3_1, c_ship2_1, c_ship2_2, c_ship1_1, c_ship1_2, c_ship1_3, c_ship1_4]

field_player = [['0' for x in range(6)] for y in range(6)]
field_computer = [['0' for x1 in range(6)] for y1 in range(6)]

for ship in ships_player:
    ship_place_rnd(ship, field_player)
# ship_place_rnd(p_ship2_1, field_player)
# ship_place(p_ship2_1, field_player)
# print('computer:')
print(field_print(field_player))
print(p_ship2_1)
# print('player:')
# print(fild_print(field_player), end='')
