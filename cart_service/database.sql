CREATE DATABASE IF NOT EXISTS cart_ecommerce;

USE cart_ecommerce;

CREATE TABLE IF NOT EXISTS cart (
    email VARCHAR(30),
    productId INT,
    quantity INT
);