import os
import requests
from datetime import datetime


APP_ID = os.getenv('NUTRITIONIX_APP_ID')
API_KEY = os.getenv('NUTRITIONIX_API_KEY')

SHEETY_API_KEY = os.getenv("Sheety_OpenWeaher_Pixela_Api_key")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

user_activity = input("Tell me which exercise you did? ")
# Also, we are able to add personal data like weight or etc.
user_exercise = {
    "query": user_activity
}

activity_response = requests.post(url=exercise_endpoint, json=user_exercise, headers=headers)
activity_data = activity_response.json()

exercise = activity_data["exercises"][0]["name"]
duration = activity_data["exercises"][0]["duration_min"]
calories = activity_data["exercises"][0]["nf_calories"]
date = datetime.today()
formatted_date = date.strftime("%d/%m/%Y")
formatted_time = date.strftime("%H:%M:%S")


# Working with sheety API

sheety_get_url = "https://api.sheety.co/a940521a9c0db98308464dc264e57b1c/myWorkouts/workouts"

# sheety_get_response = requests.get(url=sheety_get_url)
#
# print(sheety_get_response.json())

sheety_post_url = "https://api.sheety.co/a940521a9c0db98308464dc264e57b1c/myWorkouts/workouts"

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_API_KEY}"
}

post_params = {
    "workout": {
        "date": formatted_date,
        "exercise": exercise.title(),
        "time": formatted_time,
        "duration": duration,
        "calories": calories
    }
}

sheety_put_response = requests.post(url=sheety_post_url, json=post_params, headers=sheety_headers)
print(sheety_put_response.text)

