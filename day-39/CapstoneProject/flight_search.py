import requests
from datetime import datetime, timedelta
import os
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com/v2/search"
TEQUILA_API_KEY = os.environ.get("TEQUILA_API_KEY")

class FlightSearch:
    def check_flights(self, origin, destination_iata):
        tomorrow = (datetime.now() + timedelta(days=1)).strftime("%d/%m/%Y")
        six_months = (datetime.now() + timedelta(days=180)).strftime("%d/%m/%Y")
        params = {
            "fly_from": origin,
            "fly_to": destination_iata,
            "date_from": tomorrow,
            "date_to": six_months,
            "nights_in_dst_min": 7,
            "nights_in_dst_max": 28,
            "flight_type": "round",
            "one_for_city": 1,
            "curr": "GBP",
        }
        headers = {"apikey": TEQUILA_API_KEY}
        response = requests.get(TEQUILA_ENDPOINT, params=params, headers=headers)
        data = response.json()["data"]
        if not data:
            # try with stopovers
            params["max_stopovers"] = 1
            response = requests.get(TEQUILA_ENDPOINT, params=params, headers=headers)
            data = response.json()["data"]

        return data[0] if data else None
