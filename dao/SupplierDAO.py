from config.dbconfig import pg_config
import psycopg2

class SupplierDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByID(self, sid):
        cursor = self.conn.cursor()
        query = "select * from supplier where sid = %s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result

    def getSupplierByNameRegion(self, sname, sregion):
        cursor = self.conn.cursor()
        query = "select * from Supplier where sname = %s and region = %s;"
        cursor.execute(query, (sname, sregion,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByName(self, sname):
        cursor = self.conn.cursor()
        query = "select * from supplier where sname = %s;"
        cursor.execute(query, (sname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByAddress(self, saddress):
        cursor = self.conn.cursor()
        query = "select * from supplier where saddress = %s;"
        cursor.execute(query, (saddress,))
        result = cursor.fetchone()
        return result

    def getSupplierByPhone(self, sphone):
        cursor = self.conn.cursor()
        query = "select * from supplier where sphone = %s;"
        cursor.execute(query, (sphone,))
        result = cursor.fetchone()
        return result

    def getSupplierByRegion(self, sregion):
        cursor = self.conn.cursor()
        query = "select * from supplier where region = %s;"
        cursor.execute(query, (sregion,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def Insert(self, sname, spassword, saddress, sphone, sregion):
        cursor = self.conn.cursor()
        query = "insert into supplier(sname, spassword, saddress, sphone, region) values (%s, %s, %s, %s) returning sid;"
        cursor.execute(query, (sname, spassword, saddress, sphone, sregion))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid
