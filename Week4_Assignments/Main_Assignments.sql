select name from sys.tables;

use Assignment_4;

-- Q1

CREATE TABLE Orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    order_date DATE
);

CREATE TABLE OrderDetails (
    orderdetail_id INT PRIMARY KEY,
    order_id INT,
    product_id INT,
    quantity INT,
    FOREIGN KEY (order_id) REFERENCES Orders(order_id)
);

INSERT INTO Orders (order_id, customer_id, order_date) VALUES
(101, 1, '2023-01-01'),
(102, 2, '2023-01-02'),
(103, 1, '2023-01-03'),
(104, 3, '2023-01-04');

INSERT INTO OrderDetails (orderdetail_id, order_id, product_id, quantity) VALUES
(1, 101, 1, 2),
(2, 101, 2, 1),
(3, 102, 3, 3),
(4, 103, 1, 1),
(5, 104, 2, 2);
 
SELECT TOP 1 o.customer_id, COUNT(*) OVER(PARTITION BY o.customer_id) AS total_orders, o.order_date
FROM Orders o
WHERE o.customer_id = (
    SELECT customer_id
    FROM Orders
    GROUP BY customer_id
) ORDER BY total_orders DESC;


-- Q2 

CREATE TABLE Hackers (
    hacker_id INT,
    name VARCHAR(50)
);

CREATE TABLE Submissions (
    submission_id INT,
    hacker_id INT,
    challenge_id INT,
    score INT
);

INSERT INTO Hackers (hacker_id, name) VALUES
(1, 'John'),
(2, 'Jane'),
(3, 'Alice');

INSERT INTO Submissions (submission_id, hacker_id, challenge_id, score) VALUES
(1, 1, 1, 10),
(2, 1, 2, 20),
(3, 2, 1, 15),
(4, 2, 2, 25),
(5, 3, 1, 12),
(6, 3, 2, 18);


create procedure p 
as begin 

select X.Id , Hackers.name, X.Total_sore  from Hackers inner join
(select s.hacker_id as Id,  sum(s.score) as Total_sore from Submissions s group by hacker_id) as X
on X.Id = hacker_id where X.Total_sore > 0 order by X.Total_sore desc , X.Id asc

end 

execute p ;

-- Q3


CREATE TABLE Employees (
    employee_id INT,
    employee_name VARCHAR(100),
    department_id INT
);

CREATE TABLE Departments (
    department_id INT,
    department_name VARCHAR(50)
);

CREATE TABLE Salaries (
    salary_id INT,
    employee_id INT,
    salary_amount INT
);

INSERT INTO Employees (employee_id, employee_name, department_id) VALUES
(101, 'John Doe', 1),
(102, 'Jane Smith', 1),
(103, 'Bob Johnson', 2),
(104, 'Alice Brown', 2),
(105, 'Charlie Davis', 3),
(106, 'Eva White', 3);

INSERT INTO Departments (department_id, department_name) VALUES
(1, 'HR'),
(2, 'IT'),
(3, 'Finance');

INSERT INTO Salaries (salary_id, employee_id, salary_amount) VALUES
(201, 101, 60000),
(202, 102, 65000),
(203, 103, 70000),
(204, 104, 72000),
(205, 105, 80000),
(206, 106, 75000);


with cte as (
select e.employee_id , e.employee_name , d.department_name ,
rank() over(partition by d.department_id order by s.salary_amount desc) as 
ranking , s.salary_amount as salary
 from Employees e 
inner join Departments d on d.department_id = e.department_id 
inner join Salaries s on s.employee_id = e.employee_id
)

select * from cte where ranking = 1;

-- Q4 

CREATE TABLE salesman (
    salesman_id INT,
    name VARCHAR(100),
    city VARCHAR(50),
    commission DECIMAL(4,2)
);

INSERT INTO salesman (salesman_id, name, city, commission) VALUES
(5001, 'James Hoog', 'New York', 0.15),
(5002, 'Nail Knite', 'Paris', 0.13),
(5005, 'Pit Alex', 'London', 0.11),
(5006, 'Mc Lyon', 'Paris', 0.14),
(5007, 'Paul Adam', 'Rome', 0.13),
(5003, 'Lauson Hen', 'San Jose', 0.12);

