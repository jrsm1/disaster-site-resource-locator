from config.dbconfig import pg_config
import psycopg2

class ClientDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllClients(self):
        cursor = self.conn.cursor()
        query = "select * from client;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClientByID(self, cid):
        cursor = self.conn.cursor()
        query = "select * from client where cid = %s;"
        cursor.execute(query, (cid,))
        result = cursor.fetchone()
        return result

    def getClientByNameRegion(self, cname, region):
        cursor = self.conn.cursor()
        query = "select * from client where cname = %s and region = %s;"
        cursor.execute(query, (cname, region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClientByName(self, cname):
        cursor = self.conn.cursor()
        query = "select * from client where cname = %s;"
        cursor.execute(query, (cname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getClientByAddress(self, address):
        cursor = self.conn.cursor()
        query = "select * from client where address = %s;"
        cursor.execute(query, (address,))
        result = cursor.fetchone()
        return result

    def getClientByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select * from client where region = %s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def Insert(self, cname, cpassword, address, region):
        cursor = self.conn.cursor()
        query = "insert into supplier(cname, cpassword, address, region) values (%s, %s, %s, %s) returning sid;"
        cursor.execute(query, (cname, cpassword, address, region))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid

    def getClientBy(self, selection):
        cursor = self.conn.cursor()
        if selection == "cname":
            query = "select cname from client;"
        elif selection == "address":
            query = "select caddress from client;"
        elif selection == "region":
            query = "select region from client;"
        elif selection == "cid":
            query = "select cid from client;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCCByCID(self, cid):
        cursor = self.conn.cursor()
        query = "select * from creditcard where cid = %s;"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result
