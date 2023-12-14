import os
import subprocess
from dotenv import load_dotenv
# import psycopg2
from robot.api import TestSuite
from robot import run


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


def run_robot_tasks(folder_path):
    os.chdir(folder_path)
    subprocess.run(["rcc", "run"]) 


def main():
    connection_params = load_connection_params()
    print(connection_params)

    folder_path_from_database = "/Users/mayxi/CodeProjects/RPA-Nexign/example-windows-calculator"

    run_robot_tasks(folder_path_from_database)

if __name__ == '__main__':
    main()