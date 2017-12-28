from flask import jsonify
from dao.IceDAO import IceDAO


class IceHandler:

    def build_ice_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['price'] = row[1]
        result['size'] = row[2]
        return result


    def build_ice_attributes(self, rid, price, size):
        result = {}
        result['rid'] = rid
        result['price'] = price
        result['size'] = size
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


    def searchIce(self, args):
        if len(args) > 3:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            size = args.get("size")

            dao = IceDAO()
            ice_list = []
            if (len(args) == 2) and price and size:
                ice_list = dao.getIceByPriceAndSize(price, size)
            elif (len(args) == 1) and rid:
                ice_list = dao.getIceById(rid)
            elif (len(args) == 1) and price:
                ice_list = dao.getIceByPrice(price)
            elif (len(args) == 1) and size:
                ice_list = dao.getIceBySize(size)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in ice_list:
                result = self.build_ice_dict(row)
                result_list.append(result)
            return jsonify(Ice = result_list)


    def insertIce(self, form):
        if len(form) != 2:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            price = form['price']
            size = form['size']
            if price and size:
                dao = IceDAO()
                rid = dao.insert(price, size)
                result = self.build_ice_attributes(price, size)
                return jsonify(Ice = result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

