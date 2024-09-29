import psycopg2
import random


host = "77.50.236.204"
port = "42032"
database = "params"
user = "params"
password = "pass1594826"


conn = psycopg2.connect(
    host=host,
    port=port,
    dbname=database,
    user=user,
    password=password
)


cur = conn.cursor()


def generate_random_data():
    name = f"test-{random.randint(1, 100000)}"
    location = random.choice(["Data Center 1", "Data Center 2", "Data Center 3"])
    ip = f"192.168.{random.randint(0, 255)}.{random.randint(0, 255)}"
    port = random.randint(1024, 65535)
    cpu = random.randint(1, 32)  # Генерация случайного количества ядер CPU
    ram = random.randint(1024, 65536)  # Генерация случайного объема RAM в MB
    return (name, location, ip, port, cpu, ram)


for _ in range(2):
    data = generate_random_data()
    cur.execute(
        "INSERT INTO серверы (name, location, ip, port, CPU, RAM) VALUES (%s, %s, %s, %s, %s, %s)",
        data
    )


conn.commit()
cur.close()
conn.close()

print(generate_random_data())
