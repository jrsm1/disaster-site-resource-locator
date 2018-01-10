from flask import jsonify
from dao.IceDAO import IceDAO
from dao.ResourcesDAO import ResourcesDAO


class IceHandler:

    def build_ice_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['price'] = row[1]
        result['bsize'] = row[2]
        return result


    def build_ice_attributes(self, rid, price, bsize):
        result = {}
        result['rid'] = rid
        result['price'] = price
        result['bsize'] = bsize
        return result

    def build_supplierice_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['sid'] = row[1]
        result['sname'] = row[2]
        result['saddress'] = row[3]
        result['sphone'] = row[4]
        result['sregion'] = row[5]
        return result

    def build_requestice_dict(self, row):
        result = {}
        result['requestid'] = row[0]
        result['cid'] = row[1]
        result['rid'] = row[2]
        result['qty'] = row[3]
        result['price'] = row[4]
        result['bagsize'] = row[5]
        return result


    def getAllIce(self):

        dao = IceDAO()
        ice_list = dao.getAllIce()
        result_list = []
        for row in ice_list:
            result = self.build_ice_dict(row)
            result_list.append(result)
        return jsonify(Ice=result_list)


    def getIceById(self, rid):

        dao = IceDAO()

        row = dao.getIceById(rid)
        if not row:
            return jsonify(Error="Ice Not Found"), 404
        else:
            ice = self.build_ice_dict(row)
        return jsonify(Ice = ice)


    def getIceByPrice(self, price):

        dao = IceDAO()
        price_list = dao.getIceByPrice(price)
        if not price_list:
            return jsonify(Error = "No price found"), 404
        else:
            result_list = []
            for row in price_list:
                result = self.build_ice_dict(row)
                result_list.append(result)
        return jsonify(Ice = result_list)


    def getIceByBagSize(self, bsize):

        dao = IceDAO()
        size_list = dao.getIceByBagSize(bsize)
        if not size_list:
            return jsonify(Error = "No size found"), 404
        else:
            result_list = []
            for row in size_list:
                result = self.build_ice_dict(row)
                result_list.append(result)
        return jsonify(Ice = result_list)


    def searchIce(self, args):
        if len(args) > 3:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            bsize = args.get("bsize")

            dao = IceDAO()
            ice_list = []
            if (len(args) == 2) and price and bsize:
                ice_list = dao.getIceByPriceAndBagSize(price, bsize)
            elif (len(args) == 1) and rid:
                ice_list = dao.getIceById(rid)
            elif (len(args) == 1) and price:
                ice_list = dao.getIceByPrice(price)
            elif (len(args) == 1) and bsize:
                ice_list = dao.getIceByBagSize(bsize)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in ice_list:
                result = self.build_ice_dict(row)
                result_list.append(result)
            return jsonify(Ice = result_list)


    def searchIceRequests(self, args):
        if len(args) > 3:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            bsize = args.get("bsize")

            dao = IceDAO()
            ice_list = []
            if (len(args) == 2) and price and bsize:
                ice_list = dao.getIceRequestsByPriceAndBagSize(price, bsize)
            elif (len(args) == 1) and rid:
                ice_list = dao.getIceRequestsById(rid)
            elif (len(args) == 1) and price:
                ice_list = dao.getIceRequestsByPrice(price)
            elif (len(args) == 1) and bsize:
                ice_list = dao.getIceRequestsByBagSize(bsize)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in ice_list:
                result = self.build_requestice_dict(row)
                result_list.append(result)
            return jsonify(Ice = result_list)


    def insertIce(self, form):
        if len(form) != 4:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            sid = form['sid']
            qty = form['qty']
            price = form['price']
            bsize = form['bsize']
            if sid and qty and price and bsize:
                rid = ResourcesDAO().insert(sid, qty)
                dao = IceDAO()
                dao.insert(rid, price, bsize)
                result = self.build_ice_attributes(rid, price, bsize)
                return jsonify(Ice = result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

    def getIceSuppliers(self):
        dao = IceDAO()
        suppliers_list = dao.getIceSuppliers()
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplierice_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)

    def getIceSuppliersByRegion(self, region):
        dao = IceDAO()
        suppliers_list = dao.getIceSuppliersByRegion(region)
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplierice_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)


    def getAllIceRequests(self):
        dao = IceDAO()
        requests_list = dao.getAllIceRequests()
        if not requests_list:
            return jsonify(Error = "No Requests found"), 404
        else:
            result_list = []
            for row in requests_list:
                result = self.build_requestice_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)


    def getIceRequestsById(self, rid):

        dao = IceDAO()

        row = dao.getIceRequestsById(rid)
        if not row:
            return jsonify(Error="Requests Not Found"), 404
        else:
            ice = self.build_requestice_dict(row)
        return jsonify(Ice = ice)


    def getIceRequestsByPrice(self, price):

        dao = IceDAO()
        price_list = dao.getIceRequestsByPrice(price)
        if not price_list:
            return jsonify(Error = "No Requests found"), 404
        else:
            result_list = []
            for row in price_list:
                result = self.build_requestice_dict(row)
                result_list.append(result)
        return jsonify(Ice = result_list)


    def getIceRequestsByBagSize(self, bsize):

        dao = IceDAO()
        size_list = dao.getIceRequestsByBagSize(bsize)
        if not size_list:
            return jsonify(Error = "No Requests found"), 404
        else:
            result_list = []
            for row in size_list:
                result = self.build_requestice_dict(row)
                result_list.append(result)
        return jsonify(Ice = result_list)

