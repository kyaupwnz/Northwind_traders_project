select product_name, units_in_stock, suppliers.contact_name, suppliers.phone from products
full join suppliers using(supplier_id)
join categories using(category_id)
where category_name in ('Beverages', 'Seafood') and discontinued <> 1 and units_in_stock < 20
order by product_name--Найти активные (см. поле discontinued) продукты из категории Beverages и Seafood, которых в продаже менее 20 единиц. Вывести наименование продуктов, кол-во единиц в продаже, имя контакта поставщика и его телефонный номер.
