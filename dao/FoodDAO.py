from config.dbconfig import pg_config
import psycopg2

class FoodDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllFood(self):
        cursor = self.conn.cursor()
        query = "select * from food order by fname;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getFoodById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from food where rid = %s order by fname;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getFoodByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from food where price = %s order by fname;"
        cursor.execute(query, (price,))
        result = [] 
        for row in cursor:
             result.append(row)
        return result


    def getFoodByType(self, ftype):
        cursor = self.conn.cursor()
        query = "select * from food where ftype = %s order by fname;"
        cursor.execute(query, (ftype,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getFoodByExpDate(self, expdate):
        cursor = self.conn.cursor()
        query = "select * from food where expdate = %s order by fname;"
        cursor.execute(query, (ftype,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getFoodByName(self, fname):
        cursor = self.conn.cursor()
        query = "select * from food where fname = %s order by fname;"
        cursor.execute(query, (fname,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getPurchaseByFoodId(self, rid):
        cursor = self.conn.cursor()
        query = "select pid, cid, sid, rid, qty, total, ccnum from purchase natural inner join food where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, rid, price, ftype, expdate, fname):
        cursor = self.conn.cursor()
        query = "insert into food values (%s, %s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rid, price, ftype, expdate, fname))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def getFoodSuppliers(self):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where rid IN (select rid from food);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getFoodSuppliersByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where region = %s and " \
                "rid IN (select rid from food);"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

