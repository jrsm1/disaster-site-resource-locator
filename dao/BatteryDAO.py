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
        query = "select * from battery;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getBatteryById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from battery where rid = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getBatteryByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from battery where price = %s;"
        cursor.execute(query, (price,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getBatteryByVoltage(self, voltage):
        cursor = self.conn.cursor()
        query = "select * from battery where voltage = %s;"
        cursor.execute(query, (voltage,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryByType(self, btype):
        cursor = self.conn.cursor()
        query = "select * from battery where btype = %s;"
        cursor.execute(query, (btype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryByPriceAndVoltage(self, price, voltage):
        cursor = self.conn.cursor()
        query = "select * from battery where price = %s and voltage = %s;"
        cursor.execute(query, (price, voltage,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryByTypeAndVoltage(self, btype, voltage):
        cursor = self.conn.cursor()
        query = "select * from battery where btype = %s and voltage = %s;"
        cursor.execute(query, (btype, voltage,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryByPriceAndType(self, price, btype):
        cursor = self.conn.cursor()
        query = "select * from battery where price = %s and btype = %s;"
        cursor.execute(query, (price, btype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getBatteryByPriceVoltageAndType(self, price, voltage, btype):
        cursor = self.conn.cursor()
        query = "select * from battery where price = %s and voltage = %s and btype = %s;"
        cursor.execute(query, (price, voltage, btype,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, price, voltage, btype):
        cursor = self.conn.cursor()
        query = "insert into battery(price, voltage, type) values (%s, %s, %s) returning rid;"
        cursor.execute(query, (price, voltage, btype,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid
