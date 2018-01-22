from config.dbconfig import pg_config
import psycopg2


class CreditCardDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllCards(self):
        cursor = self.conn.cursor()
        query = "select * from CreditCard;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardByClientId(self, cid):
        cursor = self.conn.cursor()
        query = "select * from CreditCard where cid = %s;"
        cursor.execute(query, (cid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardByCardNumber(self, ccnum):
        cursor = self.conn.cursor()
        query = "select * from CreditCard where ccnum = %s;"
        cursor.execute(query, (ccnum,))
        result = cursor.fetchone()
        return result

    def getCardByExpirationDate(self, expdate):
        cursor = self.conn.cursor()
        query = "select * from CreditCard where expdate = %s;"
        cursor.execute(query, (expdate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardByLimit(self, limit):
        cursor = self.conn.cursor()
        query = "select * from CreditCard where climit = %s;"
        cursor.execute(query, (limit,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardByCardVerificationValue(self,cvv):
        cursor =self.conn.cursor()
        query = "select * from CreditCard where cvv = %s;"
        cursor.execute(query,(cvv,))
        result = []
        for row in cursor:
            result.append(row)
        return result




    def getCardByClientAndCardNumber(self, cid, ccnum):
        cursor = self.conn.cursor()
        query = "select * from CreditCard where cid = %s and ccnum = %s;"
        cursor.execute(query, (cid, ccnum,))
        result = cursor.fetchone()
        return result

    def getCardByClientAndExpirationDate(self, cid, expdate) :
        cursor = self.conn.cursor()
        query = "select * from CreditCard where cid = %s and expdate = %s;"
        cursor.execute(query, (cid, expdate,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardByClientAndLimit(self, cid, limit) :
        cursor = self.conn.cursor()
        query = "select * from CreditCard where cid = %s and limit = %s;"
        cursor.execute(query, (cid, limit,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardByClientAndCardVerificationValue(self, cid, cvv):
        cursor = self.conn.cursor()
        query = "select * from CreditCard where cid = %s and cvv = %s;"
        cursor.execute(query, (cid, cvv,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardByCardNumberAndExpirationDate(self, ccnum, expdate):
        cursor = self.conn.cursor()
        query = "select * from CreditCard where ccnum = %s and expdate = %s;"
        cursor.execute(query, (ccnum, expdate,))
        result = cursor.fetchone()
        return result

    def getCardByCardNumberAndLimit(self, ccnum, limit):
        cursor = self.conn.cursor()
        query = "select * from CreditCard where ccnum = %s and limit = %s;"
        cursor.execute(query, (ccnum, limit,))
        result = cursor.fetchone()
        return result

    def getCardByCardNumberAndCardVerificationValue(self, ccnum, cvv):
        cursor = self.conn.cursor()
        query = "select * from CreditCard where ccnum = %s and cvv = %s;"
        cursor.execute(query, (ccnum, cvv,))
        result = cursor.fetchone()
        return result


    def getCardByExpirationDateAndLimit(self, expdate, limit):
        cursor = self.conn.cursor()
        query = "select * from CreditCard where expdate = %s and limit = %s;"
        cursor.execute(query, (expdate, limit,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardByExpirationDateAndCardVerificationValue(self, expdate, cvv):
        cursor = self.conn.cursor()
        query = "select * from CreditCard where expdate = %s and cvv = %s;"
        cursor.execute(query, (expdate, cvv,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardByLimitAndCardVerificationValue(self, limit, cvv):
        cursor = self.conn.cursor()
        query = "select * from CreditCard where limit = %s and cvv = %s;"
        cursor.execute(query, (limit, cvv,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCardByClientAndCardNumberAndLimitAndCardVerificationValue(self, cid, ccnum, limit, cvv):
        cursor = self.conn.cursor()
        query = "select * from CreditCard where cid = %s and ccnum = %s and limit = %s and cvv = %s;"
        cursor.execute(query, (cid, ccnum, limit, cvv,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, cid, ccnum, expdate, limit, cvv):
        cursor = self.conn.cursor()
        query = "insert into CreditCard(cid, ccnum, expdate, limit, cvv) values (%s, %s, %s, %s, %s);"
        cursor.execute(query, (cid, ccnum, expdate, limit, cvv))
        self.conn.commit()

    def update(self, cid, ccnum, expdate, limit, cvv):
        cursor = self.conn.cursor()
        query = "update CreditCard set ccnum = %s, expdate = %s, limit = %s, cvv = %s where cid = %s;"
        cursor.execute(query, (ccnum, expdate, limit, cvv, cid,))
        self.conn.commit()
        return cid
