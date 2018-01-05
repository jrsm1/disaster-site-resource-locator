from config.dbconfig import pg_config
import psycopg2

class ToolsDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllTools(self):
        cursor = self.conn.cursor()
        query = "select * from tools;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getToolsById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from tools where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getToolsByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from tools where name = %s;"
        cursor.execute(query, (name,))
        result = [] 
        for row in cursor:
             result.append(row)
        return result


    def getToolsByBrand(self, brand):
        cursor = self.conn.cursor()
        query = "select * from tools where brand = %s;"
        cursor.execute(query, (brand,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getToolsByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from tools where price = %s;"
        cursor.execute(query, (price,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getToolsByNameAndBrand(self, name, brand):
        cursor = self.conn.cursor()
        query = "select * from tools where name = %s and brand = %s;"
        cursor.execute(query, (name, brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getPurchaseByToolsId(self, rid):
        cursor = self.conn.cursor()
        query = "select pid, cid, sid, rid, qty, total, ccnum from purchase natural inner join tools where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, rid, name, brand, price):
        cursor = self.conn.cursor()
        query = "insert into tools values (%s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rid, name, brand, price,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid
