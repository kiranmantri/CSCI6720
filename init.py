import select
import psycopg2 as pg
import psycopg2.extensions as pgext


dbConn = pg.connect(host="localhost", user="user", password="p4ssw0rd", dbname="CSCI6720G")
dbConn.set_isolation_level(pgext.ISOLATION_LEVEL_AUTOCOMMIT)

cursor = dbConn.cursor()
sql = open("init.sql","r").read()

cursor.execute(sql)
cursor.close()
