from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from helper import user_exists, create_account, login_check
from datetime import datetime, timedelta
import jwt

app = Flask(__name__)
app.secret_key = "your_secret_key"

gateway_url = "http://0.0.0.0:8080"
jwt_secret_key = "secret"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    msg = ''
    if request.method == 'POST':
        email = request.form['email']
        pwd = request.form['password']
        fname = request.form['firstName']
        lname = request.form['lastName']
        street = request.form['street']
        city = request.form['city']
        state = request.form['state']
        zipcode = request.form['zipcode']
        phone_no = request.form['phone']
        account = user_exists(email)

        if account:
            msg = 'Account already exists!'
        else:
            create_account(email, pwd, fname, lname, street, city, state, zipcode, phone_no)
            msg = 'You have successfully registered!'

            token = jwt.encode({'email': email}, jwt_secret_key, algorithm='HS256')
            return redirect(f"{gateway_url}/login?token={token}")
            

    return render_template('register.html', msg=msg)

@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        account = login_check(email, password)

        if account:
            token = jwt.encode({'email': email}, jwt_secret_key, algorithm='HS256')
            return redirect(f"{gateway_url}/login?token={token}")
        else:
            msg = 'Incorrect username/password!'

    return render_template('login.html', msg=msg)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8081, debug=True)