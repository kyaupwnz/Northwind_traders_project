import psycopg2
import json
import re
with psycopg2.connect(
    host='localhost',
    database='Northwind Traders',
    user='postgres',
    password='12345'
) as conn:
    with conn.cursor() as cur:
        with open('suppliers.json', 'r', encoding='utf-8') as file:
            data = json.load(file)
            result_products_list = {}
            for record in data:
                _company_name = record['company_name']
                _contact_name = record['contact'].split(',')[0]
                _contact_title = record['contact'].split(',')[1]
                _address = record['address'].split(';')[4]
                _city = record['address'].split(';')[3]
                _region = record['address'].split(';')[1]
                _postal_code = record['address'].split(';')[2]
                _country = record['address'].split(';')[0]
                _phone = record['phone']
                _fax = record['fax']
                _homepage = record['homepage']
                cur.execute("INSERT INTO suppliers (company_name, contact_name, contact_title, address, city, region, postal_code, country, phone, fax, homepage) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s) RETURNING supplier_id", (_company_name, _contact_name, _contact_title, _address, _city, _region, _postal_code, _country, _phone, _fax, _homepage))
                #_company_name = re.sub(r"'", "''", _company_name)
                #cur.execute(f"SELECT supplier_id FROM suppliers where company_name = '{_company_name}'")
                id = cur.fetchone()
                for product_item in record['products']:
                    result_products_list[product_item] = id[0]
            big_sql_row = ''
            for k, v in result_products_list.items():
                k = re.sub(r"'", "''", k)
                big_sql_row += f"UPDATE products set supplier_id = {v} where product_name = '{k}';"
            cur.execute(big_sql_row)