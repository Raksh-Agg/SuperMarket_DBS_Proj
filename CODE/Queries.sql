-- Following are the procedures written that provide functionality to the SuperMarket System

-- Inserting Into Customer, Giving all required entries as parameter, initializing the amount Spent by Customer to be 0 while registering
DELIMITER //
CREATE PROCEDURE insertIntoCustomer(IN input_First_Name VARCHAR(50), IN input_Second_Name VARCHAR(50), IN input_Phone_Number BIGINT, IN input_Address_Line_One VARCHAR(100), IN input_Address_Line_Two VARCHAR(100), IN input_Postal_Code INT)   
BEGIN  
INSERT INTO Customer (Cust_First_Name, Cust_Second_Name, Cust_Phone_Number, Cust_Amount_Spent, Cust_Address_Line_One, Cust_Address_Line_Two, Cust_Postal_Code) VALUES(input_First_Name, input_Second_Name, input_Phone_Number, 0, input_Address_Line_One, input_Address_Line_Two, input_Postal_Code);
END //
DELIMITER ; 
-- Example prompt for MySQL Terminal
    -- CALL insertIntoCustomer("Shardul", "Sharma", 8877529966, "C-201 Willow Apartments", "Faridabad", 330214);
-- Ending the Procedure for inserting into Customer

-- Inserting Into Supplier, Giving all required entries as parameter, initializing the amount Earnt by Supplier to be 0 while registering
DELIMITER //
CREATE PROCEDURE insertIntoSupplier(IN input_First_Name VARCHAR(50), IN input_Second_Name VARCHAR(50), IN input_Phone_Number BIGINT, IN input_Address_Line_One VARCHAR(100), IN input_Address_Line_Two VARCHAR(100), IN input_Postal_Code INT)   
BEGIN  
INSERT INTO Supplier (Supplier_First_Name, Supplier_Second_Name, Supplier_Phone_Number, Supplier_Amount_Earnt, Supplier_Address_Line_One, Supplier_Address_Line_Two, Supplier_Postal_Code) VALUES(input_First_Name, input_Second_Name, input_Phone_Number, 0, input_Address_Line_One, input_Address_Line_Two, input_Postal_Code);
END //
DELIMITER ;  
-- Example prompt for MySQL Terminal
    -- CALL insertIntoSupplier("Shardul", "Sharma", 8877529966, "C-201 Willow Apartments", "Faridabad", 330214);
-- Ending the Procedure for inserting into Supplier

-- Inserting Into Product, Giving all required entries as parameter, initializing the Quantity in Stock of Product to be 0 while registering
DELIMITER //
CREATE PROCEDURE insertIntoProduct(IN p_name VARCHAR(50), IN p_price INT)
BEGIN
    INSERT INTO Product (Product_Name, Price, Qty_Left) VALUES (p_name, p_price, 0);
END//
DELIMITER ;
-- Example prompt for MySQL Terminal
    -- CALL insertIntoProduct("Apple", 60);
-- Ending the Procedure for inserting into Product

-- Inserting Into Employee, Giving all required entries as parameter, initializing the Amount of Revenue Made by Employee to be 0 while registering
DELIMITER //
CREATE PROCEDURE insertIntoEmployee(
    IN emp_fname VARCHAR(50),
    IN emp_lname VARCHAR(50),
    IN emp_salary INT,
    IN emp_designation ENUM('Custodian', 'Security', 'Manager', 'Supervisor', 'Cashier'),
    IN emp_phone_number BIGINT,
    IN emp_sex ENUM('M','F'),
    IN emp_address_line_one VARCHAR(100),
    IN emp_address_line_two VARCHAR(100),
    IN emp_postal_code INT
)
BEGIN
    INSERT INTO Employee (Emp_First_Name, Emp_Second_Name, Emp_Salary, Emp_Amount_Sold, Emp_Designation, Emp_Phone_Number, Emp_Sex, Emp_Address_Line_One, Emp_Address_Line_Two, Emp_Postal_Code)
    VALUES (emp_fname, emp_lname, emp_salary, 0, emp_designation, emp_phone_number, emp_sex, emp_address_line_one, emp_address_line_two, emp_postal_code);
END //
DELIMITER ;  
-- Example prompt for MySQL Terminal
    -- CALL insertIntoEmployee("Shardul", "Sharma", 80000, "Security", 8877529966, 'M', "C-201 Willow Apartments", "Faridabad", 330214);
-- Ending the Procedure for inserting into Employee

