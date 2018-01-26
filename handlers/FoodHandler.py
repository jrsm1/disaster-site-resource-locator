from flask import jsonify
from dao.FoodDAO import FoodDAO
from dao.ResourcesDAO import ResourcesDAO


class FoodHandler:

    def build_food_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['price'] = row[1]
        result['ftype'] = row[2]
        result['expdate'] = row[3]
        result['fname'] = row[4]
        return result


    def build_food_attributes(self, rid, price, ftype, expdate, fname):
        result = {}
        result['rid'] = rid
        result['price'] = price
        result['ftype'] = ftype
        result['expdate'] = expdate
        result['fname'] = fname
        return result


    def build_supplierfood_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['sid'] = row[1]
        result['sname'] = row[2]
        result['saddress'] = row[3]
        result['sphone'] = row[4]
        result['sregion'] = row[5]
        return result

    def build_requestfood_dict(self, row):
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


    def getFoodByName(self, fname):

        dao = FoodDAO()
        food_list = dao.getFoodByName(fname)
        if not food_list:
            return jsonify(Error = "No Food found"), 404
        else:
            result_list = []
            for row in food_list:
                result = self.build_food_dict(row)
                result_list.append(result)
        return jsonify(Food = result_list)


    def searchFood(self, args):
        if len(args) > 5:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            ftype = args.get("ftype")
            expdate = args.get("expdate")
            fname = args.get("fname")

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
            elif (len(args) == 1) and fname:
                food_list = dao.getFoodByName(fname)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in food_list:
                result = self.build_food_dict(row)
                result_list.append(result)
            return jsonify(Food = result_list)


    def searchFoodRequests(self, args):
        if len(args) > 5:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            ftype = args.get("ftype")
            expdate = args.get("expdate")
            fname = args.get("fname")

            dao = FoodDAO()
            food_list = []
            if (len(args) == 1) and rid:
                food_list = dao.getFoodRequestsById(rid)
            elif (len(args) == 1) and price:
                food_list = dao.getFoodRequestsByPrice(price)
            elif (len(args) == 1) and ftype:
                food_list = dao.getFoodRequestsByType(ftype)
            elif (len(args) == 1) and expdate:
                food_list = dao.getFoodRequestsByExpDate(expdate)
            elif (len(args) == 1) and fname:
                food_list = dao.getFoodRequestsByName(fname)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in food_list:
                result = self.build_requestfood_dict(row)
                result_list.append(result)
            return jsonify(Food = result_list)


    def insertFood(self, form):
        if len(form) != 6:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            sid = form['sid']
            qty = form['qty']
            price = form['price']
            ftype = form['ftype']
            expdate = form['expdate']
            fname = form['fname']
            if sid and qty and price and ftype and expdate and fname:
                rid = ResourcesDAO().insert(sid,qty, price)
                dao = FoodDAO()
                dao.insert(rid, price, ftype, expdate, fname)
                result = self.build_food_attributes(rid, price, ftype, expdate, fname)
                return jsonify(Food = result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

    def getFoodSuppliers(self):
        dao = FoodDAO()
        suppliers_list = dao.getFoodSuppliers()
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplierfood_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)

    def getFoodSuppliersByRegion(self, region):
        dao = FoodDAO()
        suppliers_list = dao.getFoodSuppliersByRegion(region)
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplierfood_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)


    def getAllFoodRequests(self):

        dao = FoodDAO()
        food_list = dao.getAllFoodRequests()
        result_list = []
        for row in food_list:
            result = self.build_requestfood_dict(row)
            result_list.append(result)
        return jsonify(Food=result_list)


    def getFoodRequestsById(self, rid):

        dao = FoodDAO()
        row = dao.getFoodRequestsById(rid)
        if not row:
            return jsonify(Error="Food Not Found"), 404
        else:
            food = self.build_requestfood_dict(row)
        return jsonify(Food = food)


    def getFoodRequestsByPrice(self, price):

        dao = FoodDAO()
        food_list = dao.getFoodRequestsByPrice(price)
        if not food_list:
            return jsonify(Error = "No Food found"), 404
        else:
            result_list = []
            for row in food_list:
                result = self.build_requestfood_dict(row)
                result_list.append(result)
        return jsonify(Food = result_list)


    def getFoodRequestsByType(self, ftype):

        dao = FoodDAO()
        food_list = dao.getFoodRequestsByType(ftype)
        if not food_list:
            return jsonify(Error = "No Food found"), 404
        else:
            result_list = []
            for row in food_list:
                result = self.build_requestfood_dict(row)
                result_list.append(result)
        return jsonify(Food = result_list)


    def getFoodRequestsByExpDate(self, expdate):

        dao = FoodDAO()
        food_list = dao.getFoodRequestsByExpDate(expdate)
        if not food_list:
            return jsonify(Error = "No Food found"), 404
        else:
            result_list = []
            for row in food_list:
                result = self.build_requestfood_dict(row)
                result_list.append(result)
        return jsonify(Food = result_list)


    def getFoodRequestsByName(self, fname):

        dao = FoodDAO()
        food_list = dao.getFoodRequestsByName(fname)
        if not food_list:
            return jsonify(Error = "No Food found"), 404
        else:
            result_list = []
            for row in food_list:
                result = self.build_requestfood_dict(row)
                result_list.append(result)
        return jsonify(Food = result_list)

    def updateFood(self, rid, form):
        dao = FoodDAO()
        if not dao.getFoodById(rid):
            return jsonify(Error = "Food not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                price = form['price']
                ftype = form['ftype']
                expdate = form['expdate']
                fname = form['fname']

                if price and ftype and expdate and fname:
                    dao.update(rid, price, ftype, expdate, fname)
                    result = self.build_food_attributes(rid, price, ftype, expdate, fname)
                    return jsonify(Food=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400


