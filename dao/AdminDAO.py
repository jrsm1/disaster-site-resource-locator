from config.dbconfig import pg_config
import psycopg2

class AdminDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAdmins(self):
        cursor = self.conn.cursor()
        query = "select * from admin;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAdminById(self, aid):
        cursor = self.conn.cursor()
        query = "select * from admin where aid = %s;"
        cursor.execute(query, (aid,))
        result = cursor.fetchone()
        return result


    def getAdminByName(self, aname):
        cursor = self.conn.cursor()
        query = "select * from admin where aname = %s;"
        cursor.execute(query, (aname,))
        result = cursor.fetchone()
        return result


    def insert(self, aname, apassword):
        cursor = self.conn.cursor()
        query = "insert into admin values (%s, %s) returning aid;"
        cursor.execute(query, (aname, apassword,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def getAdminIds(self):
        cursor = self.conn.cursor()
        query = "select aid from admin;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminNames(self):
        cursor = self.conn.cursor()
        query = "select aname from admin;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAdminPasswords(self):
        pass
