CREATE DATABASE IF NOT EXISTS product_ecommerce;

USE product_ecommerce;

DROP TABLE IF EXISTS products;

CREATE TABLE products (
    productId INT PRIMARY KEY,
    name VARCHAR(50),
    price FLOAT,
    description VARCHAR(100),
    stock INT
);