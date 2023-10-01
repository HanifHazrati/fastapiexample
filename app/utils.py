from psycopg.rows import dict_row
import psycopg
import time


while True:
    try:
        conn = psycopg.connect(
            host="localhost", port="5433", dbname="fastapi", user="postgres", password="1234", row_factory=dict_row
        )
        cursor = conn.cursor()
        break
    except Exception as error:
        pass
    time.sleep(2)
