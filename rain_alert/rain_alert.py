import requests
# import os
from twilio.rest import Client
# from twilio.http.http_client import TwilioHttpClient


# twilio details
twilio_number = 
phone_numbers = ""
account_sid = ""
auth_token = ""

# one call weather api
OWM_ENDPOINT = ""
API_KEY  = ""

# latitude = 
# longitude =

weather_params = {
    "lat" :  ,
    "lon" : ,
    "appid" : API_KEY,
    "exclude" : "current,minutely,daily"
}

response = requests.get(url=OWM_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()
# weather_data = response.json()["hourly"][0]["weather"][0]["id"] #0 before id because theres only 1 item, to access it add 0.
weather_slice = weather_data["hourly"][:12]

will_rain = False
for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    # proxy_client = TwilioHttpClient()
    # proxy_client.session.proxies = {"https" : os.environ["http_proxy"]}
    client = Client(account_sid, auth_token) #in few error cases :  http_client=proxy_client
    message = client.messages \
                .create(
                     body= "It's going to rain ☔ bring an umbrella",
                     from_= twilio_number,
                     to= phone_numbers
                 )
    
    print(message.status)