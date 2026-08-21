import pandas as pd
import requests
import logging

BASE_URL = 'https://fakestoreapi.com/'

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def extract_product():
    try:
        url = f'{BASE_URL}/products'
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        product_df = pd.DataFrame(data)

        return product_df
        
    except Exception as e:
        logging.error(f"Some error occurred: {e}")

def extract_users():
    try:
        url = f'{BASE_URL}/users'
        response = requests.get(url)
        response.raise_for_status()

        data = response.json()
        user_df = pd.DataFrame(data)

        return user_df

    except Exception as e:
        logging.error(f"Some error occurred: {e}")


