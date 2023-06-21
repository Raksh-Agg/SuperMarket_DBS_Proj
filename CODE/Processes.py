from mysql.connector import MySQLConnection


# This file is the file containing all Stuff related to the MySQL Server
# The MySQL server is re-initialized for this file, and a cursor is maintained, which executes all MySQL queries
class Cursor_Init():
    def __init__(self, master, user_MySQL, pwd_MySQL):
        # Initializing this object
        self.dbConnection = MySQLConnection(
            user=user_MySQL, password=pwd_MySQL, host="localhost", database="SuperMarket_1463_1458")
        self.cursor = self.dbConnection.cursor()

    # Query for Selecting all attributes and records from a table
    # The table Name is given as a parameter to this function, so that, same function can be reUsed for various tables
    def showAll(self, table_Name):
        self.cursor.execute("SELECT * FROM " + table_Name)
        myResult = self.cursor.fetchall()
        return myResult

    # Query for Searching through tables (Supplier, Customer,Employee, Product) when only the Name is given
    def searchByName(self, table_Name, Name):
        if table_Name == "Customer":
            query = "SELECT * FROM Customer WHERE CONCAT (Cust_First_Name,  ' ', Cust_Second_Name) LIKE %s;"
        elif table_Name == "Employee":
            query = "SELECT * FROM Employee WHERE CONCAT (Emp_First_Name,  ' ', Emp_Second_Name) LIKE %s;"
        elif table_Name == "Supplier":
            query = "SELECT * FROM Supplier WHERE CONCAT (Supplier_First_Name,  ' ', Supplier_Second_Name) LIKE %s;"
        elif table_Name == "Product":
            query = "SELECT * FROM Product WHERE Product.Product_Name LIKE %s;"

        # The following is done so that, if, only the first few characters of the name are given, we can still see all records matching the Name
        name_with_wildcard = Name + "%"
        self.cursor.execute(query, (name_with_wildcard,))
        myResult = self.cursor.fetchall()
        return myResult

    # Following query is for searching a Table when we have an attribute name, which is not a String (Like Product IDs, etc )
    def showBySearch(self, table_Name, attribute_Name, Name):
        self.cursor.execute(f"SELECT * FROM "+table_Name +
                            " WHERE " + attribute_Name + " = " + str(Name) + ";")
        myResult = self.cursor.fetchall()
        return myResult

    # Following query is to Insert a Supplier or Customer into the database, based on the values of parameters we get from GUI
    def insertHuman(self, table_Name, Human_First_Name, Human_Second_Name, Human_Phone_Number, Human_Address_Line_One, Human_Address_Line_Two, Human_Postal_Code):
        values = '''"'''+Human_First_Name+'''", "''' + Human_Second_Name + '''", ''' + str(Human_Phone_Number) + \
            ''', 0, "''' + Human_Address_Line_One + '''", "''' + \
            Human_Address_Line_Two + '''", ''' + str(Human_Postal_Code)

        if table_Name == "Customer":
            query = "INSERT INTO Customer (Cust_First_Name, Cust_Second_Name, Cust_Phone_Number, Cust_Amount_Spent, Cust_Address_Line_One, Cust_Address_Line_Two, Cust_Postal_Code) VALUES(" + values + " );"
        elif table_Name == "Supplier":
            query = "INSERT INTO Supplier (Supplier_First_Name, Supplier_Second_Name, Supplier_Phone_Number, Supplier_Amount_Earnt, Supplier_Address_Line_One, Supplier_Address_Line_Two, Supplier_Postal_Code) VALUES(" + values + ");"
        self.cursor.execute(query)
        self.dbConnection.commit()

    # Following query is to Insert a Employee into the database, based on the values of parameters we get from GUI
    def insertEmployee(self, Emp_First_Name, Emp_Second_Name, Emp_Salary, Emp_Designation, Emp_Phone_Number, Emp_Sex, Emp_Address_Line_One, Emp_Address_Line_Two, Emp_Postal_Code):
        values = "'"+Emp_First_Name+"', '"+Emp_Second_Name+"', " + Emp_Salary + ", 0, '" + Emp_Designation + "', " + \
            Emp_Phone_Number + ", '" + Emp_Sex + "', '" + Emp_Address_Line_One + \
            "', '" + Emp_Address_Line_Two + "', " + Emp_Postal_Code
        query = "INSERT INTO Employee (Emp_First_Name, Emp_Second_Name, Emp_Salary, Emp_Amount_Sold, Emp_Designation, Emp_Phone_Number, Emp_Sex, Emp_Address_Line_One, Emp_Address_Line_Two, Emp_Postal_Code) VALUES (" + values + " );"
        self.cursor.execute(query)
        self.dbConnection.commit()

    # Inserting Product to database. Here, we initialize the Quantity in Stock of the Product to 0, since, the quantity changes only manuallu, or when a purchase or sale is made
    def insertProduct(self, Prod_Name, Prod_Price):
        values = '''"'''+Prod_Name + '''", ''' + str(Prod_Price) + ", 0"
        query = f"INSERT INTO Product(Product_Name, Price, Qty_Left) VALUES ({values});"
        self.cursor.execute(query)
        self.dbConnection.commit()

    # Making A sale, Here, many things are changed:
        # Sale is inserted into the Sale table
        # Employee's Amount Sold is incremented by the total amount of the Sale
        # Similarly, Customer's Amount Spent is incremented
        # Quantity Left of the Product is reduced by the amount taken in the sale
        # All Sale values for product_id and quantity of product bought are inserted as records in the Sale_has_Product Table
    def addSale(self, Emp_ID, Cust_ID, data):
        query = "INSERT INTO Sale (Emp_ID, Cust_ID, Sale_Date) VALUES (" + \
            str(Emp_ID)+", "+str(Cust_ID)+", CURRENT_DATE);"
        self.cursor.execute(query)
        querytwo = "SELECT LAST_INSERT_ID();"
        self.cursor.execute(querytwo)
        Sale_String = self.cursor.fetchall()
        Sale_ID = (int)(Sale_String[0][0])
        money = 0
        for line in data:
            querythree = "INSERT INTO Sale_has_Product (Sale_ID, Product_ID, Qty_Bought) VALUES (" + str(
                Sale_ID)+", "+str(line[0])+", "+str(line[1])+");"
            self.cursor.execute(querythree)
            self.cursor.execute(
                "SELECT Product.Price FROM Product WHERE Product.Product_ID = "+str(line[0])+";")
            price_list = self.cursor.fetchall()
            price = price_list[0][0]
            self.cursor.execute(
                "UPDATE Product SET Qty_left = Qty_left - "+str(line[1])+" WHERE Product_ID = "+str(line[0])+";")
            money = money + price*line[1]
        self.cursor.execute(
            "UPDATE Customer SET Cust_Amount_Spent = Cust_Amount_Spent + "+str(money)+" WHERE Cust_ID = "+Cust_ID+";")
        self.cursor.execute(
            "UPDATE Employee SET Emp_Amount_Sold = Emp_Amount_Sold + "+str(money)+" WHERE Emp_ID = "+Emp_ID+";")
        self.dbConnection.commit()

     # Making A Purchase, Here, many things are changed:
        # Purchase is inserted into the Purchase table
        # Supplier's Amount Sold is incremented by the total amount of the Purchase
        # Quantity Left of the Product is reduced by the amount taken in the Purchase
        # All Purchase values for product_id and quantity of product bought are inserted as records in the Purchase_has_Product Table
    def addPurchase(self, Supplier_ID, data):
        query = "INSERT INTO Purchase (Supplier_ID, Purchase_Date) VALUES (" + \
            str(Supplier_ID)+", CURRENT_DATE);"
        self.cursor.execute(query)
        querytwo = "SELECT LAST_INSERT_ID();"
        self.cursor.execute(querytwo)
        Purchase_String = self.cursor.fetchall()
        Purchase_ID = (int)(Purchase_String[0][0])
        money = 0
        for line in data:
            querythree = "INSERT INTO Purchase_has_Product (Purchase_ID, Product_ID, Qty_Bought) VALUES (" + str(
                Purchase_ID)+", "+str(line[0])+", "+str(line[1])+");"
            self.cursor.execute(querythree)
            self.cursor.execute(
                "SELECT Product.Price FROM Product WHERE Product.Product_ID = "+str(line[0])+";")
            price_list = self.cursor.fetchall()
            price = price_list[0][0]
            self.cursor.execute(
                "UPDATE Product SET Qty_left = Qty_left + "+str(line[1])+" WHERE Product_ID = "+str(line[0])+";")
            money = money + price*line[1]
        self.cursor.execute(
            "UPDATE Supplier SET Supplier_Amount_Earnt = Supplier_Amount_Earnt + "+str(money)+" WHERE Supplier_ID = "+Supplier_ID+";")
        self.dbConnection.commit()

    # Update Job Position by Employee ID parameter to find
    def updateJobPosition(self, value, emp_ID):
        query = "UPDATE Employee SET Emp_Designation = '" + \
            value+"' WHERE Emp_ID = " + str(emp_ID) + ";"
        self.cursor.execute(query)
        self.dbConnection.commit()

    # Update Product Quantity by Product ID parameter to find
    def updateQuantity(self, value, prod_id):
        query = "UPDATE Product SET Qty_Left = '"+value + \
            "' WHERE Product_ID = " + str(prod_id)+";"
        self.cursor.execute(query)
        self.dbConnection.commit()

    # Update Supplier Contact Information by Supplier ID parameter to find
    def updateSupplierContact(self, value, supp_ID):
        query = "UPDATE Supplier SET Supplier_Phone_Number = '" + \
            value+"' WHERE Supplier_ID = " + str(supp_ID) + ";"
        self.cursor.execute(query)
        self.dbConnection.commit()

    # Deleting the Sale, for which, we would have to do all processes we did in Insert Sale, just in the Opposite order
    def deleteSale(self, sale_ID):
        query = "UPDATE Customer SET Cust_Amount_Spent = Cust_Amount_Spent - (SELECT SUM(P.Price*S.Qty_Bought) FROM Product as P, Sale_has_Product as S WHERE P.Product_ID = S.Product_ID AND S.Sale_ID = " + \
            sale_ID + \
                ") WHERE Cust_ID = (SELECT Cust_ID FROM Sale Where Sale_ID = " + \
            sale_ID+");"
        self.cursor.execute(query)
        query1 = "UPDATE Employee SET Emp_Amount_Sold = Emp_Amount_Sold - (SELECT SUM(P.Price*S.Qty_Bought) FROM Product as P, Sale_has_Product as S WHERE P.Product_ID = S.Product_ID AND S.Sale_ID = " + \
            sale_ID + \
            ") WHERE Emp_ID = (SELECT Emp_ID FROM Sale Where Sale_ID = " + \
            sale_ID+");"
        self.cursor.execute(query1)
        self.dbConnection.commit()
        self.cursor.execute(
            "SELECT Product_ID, Qty_Bought FROM Sale_has_Product WHERE Sale_ID = "+sale_ID+";")
        data = self.cursor.fetchall()
        for line in data:
            self.cursor.execute("UPDATE Product SET Qty_Left = Qty_Left + " +
                                str(line[1])+" WHERE Product_ID = "+str(line[0])+";")
            self.dbConnection.commit()

        query3 = "DELETE FROM Sale WHERE Sale_ID = " + sale_ID + ";"
        self.cursor.execute(query3)
        self.dbConnection.commit()

    # To close the Server Connection, once the Program is exited
    def Finish(self):
        self.dbConnection.commit()
        self.cursor.close()
        self.dbConnection.close()
