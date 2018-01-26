from flask import jsonify
from dao.FuelDAO import FuelDAO
from dao.ResourcesDAO import ResourcesDAO

class FuelHandler:

    def build_fuel_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['ftype'] = row[1]
        result['price'] = row[2]
        result['csize'] = row[3]
        result['brand'] = row[4]
        return result


    def build_fuel_attributes(self, rid, ftype, price, csize, brand):
        result = {}
        result['rid'] = rid
        result['ftype'] = ftype
        result['price'] = price
        result['csize'] = csize
        result['brand'] = brand
        return result

    def build_supplierfuel_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['requestid'] = row[1]
        result['cid'] = row[2]
        result['qty'] = row[3]
        result['ftype'] = row[4]
        result['price'] = row[5]
        result['containersize'] = row[6]
        result['brand'] = row[7]
        return result

    def build_requestfuel_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['requestid'] = row[1]
        result['cid'] = row[2]
        result['qty'] = row[3]
        result['price'] = row[4]
        result['ftype'] = row[5]
        result['expdate'] = row[6]
        result['name'] = row[7]
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


    def getFuelByBrand(self, brand):

        dao = FuelDAO()
        fuel_list = dao.getFuelByBrand(brand)
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
            brand = args.get("brand")

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
            elif (len(args) == 1) and brand:
                fuel_list = dao.getFuelByBrand(brand)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in fuel_list:
                result = self.build_fuel_dict(row)
                result_list.append(result)
            return jsonify(Fuel = result_list)


    def insertFuel(self, form):
        if len(form) != 6:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            sid = form['sid']
            qty = form['qty']
            ftype = form['ftype']
            price = form['price']
            csize = form['csize']
            brand = form['brand']
            if sid and qty and ftype and price and csize and brand:
                rid = ResourcesDAO().insert(sid, qty, price)
                dao = FuelDAO()
                dao.insert(rid, ftype, price, csize, brand)
                result = self.build_fuel_attributes(rid, ftype, price, csize, brand)
                return jsonify(Fuel = result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400


    def getFuelSuppliers(self):
        dao = FuelDAO()
        suppliers_list = dao.getFuelSuppliers()
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplierfuel_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)

    def getFuelSuppliersByRegion(self, region):
        dao = FuelDAO()
        suppliers_list = dao.getFuelSuppliersByRegion(region)
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplierfuel_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)

    def getAllFuelRequests(self):

        dao = FuelDAO()
        food_list = dao.getAllFuelRequests()
        result_list = []
        for row in food_list:
            result = self.build_requestfuel_dict(row)
            result_list.append(result)
        return jsonify(Fuel=result_list)

    def searchFuelRequests(self, args):
        if len(args) > 4:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            ftype = args.get("ftype")
            price = args.get("price")
            csize = args.get("csize")
            brand = args.get("brand")

            dao = FuelDAO()
            fuel_list = []
            if (len(args) == 1) and rid:
                fuel_list = dao.getFuelRequestsById(rid)
            elif (len(args) == 1) and ftype:
                fuel_list = dao.getFuelRequestsByType(ftype)
            elif (len(args) == 1) and price:
                fuel_list = dao.getFuelRequestsByPrice(price)
            elif (len(args) == 1) and csize:
                fuel_list = dao.getFuelRequestsByContainerSize(csize)
            elif (len(args) == 1) and brand:
                fuel_list = dao.getFuelRequestsByBrand(brand)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in fuel_list:
                result = self.build_requestfuel_dict(row)
                result_list.append(result)
            return jsonify(Fuel = result_list)

    def updateFuel(self, rid, form):
        dao = FuelDAO()
        if not dao.getFuelById(rid):
            return jsonify(Error = "Food not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                ftype = form['ftype']
                price = form['price']
                csize = form['csize']
                brand = form['brand']
                if price and ftype and csize and brand:
                    rdao = ResourcesDAO()
                    rdao.updatePrice(rid, price)
                    dao.update(rid,ftype, price, csize, brand)
                    result = self.build_fuel_attributes(rid, ftype, price, csize, brand)
                    return jsonify(Food=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400

