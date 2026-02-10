
select name from sys.databases;

create database Assignment_4;


create table hr (
    emp_id int primary key identity(1,1),
    emp_name varchar(50),
    department varchar(50),
    score int
);

create table development (
    emp_id int primary key identity(1,1),
    emp_name varchar(50),
    department varchar(50),
    score int   
);

create table data_engineering (
    emp_id int primary key identity(1,1),
    emp_name varchar(50),
    department varchar(50),
    score int
);

insert into hr values 
('Alice', 'HR', 3),
('Bob', 'HR', 4),
('Charlie', 'HR', 5),
('Diana', 'HR', 3);

insert into development values 
('Eve', 'Development', 4),
('Frank', 'Development', 5),
('Grace', 'Development', 3),
('Hank', 'Development', 4);

insert into data_engineering values 
('Ivy', 'Data Engineering', 5),
('Jack', 'Data Engineering', 4),
('Kate', 'Data Engineering', 5),
('Leo', 'Data Engineering', 3);

create table #employee (
    emp_id int identity(1,1) primary key,
    emp_name varchar(50),
    department varchar(50),
    score int
);

-- Create Temp tables/ table variables using the week 3 employee table and also explore when to use which one. 

insert into #employee (emp_name , department , score)
select emp_name , department , score from hr
union all
select emp_name , department , score from development
union all 
select emp_name , department , score from data_engineering;

select * from #employee;

declare @employee_var table( 
	emp_id int identity(1,1) primary key,
    emp_name varchar(50),
    department varchar(50),
    score int
);

insert into @employee_var (emp_name, department,score)
select emp_name, department, score from #employee;

select * from @employee_var;	

-- Apply error handling in the above employee table and explore ‘Throw’ and ‘raise error’ in error handling  
	
begin transaction 
 
 begin try 
 insert into #employee values('arun', 'HR',1);

 end try 
 begin catch
 select ERROR_MESSAGE() as exception;
 rollback transaction
 end catch 

 create table employees(
    emp_id int identity(1,1),
    emp_name varchar(50),
    salary int
);


	begin transaction 

	   declare @name varchar(20);
	   set @name = 'arun'
	   declare @salary int;
	   set @salary = -900

	begin try 
	   if @salary < 0
	   begin 
			throw 50001,'Salary must be greater then 0',1;
	   end 

	   insert into employees (emp_name , salary) values(@name, @salary);
	commit transaction;

    end try

	begin catch 
		rollback transaction;
		select ERROR_MESSAGE() as error_message;
	end catch;


	begin transaction 

	   declare @name varchar(20);
	   set @name = 'arun'
	   declare @salary int;
	   set @salary = -900

	begin try 
	   if @salary < 0
	   begin 
			raiserror('Salary should be greater then 0 ', 16, 1)
	   end 

	   insert into employees (emp_name , salary) values(@name, @salary);
	commit transaction;

    end try

	begin catch 
		rollback transaction;
		select ERROR_MESSAGE() as error_message;
	end catch;


-- find the average numbers of orders placed each week in each product category 
-- using CTE (for this we have 2 tables, Orders table(Order_id, order_quantity, order_date)
-- and Products category(Product_id, Product_name)  



create table Orders (
    order_id int identity(1,1) primary key,
    product_id int,
    order_quantity int,
    order_date date
);

insert into Orders (product_id, order_quantity, order_date)
values
(1, 5, '2026-01-01'),
(2, 10, '2026-01-02'),
(1, 3, '2026-01-08'),
(3, 7, '2026-01-10'),
(2, 2, '2026-01-15');

create table Products (
    product_id int primary key,
    product_name varchar(50)
);

insert into Products (product_id, product_name)
values
(1, 'Laptop'),
(2, 'Keyboard'),
(3, 'Mouse');

with t as (
select product_id from Products group by product_id
)
select avg(order_quantity) as avg_orders , datepart(week, order_date) as order_week, t.product_id as Product_Id from Orders  
inner join t on t.product_id= Orders.product_id
group by datepart(week, order_date) , t.product_id;

--using windows functions 

select p.product_id,p.product_name , Orders.order_date , avg(order_quantity) 
over(partition by datepart(week, Orders.order_date) , p.product_id) as avg_orders_per_week  from Products as p
inner join Orders on Orders.product_id  = p.product_id;

-- Create a view to Find top 2 the best-ranking employees in each department. 

select * from #employee;

select * into employee 
from #employee;

select * from employee;

create view best_rank as 
select emp_id, emp_name , ranking from
(
select emp_id , emp_name , rank() over(partition by department order by score desc)
as ranking from employee e 
) as X;

select * from best_rank;

-- find the best department by using the performance of employees (ranking) 

alter table employee add performance int;
update employee
set performance = case emp_id
    when 1 then 80
    when 2 then 90
    when 3 then 85
    when 4 then 95
    when 5 then 88
    when 6 then 92
end;

select top 1 department, avg(performance) as avg_performance
from employee
group by department
order by avg_performance desc;
