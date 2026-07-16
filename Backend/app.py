from flask import Flask, jsonify
from flask_cors import CORS
import mysql.connector
import time
app = Flask(__name__)
CORS(app)

db = None

# Wait for MySQL to become available
for i in range(10):
    try:
        db = mysql.connector.connect(
            host="mysql",
            user="root",
            password="root123",
            database="companydb"
        )
        print("Connected to MySQL!")
        break
    except mysql.connector.Error:
        print("Waiting for MySQL...")
        time.sleep(5)

if db is None:
    raise Exception("Could not connect to MySQL")

@app.route("/employees")
def employees():
    cursor = db.cursor(dictionary=True)
    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()
    return jsonify(data)

app.run(host="0.0.0.0", port=5000)