import time

from colorama import Fore
import tkinter

root = tkinter.Tk()
root.title('x   o')

root.geometry('927x800')

player_turn = 'X'


def change_turn():
    global player_turn

    if player_turn == 'X':
        player_turn = '0'
    elif player_turn == '0':
        player_turn = 'X'
    show_turn(player_turn)


def b1_config():
    b1.config(text=player_turn)
    board[0][0] = player_turn
    change_turn()
    check_win(board)


def b2_config():
    b2.config(text=player_turn)
    board[0][1] = player_turn
    change_turn()
    check_win(board)


def b3_config():
    b3.config(text=player_turn)
    board[0][2] = player_turn
    change_turn()
    check_win(board)


def b4_config():
    b4.config(text=player_turn)
    board[1][0] = player_turn
    change_turn()
    check_win(board)


def b5_config():
    b5.config(text=player_turn)
    board[1][1] = player_turn
    change_turn()
    check_win(board)


def b6_config():
    b6.config(text=player_turn)
    board[1][2] = player_turn
    change_turn()
    check_win(board)


def b7_config():
    b7.config(text=player_turn)
    board[2][0] = player_turn
    change_turn()
    check_win(board)


def b8_config():
    b8.config(text=player_turn)
    board[2][1] = player_turn
    change_turn()
    check_win(board)


def b9_config():
    b9.config(text=player_turn)
    board[2][2] = player_turn
    change_turn()
    check_win(board)


def b_quit():
    root.quit()


def cyan_text(text):
    print(Fore.CYAN + text + Fore.RESET)


def show_turn(player_turn):
    label.config(text=player_turn)


def check_win(board):
    for i in range(3):
        'strochki'
        if board[i][0] == board[i][1] == board[i][2] and board[i][0] != '':
            show_winner(board[i][0])

        'stolbiki'
        if board[0][i] == board[1][i] == board[2][i] and board[0][i] != '':
            show_winner(board[0][i])

    'diagonal'
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != '':
        show_winner(board[0][0])

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != '':
        show_winner(board[0][2])





def show_winner(winner):
    text = f'{winner} won'
    label.config(text=text)
    time.sleep(15)
    root.quit()


board = [
    ['', '', ''],
    ['', '', ''],
    ['', '', ''],
]

b1 = tkinter.Button(root, text="", padx=100, pady=100, command=b1_config, font="helvetica 14", foreground="#004D40",
                    background="#B2DFDB")
b2 = tkinter.Button(root, text="", padx=100, pady=100, command=b2_config, font="helvetica 14", foreground="#004D40",
                    background="#B2DFDB")
b3 = tkinter.Button(root, text="", padx=100, pady=100, command=b3_config, font="helvetica 14", foreground="#004D40",
                    background="#B2DFDB")
b4 = tkinter.Button(root, text="", padx=100, pady=100, command=b4_config, font="helvetica 14", foreground="#004D40",
                    background="#B2DFDB")
b5 = tkinter.Button(root, text="", padx=100, pady=100, command=b5_config, font="helvetica 14", foreground="#004D40",
                    background="#B2DFDB")
b6 = tkinter.Button(root, text="", padx=100, pady=100, command=b6_config, font="helvetica 14", foreground="#004D40",
                    background="#B2DFDB")
b7 = tkinter.Button(root, text="", padx=100, pady=100, command=b7_config, font="helvetica 14", foreground="#004D40",
                    background="#B2DFDB")
b8 = tkinter.Button(root, text="", padx=100, pady=100, command=b8_config, font="helvetica 14", foreground="#004D40",
                    background="#B2DFDB")
b9 = tkinter.Button(root, text="", padx=100, pady=100, command=b9_config, font="helvetica 14", foreground="#004D40",
                    background="#B2DFDB", )
b10 = tkinter.Button(root, text="Quit!", padx=100, pady=100, command=b_quit, font="helvetica 14",
                     foreground="#004D40", background="#B2DFDB", )

label = tkinter.Label(text=player_turn, foreground="#004D40",
                      background="#B2DFDB")
label.grid(row=2, column=4)

b1.grid(row=1, column=0)
b2.grid(row=1, column=1)
b3.grid(row=1, column=2)
b4.grid(row=2, column=0)
b5.grid(row=2, column=1)
b6.grid(row=2, column=2)
b7.grid(row=3, column=0)
b8.grid(row=3, column=1)
b9.grid(row=3, column=2)
b10.grid(row=3, column=4)

label = tkinter.Label(text="")
label.grid(row=2, column=4)

cyan_text("Do you want to start the game?  (Y/N) ")
start_game = input().capitalize()
if start_game == "Y":
    root.mainloop()
elif start_game == "N":
    cyan_text("Goodbye, see you next time")

print(board)
