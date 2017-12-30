from config.dbconfig import pg_config
import psycopg2

class SalesRecordDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllSalesRecord(self):
        cursor = self.conn.cursor()
        query = "select * from salesrecord;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getSalesRecordById(self, sid):
        cursor = self.conn.cursor()
        query = "select * from salesrecord where sid = %s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result


    def getSalesRecordByEarnings(self, earnings):
        cursor = self.conn.cursor()
        query = "select * from salesrecord where earnings = %s;"
        cursor.execute(query, (earnings,))
        result = [] 
        for row in cursor:
            result.append(row)
        return result


    def getSalesRecordBySales(self, sales):
        cursor = self.conn.cursor()
        query = "select * from salesrecord where sales = %s;"
        cursor.execute(query, (sales,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getSalesRecordByEarningsAndSales(self, earnings, sales):
        cursor = self.conn.cursor()
        query = "select * from salesrecord where earnings = %s and sales = %s;"
        cursor.execute(query, (earnings, sales,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, sid, earnings, sales):
        cursor = self.conn.cursor()
        query = "insert into salesrecord values (%s, %s, %s) returning sid;"
        cursor.execute(query, (sid, earnings, sales,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return sid
