from flask import jsonify
from dao.FirstAidDAO import FirstAidDAO


class FirstAidHandler:

    def build_aid_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['price'] = row[1]
        result['brand'] = row[2]
        result['medconditon'] = row[3]
        return result

    def build_aid_attributes(self, rid, price, brand, medcondition):
        result = {}
        result['rid'] = rid
        result['price'] = price
        result['brand'] = brand
        result['medconditon'] = medcondition
        return result


    def getAllAid(self):

        dao = FirstAidDAO()
        aid_list = dao.getAllAid()
        result_list = []
        for row in aid_list:
            result = self.build_aid_dict(row)
            result_list.append(result)
        return jsonify(FirstAid=result_list)


    def getAidById(self, rid):

        dao = FirstAidDAO()
        row = dao.getAidById(rid)
        if not row:
            return jsonify(Error="First Aid Not Found"), 404
        else:
            aid = self.build_aid_dict(row)
        return jsonify(FirstAID=aid)


    def getAidByPrice(self, price):

        dao = FirstAidDAO()
        price_list = dao.getAidByPrice(price)
        if not price_list:
            return jsonify(Error="No price found"), 404
        else:
            result_list = []
            for row in price_list:
                result = self.build_aid_dict(row)
                result_list.append(result)
        return jsonify(FirstAid=result_list)

    def getAidByBrand(self, brand):
        dao = FirstAidDAO()
        brand_list = dao.getAidByBrand(brand)
        if not brand_list:
            return jsonify(Error = "No First Aid found"), 404
        else:
            result_list = []
            for row in brand_list:
                result = self.build_aid_dict(row)
                result_list.append(result)
        return jsonify(FirstAid=result_list)

    def getAidByMedCondition(self, condition):
        dao = FirstAidDAO()
        condition_list = dao.getAidByMedCondition(condition)
        if not condition_list:
            return jsonify(Error="No FirstAid found"), 404
        else:
            result_list = []
            for row in condition_list:
                result = self.build_aid_dict(row)
                result_list.append(result)
        return jsonify(FirstAid=result_list)

    def searchAid(self, args):
        if len(args) > 4:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            brand = args.get("brand")
            medcondition = args.get("condition")

            dao = FirstAidDAO()
            aid_list = []
            if (len(args) == 3) and price and brand and medcondition:
                aid_list = dao.getAidByPriceBrandAndMedCondition(price, brand, medcondition)
            elif (len(args) == 2) and price and brand:
                aid_list = dao.getAidByPriceAndBrand(price, brand)
            elif (len(args) == 2) and medcondition and brand:
                aid_list = dao.getAidByMedConditionAndBrand(medcondition, brand)
            elif (len(args) == 2) and price and medcondition:
                aid_list = dao.getAidByPriceAndMedCondition(price, medcondition)
            elif (len(args) == 1) and rid:
                aid_list = dao.getAidById(rid)
            elif (len(args) == 1) and price:
                aid_list = dao.getAidByPrice(price)
            elif (len(args) == 1) and brand:
                aid_list = dao.getAidByBrand(brand)
            elif (len(args) == 1) and medcondition:
                aid_list = dao.getAidByMedCondition(medcondition)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in aid_list:
                result = self.build_aid_dict(row)
                result_list.append(result)
            return jsonify(FirstAid=result_list)

    def insertGenerator(self, form):
        if len(form) != 3:
            return jsonify(Error="Malformed POST request"), 400
        else:
            price = form['price']
            brand = form['brand']
            medcondition = form['condition']
            if price and brand and medcondition:
                dao = FirstAidDAO()
                rid = dao.insert(price, brand, medcondition)
                result = self.build_aid_attributes(rid, price, brand, medcondition)
                return jsonify(FirstAid=result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

