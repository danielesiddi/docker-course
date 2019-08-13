import argparse
import logging
import os
from flask import Flask, request
import json
from flaskext.mysql import MySQL      # For newer versions of flask-mysql
# from flask.ext.mysql import MySQL   # For older versions of flask-mysql
app = Flask(__name__)

mysql = MySQL()

# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = os.getenv('MYSQL_DATABASE_USER','root')
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
    logging.debug("Function get_user called with argument {}".format(user_id))
    try:
        user=cursor.execute("SELECT * FROM employees WHERE id={}".format(user_id))
        logging.debug(user)
    except:
        return json.dumps({'success': False})
    if not user:
        logging.error("User not found")
        return json.dumps({'success': False})
    return json.dumps({'success': True, 'result': cursor.fetchone()})

@app.route("/user", methods=['POST'])
def add_user():
    logging.debug("Function add_user called with body payload {}".format(request.json))
    name=request.json['name']
    try:
        data=cursor.execute("INSERT INTO employees (name) VALUES ('{}');".format(name))
        logging.debug(data)
        conn.commit()
    except:
        logging.error("Error in add_user function")
        return json.dumps({'success': False})

    logging.info("User {} added successfully".format(name))
    return json.dumps({'success': True})

@app.route("/user/<int:user_id>", methods=['PUT'])
def set_user(user_id):
    logging.debug("Function set_user called with body payload {}".format(request.json))
    name=request.json['name']
    try:
        cursor.execute("UPDATE employees SET name='{}' WHERE id='{}'".format(name, user_id))
        conn.commit()
    except:
        logging.error("Error in set_user function")
        return json.dumps({'success': False})

    logging.info("User {} successfully renamed to {}".format(user_id, name))
    return json.dumps({'success': True})

@app.route('/users', methods=['GET'])
def get_users():
    try:
        cursor.execute("SELECT * FROM employees")
        data = cursor.fetchall()
        return json.dumps({'success': True, 'result': data})
        #for row in data:
        #    result.append({'id': row[0], 'name': row[1]})
    except:
        return json.dumps({'success': False})
    return json.dumps({'success': True, 'result': result})

if __name__ == "__main__":
    
    parser = argparse.ArgumentParser()
    parser.add_argument("-v","--verbose",help='Verbose', required=False, action='store_true')
    args = parser.parse_args()

    if args.verbose:
        logging.getLogger().setLevel(logging.DEBUG)

    app.run(port=6000,host='0.0.0.0')
