from colorama import Fore
import tkinter

root = tkinter.Tk()
root.title('x   o')

root.geometry('927x800')

player_turn = "X"
player_trn = 0


def b1_config():
    b1.config(text=player_turn)
    board[1][1] = player_turn

def b2_config():
    b2.config(text=player_turn)
    board[1][2] = player_turn


def b3_config():
    b3.config(text=player_turn)
    board[1][3] = player_turn


def b4_config():
    b4.config(text=player_turn)
    board[2][1] = player_turn


def b5_config():
    b5.config(text=player_turn)
    board[2][2] = player_turn


def b6_config():
    b6.config(text=player_turn)
    board[2][3] = player_turn


def b7_config():
    b7.config(text=player_turn)
    board[3][1] = player_turn


def b8_config():
    b8.config(text=player_turn)
    board[3][2] = player_turn


def b9_config():
    b9.config(text=player_turn)
    board[3][3] = player_turn


def b_quit():
    root.quit()


def cyan_text(text):
    print(Fore.CYAN + text + Fore.RESET)


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

label = tkinter.Label(text=player_turn)
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

start_game = input("Do you want to start the game?  (Y/N) ").capitalize()
if start_game == "Y":
    root.mainloop()
elif start_game == "N":
    cyan_text("Goodbye, see you next time")

# hello world
print(board)