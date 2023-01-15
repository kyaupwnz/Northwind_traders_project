select * from orders--Выбрать все заказы, отсортировать по required_date (по убыванию) и отсортировать по дате отгрузке (по возрастанию)
order by required_date desc, shipped_date asc;

select avg(shipped_date - order_date) from orders
where ship_country = 'USA' --Найти среднее значение дней уходящих на доставку с даты формирования заказа в USA;

select product_name, (units_in_stock * unit_price) as total_price from products
where discontinued <> 1--Найти сумму, на которую имеется товаров (количество * цену) причём таких, которые не сняты с продажи (см. на поле discontinued)