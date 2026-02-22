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

select orderdetail_id , order_id , quantity from OrderDetails,
 group by rollup (orderdeatil_id, order_id);
