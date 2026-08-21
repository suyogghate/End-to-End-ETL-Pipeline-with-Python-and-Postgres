from sqlalchemy import create_engine
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

host = 'localhost'
port = 5432
user = 'postgres'
password = 'your password'
db_name = 'fake_store_db'

def load_to_database(df, table_name):
    engine = create_engine(f'postgresql://{user}:{password}@{host}:{port}/{db_name}')

    df.to_sql(table_name,
              engine,
              if_exists = 'append',
              index = False)

    logging.info('Data loaded to database successfully....')

    