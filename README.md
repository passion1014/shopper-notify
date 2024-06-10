# shopper-notify
shopper notify


# Category Table
 CREATE TABLE IF NOT EXISTS CATEGORY (
  category_id VARCHAR(255) PRIMARY KEY,
  depth INT,
  text VARCHAR(255),
  parent_id INT
)