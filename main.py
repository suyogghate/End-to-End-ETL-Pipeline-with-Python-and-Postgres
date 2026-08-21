import logging
from ETL.extract import extract_product, extract_users
from ETL.transform import transform_product, transform_users
from ETL.load import load_to_database

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def run_pipeline():
    logging.info('Starting pipeline...')

    product_df = extract_product()
    user_df = extract_users()

    logging.info('Starting transformation...')

    product_df = transform_product(product_df)
    user_df = transform_users(user_df)

    logging.info('Loading to database...')

    load_to_database(product_df, 'products')
    load_to_database(user_df, 'users')

    logging.info('ETL pipeline completed....')

if __name__ == '__main__':
    run_pipeline()