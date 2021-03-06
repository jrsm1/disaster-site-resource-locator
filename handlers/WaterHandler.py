from flask import jsonify
from dao.WaterDAO import WaterDAO
from dao.ResourcesDAO import ResourcesDAO


class WaterHandler:

    def build_water_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['price'] = row[1]
        result['bottlesize'] = row[2]
        result['brand'] = row[3]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['spassword'] = row[2]
        result['sregion'] = row[3]
        result['sphone'] = row[4]
        result['saddress'] = row[5]
        return result

    def build_supplierwater_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['sid'] = row[1]
        result['sname'] = row[2]
        result['saddress'] = row[3]
        result['sphone'] = row[4]
        result['sregion'] = row[5]
        return result

    def build_requestwater_dict(self, row):
        result = {}
        result['requestid'] = row[0]
        result['rid'] = row[1]
        result['cid'] = row[2]
        result['qty'] = row[3]
        result['price'] = row[4]
        result['bottlesize'] = row[5]
        result['brand'] = row[6]
        return result


    def build_water_attributes(self, rid, price, bsize, brand):
        result = {}
        result['rid'] = rid
        result['price'] = price
        result['bottlesize'] = bsize
        result['brand'] = brand
        return result


    def getAllWater(self):

        dao = WaterDAO()
        water_list = dao.getAllWater()
        result_list = []
        for row in water_list:
            result = self.build_water_dict(row)
            result_list.append(result)
        return jsonify(Water=result_list)


    def getWaterById(self, rid):

        dao = WaterDAO()
        row = dao.getWaterById(rid)
        if not row:
            return jsonify(Error="Water Not Found"), 404
        else:
            water = self.build_water_dict(row)
        return jsonify(Water = water)

    def getWaterByPrice(self, price):

        dao = WaterDAO()
        price_list = dao.getWaterByPrice(price)
        if not price_list:
            return jsonify(Error = "No price found"), 404
        else:
            result_list = []
            for row in price_list:
                result = self.build_water_dict(row)
                result_list.append(result)
        return jsonify(Water = result_list)


    def getWaterByBottleSize(self, bsize):

        dao = WaterDAO()
        size_list = dao.getWaterByBottleSize(bsize)
        if not size_list:
            return jsonify(Error = "No size found"), 404
        else:
            result_list = []
            for row in size_list:
                result = self.build_water_dict(row)
                result_list.append(result)
        return jsonify(Water = result_list)


    def getWaterByBrand(self, brand):

        dao = WaterDAO()
        size_list = dao.getWaterByBrand(brand)
        if not size_list:
            return jsonify(Error = "No brand found"), 404
        else:
            result_list = []
            for row in size_list:
                result = self.build_water_dict(row)
                result_list.append(result)
        return jsonify(Water = result_list)


    def searchWater(self, args):
        if len(args) > 4:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            bsize = args.get("bsize")
            brand = args.get("brand")

            dao = WaterDAO()
            water_list = []
            if (len(args) == 2) and price and bsize:
                water_list = dao.getWaterByPriceAndBottleSize(price, bsize)
            elif (len(args) == 1) and rid:
                water_list = dao.getWaterById(rid)
            elif (len(args) == 1) and price:
                water_list = dao.getWaterByPrice(price)
            elif (len(args) == 1) and bsize:
                water_list = dao.getWaterByBottleSize(bsize)
            elif (len(args) == 1) and brand:
                water_list = dao.getWaterByBrand(brand)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in water_list:
                result = self.build_water_dict(row)
                result_list.append(result)
            return jsonify(Water = result_list)


    def searchWaterRequests(self, args):
        if len(args) > 4:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            bsize = args.get("bsize")
            brand = args.get("brand")

            dao = WaterDAO()
            water_list = []
            if (len(args) == 2) and price and bsize:
                water_list = dao.getWaterRequestsByPriceAndBottleSize(price, bsize)
            elif (len(args) == 1) and rid:
                water_list = dao.getWaterRequestsById(rid)
            elif (len(args) == 1) and price:
                water_list = dao.getWaterRequestsByPrice(price)
            elif (len(args) == 1) and bsize:
                water_list = dao.getWaterRequestsByBottleSize(bsize)
            elif (len(args) == 1) and brand:
                water_list = dao.getWaterRequestsByBrand(brand)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in water_list:
                result = self.build_requestwater_dict(row)
                result_list.append(result)
            return jsonify(Water = result_list)


    def insertWater(self, form):
        if len(form) != 5:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            sid = form['sid']
            qty = form['qty']
            price = form['price']
            bsize = form['bsize']
            brand = form['brand']
            if sid and qty and price and bsize and brand:
                rid = ResourcesDAO().insert(sid, qty)
                dao = WaterDAO()
                dao.insert(rid, price, bsize, brand)
                result = self.build_water_attributes(rid, price, bsize, brand)
                return jsonify(Water = result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400


    def getWaterSuppliers(self):
        dao = WaterDAO()
        suppliers_list = dao.getWaterSuppliers()
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplierwater_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)


    def getWaterSuppliersByRegion(self, region):
        dao = WaterDAO()
        suppliers_list = dao.getWaterSuppliersByRegion(region)
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplierwater_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)


    def getWaterRequests(self):
        dao = WaterDAO()
        requests_list = dao.getWaterRequests()
        if not requests_list:
            return jsonify(Error = "No Requests found"), 404
        else:
            result_list = []
            for row in requests_list:
                result = self.build_requestwater_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)

