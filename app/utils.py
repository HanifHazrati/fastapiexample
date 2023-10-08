from psycopg.rows import dict_row
import psycopg
import time

counter = 0
while True:
    counter += 1
    try:
        conn = psycopg.connect(
            host="localhost", port="5433", dbname="fastapi", user="postgres", password="1234", row_factory=dict_row
        )
        cursor = conn.cursor()
    except Exception as error:
        print("OOPS :(")
        if counter == 10:
            del counter
            conn = psycopg.connect(
                host="localhost", port="5433", dbname="fastapi", user="postgres", password="1234", row_factory=dict_row
            )
            break
    else:
        del counter
        break
    time.sleep(2)
