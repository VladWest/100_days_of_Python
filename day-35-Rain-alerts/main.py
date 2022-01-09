from twilio.rest import Client
import requests

api_key = "Your_Open_Weather_Map_Key"

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "Your_Twilio_sid"
auth_token = "Your_Twilio_app_token"

# Zaporozhye, Ukraine
# lat = 47.846458
# long = 35.149269

# Sumy, Ukraine
lat = 50.907700
long = 34.798100

parameters = {
    "lat": lat,
    "lon": long,
    "exclude": "current,minutely,daily",
    "units": "standard",
    "appid": api_key
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
data = response.json()
# My solution for getting weather codes for next 12 hours
# i = 0
# if_rain = True
# while if_rain:
#     weather_id = data["hourly"][i]["weather"][0]["id"]
#     i += 1
#     if i > 12:
#         if_rain = False
#     elif weather_id < 700:
#         print("Bring an umbrella.")
#         if_rain = False

# Angela's solution for the same
# Slicing the list
weather_slice = data["hourly"][:12]
will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
            body="It's going to rain in Sumy today. Remember, to bring an umbrella.",
            from_='+15862501467',
            to='+380661937959'
        )
    print(message.status)
