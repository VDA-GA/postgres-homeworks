"""Скрипт для заполнения данными таблиц в БД Postgres."""
import os
from dotenv import load_dotenv
import psycopg2
import pandas as pd
from pathlib import Path

load_dotenv()

password = os.getenv('PASSWORD_POSTGRES')

df_customers = pd.read_csv(Path(Path(Path.cwd()), 'north_data', 'customers_data.csv'))
df_employees = pd.read_csv(Path(Path(Path.cwd()), 'north_data', 'employees_data.csv'))
df_orders = pd.read_csv(Path(Path(Path.cwd()), 'north_data', 'orders_data.csv'))

with psycopg2.connect(host="localhost", database="north", user="postgres", password=password) as conn:
    with conn.cursor() as cur:
        for i in range(0, df_customers.shape[0]):
            cur.execute("INSERT INTO customers VALUES (%s, %s, %s)",
                        (df_customers.iloc[i, 0], df_customers.iloc[i, 1], df_customers.iloc[i, 2]))
        cur.execute("SELECT * FROM customers")
        conn.commit()

        for i in range(0, df_employees.shape[0]):
            cur.execute("INSERT INTO employees VALUES (%s, %s, %s, %s, %s, %s)",
                        (int(df_employees.iloc[i, 0]), df_employees.iloc[i, 1], df_employees.iloc[i, 2],
                         df_employees.iloc[i, 3], df_employees.iloc[i, 4], df_employees.iloc[i, 5]))
        cur.execute("SELECT * FROM employees")
        conn.commit()

        for i in range(0, df_orders.shape[0]):
            cur.execute("INSERT INTO orders VALUES (%s, %s, %s, %s, %s)",
                        (int(df_orders.iloc[i, 0]), df_orders.iloc[i, 1], int(df_orders.iloc[i, 2]),
                         df_orders.iloc[i, 3], df_orders.iloc[i, 4]))
        cur.execute("SELECT * FROM orders")
        conn.commit()

conn.close()
