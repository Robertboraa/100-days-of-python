import requests
import os
from datetime import datetime
APP_ID = os.environ.get("APP_ID")
API_KEY = os.environ.get("API_KEY")
gender = "male"
age = 24
height_cm = 182
weight_kg = 82
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")


url = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SHEETY_ENDPOINT ="https://api.sheety.co/79ffe777222f49155f59efa1b9af62f0/myWorkouts/workouts"
headers = {
    "Content-Type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

data = {
    "query": input("What is your exercise and time ?"),
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

response = requests.post(url, headers=headers, json=data)
result = response.json()
now = datetime.now()
today_date = now.strftime("%d/%m/%Y")
now_time = now.strftime("%H:%M:%S")


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(SHEETY_ENDPOINT,json=sheet_inputs,auth=(USERNAME, PASSWORD, ))
    print(sheet_response.text)
