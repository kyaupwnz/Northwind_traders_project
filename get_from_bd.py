import psycopg2
import json
config = {'host' : 'localhost', 'database' : 'Northwind Traders', 'user' : 'postgres', 'password' : '12345'}
def get_product_by_id(config, id):
    with psycopg2.connect(
        host=config.get('host'),
        database=config.get('database'),
        user=config.get('user'),
        password=config.get('password')
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT product_id, product_name, category_name, unit_price FROM products JOIN categories USING(category_id) WHERE product_id = {id}")
            result = cur.fetchone()
            columns =['product_id', 'product_name', 'category_name', 'unit_price']
            result = dict(zip(columns, result))
            return json.dumps(result)
def get_category_by_id(config, id):
    with psycopg2.connect(
        host=config.get('host'),
        database=config.get('database'),
        user=config.get('user'),
        password=config.get('password')
    ) as conn:
        with conn.cursor() as cur:
            cur.execute(f"SELECT category_id, category_name, description, product_name FROM categories JOIN products USING(category_id) WHERE category_id = {id}")
            answer = cur.fetchall()
            products_list = []
            for record in answer:
                products_list.append(record[3])
            result = list(answer[0])
            result[3] = products_list
            columns = ['category_id', 'category_name', 'description', 'product_name']
            result = dict(zip(columns, result))
            return json.dumps(result)


get_product_by_id(config, 15)
get_category_by_id(config, 1)