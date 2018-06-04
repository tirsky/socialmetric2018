from flask import Flask, request, jsonify, session
from flask.ext.sqlalchemy import SQLAlchemy
from config import BaseConfig
import hashlib, uuid

# config

app = Flask(__name__)
app.config.from_object(BaseConfig)

db = SQLAlchemy(app)

from models import User


# routes

@app.route('/')
def index():
    return app.send_static_file('index.html')


@app.route('/api/register', methods=['POST'])
def register():
    json_data = request.json
    user = User(
        email=json_data['email'],
        password=json_data['password']
    )
    try:
        db.session.add(user)
        db.session.commit()
        status = 'success'
    except:
        status = 'this user is already registered'
    db.session.close()
    return jsonify({'result': status})


@app.route('/api/login', methods=['POST'])
def login():
    json_data = request.json
    user = User.query.filter_by(email=json_data['email']).first()
    salt = 'socialmetric'
    print((json_data['password'] + salt).encode())
    hashed_password = hashlib.sha512((json_data['password'] + salt).encode()).hexdigest()
    print(user.password,'   sdfdf   ',  hashed_password)
    if user and user.password == hashed_password:
        session['logged_in'] = True
        status = True
    else:
        status = False
    return jsonify({'result': status})


@app.route('/api/logout')
def logout():
    session.pop('logged_in', None)
    return jsonify({'result': 'success'})


@app.route('/api/status')
def status():
    if session.get('logged_in'):
        if session['logged_in']:
            return jsonify({'status': True})
    else:
        return jsonify({'status': False})


if __name__ == "__main__":
        app.run(host='0.0.0.0')
