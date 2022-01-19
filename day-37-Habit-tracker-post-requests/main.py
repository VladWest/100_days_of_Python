import requests
from datetime import datetime

USERNAME = "YOUR_USERNAME"
TOKEN = "YOUR_TOKEN"

GRAPH_ID = "YOUR_GRAPH_ID"

# User creation process on Pixela service
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

# Creating new graph on pixela
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": "workoutgraph",
    "name": "Workout Graph",
    "unit": "Min",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# graph_response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(graph_response.text)

# Posting a new pixel in a graph
pixel_endpoint = f"{graph_endpoint}/{GRAPH_ID}"

today = datetime.now()
# print(today.strftime("%Y%m%d"))

pixel_params = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "150"
}

# pixel_response = requests.post(url=pixel_endpoint, json=pixel_params, headers=headers)
# print(pixel_response.text)

# Updating pixel
updated_date = "20220118"
updated_pixel_endpoint = f"{pixel_endpoint}/{updated_date}"
updated_pixel_params = {
    "quantity": "90"
}

# update_response = requests.put(url=updated_pixel_endpoint, json=updated_pixel_params, headers=headers)
# print(update_response.text)

# Deleting the pixel
deleting_date = "20220117"
deleted_pixel_endpoint = f"{pixel_endpoint}/{deleting_date}"

delete_response = requests.delete(url=deleted_pixel_endpoint, headers=headers)
print(delete_response.text)
