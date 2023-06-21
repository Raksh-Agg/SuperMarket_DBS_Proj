-- We don't check whether the database already exists over here, since, we handled that in your main
-- This is only the code which initializes the database if it did not exist before
-- If it already exists, then that table itself would be edited, so that, the user can maintain their progress across multiple access sessions
-- Uncomment the following line, if you want to re-initialize whole DataBase
-- DROP DATABASE IF EXISTS SuperMarket_1463_1458;
CREATE DATABASE SuperMarket_1463_1458;
use SuperMarket_1463_1458;
-- Over Here, we assume that each individual has a unique phone number, for all Suppliers, Customer, Employee
-- Creating Table for Employee, which contains Employee Personal details
-- Each Employee has an attribute Amount Sold, on the basis of which, we judge the performance of the Employee. This value updates each time an employee helps facilitate a Sale
CREATE TABLE Employee (
    Emp_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL ,
    Emp_First_Name VARCHAR(50) NOT NULL,
    Emp_Second_Name VARCHAR(50) NOT NULL,
    Emp_Salary INT NOT NULL,
    Emp_Amount_Sold INT NOT NULL,
    Emp_Designation ENUM('Custodian', 'Security', 'Manager', 'Supervisor', 'Cashier') NOT NULL,
    Emp_Phone_Number BIGINT NOT NULL UNIQUE,
    Emp_Sex ENUM('M','F') NOT NULL,
    Emp_Address_Line_One VARCHAR(100) NOT NULL,
    Emp_Address_Line_Two VARCHAR(100),
    Emp_Postal_Code INT NOT NULL
);
-- Creating Table for Customer, which contains Customer Personal details
CREATE TABLE Customer (
    Cust_ID INT AUTO_INCREMENT PRIMARY KEY ,
    Cust_First_Name VARCHAR(50) NOT NULL,
    Cust_Second_Name VARCHAR(50) NOT NULL,
    Cust_Phone_Number BIGINT NOT NULL UNIQUE,
    Cust_Amount_Spent INT NOT NULL,
    Cust_Address_Line_One VARCHAR(100) NOT NULL,
    Cust_Address_Line_Two VARCHAR(100),
    Cust_Postal_Code INT NOT NULL
);
-- Creating Table for Supplier, which contains Supplier details
CREATE TABLE Supplier (
    Supplier_ID INT AUTO_INCREMENT PRIMARY KEY ,
    Supplier_First_Name VARCHAR(50) NOT NULL,
    Supplier_Second_Name VARCHAR(50) NOT NULL,
    Supplier_Phone_Number BIGINT NOT NULL UNIQUE,
    Supplier_Amount_Earnt INT NOT NULL,
    Supplier_Address_Line_One VARCHAR(100) NOT NULL,
    Supplier_Address_Line_Two VARCHAR(100),
    Supplier_Postal_Code INT NOT NULL
);
-- Creating Table for Product, which contains Product details
CREATE TABLE Product (
    Product_ID INT AUTO_INCREMENT PRIMARY KEY ,
    Product_Name VARCHAR(50) NOT NULL,
    Price INT NOT NULL,
    Qty_Left INT NOT NULL
);
-- Creating Table for Purchases between Supplier and SuperMarket
CREATE TABLE Purchase(
    Purchase_ID INT AUTO_INCREMENT PRIMARY KEY ,
    Purchase_Date DATE NOT NULL,
    Supplier_ID INT,
    FOREIGN KEY (Supplier_ID) REFERENCES Supplier(Supplier_ID) ON DELETE CASCADE
);
-- Table, which contains which product, and quantity of that product which was included in a given Purchase
CREATE TABLE Purchase_has_Product (
    Purchase_ID INT ,
    Product_ID INT ,
    Qty_Bought INT NOT NULL,
    -- PRIMARY KEY(Purchase_ID, Product_ID),
    FOREIGN KEY (Purchase_ID) REFERENCES Purchase(Purchase_ID) ON DELETE CASCADE,
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID) ON DELETE CASCADE
);
-- Creating Table for Sales between Customer and SuperMarket, where, an Employee helps facilitate the Sale
CREATE TABLE Sale (
    Sale_ID INT AUTO_INCREMENT PRIMARY KEY NOT NULL ,
    Sale_Date DATE NOT NULL,
    Cust_ID INT,
    Emp_ID INT,
    FOREIGN KEY (Cust_ID) REFERENCES Customer(Cust_ID) ON DELETE CASCADE,
    FOREIGN KEY (Emp_ID) REFERENCES Employee(Emp_ID) ON DELETE CASCADE
);
-- Table, which contains which product, and quantity of that product which was included in a given Sale
CREATE TABLE Sale_has_Product(
    Sale_ID INT ,
    Product_ID INT ,
    Qty_Bought INT NOT NULL,
    -- PRIMARY KEY (Sale_ID, Product_ID),
    FOREIGN KEY (Sale_ID) REFERENCES Sale(Sale_ID) ON DELETE CASCADE,
    FOREIGN KEY (Product_ID) REFERENCES Product(Product_ID) ON DELETE CASCADE
);
-- Following are the queries to insert Sample Data to all the tables
INSERT INTO Employee (Emp_First_Name, Emp_Second_Name, Emp_Salary, Emp_Amount_Sold, Emp_Designation, Emp_Phone_Number, Emp_Sex, Emp_Address_Line_One, Emp_Address_Line_Two, Emp_Postal_Code)
VALUES 
    ('John', 'Doe', 50000, 100000, 'Manager', 1234567890, 'M', '123 Main Street', 'Apt 4', 123545),
    ('Jane', 'Doe', 40000, 75000, 'Supervisor', 2345678901, 'F', '456 Oak Ave', NULL, 238456),
    ('Bob', 'Smith', 35000, 50000, 'Cashier', 3456789012, 'M', '789 Elm St', NULL, 345667),
    ('Alice', 'Johnson', 30000, 25000, 'Custodian', 4567890123, 'F', '12 Pine Rd', NULL, 475678),
    ('James', 'Williams', 45000, 80000, 'Security', 5678901234, 'M', '34 Maple Dr', 'Unit B', 516789),
    ('Emily', 'Brown', 37500, 55000, 'Cashier', 6789012345, 'F', '567 Cherry Ln', NULL, 670890),
    ('David', 'Jones', 42500, 70000, 'Supervisor', 7890123456, 'M', '890 Oak St', 'Suite 2', 078901),
    ('Vikram', 'Joshi', 35000, 20000, 'Manager', 9876543210, 'M', '20/A, Park Street', 'Kolkata', 700001),
    ('Anjali', 'Sharma', 25000, 15000, 'Cashier', 9876543211, 'F', '12/B, MG Road', 'Mumbai', 400001),
    ('Pradeep', 'Singh', 30000, 10000, 'Supervisor', 9876543212, 'M', '56, Ganga Nagar', 'Delhi', 110001),
    ('Meera', 'Patel', 20000, 8000, 'Custodian', 9876543213, 'F', '13/C, Ramesh Nagar', 'Hyderabad', 500001),
    ('Ravi', 'Kumar', 22000, 12000, 'Security', 9876543214, 'M', '102, Panjabari', 'Guwahati', 781037);
