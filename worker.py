import select
import psycopg2 as pg
import psycopg2.extensions as pgext



def listen():
    dbConn = pg.connect(host="localhost", user="user", password="p4ssw0rd", dbname="CSCI6720G")
    dbConn.set_isolation_level(pgext.ISOLATION_LEVEL_AUTOCOMMIT)

    cursor = dbConn.cursor()
    cursor.execute("LISTEN test;")

    print ("Waiting for notifications on channel 'test'")
    while 1:
        if select.select([dbConn],[],[],5) == ([],[],[]):
            print ("Timeout")
        else:
            dbConn.poll()
            while dbConn.notifies:
                notify = dbConn.notifies.pop(0)
                print(notify)
                print ("Notification:", notify.pid, notify.channel, notify.payload)


if __name__=="__main__":
    listen()
