import requests

MY_LAT = 22.659060
MY_LONG = 89.807007


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    

}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()

sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]