import os

import requests
from twilio.rest import Client

# MY_LAT = 13.00  # Your latitude
# MY_LONG = 77.583333  # Your longitude
MY_LAT = 43.610767  # Test Paris latitude
MY_LONG = 3.876716  # Test Paris longitude

api_key = os.environ.get("OWM_KEY") # Only if the api key is added to envtvariable.
auth_token = os.environ.get("AUTH_TOKEN")
account_sid = "ACf21e6506da5233d77a936d156f5890db"
PHONE_NUM = "+17627603600"

parameters = {
    "lat": MY_LAT,
    "lon": MY_LONG,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

api_url = "https://api.openweathermap.org/data/2.5/onecall"

response = requests.get(api_url, params=parameters)
response.raise_for_status()
# print(response.status_code)
weather_data = response.json()
will_rain = False
weather_slice = weather_data["hourly"][:12]

for each in weather_slice:
    weather_condition_code = each['weather'][0]['id']
    if weather_condition_code < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔.",
        from_=PHONE_NUM,
        to="+919886605789"
    )
    print(message.status)
