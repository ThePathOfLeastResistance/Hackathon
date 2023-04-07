import requests
import tkinter

key = "r2VLdba2YONbzKrN1MYCZg==ePB1negMs1IvtFGY"

endpoint = "https://api.api-ninjas.com/v1/quotes"
param = {
    "category":"courage",

}

apicheck = {
    "X-Api-Key":key
}

def change():
    info = get_quote()
    author = info[0]['author']
    quote_lab.config(text=info[0]['quote'])
    person.config(text=f"-{author}")

def get_quote():
    response = requests.get(endpoint, params= param, headers=apicheck)
    quote = response.json()
    return quote

window = tkinter.Tk()

info = get_quote()
author = info[0]['author']

get = tkinter.Button(text = "Get New Quote", bg="yellow", width=10, command= change, padx=10)
get.grid(column = 3, row =0)
quote_lab = tkinter.Label(text = info[0]['quote'])
quote_lab.grid(column=0, row = 0, rowspan=4)
person = tkinter.Label(text = f"-{author}")
person.grid(column=2, row = 0, rowspan=2)

window.mainloop()
