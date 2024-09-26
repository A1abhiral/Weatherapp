import json

import requests
while True:
    city = input("enter the name of the city")
    if city == "exit":
        print("thankyou for using")
        break
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=""
    r = requests.get(url)
    dic = json.loads(r.text)
    print(f"the weather of {city} is: {dic["main"]["temp"]}")

