from flask import Flask, jsonify
import sqlite3

app = Flask(__name__)

def hae_kentta(icao):
    conn = sqlite3.connect('airports.db')
    c = conn.cursor()
    c.execute("SELECT name, municipality FROM airports WHERE ident=?", (icao,))
    row = c.fetchone()
    conn.close()
    if row is None:
        return None
    return {"ICAO": icao, "Name": row[0], "Municipality": row[1]}

@app.route('/kentta/<icao>', methods=['GET'])
def kentta(icao):
    kentta = hae_kentta(icao)
    if kentta is None:
        return jsonify({"error": "Airport not found"}), 404
    return jsonify(kentta)

if __name__ == "__main__":
    app.run(port=3000)