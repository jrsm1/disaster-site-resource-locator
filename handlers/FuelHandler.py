from flask import jsonify
from dao.FuelDAO import FuelDAO
from ResourcesDAO import ResourcesDAO

class FuelHandler:

    def build_fuel_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['ftype'] = row[1]
        result['price'] = row[2]
        result['csize'] = row[3]
        return result


    def build_fuel_attributes(self, rid, ftype, price, csize):
        result = {}
        result['rid'] = rid
        result['ftype'] = ftype
        result['price'] = price
        result['csize'] = csize
        return result


    def getAllFuel(self):

        dao = FuelDAO()
        fuel_list = dao.getAllFuel()
        result_list = []
        for row in fuel_list:
            result = self.build_fuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)


    def getFuelById(self, rid):

        dao = FuelDAO()
        row = dao.getFuelById(rid)
        if not row:
            return jsonify(Error="Fuel Not Found"), 404
        else:
            fuel = self.build_fuel_dict(row)
        return jsonify(Fuel = fuel)


    def getFuelByType(self, ftype):

        dao = FuelDAO()
        fuel_list = dao.getFuelByType(ftype)
        if not fuel_list:
            return jsonify(Error = "No Fuel found"), 404
        else:
            result_list = []
            for row in fuel_list:
                result = self.build_fuel_dict(row)
                result_list.append(result)
        return jsonify(Fuel = result_list)


    def getFuelByPrice(self, price):

        dao = FuelDAO()
        fuel_list = dao.getFuelByPrice(price)
        if not fuel_list:
            return jsonify(Error = "No Fuel found"), 404
        else:
            result_list = []
            for row in fuel_list:
                result = self.build_fuel_dict(row)
                result_list.append(result)
        return jsonify(Fuel = result_list)


    def getFuelByContainerSize(self, csize):

        dao = FuelDAO()
        fuel_list = dao.getFuelByContainerSize(csize)
        if not fuel_list:
            return jsonify(Error = "No Fuel found"), 404
        else:
            result_list = []
            for row in fuel_list:
                result = self.build_fuel_dict(row)
                result_list.append(result)
        return jsonify(Fuel = result_list)


    def searchFuel(self, args):
        if len(args) > 4:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            ftype = args.get("ftype")
            price = args.get("price")
            csize = args.get("csize")

            dao = FuelDAO()
            fuel_list = []
            if (len(args) == 1) and rid:
                fuel_list = dao.getFuelById(rid)
            elif (len(args) == 1) and ftype:
                fuel_list = dao.getFuelByType(ftype)
            elif (len(args) == 1) and price:
                fuel_list = dao.getFuelByPrice(price)
            elif (len(args) == 1) and csize:
                fuel_list = dao.getFuelByContainerSize(csize)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in fuel_list:
                result = self.build_fuel_dict(row)
                result_list.append(result)
            return jsonify(Fuel = result_list)


    def insertFuel(self, form):
        if len(form) != 5:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            sid = form['sid']
            qty = form['qty']
            ftype = form['ftype']
            price = form['price']
            csize = form['csize']
            if sid and qty and ftype and price and csize:
                rid = ResourcesDAO().insert(sid, qty)
                dao = FuelDAO()
                dao.insert(rid, ftype, price, csize)
                result = self.build_fuel_attributes(rid, ftype, price, csize)
                return jsonify(Fuel = result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

