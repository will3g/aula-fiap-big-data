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
    dt = yf.download(wallet, start='1900-01-01', end='2023-12-31')['Adj Close']
    

schedule.every(1).minutes.do(update_db)

while True:
    schedule.run_pending()
    time.sleep(1)
