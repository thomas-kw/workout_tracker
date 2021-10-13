import requests

APP_ID = "f457de60"
API_KEY = "d8ca4caad74c8306f867d7fbd21caa4c"

nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

query = {
    "query":"ran 20 miles",
    "gender":"male",
    "weight_kg":"50",
}

response = requests.post(url=nutritionix_endpoint, json=query, headers=headers)

print(response.text)
