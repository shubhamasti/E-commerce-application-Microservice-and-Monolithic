CREATE DATABASE IF NOT EXISTS bills_ecommerce;

USE bills_ecommerce;

CREATE TABLE IF NOT EXISTS bill(
    billId INT PRIMARY KEY,
    email VARCHAR(30),
    subtotal FLOAT,
    tax FLOAT,
    total FLOAT,
    date DATE
);