from config.dbconfig import pg_config
import psycopg2

class WaterDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllWater(self):
        cursor = self.conn.cursor()
        query = "select * from water;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getWaterById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from water where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getWaterByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from water where price = %s;"
        cursor.execute(query, (price,))
        result = [] 
            for row in cursor:
                result.append(row)
            return result


     def getWaterBySize(self, size):
        cursor = self.conn.cursor()
        query = "select * from water where size = %s;"
        cursor.execute(query, (size,))
        result = []                                                                                                   
            for row in cursor:
                result.append(row)
            return result


    def getWaterByPriceAndSize(self, price, size):
        cursor = self.conn.cursor()
        query = "select * from water where price = %s and size = %s;"
        cursor.execute(query, (price, size,))
        result = []
            for row in cursor:
                result.append(row)
            return result


    def getPurchaseByWaterId(self, rid):
        cursor = self.conn.cursor()
        query = "select pid, cid, sid, rid, qty, total, ccnum from purchase natural inner join water where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
            for row in cursor:
                result.append(row)
            return result


    def insert(self, price, size):
        cursor = self.conn.cursor()
        query = "insert into water(price, size) values (%s, %s) returning rid;"
        cursor.execute(query, (price, size,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid
