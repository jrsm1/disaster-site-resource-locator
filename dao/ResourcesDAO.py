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


    def getResourcesByID(self, rid):
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


    def getSupplierByResourcesId(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resources natural inner join supplier where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, sid, qty):
        cursor = self.conn.cursor()
        query = "insert into resources(sid, qty) values (%s, %s) returning rid;"
        cursor.execute(query, (sid, qty,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid
