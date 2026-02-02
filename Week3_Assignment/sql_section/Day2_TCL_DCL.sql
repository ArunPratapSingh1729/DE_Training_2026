create database vechicle_purchase;
use vechicle_purchase;

create table vehicle (
    vehicle_id int primary key auto_increment,
    vehicle_name varchar(50),
    vehicle_type varchar(30),
    price decimal(10,2)
);	

create table customer (
    customer_id int primary key auto_increment,
    customer_name varchar(50),
    phone varchar(15)
);

create table purchase (
    purchase_id int primary key auto_increment,
    customer_id int,
    vehicle_id int,
    purchase_date date,
    foreign key (customer_id) references customer(customer_id),
    foreign key (vehicle_id) references vehicle(vehicle_id)
);

start transaction;

insert into vehicle (vehicle_name, vehicle_type, price) 
values ('Car Model X', 'SUV', 500000);

insert into customer (customer_name, phone)
values ('arun', '9876543210');

insert into purchase (customer_id, vehicle_id, purchase_date)
values (1, 1, curdate());

commit;

create user 'sales_user'@'localhost' identified by 'StrongPassword123';
grant select on vechicle_purchase.customer to 'sales_user'@'localhost';
revoke insert, select on vechicle_purchase.customer from 'sales_user'@'localhost';
