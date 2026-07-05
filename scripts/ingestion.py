import requests
from airflow.providers.mysql.hooks.mysql import MySqlHook
from datetime import datetime


def fetch_crypto_data():
    url = "https://api.coingecko.com/api/v3/coins/markets"
    params = {
        "vs_currency": "usd",
        "order": "market_cap_desc",
        "ids": "bitcoin,ethereum,solana",
    }

    response = requests.get(url, params=params)

    if response.status_code == 200:
        data = response.json()
        cleaned_data = []

        for coin in data:
            cleaned_data.append((
                coin['id'],
                coin['symbol'].upper(),
                float(coin['current_price']),
                float(coin['market_cap']),
                float(coin['total_volume']),
            ))
        return cleaned_data
    else:
        print(f"Error fetching data: {response.status_code} - {response.text}")
        return None
    
def fetch_and_load():
    # 1. Fetch data from api
    records = fetch_crypto_data()
    if not records:
        print("No data fetched. aborting the load process.")
        return 
        
    # 2. Call the Airflow Connection by its Connection ID
    mysql_hook = MySqlHook(mysql_conn_id='crypto_mysql_conn')

    # 3. Insert rows using hook's helper function
    target_fields = ['coin_id', 'coin_symbol', 'price_usd', 'market_cap', 'volume_24h']

    try:
        mysql_hook.insert_rows(
            table='market_history',
            rows=records,
            target_fields=target_fields
        )
        print(f"[{datetime.now()}] Data inserted successfully via Airflow Connection Hook.")
    except Exception as e:
        print(f"Database write execution error: {e}")
        raise e
        


        


            