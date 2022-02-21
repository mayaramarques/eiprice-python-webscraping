#!/bin/bash
set -e
export PGPASSWORD=$POSTGRES_PASSWORD;
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE USER $APP_DB_USER WITH PASSWORD '$APP_DB_PASS';
  CREATE DATABASE $APP_DB_NAME;
  GRANT ALL PRIVILEGES ON DATABASE $APP_DB_NAME TO $APP_DB_USER;
  \connect $APP_DB_NAME $APP_DB_USER
  BEGIN;
    CREATE TABLE IF NOT EXISTS assortment (
	  name text NOT NULL,
	  sku text NOT NULL,
	  department text NOT NULL,
	  category text NOT NULL,
	  url text,
	  image text,
    price_to numeric(5,2),
    discount text,
    available text,
    stock_qty numeric(10),
    store text,
    created_at date,
    hour text
	);
  COMMIT;
EOSQL