select salesman_id , name ,city , commission from salesman where name > 'A' and name <= 'L';

-- Q5 
select name from sys.tables;
exec sp_help Orders;

CREATE TABLE Orders (
    ord_no INT,
    purch_amt DECIMAL(10,2),
    ord_date DATE,
    customer_id INT,
    salesman_id INT
);

INSERT INTO Orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
(70001, 150.50, '2012-10-05', 3005, 5002),
(70009, 270.65, '2012-09-10', 3001, 5005),
(70002, 65.26,  '2012-10-05', 3002, 5001),
(70004, 110.50, '2012-08-17', 3009, 5003),
(70007, 948.50, '2012-09-10', 3005, 5002),
(70005, 2400.60,'2012-07-27', 3007, 5001),
(70008, 5760.00,'2012-09-10', 3002, 5001),
(70010, 1983.43,'2012-10-10', 3004, 5006);

with cte as (
  select customer_id  , max(purch_amt) over(partition by customer_id) as max_amount_per_customer ,
  dateadd(day , 7, ord_date) as Shipment_Date , getdate() as ins_dateDateTime from Orders 
  where customer_id
  between 3002 and 3007
  )
  select customer_id  ,  max_amount_per_customer , Shipment_Date, ins_dateDateTime ,  datediff(day  , datepart(day ,ins_dateDateTime) ,datepart(day ,Shipment_Date)) as Data_Latency from cte
  where max_amount_per_customer > 1000 

-- Q6 

CREATE TABLE Ride_table (
    ride_id INT,
    start_terminal INT,
    end_terminal INT,
    ride_duration INT
);

INSERT INTO Ride_table (ride_id, start_terminal, end_terminal, ride_duration) VALUES
(1, 101, 102, 15),
(2, 102, 103, 20),
(3, 101, 104, 25),
(4, 104, 105, 18),
(5, 102, 104, 22),
(6, 101, 103, 30);

with cte as (
select ride_id , ride_duration, row_number() over( partition by end_terminal order by ride_duration desc) as ranking from Ride_table
)
select ride_id , ride_duration from cte;

-- Q7
CREATE TABLE Customers (
    customer_id INT,
    first_name VARCHAR(50),
    last_name VARCHAR(50),
    age INT
);

CREATE TABLE Orders (
    OrderID INT,
    CustomerID INT,
    OrderDate DATE,
    TotalAmount DECIMAL(10,2)
);

INSERT INTO Customers (customer_id, first_name, last_name, age) VALUES
(1, 'John', 'Doe', 31),
(2, 'Robert', 'Luna', 22),
(3, 'David', 'Robinson', 22),
(4, 'John', 'Reinhardt', 25),
(5, 'Betty', 'Doe Thomas', 28);

INSERT INTO Orders (OrderID, CustomerID, OrderDate, TotalAmount) VALUES
(1, 1, '2023-01-15', 50),
(2, 2, '2023-02-10', 30),
(3, 3, '2023-02-20', 100);

declare @OrderID int = 101;
declare @CustomerID int = 5;
declare @OrderDate date = getdate();
declare @TotalAmount decimal(10,2) = 2500.00;

begin try

    if not exists (
        select 1 
        from Customers 
        where CustomerID = @CustomerID
    )
    begin
        throw 50001, 'Invalid CustomerID. Please provide a valid CustomerID.', 1;
    end

    insert into Orders (OrderID, CustomerID, OrderDate, TotalAmount)
    values (@OrderID, @CustomerID, @OrderDate, @TotalAmount);

end try
begin catch

    print 'Error occurred while inserting the order.';
    print error_message();

end catch;


alter table Customers add fullname varhcar(20);
update Customers set fullname = firstname + ' ' + lastname;


select *
from Customers
where last_name = 'Doe';


-- Q8 

CREATE TABLE Orders (
    ord_no INT,
    purch_amt DECIMAL(10,2),
    ord_date DATE,
    customer_id INT,
    salesman_id INT
);

