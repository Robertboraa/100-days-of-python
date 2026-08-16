from twilio.rest import Client
import requests

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
api_key = ""
account_sid = ""
auth_token = ""
STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": api_key,
}
news_params = {
    "q": COMPANY_NAME,
    "apiKey": "",
    "sortBy": "popularity"
}

response = requests.get(STOCK_ENDPOINT, params=stock_params)
data = response.json()["Time Series (Daily)"]
dates = list(data.keys())
yesterday_close = float(data[dates[0]]["4. close"])
day_before_close = float(data[dates[1]]["4. close"])

difference = yesterday_close - day_before_close
percentage = abs((difference / day_before_close) * 100)
arrow = "🔺" if difference > 0 else "🔻"

if percentage > 5:
    response = requests.get(NEWS_ENDPOINT, params=news_params)
    articles = response.json()["articles"][0:3]
    for article in articles:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"TSLA: {arrow}{round(percentage)}%\nHeadline: {article['description']}\nBrief: {article['content']}",
            from_="",
            to=""
        )