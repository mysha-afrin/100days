import requests

parameters = { "days" : 1,
              "hours" : 3
              }

url = f"https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/bagerhat%2Cbangladesh?unitGroup=us&key=U8G3LPY4MZKJ8NTZRWK5P8CKC&contentType=json"

response = requests.get(url, params=parameters)
response.raise_for_status()
data = response.json()
returned_data = data["days"][0]
print(returned_data['sunrise'])