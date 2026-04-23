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
    token : token
}


response = requests.post(url = graph_endpoint, json = graph_config, headers = headers)
print(response.text)