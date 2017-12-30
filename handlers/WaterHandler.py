from flask import jsonify
from dao.WaterDAO import WaterDAO


class WaterHandler:

    def build_water_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['price'] = row[1]
        result['size'] = row[2]
        return result


    def build_water_attributes(self, rid, price, size):
        result = {}
        result['rid'] = rid
        result['price'] = price
        result['size'] = size
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


    def getWaterBySize(self, size):

        dao = WaterDAO()
        size_list = dao.getWaterBySize(size)
        if not size_list:
            return jsonify(Error = "No size found"), 404
        else:
            result_list = []
            for row in size_list:
                result = self.build_water_dict(row)
                result_list.append(result)
        return jsonify(Water = result_list)


    def searchWater(self, args):
        if len(args) > 3:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            size = args.get("size")

            dao = WaterDAO()
            water_list = []
            if (len(args) == 2) and price and size:
                water_list = dao.getWaterByPriceAndSize(price, size)
            elif (len(args) == 1) and rid:
                water_list = dao.getWaterById(rid)
            elif (len(args) == 1) and price:
                water_list = dao.getWaterByPrice(price)
            elif (len(args) == 1) and size:
                water_list = dao.getWaterBySize(size)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in water_list:
                result = self.build_water_dict(row)
                result_list.append(result)
            return jsonify(Water = result_list)


    def insertWater(self, form):
        if len(form) != 3:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            rid = form['rid']
            price = form['price']
            size = form['size']
            if rid and price and size:
                dao = WaterDAO()
                dao.insert(rid, price, size)
                result = self.build_water_attributes(rid, price, size)
                return jsonify(Water = result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

