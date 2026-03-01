
from flask import Flask, request, jsonify
from flask_cors import CORS
import mysql.connector
from datetime import datetime

app = Flask(__name__)
CORS(app)

db_config = {
    "host": "localhost",
    "user": "root",
    "password": "password",
    "database": "water_management"
}

def get_db_connection():
    return mysql.connector.connect(**db_config)

@app.route("/add_usage", methods=["POST"])
def add_usage():
    data = request.json
    apartment_no = data["apartment_no"]
    usage_liters = data["usage_liters"]

    conn = get_db_connection()
    cursor = conn.cursor()
    query = "INSERT INTO water_usage (apartment_no, usage_liters, timestamp) VALUES (%s, %s, %s)"
    cursor.execute(query, (apartment_no, usage_liters, datetime.now()))
    conn.commit()
    cursor.close()
    conn.close()

    return jsonify({"message": "Usage data added successfully"})


@app.route("/get_usage", methods=["GET"])
def get_usage():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM water_usage")
    data = cursor.fetchall()
    cursor.close()
    conn.close()
    return jsonify(data)


@app.route("/calculate_bill/<int:apartment_no>", methods=["GET"])
def calculate_bill(apartment_no):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT SUM(usage_liters) FROM water_usage WHERE apartment_no=%s", (apartment_no,))
    total_usage = cursor.fetchone()[0] or 0
    cursor.close()
    conn.close()

    rate_per_liter = 0.05
    bill = total_usage * rate_per_liter

    return jsonify({
        "apartment_no": apartment_no,
        "total_usage_liters": total_usage,
        "total_bill": bill
    })

if __name__ == "__main__":
    app.run(debug=True)
