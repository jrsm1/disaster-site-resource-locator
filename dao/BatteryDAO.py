from config.dbconfig import pg_config
import psycopg2


class BatteryDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllBattery(self):
        cursor = self.conn.cursor()
        query = "select * from battery order by btype;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getBatteryById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from battery where rid = %s order by btype;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getBatteryByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from battery where price = %s order by btype;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getBatteryByLessThanPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from battery where price < %s order by btype;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getBatteryByGreaterThanPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from battery where price > %s order by btype;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getBatteryByVoltage(self, voltage):
        cursor = self.conn.cursor()
        query = "select * from battery where voltage = %s order by btype;"
        cursor.execute(query, (voltage,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryByType(self, btype):
        cursor = self.conn.cursor()
        query = "select * from battery where btype = %s order by btype;"
        cursor.execute(query, (btype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryByPriceAndVoltage(self, price, voltage):
        cursor = self.conn.cursor()
        query = "select * from battery where price = %s and voltage = %s order by btype;"
        cursor.execute(query, (price, voltage,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryByTypeAndVoltage(self, btype, voltage):
        cursor = self.conn.cursor()
        query = "select * from battery where btype = %s and voltage = %s order by btype;"
        cursor.execute(query, (btype, voltage,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryByPriceAndType(self, price, btype):
        cursor = self.conn.cursor()
        query = "select * from battery where price = %s and btype = %s order by btype;"
        cursor.execute(query, (price, btype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryByPriceVoltageAndType(self, price, voltage, btype):
        cursor = self.conn.cursor()
        query = "select * from battery where price = %s and voltage = %s and btype = %s order by btype;"
        cursor.execute(query, (price, voltage, btype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, rid, price, voltage, btype):
        cursor = self.conn.cursor()
        query = "insert into battery(rid, price, voltage, btype) values (%s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rid, price, voltage, btype,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid


    def update(self, rid, price, voltage, btype):
        cursor = self.conn.cursor()
        query = "update battery set price = %s, voltage = %s, btype = %s where rid = %s;"
        cursor.execute(query, (price, voltage, btype, rid,))
        self.conn.commit()
        return rid



    def getBatterySuppliers(self):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where rid IN (select rid from battery);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatterySuppliersByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where region = %s and " \
                "rid IN (select rid from battery);"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getAllBatteryRequests(self):
        cursor = self.conn.cursor()
        query = "select * from battery natural inner join request order by btype;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getBatteryRequestsById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from battery natural inner join request where rid = %s order by btype;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getBatteryRequestsByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from battery natural inner join request where price = %s order by btype;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getBatteryRequestsByVoltage(self, voltage):
        cursor = self.conn.cursor()
        query = "select * from battery natural inner join request where voltage = %s order by btype;"
        cursor.execute(query, (voltage,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryRequestsByType(self, btype):
        cursor = self.conn.cursor()
        query = "select * from battery natural inner join request where btype = %s order by btype;"
        cursor.execute(query, (btype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryRequestsByPriceAndVoltage(self, price, voltage):
        cursor = self.conn.cursor()
        query = "select * from battery natural inner join request where price = %s and voltage = %s order by btype;"
        cursor.execute(query, (price, voltage,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryRequestsByTypeAndVoltage(self, btype, voltage):
        cursor = self.conn.cursor()
        query = "select * from battery natural inner join request where btype = %s and voltage = %s order by btype;"
        cursor.execute(query, (btype, voltage,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryRequestsByPriceAndType(self, price, btype):
        cursor = self.conn.cursor()
        query = "select * from battery natural inner join request where price = %s and btype = %s order by btype;"
        cursor.execute(query, (price, btype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryRequestsByPriceVoltageAndType(self, price, voltage, btype):
        cursor = self.conn.cursor()
        query = "select * from battery natural inner join request where price = %s and voltage = %s and btype = %s order by btype;"
        cursor.execute(query, (price, voltage, btype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

