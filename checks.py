# проверка на победу, проверки на корректность ввода, проверка на уже занятое место.

def victory(a):
    if a[0][0] == a[0][1] == a[0][2] or\
            a[1][0] == a[1][1] == a[1][2] or \
            a[2][0] == a[2][1] == a[2][2] or \
            a[0][0] == a[1][1] == a[2][2] or \
            a[2][0] == a[1][1] == a[0][2] or \
            a[0][0] == a[1][0] == a[2][0] or \
            a[0][1] == a[1][1] == a[2][1] or \
            a[0][2] == a[1][2] == a[2][2]:
        return True
    else:
        return False

def isdigit(value_1, value_2):
    try:
        int(value_1), int(value_2)
        return True
    except ValueError:
        return False

def moves(player, player1):
    while True:
        player = input('Введите координату строки: \n')
        player1 = input('Введите координату столбца: \n')
        if isdigit(player, player1):
            b = int(player)
            c = int(player1)
            if b > 2 or c > 2 or b < 0 or c < 0:
                print('Вы ввели несуществующую координату, повторите попытку!')
            else:
                return b, c
                break
        else:
            print('Некорректный ввод. Повторите')

def occupied(a,player, player1):

    while (a[player][player1] == '0') or (a[player][player1] == 'X'):
        print('Упс место занято, повторите ввод координаты!')
        f, g = moves(player, player1)
        if a[player][player1] != '0' or a[player][player1] != 'X':
            return f, g
            break
    f, g = player, player1
    return f, g