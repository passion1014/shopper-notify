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
parent_id VARCHAR(255),
CREATE_DT DATETIME
)

## Product

CREATE TABLE IF NOT EXISTS PRODUCT (
product_id VARCHAR(255) PRIMARY KEY,
name VARCHAR(255),
category_id VARCHAR(255) REFERENCES CATEGORY(category_id),
image_src VARCHAR(255),
rocket_yn CHAR(1),
price NUMBER,
CREATE_DT DATETIME
)


# 확인사항
- 로켓배송여부(로켓배송, 로켓설치) 뭔지
- 쿠폰할인가 기준 여부 조회 조건 추가

