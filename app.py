from flask import Flask, render_template, redirect, url_for, request, session
from helper import *

app = Flask(__name__)
app.secret_key = 'your secret key'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home', methods=['GET', 'POST'])
def home():
    top_prod = get_top_products(50)
    
    if request.method == 'POST':
        search = request.form['searchQuery']
        products = search_products(search)
        return render_template('search.html', products=products, search=search)
    
    return render_template('home.html', top_prod=top_prod)

@app.route('/search')
def search(products):
    if request.method == 'POST':
        search = request.form['searchQuery']
        products = search_products(search)
        return render_template('search.html', products=products, search=search)
    return render_template('search.html', products=products, search=search)

@app.route('/register', methods=['GET', 'POST'])
def register():
    # return render_template('register.html')
    msg = ''
    if request.method == 'POST':
        # create variables for easy access
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

            session ['loggedin'] = True
            session ['email'] = email

            return redirect(url_for('home'))
    
    return render_template('register.html', msg=msg)
    
@app.route('/login', methods=['GET', 'POST'])
def login():
    msg = ''
    if request.method == 'POST':
        # create variables for easy access
        email = request.form['email']
        password = request.form['password']

        account = login_check(email, password)

        if account:
            # create session data, we can access this data in other routes
            session['loggedin'] = True
            session['email'] = account[0]

            return redirect(url_for('home'))
        else:
            msg = 'Incorrect username/password!'
    
    # show the login form with message (if any)
    return render_template('login.html', msg=msg)

@app.route('/productDescription/<prod_id>', methods=['GET', 'POST'])
def productDescription(prod_id):
    info = get_prod_details(prod_id)
    
    if request.method == 'POST':
        if 'email' in session:
            email = session['email']
            quantity = request.form['quantity']
            add_to_cart(email, prod_id, quantity)
            return redirect(url_for('cart'))
        else:
            return redirect(url_for('login'))
    
    return render_template('productDescription.html', data=info)

@app.route('/cart', methods=['GET', 'POST'])
def cart():
    email = session['email']
    items = get_cart_items(email)
    subtotal = round(sum([item[-1] for item in items]), 2)
    
    if request.method == 'POST':
        subtotal = request.form['subtotal']
        return redirect(url_for('checkout', subtotal=subtotal))
    
    return render_template('cart.html', products=items, subtotal=subtotal)

@app.route('/checkout', methods=['GET', 'POST'])
def checkout():
    subtotal = float(request.args.get('subtotal'))
    email = session['email']
    tax = round(subtotal * 0.06, 2)
    total = round(subtotal + tax, 2)
    
    if request.method == 'POST':
        # clear cart
        # add bill to database
        insert_bill(email, subtotal, tax, total)
        clear_cart(email)
        return redirect(url_for('thankyou'))
    
    return render_template('checkout.html', account=email, costs=[subtotal, tax, total])

@app.route('/thankyou')
def thankyou():
    return render_template('thankyou.html')

@app.route('/bills')
def bills():
    email = session['email']
    bills = get_bills(email)
    return render_template('bills.html', bills=bills)


if __name__ == '__main__':
    app.run(port=8000, debug=True)