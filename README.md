# shopper-notify

shopper notify

CREATE SCHEMA coupangdb;
USE mcoupangdbydb;

# Table

## Category

CREATE TABLE IF NOT EXISTS CATEGORY (
category_id VARCHAR(255) PRIMARY KEY,
depth INT,
text VARCHAR(255),
parent_id VARCHAR(255)
)

## Product

CREATE TABLE IF NOT EXISTS PRODUCT (
product_id VARCHAR(255) PRIMARY KEY,
category_id VARCHAR(255) REFERENCES CATEGORY(category_id),
text VARCHAR(255)

)
