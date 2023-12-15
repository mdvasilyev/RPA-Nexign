import os
import psycopg2
import subprocess
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import HTMLResponse


app = FastAPI()


def load_connection_params() -> dict:
    load_dotenv()  # Загружаем переменные окружения из файла .env
    connection_params = {
        'dbname': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD'),
        'host': os.getenv('DB_HOST'),
        'port': os.getenv('DB_PORT')
    }
    return connection_params


conn = psycopg2.connect(**load_connection_params())
cur = conn.cursor()
conn.autocommit = True


@app.get("/")
def read_root():
    html_content = "<h2>Robocorp Control room analogue</h2>"
    return HTMLResponse(content=html_content)


@app.get("/robots")
def show_robots():
    cur.execute("""select *
                from scripts;""")
    result = cur.fetchall()
    return result


@app.get("/robots/{id}")
def show_robot_by_id(id: int):
    cur.execute(f"""select *
                from scripts
                where id = {id};""")
    result = cur.fetchone()
    return result


def run_robot_tasks(folder_path) -> None:
    os.chdir(folder_path)
    subprocess.run(["rcc", "run"]) 


# cur.close()
# conn.close()

# def main():
#     conn = psycopg2.connect(**load_connection_params())
#     cur = conn.cursor()
#     conn.autocommit = True

#     # cur.execute("""create table scripts (
#     #             id int primary key,
#     #             name varchar(255),
#     #             path text
#     #             );
#     # """)

#     # cur.execute("""insert into scripts (id, name, path) values
#     #             (1, 'calculator', '/Users/mayxi/CodeProjects/RPA-Nexign/example-windows-calculator'),
#     #             (2, 'web-scraper', '/Users/mayxi/CodeProjects/RPA-Nexign/example-web-scraper')
#     # """)

#     cur.execute("""select path
#                 from scripts
#                 where name = 'calculator'
#                 """)

#     # conn.commit()

#     path = cur.fetchone()[0]

#     run_robot_tasks(path)

#     cur.close()
#     conn.close()


# if __name__ == '__main__':
#     main()