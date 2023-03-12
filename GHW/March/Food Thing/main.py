Food = {
    "pork": ["bad", "600", "4.56", "mushrooms"],
    "mushrooms": ["good", "300", "0.21"],
    "lamb": ["bad", "400", "9.80", "chickpeas"],
    "chickpeas": ["good", "400", "0.32"],
    "rice": ["bad", "600", "1.02", "cauliflower"],
    "cauliflower": ["good", "6.00", "0.66"],
    "ground beef": ["bad", "4.00", "5.88", "black beans"],
    "black beans": ["good", "400", "0.32"],
    "bacon": ["bad", "400", "2.32", "eggplant"],
    "eggplant": ["good", "400", "0.44"],
    "chicken": ["bad", "300", "1.29", "tempeh"],
    "tempeh": ["good", "200", "0.4"],
    "tuna": ["bad", "300", "1.14", "tomato"],
    "tomato": ["good", "300", "0.60"],
}

from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from math import floor
screen = Tk()
screen.config(padx = 50, pady = 50, bg = "#DAE2B6")

ListOfBad = ["pork", "mushrooms", "lamb", "chickpeas",  "rice", "cauliflower",  "ground beef", "black beans",  "bacon", "eggplant", "chicken", "tempeh",  "Tuna", "tomato"]
ListOfBad1 = ["pork", "lamb", "rice",  "ground beef",  "bacon",  "chicken",  "Tuna"]

def getbetter():
    protein = EnterBadProtein.get()
    amount = EnterBadAmount.get()
    try:
        check = amount / 100
    except TypeError:
        messagebox.showinfo(title="Error", message="Enter A Number ")
    except AttributeError:
        messagebox.showinfo(title="Error", message="Enter A Protein ")
    for i in range(7):
        if protein == ListOfBad[i]:
            bad = ListOfBad[i]
            bad1 = ListOfBad[i+1]
            new = Food[bad][3]
            badamount = Food[bad][2]
            newamount = Food[bad][2]


            BetterProtein.config(text = f"Better : {new}", fg = "Green")
            BetterAmount.config(text = f"Amount : {newamount}Oz", fg = "Green")
            Before.config(text = f"Co2 Emissions (Ibs Per Oz) : {badamount}", fg = "Green")
            After.config(text = f"Co2 Emissions (Ibs Per Oz) : {newamount}", fg = "Green")
            BadProtein.config(text = f"Bad : {bad}", fg = "Red")
            BadAmount.config(text = f"Amount : {amount}", fg = "Red")


screen.title("Better Carbon Meal")

title = Label( text = "Menu Helper", font=("Ariel", 25, "bold"), bg = "#DAE2B6", padx = 8, pady = 12)
title.grid(row = 0, column = 1)
EnterBadProtein = ttk.Combobox(screen, values=ListOfBad1, state= "readonly")
EnterBadProtein.grid(column=0, row = 1)
EnterBadAmount = Entry(width = 15)
EnterBadAmount.grid(row = 1, column = 1)
EnterAmount = Button()
EnterAmount.config(width = 15, height = 1, text = "Enter Amount(oz)", command=getbetter)
EnterAmount.grid(row = 1, column = 2)

BetterProtein = Label(text = "", font=("Ariel", 15, "bold"), bg = "#DAE2B6", padx = 5, pady = 5)
BetterProtein.grid(column=0, row=4)
BetterAmount = Label(text = "", font=("Ariel", 15, "bold"), bg = "#DAE2B6", padx = 5, pady = 5)
BetterAmount.grid(column=1, row=4)
BadProtein = Label(text = "", font=("Ariel", 15, "bold"), bg = "#DAE2B6", padx = 5, pady = 5)
BadProtein.grid(column=0, row=3)
BadAmount = Label(text = "", font=("Ariel", 15, "bold"), bg = "#DAE2B6", padx = 5, pady = 5)
BadAmount.grid(column=1, row=3)
Before = Label(text = "", font=("Ariel", 15, "bold"), bg = "#DAE2B6", padx = 5, pady = 5)
Before.grid(column=2, row=3)
After = Label(text = "", font=("Ariel", 15, "bold"), bg = "#DAE2B6", padx = 5, pady = 5)
After.grid(column=2, row=4)
screen.mainloop()