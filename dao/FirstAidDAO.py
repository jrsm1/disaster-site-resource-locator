from config.dbconfig import pg_config
import psycopg2


class FirstAidDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllAid(self):
        cursor = self.conn.cursor()
        query = "select * from FirstAid;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getAidByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where price = %s;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidByBrand(self, brand):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where brand = %s;"
        cursor.execute(query, (brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidByMedCondition(self, medcondition):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where medcondition = %s;"
        cursor.execute(query, (medcondition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidByPriceAndBrand(self, price, brand):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where price = %s and brand = %s;"
        cursor.execute(query, (price, brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidByMedConditionAndBrand(self, medcondition, brand):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where medcondition = %s and brand = %s;"
        cursor.execute(query, (medcondition, brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidByPriceAndMedCondition(self, price, medcondition):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where price = %s and medcondition = %s;"
        cursor.execute(query, (price, medcondition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidByPriceBrandAndMedCondition(self, price, brand, medcondition):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where price = %s and brand = %s and medcondition = %s;"
        cursor.execute(query, (price, brand, medcondition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, rid, price, brand, medcondition):
        cursor = self.conn.cursor()
        query = "insert into FirstAid(rid, price, brand, medcondition) values (%s, %s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rid, price, brand, medcondition))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid
