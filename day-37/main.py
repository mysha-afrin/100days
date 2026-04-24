import requests
token = "asfdjhriwndnwkdn"
username = 'ultamurgi'
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token" : token,
    "username" : username,
    "agreeTermsOfService" : "yes",
    "notMinor" : "yes"
}
#response = requests.post(url = pixela_endpoint, json=user_params)
#print(response.text)
graph_endpoint = f"{pixela_endpoint}/{username}/graphs"

graph_config = {
    'id' : 'graph1',
    'name' : 'Exercise Graph',
    'unit' : 'minutes',
    'type' : 'int',
    'color' : 'kuro'
}

headers = {
    "X-USER-TOKEN" : token
}


#response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
#print(response.text)


#response = requests.get(url = graph_endpoint, headers = headers)
#print(response.text)


pixel_creation_endpoint = f"{pixela_endpoint}/{username}/graphs/graph1"

pixela_data = {
    "date" : "20240630",
    "quantity" : "30"
}

response = requests.post(url = pixel_creation_endpoint, json = pixela_data, headers = headers)
print(response.text)