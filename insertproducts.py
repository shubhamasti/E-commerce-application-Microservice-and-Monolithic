# %%
import mysql.connector as m
import random
from faker import Faker

# %%
con =m.connect(
    host='localhost',
    database='ecommerce_mono',
    user='root',
    password='####'
)

# %%
fake = Faker()

# Generate fake products
def generate_fake_product(product_id):
    # Generate name based on a combination of categories and adjectives
    name = fake.random_element(["Men's", "Women's", "Kids'", "Unisex"]) + ' ' + \
           fake.random_element(["Casual", "Formal", "Sporty", "Trendy"]) + ' ' + \
           fake.random_element(["Shirt", "Dress", "Jeans", "Sneakers", "Jacket", "Skirt", "Boots", "Bag"])
    price = round(random.uniform(5.0, 100.0), 2)
    description = fake.random_element(["High quality ", "Good quality ", "Stylish ", "Trendy ", "New "]) + name.lower() + " made from " + \
    fake.random_element(["premium", "organic", "sustainable", "eco-friendly"]) + " materials."
    stock = random.randint(0, 100)
    return product_id, name, price, description, stock

def populate_table(n):
    cur = con.cursor()
    fake_products = [generate_fake_product(id) for id in range(n)]
    cur.executemany("INSERT INTO products VALUES (%s, %s, %s, %s, %s)", fake_products)
    con.commit()
    cur.close()

# Example: Generate 10 fake products
populate_table(100)

# %%
con.close()

# %%
