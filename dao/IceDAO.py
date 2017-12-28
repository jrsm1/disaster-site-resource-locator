from config.dbconfig import pg_config
import psycopg2

class IceDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
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


    def getIceBySize(self, size):
        cursor = self.conn.cursor()
        query = "select * from ice where size = %s;"
        cursor.execute(query, (size,))
        result = []                                                                                                   
            for row in cursor:
                result.append(row)
            return result


    def getIceByPriceAndSize(self, price, size):
        cursor = self.conn.cursor()
        query = "select * from ice where price = %s and size = %s;"
        cursor.execute(query, (price, size,))
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


    def insert(self, price, size):
        cursor = self.conn.cursor()
        query = "insert into ice(price, size) values (%s, %s) returning rid;"
        cursor.execute(query, (price, size,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid
