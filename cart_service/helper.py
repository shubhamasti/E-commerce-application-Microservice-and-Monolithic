import mysql.connector as m

con = m.connect(host="host.docker.internal", user="root", \
    password="root1234")
cursor = con.cursor()

def add_to_cart(email, prod_id, qty):
    cursor.execute('INSERT INTO cart_ecommerce.cart VALUES (%s, %s, %s)', (email, prod_id, qty))
    con.commit()
    
def get_cart_items(email):
    cursor.execute('SELECT p.name, p.price, c.quantity, ROUND(p.price*c.quantity, 2) \
        FROM product_ecommerce.products p, cart_ecommerce.cart c WHERE c.email = %s AND c.productId = p.productId', (email,))
    return cursor.fetchall()