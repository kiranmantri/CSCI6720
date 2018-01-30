import pandas as pd
import select
import psycopg2 as pg
import psycopg2.extensions as pgext


dbConn = pg.connect(host="localhost", user="user", password="p4ssw0rd", dbname="CSCI6720G")
dbConn.set_isolation_level(pgext.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = dbConn.cursor()
sql = open("init.sql","r").read()
cursor.execute(sql)


sqlString = """ select * from information_schema.tables  where table_schema='public' """
cursor.execute(sqlString)
tables = cursor.fetchall()
tables = sorted([t[2] for t in tables if "pg_" not in t[2]])


for t in tables:
    sqlString = """ select column_name, data_type, character_maximum_length from INFORMATION_SCHEMA.COLUMNS where table_name = '{}';  """.format(t)    
    cursor.execute(sqlString)
    columns = [desc[0] for desc in cursor.description]
    table = pd.DataFrame(cursor.fetchall(), columns=columns)
    print("Table: {}\n\t{}".format(t, table))

    


cursor.close()



