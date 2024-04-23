from flask import Flask, request, redirect
import requests as re
import jwt
from helper import *

app = Flask(__name__)
jwt_secret_key = "secret"

auth_service_url = "http://0.0.0.0:8081"
product_service_url = "http://0.0.0.0:8082"
cart_service_url = "http://0.0.0.0:8083"
bill_service_url = "http://0.0.0.0:8084"


@app.route('/index')
def index():
    return redirect(f"{auth_service_url}")


@app.route('/login', methods=['GET', 'POST'])
def login():
    token = request.args.get('token')
    if token:
        try:
            return redirect(f"{product_service_url}/home?token={token}")
        except jwt.ExpiredSignatureError:
            return "Token expired. Please log in again."
        except jwt.InvalidTokenError:
            return "Invalid token. Please log in again."
    else:
        return redirect(f"{auth_service_url}")
    

@app.route('/add_cart', methods=['GET', 'POST'])
def add_cart():
    token = request.args.get('token')
    if token:
        return redirect(f"{cart_service_url}/add_cart?token={token}")
    else:
        return "No token provided", 400

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    token = request.args.get('token')
    if token:
        return redirect(f"{cart_service_url}/cart?token={token}")
    else:
        return "No token provided", 400

    
@app.route('/bills', methods=['GET', 'POST'])
def bills():
    token = request.args.get('token')
    if token:
        return redirect(f"{bill_service_url}/bills?token={token}")
    else:
        return "No token provided", 400


@app.route('/checkout', methods=['GET', 'POST'])    
def checkout():
    token = request.args.get('token')
    if token:
        data = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
        email = data['email']
        subtotal = data['subtotal']
        tax = data['tax']
        total = data['total']
        token = jwt.encode({'email': email, 'subtotal': subtotal, 'tax': tax, 'total': total}, \
            jwt_secret_key, algorithm='HS256')
        return redirect(f"{bill_service_url}/checkout?token={token}")
    else:
        return "No token provided", 400


@app.route('/home', methods=['GET', 'POST'])
def home():
    token = request.args.get('token')
    if token:
        return redirect(f"{product_service_url}/home?token={token}")
    else:
        return redirect(f"{product_service_url}/login")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)