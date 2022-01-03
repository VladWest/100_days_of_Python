import requests
from datetime import datetime

# Connecting to API
response = requests.get(url="http://api.open-notify.org/iss-now.json")
# Creating an exception in case is API will not provide response
response.raise_for_status()

# Adding JSON data to variable
data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)

# print(iss_position)

# Creating requests with parameters to get the time of surise or sunset
# Using this API - https://sunrise-sunset.org/api
# This API require some parameters such as longtitude and latitude
MY_LAT = 47.846460
MY_LONG = 35.149270

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

sun_response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
# Creating an exception in case is API will not provide response
sun_response.raise_for_status()

sun_data = sun_response.json()

sunrise = sun_data["results"]["sunrise"]
sunset = sun_data["results"]["sunset"]
# Picking up the hours of sunrise/sunset
sunrise = sunrise.split("T")[1].split(":")[0]
sunset = sunset.split("T")[1].split(":")[0]

print(datetime.now().hour)
print(sunrise)

