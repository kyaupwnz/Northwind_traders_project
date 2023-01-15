select first_name, last_name, home_phone, region from employees
where region is null--Выбрать записи работников (включить колонки имени, фамилии, телефона, региона) в которых регион неизвестен;

select distinct country from customers--Выбрать такие страны в которых "зарегистированы" одновременно заказчики и поставщики, но при этом в них не "зарегистрированы" работники
where exists(select 1 from suppliers where customers.country = suppliers.country) and not exists(select 1 from employees where customers.country = employees.country)



