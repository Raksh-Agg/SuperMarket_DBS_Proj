<a name="_bezikt6z4jnq"></a>Documentation for SuperMarket Database Management System(MyMART)

MyMART is a relational database management system designed to manage the operations of a supermarket efficiently. It is a comprehensive system that handles all aspects of the supermarket's operations, including managing employees, customers, suppliers, products, purchases, and sales.

## <a name="_genqoega6zv"></a>Installation Instructions
To use the Supermart Application (For users using the Application), follow these instructions:

- Download and install MySQL Community Server:

1. Go to <https://dev.mysql.com/downloads/mysql/> to download the MySQL Community Server.
1. Choose the appropriate version for your operating system and follow the instructions to install it.

- Configure MySQL:

1. Once installed, you need to configure MySQL to run on your machine.
1. During installation, you will be prompted to set a root password for MySQL. Make sure to choose a strong password and keep it secure. 
1. After installation, you can access the MySQL Server from the command line using the command "mysql -u root -p" and enter the root password when prompted.

- Run the Application:
1. You need to run the Python file named “FinalLoginPage.py”, and you will be prompted to enter your MySQL username and password. On Authenticating this information, The window will lead you to the application Dashboard, where you can use the application with the requirements specified.


## <a name="_im7zxvrxr6wy"></a>Database Design

MyMART is designed using the relational database model. The database contains five tables: Employee, Customer, Supplier, Product, Purchase, and Sale.

- Employee Table: This table contains the personal details of all the supermarket employees. Each employee is assigned a unique ID. The table includes details such as the employee's first name, second name, salary, amount sold, designation, phone number, sex, address line one, address line two, and postal code.

- Customer Table: This table contains the personal details of all the supermarket's customers. Each customer is assigned a unique ID, and the table includes details such as the customer's first name, second name, phone number, the amount spent, address line one, address line two, and postal code.

- Supplier Table: This table contains details of all the suppliers that provide products to the supermarket. Each supplier is assigned a unique ID, and the table includes details such as the supplier's first name, second name, phone number, the amount earned, address line one, address line two, and postal code.

- Product Table: This table contains details of all the products available in the supermarket. Each product is assigned a unique ID, and the table includes details such as the product's name, price, and quantity left.

- Purchase Table: This table contains details of all the purchases made by the supermarket from the suppliers. Each purchase is assigned a unique ID, and the table includes details such as the purchase date and the supplier ID.

- Sale Table: This table contains details of all the sales made by the supermarket to customers. Each sale is assigned a unique ID, and the table includes details such as the sale date, customer ID, and employee ID.

## <a name="_yxxoe2a3yrw"></a>Data Management

MyMART provides various functionalities to manage the data in the database. These functionalities include:

- Inserting Data: The system provides SQL queries to insert data into the database tables. Sample data has been provided in the SQL file for each table.

- Updating Data: The system provides SQL queries to update the data in the database tables. The user can edit the employee's amount sold or the customer's amount spent based on their progress.

- Deleting Data: The system provides SQL queries to delete data from the database tables. The user can delete a purchase or sale record from the respective tables.

- Retrieving Data: The system provides SQL queries to retrieve data from the database tables. The user can retrieve the employee's details based on their ID or the customer's details based on their phone number.

For further information, refer to the file “Queries.sql”, which has SQL implementation of the functionalities used in the application.

## <a name="_t8tb87nm3tgb"></a>Conclusion

MyMART is a comprehensive system that provides functionalities to manage the operations of a supermarket efficiently. It uses the relational database model and provides functionalities to insert, update, delete, and retrieve data from the database tables. The system is easy to install and use and can be customised based on the requirements of the supermarket.






