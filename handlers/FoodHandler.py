from flask import jsonify
from dao.FoodDAO import FoodDAO


class FoodHandler:

    def build_food_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['price'] = row[1]
        result['ftype'] = row[2]
        result['expdate'] = row[3]
        return result


    def build_food_attributes(self, rid, price, ftype, expdate):
        result = {}
        result['rid'] = rid
        result['price'] = price
        result['ftype'] = ftype
        result['expdate'] = expdate
        return result


    def getAllFood(self):

        dao = FoodDAO()
        food_list = dao.getAllFood()
        result_list = []
        for row in food_list:
            result = self.build_food_dict(row)
            result_list.append(result)
        return jsonify(Food=result_list)


    def getFoodById(self, rid):

        dao = FoodDAO()
        row = dao.getFoodById(rid)
        if not row:
            return jsonify(Error="Food Not Found"), 404
        else:
            food = self.build_food_dict(row)
        return jsonify(Food = food)


    def getFoodByPrice(self, price):

        dao = FoodDAO()
        food_list = dao.getFoodByPrice(price)
        if not food_list:
            return jsonify(Error = "No Food found"), 404
        else:
            result_list = []
            for row in food_list:
                result = self.build_food_dict(row)
                result_list.append(result)
        return jsonify(Food = result_list)


    def getFoodByType(self, ftype):

        dao = FoodDAO()
        food_list = dao.getFoodByType(ftype)
        if not food_list:
            return jsonify(Error = "No Food found"), 404
        else:
            result_list = []
            for row in food_list:
                result = self.build_food_dict(row)
                result_list.append(result)
        return jsonify(Food = result_list)


    def getFoodByExpDate(self, expdate):

        dao = FoodDAO()
        food_list = dao.getFoodByExpDate(expdate)
        if not food_list:
            return jsonify(Error = "No Food found"), 404
        else:
            result_list = []
            for row in food_list:
                result = self.build_food_dict(row)
                result_list.append(result)
        return jsonify(Food = result_list)



    def searchFood(self, args):
        if len(args) > 4:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            ftype = args.get("ftype")
            expdate = args.get("expdate")

            dao = FoodDAO()
            food_list = []
            if (len(args) == 1) and rid:
                food_list = dao.getFoodById(rid)
            elif (len(args) == 1) and price:
                food_list = dao.getFoodByPrice(price)
            elif (len(args) == 1) and ftype:
                food_list = dao.getFoodByType(ftype)
            elif (len(args) == 1) and expdate:
                food_list = dao.getFoodByExpDate(expdate)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in food_list:
                result = self.build_food_dict(row)
                result_list.append(result)
            return jsonify(Food = result_list)


    def insertFood(self, form):
        if len(form) != 4:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            rid = form['rid']
            price = form['price']
            ftype = form['ftype']
            expdate = form['expdate']
            if rid and price and ftype and expdate:
                dao = FoodDAO()
                dao.insert(rid, price, ftype, expdate)
                result = self.build_food_attributes(rid, price, ftype, expdate)
                return jsonify(Food = result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

