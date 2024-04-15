CREATE DATABASE IF NOT EXISTS ecommerce_mono;

USE ecommerce_mono;

CREATE TABLE IF NOT EXISTS users (
    email VARCHAR(30) PRIMARY KEY,
    pwd VARCHAR(20),
    firstName VARCHAR(25),
    lastName VARCHAR(25),
    street VARCHAR(30),
    city VARCHAR(20),
    state VARCHAR(15),
    zipcode CHAR(6),
    phone CHAR(10)
);

CREATE TABLE IF NOT EXISTS products (
    productId INT PRIMARY KEY,
    name VARCHAR(50),
    price FLOAT,
    description VARCHAR(100),
    stock INT
);

CREATE TABLE IF NOT EXISTS cart (
    email VARCHAR(30),
	productId INT,
    quantity INT,
    FOREIGN KEY(email) REFERENCES users(email),
    FOREIGN KEY(productId) REFERENCES products(productId)
);