import mysql.connector as m

con = m.connect(host = "host.docker.internal", user = "root", password = "####",
                database = "user_auth_ecommerce")
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