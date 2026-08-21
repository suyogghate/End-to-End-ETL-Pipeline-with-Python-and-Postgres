# End-to-End-ETL-Pipeline-with-Python-and-Postgres

A simple ETL (Extract, Transform, Load) pipeline that pulls product and user data from the [Fake Store API](https://fakestoreapi.com/), cleans and reshapes it with pandas, and loads it into a PostgreSQL database.

## Overview

The pipeline runs in three stages:

1. **Extract** — Fetches raw product and user data from the Fake Store API.
2. **Transform** — Cleans, renames, and flattens the data into analysis-ready tables.
3. **Load** — Writes the transformed data into PostgreSQL tables, replacing existing data on each run.

## Project Structure

```
End-to-End-ETL-Pipeline-with-Python-and-Postgres/
├── ETL/
│   ├── extract.py      # Pulls raw data from the Fake Store API
│   ├── transform.py     # Cleans and reshapes the extracted data
│   └── load.py           # Loads transformed data into PostgreSQL
├── main.py                # Orchestrates the full pipeline
└── README.md
```

## Data Flow

### Extract (`extract.py`)
- `extract_product()` — fetches `/products` and returns a raw DataFrame.
- `extract_users()` — fetches `/users` and returns a raw DataFrame.

### Transform (`transform.py`)
- `transform_product()` — renames columns to a `prod_*` naming convention (`prod_id`, `prod_title`, `prod_price`, `prod_category`, `prod_img`) and casts price to `float`.
- `transform_users()` — flattens nested `name` and `address` JSON fields into flat columns (`first_name`, `last_name`, `street`, `city`, `zipcode`) and renames identifiers (`user_id`, `user_email`).

### Load (`load.py`)
- `load_to_database()` — writes a DataFrame to a PostgreSQL table via SQLAlchemy, replacing the table if it already exists.

## Requirements

- Python 3.9+
- PostgreSQL running locally (or accessible via network)
- Python packages:
  ```
  pandas
  requests
  sqlalchemy
  psycopg2-binary
  ```

Install dependencies:

```bash
pip install pandas requests sqlalchemy psycopg2-binary
```

## Setup

1. **Create the database** in PostgreSQL:
   ```sql
   CREATE DATABASE fake_store_db;
   ```

2. **Configure database credentials** in `ETL/load.py`:
   ```python
   host = 'localhost'
   port = 5432
   user = 'postgres'
   password = 'your_password'
   db_name = 'fake_store_db'
   ```
   > For production use, move these into environment variables instead of hardcoding them (see [Notes](#notes) below).

3. **Run the pipeline**:
   ```bash
   python main.py
   ```

## Output

On a successful run, two tables are created (or replaced) in the `fake_store_db` database:

| Table      | Description                                   |
|------------|------------------------------------------------|
| `products` | Product ID, title, price, category, description, image URL |
| `users`    | User ID, email, username, name, and address fields |

## Logging

Both `extract.py` and `load.py` use Python's built-in `logging` module to report progress and errors to the console, including timestamps and log levels.
