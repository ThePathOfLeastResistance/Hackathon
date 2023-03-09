from tkinter import *
import pandas
import random
import time

screen = Tk()
screen.config(padx=50, pady=50, bg= "#FF9F9F")
screen.title("Education")

number = 0

def delete():
    canvas.itemconfig(prompt, text="")
    enter.delete(0,END)
    create()

def check():
    the_answer = enter.get()
    correct = math["anw"][number]
    if int(the_answer) == int(correct):
        canvas.itemconfig(prompt, text = "Correct ✅")
        screen.after(2000, func=delete)
    else:
        canvas.itemconfig(prompt, text = f"Wrong ❌\n Correct Answer : {correct}")
        canvas.create_text(400,100, text="", font=("Times New Roman", 60, "bold"))
        screen.after(2000, func=delete)


def create():
    global number
    number = random.randint(0,12)
    question = math["qus"][number]
    canvas.itemconfig(prompt, text = f'What Is {question}?')

math = pandas.read_csv("math_qus.txt")


flashcard = PhotoImage("card_front.png")
canvas = Canvas(width=800, height=526, highlightthickness= 0)
canvas.create_image(400, 263, image = flashcard)
prompt = canvas.create_text(400,100, text="", font=("Times New Roman", 60, "bold"))
canvas.grid(column = 1, row = 0, rowspan=3)

enter = Entry(width = 45, font = ("Times New Roman", 20, "bold"), highlightthickness= 1)
enter.grid(column = 1, row = 1)


check = Button(text = "Done ✅", bg = "Green", highlightthickness=0, command=check)
check.config(height=5, width=50)
check.grid(column = 1, row = 2)

create()





screen.mainloop()