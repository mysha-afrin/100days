import requests

url = "http://api.open-notify.org/iss-now.json"
response = requests.get(url)
response.raise_for_status()  # Check if the request was successful


print ("responseed")
data = response.json()

latitude = data["iss_position"]["latitude"]
longitude = data["iss_position"]["longitude"]

print(f"Latitude: {latitude}, Longitude: {longitude}")