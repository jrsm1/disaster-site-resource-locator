from config.dbconfig import pg_config
import psycopg2

class PurchaseDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllPurchases(self):
        cursor = self.conn.cursor()
        query = "select * from purchase;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getPurchaseById(self, pid):
        cursor = self.conn.cursor()
        query = "select * from purchase where pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result


     def getPurchasesByClientId(self, cid):
        cursor = self.conn.cursor()
        query = "select * from purchase where cid = %s;"
        cursor.execute(query, (cid,))
        result = []                                                                                                   
            for row in cursor:
                result.append(row)
            return result


    def getPurchaseBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select * from purchase where sid = %s;"
        cursor.execute(query, (cid,))
        result = []
            for row in cursor:
                result.append(row)
            return result


    def getPurchaseByResourceId(self, rid):
        cursor = self.conn.cursor()
        query = "select * from purchase where rid = %s;"
        cursor.execute(query, (cid,))
        result = []
            for row in cursor:
                result.append(row)
            return result


    def getPurchaseByQuantity(self, qty):
        cursor = self.conn.cursor()
        query = "select * from purchase where qty = %s;"
        cursor.execute(query, (qty,))
        result = []
            for row in cursor:
                result.append(row)
            return result


    def getPurchaseByTotal(self, total):
        cursor = self.conn.cursor()
        query = "select * from purchase where total = %s;"
        cursor.execute(query, (total,))
        result = []
            for row in cursor:
                result.append(row)
            return result


    def getPurchaseBySupplierAndTotal(self, sid, total):
        cursor = self.conn.cursor()
        query = "select * from purchase where sid = %s and total = %s;"
        cursor.execute(query, (sid, total,))
        result = []
            for row in cursor:
                result.append(row)
            return result


    def getPurchaseBySupplierAndQuantity(self, sid, qty):
        cursor = self.conn.cursor()
        query = "select * from purchase where sid = %s and qty = %s;"
        cursor.execute(query, (sid, qty,))
        result = []
            for row in cursor:
                result.append(row)
            return result


    def getPurchasesByClientAndTotal(self, cid, total):
        cursor = self.conn.cursor()
        query = "select * from purchase where cid = %s and total = %s;"
        cursor.execute(query, (cid, total,))
        result = []
            for row in cursor:
                result.append(row)
            return result


    def getPurchaseByClientAndQuantity(self, cid, qty):
        cursor = self.conn.cursor()
        query = "select * from purchase where cid = %s and qty = %s;"
        cursor.execute(query, (cid, qty,))
        result = []
            for row in cursor:
                result.append(row)
            return result


    def getSupplierByPurchaseId(self, pid):
        cursor = self.conn.cursor()
        query = "select sid, sname, region, phone, address from purchase natural inner join supplier where pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result


    def getClientByPurchaseId(self, pid):
        cursor = self.conn.cursor()
        query = "select cid, cname, region, address from purchase natural inner join client where pid = %s;"
        cursor.execute(query, (pid,))
        result = cursor.fetchone()
        return result


    def insert(self, cid, sid, rid, qty, total, ccnum):
        cursor = self.conn.cursor()
        query = "insert into purchase(cid, sid, rid, qty, total, ccnum) values (%s, %s, %s, %s, %s, %s) returning pid;"
        cursor.execute(query, (cid, sid, rid, qty, total, ccnum,))
        pid = cursor.fetchone()[0]
        self.conn.commit()
        return pid
