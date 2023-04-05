

import requests
import datetime

date_time = datetime.date.today()
Now = date_time.strftime("%Y-%m-%d")
yesterday = (date_time - datetime.timedelta(days = 1)).strftime("%Y-%m-%d")


Api = "VEzlsihQxrQZwLNhtV5tRSrAcMT9uhnq4DweCRrs"
Endpoint = f"https://api.nasa.gov/neo/rest/v1/feed?start_date={Now}&end_date={yesterday}&api_key={Api}"


response = requests.get(Endpoint)
response.raise_for_status()

Date = date_time.strftime("%Y-%m-%d")
list = response.json()["near_earth_objects"][Now]

num = 0
Bad = 0

for i in list:
    num += 1
    if i["is_potentially_hazardous_asteroid"] == "True":
        Bad += 1

print(f"Hello, today there was {num} number of asteroids that was close to earth and {Bad} of them where potentially hazardous ")