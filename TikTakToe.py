from tkinter import *
from tkinter import messagebox 


positions = []
buttons = []
for i in range(9):
    positions.append("-")
    buttons.append(Button)

size = 100
board = Tk()
board.title("TicTacToe")
board.geometry("340x340")
board["bg"] = "green"
turn = ["x"]


def check():
    row_1 = positions[0] == positions[1] == positions[2] != "-"
    row_2 = positions[3] == positions[4] == positions[5] != "-"
    row_3 = positions[6] == positions[7] == positions[8] != "-"
    column_1 = positions[0] == positions[3] == positions[6] != "-"
    column_2 = positions[1] == positions[4] == positions[7] != "-"
    column_3 = positions[2] == positions[5] == positions[8] != "-"
    diogonal_1 = positions[0] == positions[4] == positions[8] != "-"
    diogonal_2 = positions[2] == positions[4] == positions[6] != "-"

    if row_1 or row_2 or row_3 or column_1 or column_2 or column_3 or diogonal_1 or diogonal_2:
        if turn[-1] == "X":
            messagebox.showinfo("showinfo", "X win")
        else:
            messagebox.showinfo("showinfo", "O win")
        return True
    else:
        return False




def change(i):
    if positions[i] == "-":
        if turn[-1] == "O":
            positions[i] = "X"
            turn.append("X")
        else:
            positions[i] = "O"
            turn.append("O")
    

    
        buttons[i].config(text = positions[i])
        if check():
            for i in range(9):
                positions[i] = ("-")
                buttons[i].config(text = positions[i])
    else:
        messagebox.askretrycancel("info", "It is already choosen. Please choose another one.")   


        


buttons[0] = Button(text = positions[0], font=('Helvetica', '70'), command=lambda: change(0))
buttons[0].place(x = 10, y = 10, width = size, height = size)

buttons[1] = Button(text = positions[1], font=('Helvetica', '70'), command=lambda: change(1))
buttons[1].place(x = 120, y = 10, width = size, height = size)

buttons[2] = Button(text = positions[2], font=('Helvetica', '70'), command=lambda: change(2))
buttons[2].place(x = 230, y = 10, width = size, height = size)
    
buttons[3] = Button(text = positions[3], font=('Helvetica', '70'), command=lambda: change(3))
buttons[3].place(x = 10, y = 120, width = size, height = size)
    
buttons[4] = Button(text = positions[4], font=('Helvetica', '70'), command=lambda: change(4))
buttons[4].place(x = 120, y = 120, width = size, height = size)
    
buttons[5] = Button(text = positions[5], font=('Helvetica', '70'), command=lambda: change(5))
buttons[5].place(x = 230, y = 120, width = size, height = size)
    
buttons[6] = Button(text = positions[6], font=('Helvetica', '70'), command=lambda: change(6))
buttons[6].place(x = 10, y = 230, width = size, height = size)
    
buttons[7] = Button(text = positions[7], font=('Helvetica', '70'), command=lambda: change(7))
buttons[7].place(x = 120, y = 230, width = size, height = size)
    
buttons[8] = Button(text = positions[8], font=('Helvetica', '70'), command=lambda: change(8))
buttons[8].place(x = 230, y = 230, width = size, height = size)
board.mainloop()