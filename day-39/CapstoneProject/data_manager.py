import requests
import os
SHEETY_ENDPOINT = os.environ.get("SHEETY_ENDPOINT")
SHEETY_USERS_ENDPOINT = os.environ.get("SHEETY_USERS_ENDPOINT")

class DataManager:
    def __init__(self):
        self.destination_data = []

    def get_destination_data(self):
        response = requests.get(SHEETY_ENDPOINT)
        self.destination_data = response.json()["sayfa1"]
        return self.destination_data

    def get_customer_emails(self):
        response = requests.get(SHEETY_USERS_ENDPOINT)
        return response.json()["users"]