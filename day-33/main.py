import requests
from datetime import datetime
import smtplib
import time
MY_LAT =51.479269
MY_LONG=-0.119799
def is_iss_overhead() :
    response = requests.get(" https://api.sunrise-sunset.org/v2")
    response.raise_for_status()
    data = response.json()

    iss_lat = float(data['iss_position']['latitude'])
    iss_long = float(data['iss_position']['longitude'])

    if MY_LAT - 5 <= iss_lat <=MY_LAT + 5 and MY_LONG - 5 <= iss_long <= MY_LONG + 5:
        return True



def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0 }
    response = requests.get("https://api.sunrise-sunset.org/json" ,params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data['results']["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data['results']['sunset'].split("T")[1].split(":")[0])

    time_now = datetime.now().hour

    if time_now >= sunset or time_now <= sunrise:
        return True



while True :
    time.sleep(600)
    if is_iss_overhead() and is_night():
        my_email = "denemebora1234@gmail.com"
        password = "pwro gbcb kviy bptx"
        with smtplib.SMTP('smtp.gmail.com', 587) as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="robert.bora@hotmail.com",
                msg=f"Subject: LOOK UP!!\n\nThe iss is visible"
            )











