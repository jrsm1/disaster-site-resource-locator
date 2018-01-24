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
        query = "select * from HeavyEquip order by function;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where rid = %s order by function;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getEquipByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s order by function;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getEquipByLessThanPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price < %s order by function;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getEquipByGreaterThanPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price > %s order by function;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getEquipByMake(self, make):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where make = %s order by function;"
        cursor.execute(query, (make,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByCondition(self, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where condition = %s order by function;"
        cursor.execute(query, (condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByFunction(self, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where function = %s order by function;"
        cursor.execute(query, (equipfunction,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceAndMake(self, price, make):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and make= %s order by function;"
        cursor.execute(query, (price, make,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByConditionAndMake(self, condition, make):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where condition = %s and make = %s order by function;"
        cursor.execute(query, (condition, make,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceAndCondition(self, price, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and condition= %s order by function;"
        cursor.execute(query, (price, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceAndFunction(self, price, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and function = %s order by function;"
        cursor.execute(query, (price, equipfunction,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByFunctionAndCondition(self, equipfunction, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where function = %s and condition = %s order by function;"
        cursor.execute(query, (equipfunction, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByMakeAndFunction(self, make, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where make = %s and function = %s order by function;"
        cursor.execute(query, (make, equipfunction,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceMakeAndCondition(self, price, make, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and make = %s and condition= %s order by function;"
        cursor.execute(query, (price, make, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceMakeAndFunction(self, price, brand, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and make = %s and function = %s order by function;"
        cursor.execute(query, (price, brand, equipfunction,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceFunctionAndCondition(self, price, equipfunction, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and function= %s and condition = %s order by function;"
        cursor.execute(query, (price, equipfunction, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByFunctionMakeAndCondition(self, equipfunction, make, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where function = %s and make = %s and condition = %s order by function;"
        cursor.execute(query, (equipfunction, make, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceMakeConditionAndFunction(self, price, make, condition, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and make = %s and condition = %s and function = %s order by function;"
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


    def update(self, rid, price, make, condition, equipfunction):
        cursor = self.conn.cursor()
        query = "update HeavyEquip set price = %s, make = %s, condition = %s, equipfunction = %s where rid = %s;"
        cursor.execute(query, (price, make, condition, equipfunction, rid,))
        self.conn.commit()
        return rid


    def getEquipSuppliers(self):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where rid IN (select rid from HeavyEquip);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getEquipSuppliersByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where region = %s and " \
                "rid IN (select rid from HeavyEquip);"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAllEquipRequests(self):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip natural inner join request order by function;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipRequestsById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip natural inner join request where rid = %s order by function;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getEquipRequestsByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip natural inner join request where price = %s order by function;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipRequestsByMake(self, make):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip natural inner join request where make = %s order by function;"
        cursor.execute(query, (make,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipRequestsByCondition(self, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip natural inner join request where condition = %s order by function;"
        cursor.execute(query, (condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipRequestsByFunction(self, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip natural inner join request where function = %s order by function;"
        cursor.execute(query, (equipfunction,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipRequestsByPriceAndMake(self, price, make):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip natural inner join request where price = %s and make= %s order by function;"
        cursor.execute(query, (price, make,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipRequestsByConditionAndMake(self, condition, make):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip natural inner join request where condition = %s and make = %s order by function;"
        cursor.execute(query, (condition, make,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipRequestsByPriceAndCondition(self, price, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip natural inner join request where price = %s and condition= %s order by function;"
        cursor.execute(query, (price, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipRequestsByPriceAndFunction(self, price, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip natural inner join request where price = %s and function = %s order by function;"
        cursor.execute(query, (price, equipfunction,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipRequestsByFunctionAndCondition(self, equipfunction, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip natural inner join request where function = %s and condition = %s order by function;"
        cursor.execute(query, (equipfunction, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipRequestsByMakeAndFunction(self, make, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip natural inner join request where make = %s and function = %s order by function;"
        cursor.execute(query, (make, equipfunction,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceMakeAndCondition(self, price, make, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip natural inner join request where price = %s and make = %s and condition= %s order by function;"
        cursor.execute(query, (price, make, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceMakeAndFunction(self, price, brand, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and make = %s and function = %s order by function;"
        cursor.execute(query, (price, brand, equipfunction,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceFunctionAndCondition(self, price, equipfunction, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and function= %s and condition = %s order by function;"
        cursor.execute(query, (price, equipfunction, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByFunctionMakeAndCondition(self, equipfunction, make, condition):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where function = %s and make = %s and condition = %s order by function;"
        cursor.execute(query, (equipfunction, make, condition,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getEquipByPriceMakeConditionAndFunction(self, price, make, condition, equipfunction):
        cursor = self.conn.cursor()
        query = "select * from HeavyEquip where price = %s and make = %s and condition = %s and function = %s order by function;"
        cursor.execute(query, (price, make, condition, equipfunction))
        result = []
        for row in cursor:
            result.append(row)
        return result

