from sqlalchemy import text

from services.mysql_connection import MYSQL_CONNECTION


def remove_duplicates(table_name: str) -> None:
    connection = MYSQL_CONNECTION.connect()

    print(f'Removing duplicates in {table_name} table...')
    if table_name == 'stock_data':
        query = text(f'''
            DELETE n1 FROM stock_data n1, stock_data n2
            WHERE n1.date = n2.date AND n1.ticker = n2.ticker
        ''')
    else:
        raise Exception(f"[ERROR - remove_duplicates function] Table > {table_name} < doesn't exist")

    connection.execute(query)
    connection.close()
    print(f'Duplicates data was removed in {table_name} table.')
