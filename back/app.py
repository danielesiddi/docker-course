import os
from flask import Flask
import json
from flaskext.mysql import MySQL      # For newer versions of flask-mysql
# from flask.ext.mysql import MySQL   # For older versions of flask-mysql
app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER','db_user')
app.config['MYSQL_DATABASE_PASSWORD'] = os.getenv('MYSQL_DATABASE_PASSWORD','K4ir0s')
app.config['MYSQL_DATABASE_DB'] = os.getenv('MYSQL_DATABASE_DB','employee_db')
app.config['MYSQL_DATABASE_HOST'] = os.getenv('MYSQL_DATABASE_HOST','localhost')
mysql.init_app(app)

try:
    conn = mysql.connect()
except:
    raise Exception('Server connection error')

cursor = conn.cursor()

@app.route("/user/<int:user_id>", methods=['GET'])
def get_user(user_id):
    try:
        user=cursor.execute("SELECT * FROM employees WHERE id={}".format(user_id))
    except:
        return json.dumps({'success': False})
    return json.dumps({'success': True, 'result': user})

@app.route("/user", methods=['POST'])
def add_user():
    try:
        cursor.execute("INSERT INTO employees VALUES ('','{}')".format(name))
    except:
        return json.dumps({'success': False})

@app.route("/user/<int:user_id>/<string:name>", methods=['PUT'])
def set_user(user_id, name):
    try:
        cursor.execute("UPDATE employees SET name='{}' WHERE id={}".format(name, user_id))
    except:
        return json.dumps({'success': False})

    return json.dumps({'success': True})

@app.route('/users', methods=['GET'])
def get_users():
    try:
        cursor.execute("SELECT * FROM employees")
        row = cursor.fetchone()
        result = []
        while row is not None:
            result.append(row[0])
            row = cursor.fetchone()
    except:
        return json.dumps({'success': False})
    return json.dumps({'success': True, 'result': result})

if __name__ == "__main__":
    app.run()
