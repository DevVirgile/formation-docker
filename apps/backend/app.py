import os
import mysql.connector
from mysql.connector import Error
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/chip/<id>', methods=['GET'])
def get_chip(id : int):
    try:
        db_host = os.environ.get('MYSQL_HOST')
        db_user = os.environ.get('MYSQL_USER')
        db_password = os.environ.get('MYSQL_PASSWORD')
        db_name = os.environ.get('MYSQL_DATABASE')

        conn = mysql.connector.connect(
            host=db_host,
            user=db_user,
            password=db_password,
            database=db_name
        )

        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT \
	            ID AS id, \
	            MARQUE AS marque, \
	            PRICE AS price \
            FROM PAQUET_CHIPS \
            WHERE \
	            ID = %s", (id,)
        )
        result = cursor.fetchone()

        cursor.close()
        conn.close()

        if result is None:
            return jsonify({"error": "Chip not found"}), 404

        return jsonify(result)

    except Error as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=os.environ.get('FLASK_PORT', 5000))