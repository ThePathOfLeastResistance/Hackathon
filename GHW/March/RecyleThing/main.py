from tkinter import *
import random
from tkinter import messagebox

list = ["🍉","🥭","🍎","🍓","🍄","🥞","🍔"]


def spin():
    global one
    global two
    global three
    one = random.choice(list)
    two = random.choice(list)
    three = random.choice(list)
    canvas.itemconfig(num1, text = one)
    canvas.itemconfig(num2,text = two)
    canvas.itemconfig(num3,text = three)
    check()

def check():

    if one == two == three:
        messagebox.showinfo(title= "JackPot!!!", message = "Redeem 5 Cents At The Front")
    else:
        messagebox.showinfo(title= "Try Again Later", message = "Thanks For Saving the Planet")

screen = Tk()
screen.config(padx = 50, pady = 50, bg = "#B4E4FF")

img = PhotoImage(file = "img.png")

canvas = Canvas(width=400, height=200, highlightthickness=0)

imgon = canvas.create_image(200, 100, image = img)
canvas.config(bg = "#DFFFD8")
canvas.grid(row=1, column=1)

insert_pla = Button(text = "Insert Trash \n Below To Play", bg = "#F7C8E0", command= spin)
insert_pla.grid(column=0, row = 2)

num1 = canvas.create_text(135, 86, text = "", font=("Ariel", 25, "bold"))
num2 = canvas.create_text(200, 86, text = "", font=("Ariel", 25, "bold"))
num3 = canvas.create_text(265, 86, text = "", font=("Ariel", 25, "bold"))

screen.mainloop()

