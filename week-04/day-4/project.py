import psycopg2, networkx as nx
from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    pass

conn = psycopg2.connect(host="localhost",
                 database="slack",
                 user="postgres",
                 password="password")

cur = conn.cursor()


cur.close()
conn.close()