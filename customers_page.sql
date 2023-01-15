select count(1) from customers--Посчитать количество заказчиков;

select distinct city, country from customers
order by country, city--Выбрать все уникальные сочетания городов и стран, в которых "зарегестрированы" заказчики;

select customers.company_name, customers.contact_name from orders
join customers using(customer_id)--Найти заказчиков и обслуживающих их заказы сотрудников, таких, что и заказчики и сотрудники из города London, а доставка идёт компанией Speedy Express. Вывести компанию заказчика и ФИО сотрудника.
join employees using(employee_id)
join shippers on shippers.shipper_id = orders.ship_via
where customers.city = 'London' and employees.city = 'London' and shippers.company_name = 'Speedy Express';

select contact_name, order_id from customers
full join orders using(customer_id)
where orders.customer_id is null--Найти заказчиков, не сделавших ни одного заказа. Вывести имя заказчика и order_id.

