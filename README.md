# Pizza Project: Database

## Description
This project focuses on creating and managing a database for a pizzeria, aiming to handle orders, customers, and available pizzas. Although initially proposed to develop an API, the current phase of the project has concentrated on establishing a solid database to support the required operations.

## Database Schema
The database is designed to store information about customers, orders, and pizzas. Below are the main tables and their relationships:

- **Customers**: Stores customer information such as ID, email, and phone number.
- **Orders**: Records the orders placed, including order ID, date, time, and the relationship with the customer who places the order.
- **Pizzas**: Contains the available pizzas, with fields for the pizza name and whether it is available or not.
- **Order Details**: A relationship table that links orders with the ordered pizzas, including the quantity of each pizza.

## Technologies Used
- **SQL**: Language used for the creation and management of the database.
- **SQLite/PostgreSQL**: Database management system. The choice depends on the development and production environment.

## Implementation
The initial implementation has focused on creating the tables and relationships necessary to support the basic operations of the pizzeria. Below are the SQL scripts to create the mentioned tables.

### Table Creation
```sql
CREATE TABLE Customers (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    email VARCHAR(255) UNIQUE NOT NULL,
    phone VARCHAR(20) UNIQUE NOT NULL
);

CREATE TABLE Pizzas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name VARCHAR(255) UNIQUE NOT NULL,
    available BOOLEAN DEFAULT TRUE
);

CREATE TABLE Orders (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    dateTime DATETIME NOT NULL,
    customerId INTEGER,
    FOREIGN KEY (customerId) REFERENCES Customers(id)
);

CREATE TABLE OrderDetails (
    orderId INTEGER,
    pizzaId INTEGER,
    quantity INTEGER,
    FOREIGN KEY (orderId) REFERENCES Orders(id),
    FOREIGN KEY (pizzaId) REFERENCES Pizzas(id),
    PRIMARY KEY (orderId, pizzaId)
);

## Basic Operations
Basic operations include inserting data into the tables, updating the availability of pizzas, and querying orders and the most sold pizzas.

## Next Steps
The next step in the project development is the implementation of an API that allows interacting with the database programmatically, facilitating the placing of orders, customer management, and querying relevant information through specific endpoints.

## Final Thoughts
The initial focus on the database has allowed establishing a solid foundation for the project. Although the development of the API is pending, the current database structure is prepared to support the planned functionalities and future expansions.

## Time Invested
The development of the database and associated documentation has taken approximately 9 hours, spread over a weekend. This time includes planning, database schema design, and drafting this document. ```

