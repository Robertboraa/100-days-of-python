import requests
from datetime import datetime
TOKEN = "142314boboido"
USERNAME = "borarob123"
GRAPHID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users/"
user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)




graph_endpoint = f"{pixela_endpoint}{USERNAME}/graphs"
graph_params = {
    "id": GRAPHID,
    "name": "Runing Graph",
    "unit" : "Km",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
#response = requests.post(graph_endpoint, json=graph_params,headers=headers)
#print(response.text)


today = datetime.now()
#any_date = datetime(year=2026, month=8, day=1)
pixel_upload_endpoint = f"{graph_endpoint}/{GRAPHID}"
pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many Km?"),
}
response = requests.post(pixel_upload_endpoint,json=pixel_data , headers=headers)
print(response.text)