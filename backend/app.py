from flask import Flask, jsonify, request
import psycopg2
import time

app = Flask(__name__)

def get_db():
    return psycopg2.connect(host="db", dbname="shop", user="postgres", password="postgres")

while True:
    try:
        conn = get_db()
        break
    except Exception:
        print("база еще не запустилась, жду...")
        time.sleep(2)

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS products (id SERIAL PRIMARY KEY, name TEXT, price INT)")
conn.commit()
conn.close()

@app.route("/api/products", methods=["GET"])
def get_products():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("SELECT id, name, price FROM products")
    rows = cur.fetchall()
    conn.close()

    products = []
    for row in rows:
        products.append({"id": row[0], "name": row[1], "price": row[2]})
    return jsonify(products)

@app.route("/api/products", methods=["POST"])
def add_product():
    data = request.json
    conn = get_db()
    cur = conn.cursor()
    cur.execute("INSERT INTO products (name, price) VALUES (%s, %s)", (data["name"], data["price"]))
    conn.commit()
    conn.close()
    return jsonify({"status": "ok"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
