import json
import psycopg2

conn = psycopg2.connect(
    host="localhost",
    database="workshop",
    user="postgres",
    password="password"
)

cur = conn.cursor()

## create the table
cur.execute("CREATE TABLE car_dealer(\
id serial PRIMARY KEY,\
brand VARCHAR,\
model VARCHAR,\
year INTEGER,\
condition VARCHAR,\
price INTEGER,\
count INTEGER);")

## migrate the data
with open("dealer.json") as f:
    cars = json.load(f)

for car in cars:
    cur.execute("INSERT INTO car_dealer \
    VALUES (%(id)s, %(brand)s, %(model)s, %(year)s, %(condition)s, %(price)s, %(count)s);", {
        "id": car["id"],
        "brand": car["brand"],
        "model": car["model"],
        "year": car["year"],
        "condition": car["condition"],
        "price": car["price"],
        "count": car["count"]
    })

## remove cars with count 0
cur.execute("DELETE FROM car_dealer WHERE count = 0;")
print(cur.rowcount)
print("The cars with count 0 are removed")

## decrease price of wrecks
cur.execute("UPDATE car_dealer SET price = 0.8 * price WHERE condition = 'wreck';")
print(cur.rowcount)
print("The price of wreck cars are decreased by 20%.")

## average age of the cars
cur.execute("SELECT ROUND(AVG(EXTRACT(YEAR FROM NOW())::INTEGER - year), 2) FROM car_dealer;")
print(f"The average price is {cur.fetchone()[0]} years.")

cur.close()
conn.commit()
conn.close()