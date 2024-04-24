import mysql.connector as m

con = m.connect(host = "host.docker.internal", user = "root", password = "####")
cursor = con.cursor()

def insert_bill(email, subtotal, tax, total):
    # get last bill no and current date
    cursor.execute('SELECT MAX(billId) FROM bills_ecommerce.bill')
    # if no bills exist, set bill no to 1
    bill_no = cursor.fetchone()[0]
    if not bill_no:
        bill_no = 1
    else:
        bill_no += 1
        
    cursor.execute('SELECT CURDATE()')
    date = cursor.fetchone()[0]
    
    cursor.execute('INSERT INTO bills_ecommerce.bill VALUES (%s, %s, %s, %s, %s, %s)',
                     (bill_no, email, subtotal, tax, total, date))
    con.commit()

def clear_cart(email):
    cursor.execute('DELETE FROM cart_ecommerce.cart WHERE email = %s', (email,))
    con.commit()
    
def get_bills(email):
    cursor.execute('SELECT * FROM bills_ecommerce.bill WHERE email = %s', (email,))
    return cursor.fetchall()