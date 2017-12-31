from config.dbconfig import pg_config
import psycopg2

class ReservationDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s host=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['host'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    def getAllReservation(self):
        cursor = self.conn.cursor()
        query = "select * from reservation;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getReservationById(self, reservationid):
        cursor = self.conn.cursor()
        query = "select * from reservation where reservationid = %s;"
        cursor.execute(query, (reservationid,))
        result = cursor.fetchone()
        return result


    def getReservationByClientId(self, cid):
        cursor = self.conn.cursor()
        query = "select * from reservation where cid = %s;"
        cursor.execute(query, (cid,))
        result = []                                                                                                   
        for row in cursor:
            result.append(row)
        return result


    def getReservationBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select * from reservation where sid = %s;"
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getReservationByResourceId(self, rid):
        cursor = self.conn.cursor()
        query = "select * from reservation where rid = %s;"
        cursor.execute(query, (rid,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getReservationByQuantity(self, qty):
        cursor = self.conn.cursor()
        query = "select * from reservation where qty = %s;"
        cursor.execute(query, (qty,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getReservationByResourceIdAndQuantity(self, rid, qty):
        cursor = self.conn.cursor()
        query = "select * from reservation where rid = %s and qty = %s;"
        cursor.execute(query, (rid, qty,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getSupplierByReservationId(self, reservationid):
        cursor = self.conn.cursor()
        query = "select sid, sname, region, phone, address from reservation natural inner join supplier where reservationid = %s;"
        cursor.execute(query, (reservationid,))
        result = cursor.fetchone()
        return result


    def getClientByReservationId(self, reservationid):
        cursor = self.conn.cursor()
        query = "select cid, cname, region, address from reservation natural inner join client where reservationid = %s;"
        cursor.execute(query, (reservationid,))
        result = cursor.fetchone()
        return result


    def insert(self, cid, sid, rid, qty):
        cursor = self.conn.cursor()
        query = "insert into reservation(cid, sid, rid, qty) values (%s, %s, %s, %s) returning reservationid;"
        cursor.execute(query, (cid, sid, rid, qty,))
        reservationid = cursor.fetchone()[0]
        self.conn.commit()
        return reservationid
