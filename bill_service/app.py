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


@app.route('/bills')
def bills():
    token = request.args.get('token')
    if token:
        payload = jwt.decode(token, jwt_secret_key, algorithms=['HS256'])
        session['email'] = payload['email']
        bills = get_bills(session['email'])
        return render_template('bills.html', bills=bills)
    else:
        return redirect(f"{auth_service_url}/index")
    

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    data = jwt.decode(request.args.get('token'), jwt_secret_key, algorithms=['HS256'])
    
    if data:
        session['email'] = data['email']
        email = data['email']
        subtotal = data['subtotal']
        tax = data['tax']
        total = data['total']
        
        if request.method == 'POST':
            # clear cart
            insert_bill(email, subtotal, tax, total)
            clear_cart(email)
            return redirect(url_for('thankyou'))
    
        return render_template('checkout.html', account=email, costs=[subtotal, tax, total])
    else:
        return redirect(f"{auth_service_url}/index")


@app.route('/home', methods=['GET', 'POST'])
def home():
    email = session['email']
    if email:
        return redirect(f"{product_service_url}/home")
    else:
        return redirect(f"{auth_service_url}")


@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8084, debug=True)