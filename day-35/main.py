import requests
from twilio.rest import Client
client_secret = "vf6iii8r5b18SfICSDFZlc4ezLMjCesK"
api_key =  "3205c5797826847419a6bc53fa06b8bc"
OWM_endpoint = "https://api.openweathermap.org/data/2.5/forecast"
auth_token = "9e9dc4bb63f5983d0e78db31927d93d0"
account_sid="ACfada2ace2402fbed617803d679baf401"
weather_params = {
    "lat": 40.417286,
    "lon": -82.907120,
    "appid": api_key,
    "cnt": 4
}
will_rain= False
response = requests.get(OWM_endpoint, params=weather_params)
data = response.json()
for forecast in data["list"]:
    weather_id = forecast["weather"][0]["id"]
    if int(weather_id) <700:
        will_rain = True
if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body='Your Twilio trial account can send this message',
        from_="+447460077297",
        to="+447345643840",
    )
    print(message.status)


