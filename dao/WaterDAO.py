from config.dbconfig import pg_config
import psycopg2

class WaterDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllWater(self):
        cursor = self.conn.cursor()
        query = "select * from water order by brand;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getWaterById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from water where rid = %s order by brand;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getWaterByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from water where price = %s order by brand;"
        cursor.execute(query, (price,))
        result = [] 
        for row in cursor:
            result.append(row)
        return result


    def getWaterByBottleSize(self, bsize):
        cursor = self.conn.cursor()
        query = "select * from water where bottlesize = %s order by brand;"
        cursor.execute(query, (bsize,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getWaterByBrand(self, brand):
        cursor = self.conn.cursor()
        query = "select * from water where brand = %s order by brand;"
        cursor.execute(query, (brand,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getWaterByPriceAndBottleSize(self, price, bsize):
        cursor = self.conn.cursor()
        query = "select * from water where price = %s and bottlesize = %s order by brand;"
        cursor.execute(query, (price, bsize,))
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


    def insert(self, rid, price, bsize, brand):
        cursor = self.conn.cursor()
        query = "insert into water values (%s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rid, price, bsize, brand,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid


    def update(self, rid, price, bsize, brand):
        cursor = self.conn.cursor()
        query = "update water set price = %s, bsize = %s, brand = %s, where rid = %s;"
        cursor.execute(query, (price, bsize, brand, rid,))
        self.conn.commit()
        return rid


    def getWaterSuppliers(self):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where rid IN (select rid from water);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getWaterSuppliersByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where region = %s and " \
                "rid IN (select rid from water);"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getWaterRequests(self):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join water order by brand;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getWaterRequestsById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join water where rid = %s order by brand;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getWaterRequestsByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join water where price = %s order by brand;"
        cursor.execute(query, (price,))
        result = [] 
        for row in cursor:
            result.append(row)
        return result


    def getWaterRequestsByBottleSize(self, bsize):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join water where bottlesize = %s order by brand;"
        cursor.execute(query, (bsize,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getWaterRequestsByBrand(self, brand):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join water where brand = %s order by brand;"
        cursor.execute(query, (brand,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getWaterRequestsByPriceAndBottleSize(self, price, bsize):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join water where price = %s and bottlesize = %s order by brand;"
        cursor.execute(query, (price, bsize,))
        result = []
        for row in cursor:
            result.append(row)
        return result

