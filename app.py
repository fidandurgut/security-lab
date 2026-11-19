import sqlite3
from flask import Flask, request

app = Flask(__name__)

@app.route("/payment")
def get_payment():
    payment_id = request.args.get("id")
    conn = sqlite3.connect("payments.db")
    query = f"SELECT * FROM payments WHERE id = '{payment_id}'"
    return str(conn.execute(query).fetchall())
