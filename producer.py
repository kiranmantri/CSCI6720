import time
import select
import psycopg2 as pg
import psycopg2.extensions as pgext



def produce():
    dbConn = pg.connect(host="localhost", user="user", password="p4ssw0rd", dbname="CSCI6720G")
    dbConn.set_isolation_level(pgext.ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = dbConn.cursor()
    for i in range(100):
        print(i)
        cursor.execute("NOTIFY test;")
        time.sleep(1)




if __name__=="__main__":
    produce()
