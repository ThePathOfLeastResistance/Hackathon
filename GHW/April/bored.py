import requests

price = int(input("On a Scale of 1 to 5, how much money are you willing to spend: "))/10
Num = int(input("How Many People do you want to do this activity with?:" ))

para = {
    "participants": Num,
    "price" : price
}


url = "http://www.boredapi.com/api/activity?"
response = requests.get(url, params= para)
activity = response.json()["activity"]
type = response.json()["type"]
participants= response.json()["participants"]
price= response.json()["price"]

print(f"You should {activity.lower()} with {participants -1 } other people, which would cost around {price*10} on a scale of 1 to 5")
