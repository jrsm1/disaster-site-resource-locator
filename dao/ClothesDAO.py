from config.dbconfig import pg_config
import psycopg2

class ClothesDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllClothes(self):
        cursor = self.conn.cursor()
        query = "select * from clothes order by piece;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getClothesById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from clothes where rid = %s order by piece;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result


    def getClothesByPrice(self, price):
        cursor = self.conn.cursor()
        query = "select * from clothes where price = %s order by piece;"
        cursor.execute(query, (price,))
        result = [] 
        for row in cursor:
             result.append(row)
        return result


    def getClothesByColor(self, color):
        cursor = self.conn.cursor()
        query = "select * from clothes where color = %s order by piece;"
        cursor.execute(query, (color,))
        result = [] 
        for row in cursor:
             result.append(row)
        return result


    def getClothesBySize(self, size):
        cursor = self.conn.cursor()
        query = "select * from clothes where size = %s order by piece;"
        cursor.execute(query, (size,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getClothesByGender(self, gender):
        cursor = self.conn.cursor()
        query = "select * from clothes where gender = %s order by piece;"
        cursor.execute(query, (gender,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getClothesByPiece(self, piece):
        cursor = self.conn.cursor()
        query = "select * from clothes where piece = %s order by piece;"
        cursor.execute(query, (piece,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getPurchaseByClothesId(self, rid):
        cursor = self.conn.cursor()
        query = "select pid, cid, sid, rid, qty, total, ccnum from purchase natural inner join clothes where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def insert(self, rid, price, color, size, gender, piece):
        cursor = self.conn.cursor()
        query = "insert into clothes values (%s, %s, %s, %s, %s, %s) returning rid;"
        cursor.execute(query, (rid, price, color, size, gender, piece,))
        rid = cursor.fetchone()[0]
        self.conn.commit()
        return rid

    def getClothesSuppliers(self):
        cursor = self.conn.cursor()
        query = "select rid, sid, sname, saddress, sphone, region from supplier natural inner join resources where rid IN (select rid from clothes);"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result
