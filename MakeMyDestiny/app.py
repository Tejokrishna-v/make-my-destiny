from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

def connect():
    return sqlite3.connect("booking.db")

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/signup", methods=["POST"])
def signup():
    data = request.json
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO users VALUES (?, ?, ?, ?, ?, ?)
    """, (
        data["username"],
        data["first"],
        data["last"],
        data["phone"],
        data["email"],
        data["password"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"status": "Signup Success"})

@app.route("/login", methods=["POST"])
def login():
    data = request.json
    conn = connect()
    cur = conn.cursor()

    cur.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (data["username"], data["password"])
    )

    user = cur.fetchone()
    conn.close()

    if user:
        return jsonify({"status": "Login Success"})
    else:
        return jsonify({"status": "Login Failed"})

@app.route("/book", methods=["POST"])
def book():
    data = request.json
    conn = connect()
    cur = conn.cursor()

    cur.execute("""
        INSERT INTO bookings (username, service, from_loc, to_loc, date, persons, seat)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        data["username"],
        data["service"],
        data["from"],
        data["to"],
        data["date"],
        data["persons"],
        data["seat"]
    ))

    conn.commit()
    conn.close()

    return jsonify({"status": "Booking Success"})

@app.route("/mybookings/<username>")
def mybookings(username):
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM bookings WHERE username=?", (username,))
    rows = cur.fetchall()

    conn.close()

    return jsonify(rows)

@app.route("/allbookings")
def allbookings():
    conn = connect()
    cur = conn.cursor()

    cur.execute("SELECT * FROM bookings")
    rows = cur.fetchall()

    conn.close()

    result = []
    for r in rows:
        result.append({
            "id": r[0],
            "username": r[1],
            "service": r[2],
            "from_loc": r[3],
            "to_loc": r[4],
            "date": r[5],
            "persons": r[6],
            "seat": r[7]
        })

    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)