-- Updating a specific Supplier's Contact Info, based on their personal unique Supplier_ID
DELIMITER // 
CREATE PROCEDURE updateSupplierContact(IN s_id INT, IN s_pno BIGINT)
BEGIN
    UPDATE Supplier SET Supplier_Phone_Number = s_pno WHERE Supplier_ID = s_id;
END //
DELIMITER ;
-- Example prompt for MySQL Terminal
    -- CALL updateSupplierContact(2, 8800559944);
-- Ending procedure for Updating Contact info of Supplier

-- Updating a specific Product's Quantity left in Stock, based on its unique Product_ID
DELIMITER // 
CREATE PROCEDURE updateProductQuantity(IN p_id INT, IN qty INT)
BEGIN
    UPDATE Product SET Product.Qty_Left = qty WHERE Product_ID = p_id;
END //
DELIMITER ;
-- Example prompt for MySQL Terminal
    -- CALL updateProductQuantity(2, 45);
-- Ending procedure for Updating Quantity left in Stock of Product

-- Updating a specific Employee's Job Designation, based on their unique Employee_ID
DELIMITER // 
CREATE PROCEDURE updateJobPosition(IN ep_id INT, IN pos ENUM('Custodian', 'Security', 'Manager', 'Supervisor', 'Cashier'))
BEGIN
    UPDATE Employee SET Emp_Designation = pos WHERE Emp_ID = ep_id;
END //
DELIMITER ;
-- Example prompt for MySQL Terminal
    -- CALL updateJobPosition(2, 'Custodian');
-- Ending procedure for Updating Job Designation of Employee

-- Creating a Purchase 
DELIMITER //
CREATE PROCEDURE addPurchase (
    IN supplier_id INT,
    IN products VARCHAR(255),
    IN quantities VARCHAR(255)
)
-- Taking array of product IDs and their quantities in an array as inputs
BEGIN
    -- Inserting into the table Purchase
    INSERT INTO Purchase (Purchase_Date, Supplier_ID)
    VALUES (CURRENT_DATE(), supplier_id);
    -- Storing unique purchase id into a variable
    SET @purchase_id = LAST_INSERT_ID();
    SET @products = products;
    SET @quantities = quantities;
    SET @products_array = JSON_EXTRACT(@products, '$');
    SET @quantities_array = JSON_EXTRACT(@quantities, '$');
    -- Setting variable for keeping index of while loop
    SET @i = 0;
    WHILE (@i < JSON_LENGTH(@products_array)) DO
        -- Storing product ID and their quantity bought in variables
        -- Finding ith product and quantity
        SET @product_id = JSON_EXTRACT(@products_array, CONCAT('$[', @i, ']'));
        SET @qty_bought = JSON_EXTRACT(@quantities_array, CONCAT('$[', @i, ']'));
        -- Inserting record into Purchase_has_Product
        INSERT INTO Purchase_has_Product (Purchase_ID, Product_ID, Qty_Bought)
        VALUES (@purchase_id, @product_id, @qty_bought);
        -- Updating value of Quantity left of Product in the supermarket
        UPDATE Product SET Qty_Left = Qty_Left + @qty_bought WHERE Product_ID = @product_id;
        -- Incrementing value of index
        SET @i = @i + 1;
    END WHILE;
    -- Storing sum of Price of total purchase
    SET @total_purchase = (
        SELECT SUM(Price * Qty_Bought)
        FROM Purchase_has_Product
        JOIN Product ON Product.Product_ID = Purchase_has_Product.Product_ID
        WHERE Purchase_ID = @purchase_id
    );
    -- Update Supplier's amount earnt by above sum
    UPDATE Supplier
    SET Supplier_Amount_Earnt = Supplier_Amount_Earnt + @total_purchase
    WHERE Supplier_ID = supplier_id;
END //
DELIMITER ;
-- Example prompt for MySQL Terminal
    -- CALL addPurchase(2, '[1,3,4]', '[7,2,8]');
-- Ending Procedure for inserting a purchase