INSERT INTO Customer (Cust_First_Name, Cust_Second_Name, Cust_Phone_Number, Cust_Amount_Spent, Cust_Address_Line_One, Cust_Address_Line_Two, Cust_Postal_Code)
VALUES 
    ('Amy', 'Smith', 9876543210, 5000, '123 Main Street', 'Apt 4', 128345),
    ('Bob', 'Johnson', 8765432109, 7500, '456 Oak Ave', NULL, 234056),
    ('Charlie', 'Williams', 7654321098, 10000, '789 Elm St', NULL, 034567),
    ('David', 'Brown', 6543210987, 12500, '12 Pine Rd', NULL, 450678),
    ('Emily', 'Jones', 5432109876, 15000, '34 Maple Dr', 'Unit B', 560789),
    ('Rahul', 'Shah', 7896541230, 5000, '34, Bapuji Nagar', 'Bhubaneswar', 751009),
    ('Shweta', 'Sinha', 7896541231, 7000, '12, Gandhi Nagar', 'Chennai', 600001),
    ('Amit', 'Chatterjee', 7896541232, 15000, '2, Salt Lake', 'Kolkata', 700064),
    ('Smita', 'Rao', 7896541233, 8000, '4, Bhoiwada', 'Mumbai', 400002),
    ('Rajesh', 'Patil', 7896541234, 12000, '22, Jangli Maharaj Road', 'Pune', 411004);
