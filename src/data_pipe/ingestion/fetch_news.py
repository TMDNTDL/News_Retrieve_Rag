import os
import finnhub

from datetime import datetime, timedelta
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("FINNHUB_API_KEY")

if not api_key:
    raise ValueError("FINNHUB_API_KEY environment variable is not set.")

client = finnhub.Client(api_key=api_key)

def get_quotes(symbols: str):
    quote = client.quote(symbols)
    print(f"\n--- {symbols} Quote ---")
    print(f"Current Price: {quote['c']}")
    print(f"Change: {quote['d']} ({quote['dp']}%)")
    print(f"High Price of the day: {quote['h']}")
    print(f"Low Price of the day: {quote['l']}")
    return quote

def get_company_news(symbols: str, day_back: int = 3):
    today = datetime.now()
    start_date = (today - timedelta(days=day_back)).strftime('%Y-%m-%d')
    end_date = today.strftime('%Y-%m-%d')

    news = client.company_news(symbols, _from=start_date, to=end_date)

    print(f"\n--- {symbols} News (last {day_back} days) ---")
    for article in news[:5]:
        published = datetime.fromtimestamp(article['datetime']).strftime('%Y-%m-%d %H:%M:%S')
        print(f"\n[{published}] {article['headline']}")
        print(f"Source: {article['source']}")
        print(f"URL: {article['url']}\n")
    return news

if __name__ == "__main__":
    ticker = "AAPL"
    
    get_quotes(ticker)
    get_company_news(ticker)
