from flask import jsonify
from dao.ReservationDAO import ReservationDAO
from dao.ResourcesDAO import ResourcesDAO

class ReservationHandler:

    def build_reservation_dict(self, row):
        result = {}
        result['reservationid'] = row[0]
        result['cid'] = row[1]
        result['sid'] = row[2]
        result['rid'] = row[3]
        result['qty'] = row[4]
        return result


    def build_reservation_attributes(self, reservationid, cid, sid, rid, qty):
        result = {}
        result['reservationid'] = reservationid
        result['cid'] = cid
        result['sid'] = sid
        result['rid'] = rid
        result['qty'] = qty
        return result


    def getAllReservation(self):

        dao = ReservationDAO()
        reservation_list = dao.getAllReservation()
        result_list = []
        for row in reservation_list:
            result = self.build_reservation_dict(row)
            result_list.append(result)
        return jsonify(Reservation=result_list)


    def getReservationById(self, reservationid):

        dao = ReservationDAO()

        row = dao.getReservationById(reservationid)
        if not row:
            return jsonify(Error="Reservation Not Found"), 404
        else:
            reservation = self.build_reservation_dict(row)
        return jsonify(Reservation = reservation)


    def searchReservation(self, args):
        if len(args) > 5:
            return jsonify(Error = "Malformed search string."), 400
        else:
            reservationid = args.get("reservationid")
            cid = args.get("cid")
            sid = args.get("sid")
            rid = args.get("rid")
            qty = args.get("qty")

            dao = ReservationDAO()
            reservation_list = []
            if (len(args) == 2) and rid and qty:
                reservation_list = dao.getReservationByResourceIdAndQuantity(rid, qty)
            elif (len(args) == 1) and reservationid:
                reservation_list = dao.getReservationById(reservationid)
            elif (len(args) == 1) and cid:
                reservation_list = dao.getReservationByClientId(cid)
            elif (len(args) == 1) and sid:
                reservation_list = dao.getReservationBySupplierId(sid)
            elif (len(args) == 1) and rid:
                reservation_list = dao.getReservationByResourceId(rid) 
            elif (len(args) == 1) and qty:
                reservation_list = dao.getReservationByQuantity(qty) 
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in reservation_list:
                result = self.build_reservation_dict(row)
                result_list.append(result)
            return jsonify(Reservation=result_list)


    def insertReservation(self, form):
        if len(form) != 4:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            cid = form['cid']
            sid = form['sid']
            rid = form['rid']
            qty = form['qty']
            if cid and sid and rid and qty:
                dao = ReservationDAO()
                resourcedao = ResourcesDAO()
                currentQty = resourceDAO().getResourceQuantity(rid)
                resourcePrice = resourceDAO().getResourcePrice(rid)
                if(int(currentQty) - int(qty) < 0):
                    return jsonify(Error = "Invalid Reservation request"), 400
                elif(int(resourcePrice) != 0)
                    return jsonify(Error = "Invalid Reservation request"), 400
                else:
                    reservationid = dao.insert(cid, sid, rid, qty)
                    result = self.build_reservation_attributes(reservationid, cid, sid, rid, qty)
                    return jsonify(Reservation=result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

