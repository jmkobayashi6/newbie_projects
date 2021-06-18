import requests
import datetime as dt
from twilio.rest import Client


API_NEWS_KEY = "ed3767f3e6b34a00abf138fd7fc7b98e"
API_KEY = "WMJ3R6TLF54QCS1O"
STOCK = "IBM"
number_articles = 3
def stock_price_change(trade_day_before, trade_day_yesterday):
    global API_KEY, STOCK
    percet = 0
    url = "https://www.alphavantage.co/query"
    parameters = {
        'function': "TIME_SERIES_DAILY",
        'symbol': STOCK,
        "apikey": API_KEY,
    }
    response = requests.get(url=url, params=parameters)
    response.raise_for_status()
    stock_data = response.json()
    trade_price_yesterday = float(stock_data["Time Series (Daily)"][trade_day_yesterday]['1. open'])
    trade_price_before = float(stock_data["Time Series (Daily)"][trade_day_before]['1. open'])
    ##dummies
    # trade_price_yesterday = 10
    # trade_price_before = 9.5

    percent = float(((trade_price_yesterday - trade_price_before)/trade_price_before) * 100)
    return percent

def get_news(date, article):

   global API_NEWS_KEY, STOCK
   news = []
   url = "https://newsapi.org/v2/everything"
   parameters = {
       'from': date,
       'q': STOCK,
       "apiKey": API_NEWS_KEY,
       "sortBy": "publishedAt",
       "language": "en",

   }
   response = requests.get(url=url, params=parameters)
   response.raise_for_status()
   news_data = response.json()

   source_name = news_data["articles"][article]['source']['name']
   news_title = news_data["articles"][article]['title']
   #news_descrip = news_data["articles"][2]['description']
   news_url = news_data["articles"][2]['url']
   string = f"{source_name}: {news_title}\n{news_url}\n"

   return string





## DATES
current_time = dt.datetime.now()
week_day = current_time.weekday()
year = current_time.year
month = current_time.month

day = current_time.day

if day == 6:
    day = day - 2
else:
    day = day - 1

trade_day_yesterday = f"{year}-0{month}-0{day}"
day_before = day - 1
trade_day_before = f"{year}-0{month}-0{day_before}"

### Get percent
percent = stock_price_change(trade_day_before, trade_day_yesterday)
# percent = 7.7
print(percent)
### Get news
news ={}
string = ""
account_sid = "ACffc3e3e12c6f46d2ac64aa90954ce726"
auth_token = "2f18ef882f76771adcdc44d17fa15c4c"
if percent >= 5 or percent <= -5:
    if percent <= -5:
        format_percent = f"🔻{percent}%"
    if percent >= 5:
        format_percent = f"🔺{percent}%"

    for articles in range(number_articles):
        x = get_news(trade_day_before, articles)
        string = string + f"{x}\n"


    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(

        body=f"{STOCK}:{format_percent}\n{string}",
        from_='+1 604 265 7175',
        to='+12505162111'
        )
    print(message.status)


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

