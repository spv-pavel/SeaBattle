from myclass import Ship


def print_data(data_):
    print(' ', end=' ')
    for i_ in range(1, len(data_[0]) + 1):
        print(i_, end=' ')
    print('\n', end='')
    for ny, y in enumerate(range(len(data_))):
        print(ny + 1, end=' ')
        for x in range(len(data_[y])):
            print(data_[y][x], end=' ')
        print('\n', end='')
    return ''


def place_ship(_ships, _field):
    for ship in _ships:
        for i in range(ship.size):
            _field[ship.y][ship.x + i] = '='
    return _field


# army player
p_ship3_1 = Ship(0, 0, 3)  # three-deck ship
p_ship2_1 = Ship(1, 0, 2)  # two-deck ship
p_ship2_2 = Ship(2, 0, 2)  # two-deck ship
p_ship1_1 = Ship(3, 0, 1)  # one-deck ship
p_ship1_2 = Ship(4, 0, 1)  # one-deck ship
p_ship1_3 = Ship(5, 0, 1)  # one-deck ship
p_ship1_4 = Ship(5, 3, 1)  # one-deck ship
ships_player = [p_ship3_1, p_ship2_1, p_ship2_2, p_ship1_1, p_ship2_2, p_ship1_3, p_ship1_4]
# army computer
c_ship3_1 = Ship(0, 0, 3)  # three-deck ship
c_ship2_1 = Ship(1, 0, 2)  # two-deck ship
c_ship2_2 = Ship(2, 0, 2)  # two-deck ship
c_ship1_1 = Ship(3, 0, 1)  # one-deck ship
c_ship1_2 = Ship(4, 0, 1)  # one-deck ship
c_ship1_3 = Ship(5, 0, 1)  # one-deck ship
c_ship1_4 = Ship(5, 3, 1)  # one-deck ship
ships_computer = [c_ship3_1, c_ship2_1, c_ship2_2, c_ship1_1, c_ship2_2, c_ship1_3, c_ship1_4]

field_player = [['O' for x in range(6)] for y in range(6)]
field_computer = [['O' for x in range(6)] for y in range(6)]

field_player = place_ship(ships_player, field_player)
# print(list(enumerate(data)))
# print('computer:')
# print(print_data(field_computer))
print('player:')
print(print_data(field_player), end='')

