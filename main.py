import os
from dotenv import load_dotenv
import psycopg2


def load_connection_params():
    load_dotenv()  # Загружаем переменные окружения из файла .env
    connection_params = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT')
    }
    return connection_params


def main():
    connection_params = load_connection_params()


if __name__ == '__main__':
    main()