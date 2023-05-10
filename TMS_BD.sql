CREATE TABLE customers (
    ID SERIAL PRIMARY KEY,
    UserID INT NOT NULL,
    UserName VARCHAR(100) NOT NULL,
    email VARCHAR(100),
    UNIQUE(UserID)
);

CREATE TABLE products (
    ID SERIAL PRIMARY KEY,
    ProductID INT NOT NULL,
    ProductName VARCHAR(100) NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    UNIQUE(ProductID, Price)
);

CREATE TABLE orders (
    ID SERIAL PRIMARY KEY,
    UserID INT NOT NULL,
    ProductID INT NOT NULL,
    Price DECIMAL(10,2) NOT NULL,
    FOREIGN KEY (UserID) REFERENCES customers (UserID),
    FOREIGN KEY (ProductID, Price) REFERENCES products(ProductID, Price)
);
