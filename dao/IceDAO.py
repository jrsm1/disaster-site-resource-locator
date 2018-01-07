from config.dbconfig import pg_config
import psycopg2

class IceDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllIce(self):
        cursor = self.conn.cursor()
        query = "select * from ice;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getIceById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from ice where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getIceByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from ice where price = %s;"
        cursor.execute(query, (price,))
        result = [] 
        for row in cursor:
             result.append(row)
        return result


    def getIceByBagSize(self, bsize):
        cursor = self.conn.cursor()
        query = "select * from ice where bsize = %s;"
        cursor.execute(query, (bsize,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getIceByPriceAndBagSize(self, price, bsize):
        cursor = self.conn.cursor()
        query = "select * from ice where price = %s and bsize = %s;"
        cursor.execute(query, (price, bsize,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getPurchaseByIceId(self, rid):
        cursor = self.conn.cursor()
        query = "select pid, cid, sid, rid, qty, total, ccnum from purchase natural inner join ice where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, rid, price, bsize):
        cursor = self.conn.cursor()
        query = "insert into ice values (%s, %s, %s) returning rid;"
        cursor.execute(query, (rid, price, bsize,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid
