import os

import requests
import json

import requests as requests



apikey = os.environ["api"]
ckey = "my_test_app"


search_term = input("what do you want the gif to be about? : ")
lmt = int(input(f"How Many Gifs that show {search_term} : "))


r = requests.get(
    "https://tenor.googleapis.com/v2/search?q=%s&key=%s&client_key=%s&limit=2%s" % (search_term, apikey, ckey,  lmt))

if r.status_code == 200:

    gifs = r.json()
    x = 0
    for i in range(0,lmt):
        link = gifs["results"][x]["media_formats"]
        url = link.values()
        x += 1
        print(list(url)[0]["url"])
else:
    gifs = None


