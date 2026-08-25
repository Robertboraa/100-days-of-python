import requests

SHEETY_ENDPOINT = "https://api.sheety.co/YOUR_ID/yourProject/sayfa1"

class DataManager:
    def __init__(self):
        self.destination_data = []

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        self.destination_data = response.json()["sayfa1"]
        return self.destination_data