INSERT INTO Orders (ord_no, purch_amt, ord_date, customer_id, salesman_id) VALUES
(70001, 150.50, '2012-10-05', 3005, 5002),
(70009, 270.65, '2012-09-10', 3001, 5005),
(70002, 65.26,  '2012-10-05', 3002, 5001),
(70004, 110.50, '2012-08-17', 3009, 5003),
(70007, 948.50, '2012-09-10', 3005, 5002),
(70005, 2400.60,'2012-07-27', 3007, 5001),
(70008, 5760.00,'2012-09-10', 3002, 5001),
(70010, 1983.43,'2012-10-10', 3004, 5006);


select customer_id , salesman_id from Orders;

-- Q9 

CREATE TABLE Transactions (
    transaction_id INT,
    product_name VARCHAR(50),
    transaction_date DATE,
    revenue DECIMAL(10,2)
);

INSERT INTO Transactions (transaction_id, product_name, transaction_date, revenue) VALUES
(1, 'ProductA', '2023-01-01', 100.50),
(2, 'ProductB', '2023-01-03', 150.75),
(3, 'ProductA', '2023-01-05', 200.00),
(4, 'ProductC', '2023-01-08', 120.25),
(5, 'ProductB', '2023-01-10', 180.50);

select transaction_date, product_name,  revenue , transaction_date as dateoftransactions,
lag(transaction_date) over(order by transaction_date) as previous_transaction ,
lead(transaction_date) over(order by transaction_date) as next_transaction
from Transactions ;

-- Q 10
CREATE TABLE Sales (
    SaleID INT,
    ProductID INT,
    CustomerID INT,
    SaleDate DATE,
    Quantity INT
);

CREATE TABLE Product (
    ProductID INT,
    ProductName VARCHAR(100),
    Category VARCHAR(50),
    Price DECIMAL(10,2)
);

CREATE TABLE Customers (
    CustomerID INT,
    CustomerName VARCHAR(100),
    Email VARCHAR(100),
    Country VARCHAR(50)
);

CREATE TABLE Shipments (
    ShippingID INT,
    SaleID INT,
    ShipmentDate DATE,
    ShipmentCost DECIMAL(10,2)
);

INSERT INTO Sales (SaleID, ProductID, CustomerID, SaleDate, Quantity) VALUES
(1, 101, 201, '2023-01-01', 2),
(2, 102, 202, '2023-01-02', 1),
(3, 103, 203, '2023-01-02', 3);

INSERT INTO Product (ProductID, ProductName, Category, Price) VALUES
(101, 'Laptop', 'Electronics', 800),
(102, 'Headphones', 'Electronics', 50),
(103, 'Book', 'Books', 20);

INSERT INTO Customers (CustomerID, CustomerName, Email, Country) VALUES
(201, 'Alice', 'alice@email.com', 'USA'),
(202, 'Bob', 'bob@email.com', 'Canada'),
(203, 'Carol', 'carol@email.com', 'UK');

INSERT INTO Shipments (ShippingID, SaleID, ShipmentDate, ShipmentCost) VALUES
(501, 1, '2023-01-03', 10),
(502, 2, '2023-01-03', 8),
(503, 3, '2023-01-04', 12);

with cte as (
    select 
        p.ProductID,  p.ProductName, p.Category,
        sum(s.Quantity) as total_quantity,
        sum(s.Quantity * p.Price) as total_sales
    from product p
    inner join sales s 
        on s.ProductID = p.ProductID
    group by 
        p.ProductID,  p.ProductName,  p.Category
),

rankedproducts as (
    select *,
        rank() over(order by total_sales desc, total_quantity desc) as Ranking
    from cte
),

latestcustomer as (
    select 
        s.ProductID,   s.CustomerID,
        row_number() over (
            partition by s.ProductID 
            order by s.SaleDate desc
        ) as row_num
    from sales s
)

select 
    rankedproducts.ProductID, rankedproducts.ProductName, rankedproducts.Category,
	rankedproducts.total_quantity, rankedproducts.total_sales,
    customers.CustomerID, customers.CustomerName, customers.Email
from rankedproducts
join latestcustomer
    on rankedproducts.ProductID = latestcustomer.ProductID 
    and latestcustomer.row_num = 1
join customers
    on customers.CustomerID = latestcustomer.CustomerID
where rankedproducts.Ranking <= 3
order by rankedproducts.Ranking;
