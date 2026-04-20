import requests



url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/bagerhat%2Cbangladesh?unitGroup=us&key=U8G3LPY4MZKJ8NTZRWK5P8CKC&contentType=json"


response = requests.get(url)
data = response.json()
print(data)