import yfinance as yf
import investpy as inv

from datetime import datetime

from services.mysql_connection import MYSQL_CONNECTION

def update_db(country: str):
    current_date = datetime.now().strftime('%Y-%m-%d')
    br_tickers = inv.stocks.get_stocks(country=country)
    for ticker in br_tickers['symbol']:

        if len(ticker) > 5: continue

        if country.lower() == 'brazil': ticker = f'{ticker}.SA'

        # series = yf.download(ticker, start='1600-01-01', end=current_date)['Adj Close']['Currency']
        series = yf.download(ticker, start='1300-01-01', end=current_date)['Adj Close']
        df = series.to_frame(name='Adj Close')
        df.insert(1, 'ticker', ticker)
        df.reset_index(inplace=True)

        if df['Date'].empty: continue # removing NULLs of date columns

        df['Date'] = df['Date'].dt.date

        df.to_sql('stock_data', con=MYSQL_CONNECTION, if_exists='append', index=False)

        # data = investpy.get_crypto_historical_data(crypto='bitcoin',
        #                                    from_date='01/01/2014',
        #                                    to_date='01/01/2019')


if __name__ == '__main__':
    # update_db(country='brazil')
    update_db(country='united states')