-- Creating a Sale 
DELIMITER //
CREATE PROCEDURE addSale (
    IN customer_id INT,
    IN products VARCHAR(255),
    IN quantities VARCHAR(255),
    IN employee_id INT
)
-- Taking array of product IDs and their quantities in an array as inputs
BEGIN
    -- Inserting into the table Sale
    INSERT INTO Sale (Sale_Date, Cust_ID, Emp_ID)
    VALUES (CURRENT_DATE(), customer_id, employee_id);
    -- Storing unique Sale id into a variable
    SET @sale_id = LAST_INSERT_ID();
    SET @products = products;
    SET @quantities = quantities;
    SET @products_array = JSON_EXTRACT(@products, '$');
    SET @quantities_array = JSON_EXTRACT(@quantities, '$');
    -- Setting variable for keeping index of while loop
    SET @i = 0;
    WHILE (@i < JSON_LENGTH(@products_array)) DO
        -- Storing product ID and their quantity sold in variables
        -- Finding ith product and quantity
        SET @product_id = JSON_EXTRACT(@products_array, CONCAT('$[', @i, ']'));
        SET @qty_sale = JSON_EXTRACT(@quantities_array, CONCAT('$[', @i, ']'));
        -- Inserting record into Sale_has_Product
        INSERT INTO Sale_has_Product (Sale_ID, Product_ID, Qty_Bought)
        VALUES (@sale_id, @product_id, @qty_sale);
        -- Updating value of Quantity left of Product in the supermarket
        UPDATE Product SET Qty_Left = Qty_Left - @qty_sale WHERE Product_ID = @product_id;
        -- Incrementing value of index
        SET @i = @i + 1;
    END WHILE;
    -- Storing sum of Price of total Sale
    SET @total_sale = (
        SELECT SUM(Price * Qty_Bought)
        FROM Sale_has_Product
        JOIN Product ON Product.Product_ID = Sale_has_Product.Product_ID
        WHERE Sale_ID = @sale_id
    );
    -- Update Customer's amount earnt by above sum
    UPDATE Customer
    SET Cust_Amount_Spent = Cust_Amount_Spent + @total_sale
    WHERE Cust_ID = customer_id;
    -- Update Employee's amount earnt by above sum
    UPDATE Employee 
    SET Emp_Amount_Sold = Emp_Amount_Sold + @total_sale 
    WHERE Emp_ID = employee_id;

END //
DELIMITER ;
-- Example prompt for MySQL Terminal
    -- CALL addSale(2, '[1,3,4]', '[7,2,8]', 3);
-- Ending Procedure for inserting a Sale

-- Deleting a Sale
DELIMITER //
CREATE PROCEDURE deleteSale(IN sale_id INT)
BEGIN
    -- Declaring variables for index for while loop, and number of different records in Sale_has_Product with sale ID same as given
    DECLARE i INT DEFAULT 0;
    DECLARE n INT DEFAULT 0;
    -- Declaring a variable for storing total money involved in a Sale
    SELECT SUM(P.Price*S.Qty_Bought) FROM Product as P, Sale_has_Product as S WHERE P.Product_ID = S.Product_ID AND S.Sale_ID = sale_id INTO @sum;
    -- Updating Money Spent by Customer by the above @sum declared
    UPDATE Customer SET Customer.Cust_Amount_Spent = (Customer.Cust_Amount_Spent - @sum) WHERE Customer.Cust_ID = (SELECT Sale.Cust_ID FROM Sale Where Sale.Sale_ID = sale_id LIMIT 1);
    -- Updating Money Sold by Employee by the above @sum declared
    UPDATE Employee SET Employee.Emp_Amount_Sold = (Employee.Emp_Amount_Sold - @sum) WHERE Employee.Emp_ID = (SELECT Sale.Emp_ID FROM Sale Where Sale.Sale_ID = sale_id LIMIT 1);
    -- Temporary table, only containing those records of Sale_has_Product, which have sale id same as given
    CREATE TEMPORARY TABLE Specific_Sale SELECT * FROM Sale_has_Product WHERE Sale_has_Product.Sale_ID = sale_id;
    -- Giving n value of size of Specific_Sale table
    SET n = (SELECT COUNT(*) FROM Specific_Sale);
    WHILE ( i < n ) DO
        -- Storing Product ID and Qty Bought of each record of table in variables in each iteration of the loop
        SELECT Specific_Sale.Product_ID from Specific_Sale limit i,1 INTO @prod_id;
        SELECT Specific_Sale.Qty_Bought from Specific_Sale limit i,1 INTO @qty_bt;
        -- Updating Quantity Left in Stock in Product table using these variable values
        UPDATE Product SET Product.Qty_Left = (Product.Qty_Left - @qty_bt) 
        WHERE Product.Product_ID = @prod_id;
        -- Incrementing index value for while loop
        SET i = i+1;
    END WHILE;
    -- Deleting records from Sale_has_Product and Sale, associated with the given Sale_id
    DELETE FROM Sale_has_Product WHERE Sale_has_Product.Sale_ID = sale_id;
    DELETE FROM Sale WHERE Sale.Sale_ID = sale_id;
END //
DELIMITER ;
-- Example prompt for MySQL Terminal
    -- CALL deleteSale(2);
-- Ending Procedure for deleting a Sale