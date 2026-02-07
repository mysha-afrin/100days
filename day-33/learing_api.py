import requests
import json

MY_LAT = 22.845640
MY_LONG = 89.540329


'''response = requests.get(url = "http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json() ["iss_position"]
print(data)'''


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get(url = "https://api.sunrise-sunset.org/json" , params = parameters)
response.raise_for_status()
data = response.json()
#sunrise = data["results"]["sunrise"]
#sunset = data["results"]["sunset"]
#print(sunrise)
#print(sunset)
print(data)

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
print(sunrise)
print(sunset)