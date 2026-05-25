import requests
import os
from twilio.rest import Client

OWM_Endpoint = "https://api.openweathermap.org/data/2.5/forecast"
api_key = os.environ.get("OWM_API_KEY")
acc_sid = os.environ.get("ACC_SID")
auth_token = os.environ.get("AUTH_TOKEN")


weather_params = {
    "lat": 48.209209,
    "lon": 16.372780,
    "appid": api_key,
    "cnt": 4,
}
response = requests.get(OWM_Endpoint, params=weather_params)
response.raise_for_status()
weather_data = response.json()
weather_id = weather_data["list"][0]["weather"][0]["id"]

will_rain = False
for list in weather_data["list"]:
    condition_code = list["weather"][0]["id"]
    if int(condition_code) < 800:
        will_rain = True
if will_rain:
    client = Client(acc_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring an ☔",
        from_="+19066614369",
        to=os.environ.get("MY_NUM"),
    )
    print(message.status)
