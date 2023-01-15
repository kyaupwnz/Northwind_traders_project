import psycopg2

def executeScriptsFromFile(filename):
    with psycopg2.connect(
            host='localhost',
            database='Northwind Traders',
            user='postgres',
            password='12345'
    ) as conn:
        with conn.cursor() as cur:
            fd = open(filename, 'r', encoding='UTF-8')
            sqlFile = fd.read()
            fd.close()
            sqlCommands = sqlFile.split(';')
            for command in sqlCommands:
                cur.execute(command)
                result = cur.fetchall()
                print(result)




executeScriptsFromFile('customers_page.sql')