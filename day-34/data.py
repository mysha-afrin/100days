import requests

url = "https://opentdb.com/api.php"
parameters = {"amount": 10,
              
              "type":"boolean"}


def fetch_questions():
    response = requests.get(url, params = parameters)
    response.raise_for_status()
    data = response.json()
    return data["results"]

question_data = fetch_questions()


