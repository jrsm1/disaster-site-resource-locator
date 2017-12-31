from config.dbconfig import pg_config
import psycopg2

class RequestDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllRequest(self):
        cursor = self.conn.cursor()
        query = "select * from request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getRequestById(self, requestid):
        cursor = self.conn.cursor()
        query = "select * from request where requestid = %s;"
        cursor.execute(query, (requestid,))
        result = cursor.fetchone()
        return result


    def getRequestByClientId(self, cid):
        cursor = self.conn.cursor()
        query = "select * from request where cid = %s;"
        cursor.execute(query, (cid,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getRequestByResourceId(self, rid):
        cursor = self.conn.cursor()
        query = "select * from request where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getRequestByQuantity(self, qty):
        cursor = self.conn.cursor()
        query = "select * from request where qty = %s;"
        cursor.execute(query, (qty,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getRequestByResourceIdAndQuantity(self, rid, qty):
        cursor = self.conn.cursor()
        query = "select * from request where rid = %s and qty = %s;"
        cursor.execute(query, (rid, qty,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getClientByRequestId(self, requestid):
        cursor = self.conn.cursor()
        query = "select cid, cname, region, address from client natural inner join request where requestid = %s;"
        cursor.execute(query, (requestid,))
        result = cursor.fetchone()
        return result


    def insert(self, cid, rid, qty):
        cursor = self.conn.cursor()
        query = "insert into request(cid, rid, qty) values (%s, %s, %s) returning requestid;"
        cursor.execute(query, (cid, rid, qty,))
        requestid = cursor.fetchone()[0]
        self.conn.commit()
        return requestid
