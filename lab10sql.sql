select * from vendor

-- CREATE TABLE vendor (
-- 	vendor_id int primary key,
-- 	vendor_name varchar(100),
-- 	vendor_acct_payable smallint
-- );

-- CREATE TABLE product (
-- 	product_id int primary key,
-- 	product_name varchar(100),
-- 	product_desc text,
-- 	product_price decimal(9,2),
--  vendor_id int,
-- 	foreign key (vendor_id) references vendor(vendor_id)
-- );

-- CREATE TABLE order_table (
-- 	order_id int primary key,
-- 	order_date date,
-- 	order_arrival_date date,
--     vendor_id int,
--     foreign key (vendor_id) references vendor(vendor_id)
-- );

-- CREATE TABLE line_item (
-- 	order_id int,
-- 	line_number smallint,
-- 	product_id int,
-- 	line_quantity int,
-- 	line_cost decimal(10,2),
-- 	primary key(order_id, line_number),
-- 	foreign key (order_id) references order_table(order_id),
-- 	foreign key (product_id) references product(product_id)
-- );

-- CREATE TABLE william_beckaskenaizer (
-- 	vendor_id int primary key,
--    FOREIGN KEY (vendor_id) REFERENCES vendor(vendor_id)
-- );


