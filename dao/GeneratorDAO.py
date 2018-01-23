from config.dbconfig import pg_config
import psycopg2


class GeneratorDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllGenerator(self):
        cursor = self.conn.cursor()
        query = "select * from generator order by brand;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from generator where rid = %s order by brand;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getGeneratorByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from generator where price = %s order by brand;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorByBrand(self, brand):
        cursor = self.conn.cursor()
        query = "select * from generator where brand = %s order by brand;"
        cursor.execute(query, (brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorByPowerRating(self, powerrating):
        cursor = self.conn.cursor()
        query = "select * from generator where powerrating = %s order by brand;"
        cursor.execute(query, (powerrating,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorByFuelType(self, fueltype):
        cursor = self.conn.cursor()
        query = "select * from generator where fueltype = %s order by brand;"
        cursor.execute(query, (fueltype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorByPriceAndBrand(self, price, brand):
        cursor = self.conn.cursor()
        query = "select * from generator where price = %s and brand = %s order by brand;"
        cursor.execute(query, (price, brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorByFuelTypeAndBrand(self, fueltype, brand):
        cursor = self.conn.cursor()
        query = "select * from generator where fueltype = %s and brand = %s order by brand;"
        cursor.execute(query, (fueltype, brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorByPriceAndFuelType(self, price, fueltype):
        cursor = self.conn.cursor()
        query = "select * from generator where price = %s and fueltype = %s order by brand;"
        cursor.execute(query, (price, fueltype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorByPriceAndPowerRating(self, price, powerrating):
        cursor = self.conn.cursor()
        query = "select * from generator where price = %s and powerrating = %s order by brand;"
        cursor.execute(query, (price, powerrating,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorByPowerRatingAndFuelType(self, powerrating, fueltype):
        cursor = self.conn.cursor()
        query = "select * from generator where powerrating = %s and fueltype = %s order by brand;"
        cursor.execute(query, (powerrating, fueltype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorByBrandAndPowerRating(self, brand, powerrating):
        cursor = self.conn.cursor()
        query = "select * from generator where brand = %s and powerrating = %s order by brand;"
        cursor.execute(query, (brand, powerrating,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorByPriceBrandAndFuelType(self, price, brand, fueltype):
        cursor = self.conn.cursor()
        query = "select * from generator where price = %s and brand = %s and fueltype = %s order by brand;"
        cursor.execute(query, (price, brand, fueltype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorByPriceBrandAndPowerRating(self, price, brand, powerrating):
        cursor = self.conn.cursor()
        query = "select * from generator where price = %s and brand = %s and powerrating = %s order by brand;"
        cursor.execute(query, (price, brand, powerrating,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorByPricePowerRatingAndFuelType(self, price, powerrating, fueltype):
        cursor = self.conn.cursor()
        query = "select * from generator where price = %s and powerrating = %s and fueltype = %s order by brand;"
        cursor.execute(query, (price, powerrating, fueltype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorByPowerRatingBrandAndFuelType(self, powerrating, brand, fueltype):
        cursor = self.conn.cursor()
        query = "select * from generator where powerrating = %s and brand = %s and fueltype = %s order by brand;"
        cursor.execute(query, (powerrating, brand, fueltype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorByPriceBrandFuelTypeAndPowerRating(self, price, brand, fueltype, powerrating):
        cursor = self.conn.cursor()
        query = "select * from generator where price = %s and brand = %s and fueltype = %s and powerrating = %s order by brand;"
        cursor.execute(query, (price, brand, fueltype, powerrating))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, rid, price, brand, fueltype, powerrating):
        cursor = self.conn.cursor()
        query = "insert into generator(rid, price, brand, fueltype, powerrating) values (%s, %s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rid, price, brand, fueltype, powerrating,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def update(self, rid, price, brand, fueltype, powerrating):
        cursor = self.conn.cursor()
        query = "update generator set price = %s, brand = %s, fueltype = %s, powerrating = %s where rid = %s;"
        cursor.execute(query, (price, brand, fueltype, powerrating, rid,))
        self.conn.commit()
        return rid

    def getGeneratorSuppliers(self):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where rid IN (select rid from generator);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorSuppliersByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where region = %s and " \
                "rid IN (select rid from generator);"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAllGeneratorRequests(self):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator order by brand;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where rid = %s order by brand;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    def getGeneratorRequestsByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where price = %s order by brand;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsByBrand(self, brand):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where brand = %s order by brand;"
        cursor.execute(query, (brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsByPowerRating(self, powerrating):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where powerrating = %s order by brand;"
        cursor.execute(query, (powerrating,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsByFuelType(self, fueltype):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where fueltype = %s order by brand;"
        cursor.execute(query, (fueltype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsByPriceAndBrand(self, price, brand):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where price = %s and brand = %s order by brand;"
        cursor.execute(query, (price, brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsByFuelTypeAndBrand(self, fueltype, brand):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where fueltype = %s and brand = %s order by brand;"
        cursor.execute(query, (fueltype, brand,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsByPriceAndFuelType(self, price, fueltype):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where price = %s and fueltype = %s order by brand;"
        cursor.execute(query, (price, fueltype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsByPriceAndPowerRating(self, price, powerrating):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where price = %s and powerrating = %s order by brand;"
        cursor.execute(query, (price, powerrating,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsByPowerRatingAndFuelType(self, powerrating, fueltype):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where powerrating = %s and fueltype = %s order by brand;"
        cursor.execute(query, (powerrating, fueltype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsByBrandAndPowerRating(self, brand, powerrating):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where brand = %s and powerrating = %s order by brand;"
        cursor.execute(query, (brand, powerrating,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsByPriceBrandAndFuelType(self, price, brand, fueltype):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where price = %s and brand = %s and fueltype = %s order by brand;"
        cursor.execute(query, (price, brand, fueltype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsByPriceBrandAndPowerRating(self, price, brand, powerrating):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where price = %s and brand = %s and powerrating = %s order by brand;"
        cursor.execute(query, (price, brand, powerrating,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsByPricePowerRatingAndFuelType(self, price, powerrating, fueltype):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where price = %s and powerrating = %s and fueltype = %s order by brand;"
        cursor.execute(query, (price, powerrating, fueltype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsByPowerRatingBrandAndFuelType(self, powerrating, brand, fueltype):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where powerrating = %s and brand = %s and fueltype = %s order by brand;"
        cursor.execute(query, (powerrating, brand, fueltype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getGeneratorRequestsByPriceBrandFuelTypeAndPowerRating(self, price, brand, fueltype, powerrating):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join generator where price = %s and brand = %s and fueltype = %s and powerrating = %s order by brand;"
        cursor.execute(query, (price, brand, fueltype, powerrating))
        result = []
        for row in cursor:
            result.append(row)
        return result
