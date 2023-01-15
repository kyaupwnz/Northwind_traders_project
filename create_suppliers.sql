create table suppliers (
	supplier_id serial Primary key,
	company_name varchar(50),
	contact_name varchar(50),
	contact_title varchar(50),
	address varchar(60),
	city varchar(20),
	region varchar(15),
	postal_code varchar(10),
	country varchar(15),
	phone varchar(25),
	fax varchar(25),
	homepage text
);

alter table products add column supplier_id smallint;
alter table products add constraint fk_products_suppliers
foreign key (supplier_id) references suppliers (supplier_id)
on delete cascade
on update cascade;
select * from categories