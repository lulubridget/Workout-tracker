import requests, os, datetime

api_key = os.environ.get('api_key')
api_id = os.environ.get('api_id')
sheety_endpoint = os.environ.get('sheety_endpoint')
TOKEN = os.environ.get('TOKEN')


GENDER = "female"
WEIGHT_KG = 48
HEIGHT_CM = 160
AGE = 32

endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_text = input("Tell me which exercises you did: ")
headers = {
    "x-app-id": api_id,
    "x-app-key": api_key,
}
parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

resp = requests.post(url=endpoint, json=parameters, headers=headers, verify=False)
result = resp.json()


headers = {
    "Authorization": "Bearer Wshd12!"
}
today_date = datetime.datetime.now().strftime("%x")
today_time = datetime.datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_input = {
        "workout": {
            "date": today_date,
            "time": today_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    sheet_post = requests.post(url=sheety_endpoint, json=sheet_input, headers=headers, verify=False)

    print(sheet_post.text)