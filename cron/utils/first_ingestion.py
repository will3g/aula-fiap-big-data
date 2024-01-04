import time
import schedule

import pandas as pd
import yfinance as yf
import investpy as inv

from cron.services.mysql_connection import MYSQL_CONNECTION

def update_db():
    br_tickers = inv.stocks.get_stocks(country='brazil')
    wallet = []
    for ticker in br_tickers['symbol']:
        if len(ticker) <= 5: wallet.append(f'{ticker}.SA')
    # dt = yf.download(wallet, start='1900-01-01', end='2023-12-31')['Adj Close']
    dt = yf.download('TAEE11.SA', start='2023-12-28', end='2024-01-01')['Adj Close']
    dt.to_sql('stock_data', con=MYSQL_CONNECTION, if_exists='replace')
    # dt.to_sql('stock_data', con=MYSQL_CONNECTION, if_exists='replace', index=False)

schedule.every(1).minutes.do(update_db)

while True:
    schedule.run_pending()
    time.sleep(1)
