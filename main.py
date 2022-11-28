from myclass import Ship
from random import randrange


def field_print(field_):
    print(' ', end=' ')
    for i_ in range(0, len(field_[0])):  # range(1, len(_field[0]) + 1)
        print(i_, end=' ')
    print('\n', end='')
    for ny_, y_ in enumerate(range(len(field_))):
        print(ny_, end=' ')  # ny_ + 1
        for x_ in range(len(field_[y_])):
            print(field_[y_][x_], end=' ')
        print('\n', end='')
    return ''


def field_clear(field_):
    for y_ in range(len(field_)):
        for x_ in range(len(field_[y_])):
            field_[y_][x_] = '0'
    return ''


def ships_place_rnd(ships_, field_):
    check1_ = 0
    while check1_ == 0:
        check1_ = 1
        for ship_ in ships_:
            check2_, n_ = 0, 0
            while check2_ == 0:
                n_ += 1
                check2_ = 1
                ship_.y = randrange(6)
                y_start_check = ship_.y - 1
                if y_start_check < 0:
                    y_start_check = 0
                y_end_check = ship_.y + 1
                if y_end_check > 5:
                    y_end_check = 5
                ship_.x = randrange(6)
                if ship_.x + ship_.size > 6:
                    ship_.x = ship_.x - (ship_.x + ship_.size - 6)
                x_start_check = ship_.x - 1
                if x_start_check < 0:
                    x_start_check = 0
                x_end_check = ship_.x + ship_.size
                if x_end_check > 5:
                    x_end_check = 5
                for y in range(y_start_check, y_end_check + 1):
                    for x in range(x_start_check, x_end_check + 1):
                        if field_[y][x] != '0':  # and field_[y][x] != '*':
                            check2_ = 0
                        # else:
                        #    field_[y][x] = '*'
                if check2_ == 1:
                    for i in range(ship_.size):
                        field_[ship_.y][ship_.x + i] = '■'  # ship_.name
                if n_ > 100:
                    check1_ = 0
                    field_clear(field_)
                    break
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

ships_place_rnd(ships_player, field_player)
print(field_print(field_player), end='')
