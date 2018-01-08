from config.dbconfig import pg_config
import psycopg2


class HeavyEquipDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllEquip(self):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getEquipByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByMake(self, make):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where make = %s;"
        cursor.execute(query, (make,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByCondition(self, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where condition = %s;"
        cursor.execute(query, (condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByFunction(self, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where function = %s;"
        cursor.execute(query, (equipfunction,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceAndMake(self, price, make):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and make= %s;"
        cursor.execute(query, (price, make,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByConditionAndMake(self, condition, make):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where condition = %s and make = %s;"
        cursor.execute(query, (condition, make,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceAndCondition(self, price, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and condition= %s;"
        cursor.execute(query, (price, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceAndFunction(self, price, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and function = %s;"
        cursor.execute(query, (price, equipfunction,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByFunctionAndCondition(self, equipfunction, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where function = %s and condition = %s;"
        cursor.execute(query, (equipfunction, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByMakeAndFunction(self, make, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where make = %s and function = %s;"
        cursor.execute(query, (make, equipfunction,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceMakeAndCondition(self, price, make, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and make = %s and condition= %s;"
        cursor.execute(query, (price, make, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceMakeAndFunction(self, price, brand, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and make = %s and function = %s;"
        cursor.execute(query, (price, brand, equipfunction,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceFunctionAndCondition(self, price, equipfunction, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and function= %s and condition = %s;"
        cursor.execute(query, (price, equipfunction, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByFunctionMakeAndCondition(self, equipfunction, make, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where function = %s and make = %s and condition = %s;"
        cursor.execute(query, (equipfunction, make, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceMakeConditionAndFunction(self, price, make, condition, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and make = %s and condition = %s and function = %s;"
        cursor.execute(query, (price, make, condition, equipfunction))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, rid, price, make, condition, equipfunction):
        cursor = self.conn.cursor()
        query = "insert into HeavyEquip(rid, price, make, condition, function) values (%s, %s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rid, price, make, condition, equipfunction,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid
