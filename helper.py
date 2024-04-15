import mysql.connector as m

con = m.connect(host = "localhost", user = "root", password = "root1234",
                database = "ecommerce_mono")
cursor = con.cursor()

def user_exists(email):
    cursor.execute('SELECT * FROM users WHERE email = %s', (email,))
    if cursor.fetchone():
        return cursor.fetchone()
    return None

def create_account(email, password, fname, lname, street, city, state, zipcode, phone_no):
    cursor.execute('INSERT INTO users VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)', 
                   (email, password, fname, lname, street, city, state, zipcode, phone_no))
    con.commit()

def login_check(email, password):
    cursor.execute('SELECT email FROM users WHERE email = %s AND pwd = %s', (email, password))
    return cursor.fetchone()

def get_top_products(n):
    cursor.execute('SELECT * FROM products ORDER BY RAND() LIMIT %s', (n,))
    return cursor.fetchall()

def get_prod_details(prod_id):
    cursor.execute('SELECT * FROM products WHERE productId = %s', (prod_id,))
    return cursor.fetchone()

def add_to_cart(email, prod_id, qty):
    cursor.execute('INSERT INTO cart VALUES (%s, %s, %s)', (email, prod_id, qty))
    con.commit()
    
def get_cart_items(email):
    cursor.execute('SELECT p.name, p.price, c.quantity, ROUND(p.price*c.quantity, 2) \
        FROM products p, cart c WHERE c.email = %s AND c.productId = p.productId', (email,))
    return cursor.fetchall()

def search_products(search_term):
    # match name or description
    cursor.execute('SELECT * FROM products WHERE name LIKE %s OR description LIKE %s', 
                   ('%'+search_term+'%', '%'+search_term+'%'))
    return cursor.fetchall()