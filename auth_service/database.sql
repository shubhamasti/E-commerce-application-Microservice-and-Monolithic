CREATE DATABASE IF NOT EXISTS user_auth_ecommerce;

USE user_auth_ecommerce;

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