import player_field as pf
import checks as ch
import tkinter as tk

def fill_field():
    a = pf.field()
    for i in range(5):
        if i == 4:
            print('Ход 1-го игрока!')
            player_1, player_11 = 0, 0
            player_1, player_11 = ch.moves(player_1, player_11)
            player_1, player_11 = ch.occupied(a, player_1, player_11)
            a[player_1][player_11] = '0'
            pf.print_field(a)
            if ch.victory(a) == True:
                print('Ура победил 1-ый игрок!')
                break
            else:
                print('Ничья!')
                break
        print('Ход 1-го игрока!')
        player_1, player_11 = 0, 0
        player_1, player_11 = ch.moves(player_1, player_11)
        player_1, player_11 = ch.occupied(a, player_1, player_11)
        a[player_1][player_11] = '0'
        pf.print_field(a)
        if ch.victory(a) == True:
            print('Ура победил 1-ый игрок!')
            break

        print('Ход 2-го игрока!')
        player_2, player_22 = 0, 0
        player_2, player_22 = ch.moves(player_2, player_22)
        player_2, player_22 = ch.occupied(a, player_2, player_22)
        a[player_2][player_22] = 'X'
        pf.print_field(a)
        if ch.victory(a) == True:
            print('Ура победил 2-ой игрок!')
            break
    return a

a = fill_field()
pf.print_field(a)

window = tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=1, minsize=75)
    window.rowconfigure(i, weight=1, minsize=50)

    for j in range(0, 3):
        frame = tk.Frame(
            master=window,
            relief=tk.RAISED,
            borderwidth=1
        )
        frame.grid(row=i, column=j, padx=5, pady=5)

        label = tk.Label(master=frame, text=a[i][j])
        label.pack(padx=5, pady=5)

window.mainloop()

