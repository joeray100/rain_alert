# For some reason your rain_alert key is not working
# So your using your appid API KEY for now

# ---------------------------- IMPORTS ---------------------------- #

import requests
import os
from twilio.rest import Client

# ---------------------------- GLOBAL CONSTANTS ---------------------------- #

# OWM
OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/onecall"
API_KEY = os.environ.get("OWM_API_KEY")
# Eagle lat/long
LAT = 39.393452
LONG = -107.091614
WEATHER_PARAMS = {
    "lat": LAT,
    "lon": LONG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"
}

# Twilio
ACCOUNT_SID = "ACebf5384e7b399e284c2452f85df4d1ef"
AUTH_TOKEN = os.environ.get("TWILIO_AUTH_TOKEN")
FROM_NUMBER = "+18443112341"
TO_NUMBER = "+17207669589"

# ---------------------------- CODE ---------------------------- #

response = requests.get(OWM_ENDPOINT, params=WEATHER_PARAMS)
response.raise_for_status()
weather_data = response.json()["hourly"][:12]

will_rain = False

for hour in weather_data:
    if int(hour["weather"][0]["id"]) < 700:
        will_rain = True

if will_rain:
    client = Client(ACCOUNT_SID, AUTH_TOKEN)
    message = client.messages \
        .create(
        body="It's going to rain or snow today.",
        from_=FROM_NUMBER,
        to=TO_NUMBER
    )
    print(message.status)

