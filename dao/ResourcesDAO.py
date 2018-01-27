from config.dbconfig import pg_config
import psycopg2

class ResourcesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resources;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourcesById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resources where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getResourcesBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select * from resources where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getResourcesByQuantity(self, qty):
        cursor = self.conn.cursor()
        query = "select * from resources where qty = %s;"
        cursor.execute(query, (qty,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourceQuantity(self, rid):
        cursor = self.conn.cursor()
        query = "select qty from resources where rid = %s;"
        cursor.execute(query, (rid,))
        qty = cursor.fetchone()[0]
        self.conn.commit()
        return qty

    def getResourcePrice(self, rid):
        cursor = self.conn.cursor()
        query = "select price from resources where rid = %s;"
        cursor.execute(query, (rid,))
        price = cursor.fetchone()[0]
        self.conn.commit()
        return price

    def getResourceSupplierId(self, rid):
        cursor = self.conn.cursor()
        query = "select sid from resources where rid = %s;"
        cursor.execute(query, (rid,))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid


    def getSupplierByResourcesId(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resources natural inner join supplier where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, sid, qty, price):
        cursor = self.conn.cursor()
        query = "insert into resources(sid, qty, price) values (%s, %s, %s) returning rid;"
        cursor.execute(query, (sid, qty, price,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def updateQuantity(self, rid, qty):
        cursor = self.conn.cursor()
        query = "update resources set qty = qty - %s where rid = %s;"
        cursor.execute(query, (qty, rid,))
        self.conn.commit()
        return rid


    def updatePrice(self, rid, price):
        cursor = self.conn.cursor()
        query = "update resources set price = %s where rid = %s;"
        cursor.execute(query, (price, rid,))
        self.conn.commit()
        return rid

    def verifyResourceId(self, rid):
        cursor = self.conn.cursor()
        query = "select rid from resources where rid = %s;"
        cursor.execute(query, (rid,))
        vrid = cursor.fetchone()[0]
        self.conn.commit()
        return vrid

