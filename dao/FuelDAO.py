from config.dbconfig import pg_config
import psycopg2

class FuelDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllFuel(self):
        cursor = self.conn.cursor()
        query = "select * from fuel;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getFuelById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from fuel where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getFuelByType(self, ftype):
        cursor = self.conn.cursor()
        query = "select * from fuel where ftype = %s;"
        cursor.execute(query, (ftype,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getFuelByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from fuel where price = %s;"
        cursor.execute(query, (price,))
        result = [] 
        for row in cursor:
             result.append(row)
        return result


    def getFuelByContainerSize(self, csize):
        cursor = self.conn.cursor()
        query = "select * from fuel where containersize = %s;"
        cursor.execute(query, (csize,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getPurchaseByFuelId(self, rid):
        cursor = self.conn.cursor()
        query = "select pid, cid, sid, rid, qty, total, ccnum from purchase natural inner join fuel where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, rid, ftype, price, csize):
        cursor = self.conn.cursor()
        query = "insert into fuel values (%s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rid, ftype, price, csize,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid
