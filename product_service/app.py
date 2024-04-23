from flask import Flask, render_template, redirect, url_for, request, session, jsonify
from helper import *
from functools import wraps
import requests as re
import jwt

app = Flask(__name__)
app.secret_key = 'your secret key'
jwt_secret_key = "secret"

gateway_url = "http://0.0.0.0:8080"

@app.route('/home', methods=['GET', 'POST'])
def home():
    try:
        token = request.args.get('token')
        if token:
            payload = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
            session['email'] = payload['email'] 
    except:
        pass

    top_prod = get_top_products(50)
    if request.method == 'POST':
        search = request.form['searchQuery']
        products = search_products(search)
        return render_template('search.html', products=products, search=search)
    
    return render_template('home.html', top_prod=top_prod)

@app.route('/productDescription/<prod_id>', methods=['GET', 'POST'])
def productDescription(prod_id):
    # user_data = request.user_data
    info = get_prod_details(prod_id)
    
    if request.method == 'POST':
        email = session['email']
        if email:
            quantity = request.form['quantity']
            token = jwt.encode({'email': email, 'quantity': quantity, 'prod_id': prod_id}, \
                jwt_secret_key, algorithm='HS256')
            return redirect(f"{gateway_url}/add_cart?token={token}")
        else:
            return redirect(f"{gateway_url}/index")
    
    return render_template('productDescription.html', data=info)


@app.route('/bills', methods=['GET', 'POST'])
def bills():
    email = session['email']
    if email:
        token = jwt.encode({'email': email}, jwt_secret_key, algorithm='HS256')
        return redirect(f"{gateway_url}/bills?token={token}")
    else:
        return redirect(f"{gateway_url}/index")


@app.route('/cart', methods=['GET', 'POST'])
def cart():
    email = session['email']
    if email:
        token = jwt.encode({'email': email}, jwt_secret_key, algorithm='HS256')
        return redirect(f"{gateway_url}/cart?token={token}")
    else:
        return redirect(f"{gateway_url}/index")


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8082, debug=True)