import os
import requests

SHEETY_API_KEY = os.getenv("Sheety_OpenWeaher_Pixela_Api_key")

sheety_endpoint = "https://api.sheety.co/a940521a9c0db98308464dc264e57b1c/flightDeals/prices"

sheety_headers = {
    "Authorization": f"Bearer {SHEETY_API_KEY}"
}


class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        sheety_get_response = requests.get(url=sheety_endpoint, headers=sheety_headers)
        data = sheety_get_response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{sheety_endpoint}/{city['id']}",
                json=new_data,
                headers=sheety_headers
            )
            print(response.text)

