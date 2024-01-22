import yfinance as yf
import investpy as inv

from datetime import datetime

from services.mysql_connection import MYSQL_CONNECTION

from utils.remove_duplicates_of_tables import remove_duplicates

TABLE_NAME = 'stock_data'


def ingestion(
    country: str,
    current_date: datetime,
    br_tickers: object
) -> None:

    for ticker in br_tickers['symbol']:
        try:
            if len(ticker) > 5: continue

            if country.lower() == 'brazil': ticker = f'{ticker}.SA'

            data = yf.Ticker(ticker)

            df = data.history(start='1000-01-01',end=current_date)
            df.insert(1, 'Ticker', ticker.replace('.SA', ''))
            df.insert(1, 'Country', country)
            df.reset_index(inplace=True)

            if df['Date'].empty: continue

            df['Date'] = df['Date'].dt.date

            df.to_sql(TABLE_NAME, con=MYSQL_CONNECTION, if_exists='append', index=False)

        except Exception as err:
            print(err)
            continue

def update_db(country: str):
    current_date = datetime.now().strftime('%Y-%m-%d')
    br_tickers = inv.stocks.get_stocks(country=country)

    ingestion(
        country=country,
        current_date=current_date,
        br_tickers=br_tickers
    )

    remove_duplicates(TABLE_NAME)


if __name__ == '__main__':
    update_db(country='brazil')
    # update_db(country='united states')
