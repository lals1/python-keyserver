from flask import Flask, jsonify
from flask import abort
from flask import request
import logging
from flask import Flask, render_template
from flask_basicauth import BasicAuth

import MySQLdb


#from OpenSSL import SSL
#context = SSL.Context(SSL.SSLv23_METHOD)
#context.use_privatekey_file('key.pem')
#context.use_certificate_file('cert.pem')

app = Flask(__name__)

app.config['BASIC_AUTH_USERNAME'] = 'admin'
app.config['BASIC_AUTH_PASSWORD'] = 'allgood'

basic_auth = BasicAuth(app)

logger = logging.getLogger('werkzeug')
handler = logging.FileHandler('access.log')
logger.addHandler(handler)



@app.route('/showallkeys', methods=['GET'])
@basic_auth.required
def show_keys():
        connection = MySQLdb.connect (host = "db", user = "root", passwd = "", db = "secret")
        cursor = connection.cursor ()
        cursor.execute ("SELECT * from crypto")
        row = cursor.fetchall ()
        cursor.close ()
        connection.commit ()
        connection.close ()

        return jsonify({'keys': row})

@app.route('/getkey/<string:task_id>', methods=['GET'])
@basic_auth.required
def get_task(task_id):
        connection = MySQLdb.connect (host = "db", user = "root", passwd = "", db = "secret")
        cursor = connection.cursor ()
        cursor.execute ("SELECT * from crypto where uid = '" + task_id + "'")
        row = cursor.fetchall ()
        cursor.execute ("UPDATE crypto SET count = count + 1 where uid = '" + task_id + "'")
        cursor.close ()
        connection.commit ()
        connection.close ()

        if len(row) == 0:
                abort(404)
        if len(row[0]) == 0:
                abort(404)
        task = row[0][1]
        count = row[0][2]
        if count > 15:
            return jsonify({'Key usage limit exceed for uid': task_id})
        else:
            return jsonify({'key': task})


@app.route('/register', methods=['GET'])
def register_key():
   uid1 = request.args.get('uid')
   cryptokey1 = request.args.get('cryptokey')
   connection = MySQLdb.connect (host = "db", user = "root", passwd = "", db = "secret")

   cursor = connection.cursor ()

   sql = "INSERT INTO crypto (uid, cryptokey) VALUES (%s, %s)"
   val = (uid1,cryptokey1)

   cursor.execute(sql, val)

   connection.commit()

   return jsonify({'Registration successfull for uid': uid1 })

@app.route('/updatekey', methods=['GET'])
def update_key():
   uid1 = request.args.get('uid')
   cryptokey1 = request.args.get('cryptokey')
   connection = MySQLdb.connect (host = "db", user = "root", passwd = "", db = "secret")

   cursor = connection.cursor ()

   cursor.execute ("""
   UPDATE crypto
   SET cryptokey=%s
   WHERE uid=%s
""", (cryptokey1,uid1))

   connection.commit()

   return jsonify({'key update successfull for uid': uid1 })

@app.errorhandler(404)
def not_found(e):
        return jsonify({'No key found in database for uid': task_id })


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
    app.logger.addHandler(handler)
