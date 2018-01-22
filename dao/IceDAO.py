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
        query = "select * from ice order by bagsize;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getIceById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from ice where rid = %s order by bagsize;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getIceByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from ice where price = %s order by bagsize;"
        cursor.execute(query, (price,))
        result = [] 
        for row in cursor:
             result.append(row)
        return result


    def getIceByBagSize(self, bsize):
        cursor = self.conn.cursor()
        query = "select * from ice where bagsize = %s order by bagsize;"
        cursor.execute(query, (bsize,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getIceByPriceAndBagSize(self, price, bsize):
        cursor = self.conn.cursor()
        query = "select * from ice where price = %s and bagsize = %s order by bagsize;"
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

    def getIceSuppliers(self):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where rid IN (select rid from ice);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getIceSuppliersByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where region = %s and " \
                "rid IN (select rid from ice);"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAllIceRequests(self):
        cursor = self.conn.cursor()
        query = "select * from ice natural inner join request order by bagsize;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getIceRequestsById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from ice natural inner join request where rid = %s order by bagsize;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getIceRequestsByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from ice natural inner join request where price = %s order by bagsize;"
        cursor.execute(query, (price,))
        result = [] 
        for row in cursor:
             result.append(row)
        return result


    def getIceRequestsByBagSize(self, bsize):
        cursor = self.conn.cursor()
        query = "select * from ice natural inner join request where bagsize = %s order by bagsize;"
        cursor.execute(query, (bsize,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getIceRequestsByPriceAndBagSize(self, price, bsize):
        cursor = self.conn.cursor()
        query = "select * from ice natural inner join request where price = %s and bagsize = %s order by bagsize;"
        cursor.execute(query, (price, bsize,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, rid, price, bagsize):
        cursor = self.conn.cursor()
        query = "insert into ice values (%s, %s, %s) returning rid;"
        cursor.execute(query, (rid, price, bagsize,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid


    def update(self, rid, price, bagsize):
        cursor = self.conn.cursor()
        query = "update ice set price = %s, bagsize = %s where rid = %s;"
        cursor.execute(query, (price, bagsize, rid,))
        self.conn.commit()
        return rid