INSERT INTO Supplier (Supplier_First_Name, Supplier_Second_Name, Supplier_Phone_Number, Supplier_Amount_Earnt, Supplier_Address_Line_One, Supplier_Address_Line_Two, Supplier_Postal_Code)
VALUES 
    ('Mark', 'Wilson', 1234567890, 10000, '123 Main St', NULL, 123745),
    ('Sarah', 'Thomas', 2345678901, 15000, '456 Elm St', 'Apt 5', 273456),
    ('David', 'Lee', 3456789012, 20000, '789 Oak Ave', NULL, 345867),
    ('Karen', 'Nguyen', 4567890123, 25000, '1011 Maple Dr', NULL, 459678),
    ('Chris', 'Jones', 5678901234, 30000, '1213 Pine Rd', 'Unit C', 506789),
    ('Ravi', 'Sharma', 9876543200, 50000, '12, Church Street', 'Bangalore', 560001),
    ('Priya', 'Gupta', 9876543201, 60000, '24, Park Avenue', 'Mumbai', 400001),
    ('Alok', 'Verma', 9876543202, 40000, '78, Model Town', 'Delhi', 110009),
    ('Asha', 'Kulkarni', 9876543203, 30000, '3, Kirti Nagar', 'Chennai', 600001),
    ('Gopal', 'Sethi', 9876543204, 20000, '10, Raja Bazar', 'Kolkata', 700016);
INSERT INTO Product (Product_Name, Price, Qty_Left)
VALUES 
    ('iPhone 12', 1000, 10),
    ('Samsung Galaxy S21', 900, 15),
    ('Google Pixel 5', 800, 12),
    ('MacBook Air', 1200, 8),
    ('Dell XPS 13', 1100, 9),
    ('HP Spectre x360', 1000, 11),
    ('Sony PlayStation 5', 500, 20),
    ('Microsoft Xbox Series X', 500, 18),
    ('Nintendo Switch', 300, 25),
    ('Bose QuietComfort 35 II', 350, 30),
    ('Sony WH-1000XM4', 400, 28),
    ('Apple AirPods Pro', 250, 35),
    ('Samsung Galaxy Buds Pro', 200, 40),
    ('Sony WF-1000XM3', 300, 32),
    ('JBL Flip 5', 100, 50);
INSERT INTO Purchase (Purchase_Date, Supplier_ID)
VALUES 
    ('2023-04-06', 1),
    ('2023-04-05', 2),
    ('2023-04-04', 3),
    ('2023-04-03', 4),
    ('2023-04-02', 5),
    ('2023-04-01', 1),
    ('2023-03-31', 2),
    ('2023-02-04', 7),
    ('2023-03-06', 9),
    ('2023-04-18', 1);
INSERT INTO Purchase_has_Product (Purchase_ID, Product_ID, Qty_Bought)
VALUES 
    (1, 1, 5),
    (1, 2, 10),
    (2, 2, 5),
    (2, 3, 8),
    (3, 4, 3),
    (3, 5, 4),
    (4, 6, 7),
    (4, 7, 9),
    (5, 8, 6),
    (5, 9, 7),
    (6, 10, 12),
    (6, 11, 15),
    (7, 12, 10),
    (7, 13, 8),
    (7, 10, 2),
    (8, 2, 4),
    (8, 4, 1),
    (9, 2, 5),
    (9, 11, 8),
    (10, 4, 4),
    (10, 8, 1),
    (10, 7, 10);
INSERT INTO Sale (Sale_Date, Cust_ID, Emp_ID) VALUES
    ('2022-03-01', 1, 1),
    ('2022-04-15', 2, 2),
    ('2022-05-10', 3, 3),
    ('2022-06-21', 4, 4),
    ('2022-07-14', 5, 5),
    ('2022-08-06', 1, 6),
    ('2022-09-30', 2, 7),
    ('2022-12-17', 1, 3),
    ('2022-04-10', 4, 2),
    ('2022-01-29', 5, 2),
    ('2022-03-14', 7, 8),
    ('2022-06-29', 8, 6);
INSERT INTO Sale_has_Product (Sale_ID, Product_ID, Qty_Bought) VALUES
    (1, 1, 2),
    (1, 2, 1),
    (1, 3, 5),
    (2, 4, 3),
    (2, 5, 2),
    (2, 6, 1),
    (3, 7, 4),
    (3, 8, 2),
    (4, 9, 1),
    (4, 10, 3),
    (5, 11, 2),
    (5, 12, 1),
    (6, 13, 5),
    (6, 14, 3),
    (6, 15, 2),
    (7, 1, 4),
    (7, 2, 1),
    (7, 3, 2),
    (8, 1, 4),
    (8, 8, 8),
    (9, 10, 4),
    (9, 12, 5),
    (10, 6, 7),
    (11, 4, 1),
    (11, 2, 3),
    (11, 9, 7),
    (12, 3, 2);