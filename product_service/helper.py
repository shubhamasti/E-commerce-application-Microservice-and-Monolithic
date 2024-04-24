import mysql.connector as m

con = m.connect(host = "host.docker.internal", user = "root", password = "####",
                database = "product_ecommerce")
cursor = con.cursor()

def get_top_products(n):
    cursor.execute('SELECT * FROM products ORDER BY RAND() LIMIT %s', (n,))
    return cursor.fetchall()

def get_prod_details(prod_id):
    cursor.execute('SELECT * FROM products WHERE productId = %s', (prod_id,))
    return cursor.fetchone()

def search_products(search_term):
    # match name or description
    cursor.execute('SELECT * FROM products WHERE name LIKE %s OR description LIKE %s', 
                   ('%'+search_term+'%', '%'+search_term+'%'))
    return cursor.fetchall()