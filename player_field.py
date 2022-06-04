# Создание игрового поля и вывод

def field():
    a = [['.', '.', ' '],
         [' ', '.', '.'],
         ['.', ' ', ' ']]
    return a

def print_field(field):
    for i in range(len(field)):
        for j in range(len(field[i])):
            print(field[i][j], ' ', end='', sep="|")
        print()