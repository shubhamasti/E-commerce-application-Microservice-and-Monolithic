from flask import Flask, render_template, redirect, url_for, request, session
import requests  # Import requests library for making HTTP requests
from helper import *
import jwt


app = Flask(__name__)
app.secret_key = 'your secret key'
jwt_secret_key = "secret"

gateway_url = "http://0.0.0.0:8080"
auth_service_url = "http://0.0.0.0:8081"
product_service_url = "http://0.0.0.0:8082"
bill_service_url = "http://0.0.0.0:8084"


# Route for adding items to the cart
@app.route('/add_cart', methods=['GET', 'POST'])
def add_cart():
    try:
        token = request.args.get('token')
        if token:
            payload = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
            session['email'] = payload['email']
            session['quantity'] = payload['quantity']
            session['prod_id'] = payload['prod_id']
            add_to_cart(session['email'], session['prod_id'], session['quantity'])
            return redirect(f"{product_service_url}/home")
        else:
            return 'Failed to add item to cart', 500
    except:
        pass


# Route for displaying the cart
@app.route('/cart', methods=['GET', 'POST'])
def cart():
    if 'email' in session:
        email = session['email']
        items = get_cart_items(email)
        subtotal = round(sum([item[-1] for item in items]), 2)
        
        if request.method == 'POST':
            token = jwt.encode({'email': email, 'subtotal': subtotal}, jwt_secret_key, algorithm='HS256')
            return redirect(f"{gateway_url}/checkout?token={token}")
        else:
            return render_template('cart.html', products=items, subtotal=subtotal)
    else:
        return redirect(f"{auth_service_url}/index")


@app.route('/home', methods=['GET', 'POST'])
def home():
    email = session.get('email')
    if email:
        return redirect(f"{product_service_url}/home")
    else:
        return redirect(f"{auth_service_url}")


@app.route('/bills', methods=['GET', 'POST'])
def bills():
    token = request.args.get('token')
    if token:
        payload = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
        session['email'] = payload['email']
        return redirect(f"{gateway_url}/bills?token={token}")
    else:
        return redirect(f"{auth_service_url}")
    
    
@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    if request.method == 'POST':
        subtotal = float(request.form['subtotal'])
        email = session['email']
        tax = round(subtotal * 0.06, 2)
        total = round(subtotal + tax, 2)
        
        token = jwt.encode({'email': email, 'subtotal': subtotal, 'tax': tax, 'total':total}, \
            jwt_secret_key, algorithm='HS256')
        
        return redirect(f"{gateway_url}/checkout?token={token}")
        
    
    return render_template('checkout.html', account=email, costs=[subtotal, tax, total])


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8083, debug=True)