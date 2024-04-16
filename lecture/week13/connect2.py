
import psycopg2

def connect():
    try:
        # connecting to the PostgreSQL server
        with psycopg2.connect(host="localhost",database="suppliers",user="postgres",password="123") as conn:
            print('Connected to the PostgreSQL server.')
            return conn
    except (psycopg2.DatabaseError, Exception) as error:
        print(error)


if __name__ == '__main__':
    connect()