set sql_safe_updates = 0;

create table hr (
    emp_id int primary key auto_increment,
    emp_name varchar(50),
    department varchar(50),
    score int
);

create table development (
    emp_id int primary key auto_increment,
    emp_name varchar(50),
    department varchar(50),
    score int
);

create table data_engineering (
    emp_id int primary key auto_increment,
    emp_name varchar(50),
    department varchar(50),
    score int
);

insert into hr (emp_name, department, score) values 
('Alice', 'HR', 3),
('Bob', 'HR', 4),
('Charlie', 'HR', 5),
('Diana', 'HR', 3);

insert into development (emp_name, department, score) values 
('Eve', 'Development', 4),
('Frank', 'Development', 5),
('Grace', 'Development', 3),
('Hank', 'Development', 4);

insert into data_engineering (emp_name, department, score) values 
('Ivy', 'Data Engineering', 5),
('Jack', 'Data Engineering', 4),
('Kate', 'Data Engineering', 5),
('Leo', 'Data Engineering', 3);

create table employee as
select * from hr
union all
select * from development
union all
select * from data_engineering;

select * from employee;

alter table employee add column rating char(1);

select * from employee;

update employee
set rating = case 
    when score = 3 then 'M'
    when score = 4 then 'E'
    when score = 5 then 'S'
end;
select * from employee;


update employee set department = 'Data Science' where department = 'Data Engineering' and rating = 'S';
select * from employee;

alter table employee add index idx_name(emp_name);
select * from employee;


select * from employee use index(idx_name);
select * from employee;
