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
        query = "select * from FirstAid order by brand;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAidById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where rid = %s order by brand;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getAidByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where price = %s order by brand;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAidByLessThanPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where price < %s order by brand;"
        cursor.execute(query, (price,))
        result = [] 
        for row in cursor:
            result.append(row)
        return result


    def getAidByGreaterThanPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where price > %s order by brand;"
        cursor.execute(query, (price,))
        result = [] 
        for row in cursor:
            result.append(row)
        return result


    def getAidByBrand(self, brand):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where brand = %s order by brand;"
        cursor.execute(query, (brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAidByMedCondition(self, medcondition):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where medcondition = %s order by brand;"
        cursor.execute(query, (medcondition,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAidByPriceAndBrand(self, price, brand):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where price = %s and brand = %s order by brand;"
        cursor.execute(query, (price, brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidByMedConditionAndBrand(self, medcondition, brand):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where medcondition = %s and brand = %s order by brand;"
        cursor.execute(query, (medcondition, brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAidByPriceAndMedCondition(self, price, medcondition):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where price = %s and medcondition = %s order by brand;"
        cursor.execute(query, (price, medcondition,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAidByPriceBrandAndMedCondition(self, price, brand, medcondition):
        cursor = self.conn.cursor()
        query = "select * from FirstAid where price = %s and brand = %s and medcondition = %s order by brand;"
        cursor.execute(query, (price, brand, medcondition,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, rid, price, brand, medcondition):
        cursor = self.conn.cursor()
        query = "insert into FirstAid(rid, price, brand, medcondition) values (%s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rid, price, brand, medcondition))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid


    def update(self, rid, price, brand, medcondition):
        cursor = self.conn.cursor()
        query = "update FirstAid set price = %s, brand = %s, medcondition = %s where rid = %s;"
        cursor.execute(query, (price, brand, medcondition, rid,))
        self.conn.commit()
        return rid


    def getFirstAidSuppliers(self):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where rid IN (select rid from FirstAid);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidSuppliersByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where region = %s and " \
                "rid IN (select rid from firstaid);"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAllAidRequests(self):
        cursor = self.conn.cursor()
        query = "select * from FirstAid natural inner join request order by brand;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidRequestsById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from FirstAid natural inner join request where rid = %s order by brand;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getAidRequestsByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from FirstAid natural inner join request where price = %s order by brand;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidRequestsByBrand(self, brand):
        cursor = self.conn.cursor()
        query = "select * from FirstAid natural inner join request where brand = %s order by brand;"
        cursor.execute(query, (brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidRequestsByMedCondition(self, medcondition):
        cursor = self.conn.cursor()
        query = "select * from FirstAid natural inner join request where medcondition = %s order by brand;"
        cursor.execute(query, (medcondition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidRequestsByPriceAndBrand(self, price, brand):
        cursor = self.conn.cursor()
        query = "select * from FirstAid natural inner join request where price = %s and brand = %s order by brand;"
        cursor.execute(query, (price, brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidRequestsByMedConditionAndBrand(self, medcondition, brand):
        cursor = self.conn.cursor()
        query = "select * from FirstAid natural inner join request where medcondition = %s and brand = %s order by brand;"
        cursor.execute(query, (medcondition, brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidRequestsByPriceAndMedCondition(self, price, medcondition):
        cursor = self.conn.cursor()
        query = "select * from FirstAid natural inner join request where price = %s and medcondition = %s order by brand;"
        cursor.execute(query, (price, medcondition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAidRequestsByPriceBrandAndMedCondition(self, price, brand, medcondition):
        cursor = self.conn.cursor()
        query = "select * from FirstAid natural inner join request where price = %s and brand = %s and medcondition = %s order by brand;"
        cursor.execute(query, (price, brand, medcondition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

