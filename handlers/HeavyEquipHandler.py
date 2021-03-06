from flask import jsonify
from dao.HeavyEquipDAO import HeavyEquipDAO
from dao.ResourcesDAO import ResourcesDAO

class HeavyEquipHandler:

    def build_equip_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['price'] = row[1]
        result['make'] = row[2]
        result['condition'] = row[3]
        result['function'] = row[4]
        return result

    def build_equip_attributes(self, rid, price, make, condition, equipfunction):
        result = {}
        result['rid'] = rid
        result['price'] = price
        result['make'] = make
        result['condition'] = condition
        result['equipfunction'] = equipfunction
        return result

    def build_supplierequip_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['sid'] = row[1]
        result['sname'] = row[2]
        result['saddress'] = row[3]
        result['sphone'] = row[4]
        result['sregion'] = row[5]
        return result


    def build_requestequip_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['requestid'] = row[1]
        result['cid'] = row[2]
        result['qty'] = row[3]
        result['make'] = row[4]
        result['condition'] = row[5]
        result['function'] = row[6]
        result['price'] = row[7]
        return result


    def getAllEquip(self):

        dao = HeavyEquipDAO()
        equip_list = dao.getAllEquip()
        result_list = []
        for row in equip_list:
            result = self.build_equip_dict(row)
            result_list.append(result)
        return jsonify(HeavyEquip=result_list)


    def getEquipById(self, rid):

        dao = HeavyEquipDAO()
        row = dao.getEquipById(rid)
        if not row:
            return jsonify(Error="Equipment Not Found"), 404
        else:
            equip = self.build_equip_dict(row)
        return jsonify(HeavyEquip=equip)


    def getEquipByPrice(self, price):

        dao = HeavyEquipDAO()
        price_list = dao.getEquipByPrice(price)
        if not price_list:
            return jsonify(Error = "No Equipment found"), 404
        else:
            result_list = []
            for row in price_list:
                result = self.build_equip_dict(row)
                result_list.append(result)
        return jsonify(HeavyEquip=result_list)

    def getEquipByMake(self, make):
        dao = HeavyEquipDAO()
        make_list = dao.getEquipByMake(make)
        if not make_list:
            return jsonify(Error = "No Make found"), 404
        else:
            result_list = []
            for row in make_list:
                result = self.build_equip_dict(row)
                result_list.append(result)
        return jsonify(HeavyEquip=result_list)

    def getEquipByCondition(self, condition):
        dao = HeavyEquipDAO()
        equip_list = dao.getEquipByCondition(condition)
        if not equip_list:
            return jsonify(Error="No equipment found"), 404
        else:
            result_list = []
            for row in equip_list:
                result = self.build_equip_dict(row)
                result_list.append(result)
        return jsonify(HeavyEquip=result_list)

    def getEquipByFunction(self, equipfunction):
        dao = HeavyEquipDAO()
        equip_list = dao.getEquipByFunction(equipfunction)
        if not equip_list:
            return jsonify(Error="No equipment found"), 404
        else:
            result_list = []
            for row in equip_list:
                result = self.build_equip_dict(row)
                result_list.append(result)
        return jsonify(HeavyEquip=result_list)

    def searchEquip(self, args):
        if len(args) > 5:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            make = args.get("make")
            condition = args.get("condition")
            equipfunction = args.get("function")

            dao = HeavyEquipDAO()
            equip_list = []
            if (len(args) == 4) and price and make and condition and equipfunction:
                equip_list = dao.getEquipByPriceMakeConditionAndFunction(price, make, condition, equipfunction)
            elif (len(args) == 3) and price and make and condition:
                equip_list = dao.getEquipByPriceMakeAndCondition(price, make, condition)
            elif (len(args) == 3) and price and make and equipfunction:
                equip_list = dao.getEquipByPriceMakeAndFunction(price, make, equipfunction)
            elif (len(args) == 3) and price and equipfunction and condition:
                equip_list = dao.getEquipByPriceFunctionAndCondition(price, equipfunction, condition)
            elif (len(args) == 3) and equipfunction and make and condition:
                equip_list = dao.getEquipByFunctionMakeAndCondition(equipfunction, make, condition)
            elif (len(args) == 2) and price and make:
                equip_list = dao.getEquipByPriceAndMake(price, make)
            elif (len(args) == 2) and condition and make:
                equip_list = dao.getEquipByConditionAndMake(condition, make)
            elif (len(args) == 2) and price and condition:
                equip_list = dao.getEquipByPriceAndCondition(price, condition)
            elif (len(args) == 2) and price and equipfunction:
                equip_list = dao.getEquipByPriceAndFunction(price, equipfunction)
            elif (len(args) == 2) and equipfunction and condition:
                equip_list = dao.getEquipByFunctionAndCondition(equipfunction, condition)
            elif (len(args) == 2) and make and equipfunction:
                equip_list = dao.getEquipByMakeAndFunction(make, equipfunction)
            elif (len(args) == 1) and rid:
                equip_list = dao.getEquipById(rid)
            elif (len(args) == 1) and price:
                equip_list = dao.getEquipByPrice(price)
            elif (len(args) == 1) and make:
                equip_list = dao.getEquipByMake(make)
            elif (len(args) == 1) and condition:
                equip_list = dao.getEquipByCondition(condition)
            elif (len(args) == 1) and equipfunction:
                equip_list = dao.getEquipByFunction(equipfunction)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in equip_list:
                result = self.build_equip_dict(row)
                result_list.append(result)
            return jsonify(HeavyEquip=result_list)


    def searchEquipRequests(self, args):
        if len(args) > 5:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            make = args.get("make")
            condition = args.get("condition")
            equipfunction = args.get("function")

            dao = HeavyEquipDAO()
            equip_list = []
            if (len(args) == 4) and price and make and condition and equipfunction:
                equip_list = dao.getEquipRequestsByPriceMakeConditionAndFunction(price, make, condition, equipfunction)
            elif (len(args) == 3) and price and make and condition:
                equip_list = dao.getEquipRequestsByPriceMakeAndCondition(price, make, condition)
            elif (len(args) == 3) and price and make and equipfunction:
                equip_list = dao.getEquipRequestsByPriceMakeAndFunction(price, make, equipfunction)
            elif (len(args) == 3) and price and equipfunction and condition:
                equip_list = dao.getEquipRequestsByPriceFunctionAndCondition(price, equipfunction, condition)
            elif (len(args) == 3) and equipfunction and make and condition:
                equip_list = dao.getEquipRequestsByFunctionMakeAndCondition(equipfunction, make, condition)
            elif (len(args) == 2) and price and make:
                equip_list = dao.getEquipRequestsByPriceAndMake(price, make)
            elif (len(args) == 2) and condition and make:
                equip_list = dao.getEquipRequestsByConditionAndMake(condition, make)
            elif (len(args) == 2) and price and condition:
                equip_list = dao.getEquipRequestsByPriceAndCondition(price, condition)
            elif (len(args) == 2) and price and equipfunction:
                equip_list = dao.getEquipRequestsByPriceAndFunction(price, equipfunction)
            elif (len(args) == 2) and equipfunction and condition:
                equip_list = dao.getEquipRequestsByFunctionAndCondition(equipfunction, condition)
            elif (len(args) == 2) and make and equipfunction:
                equip_list = dao.getEquipRequestsByMakeAndFunction(make, equipfunction)
            elif (len(args) == 1) and rid:
                equip_list = dao.getEquipRequestsById(rid)
            elif (len(args) == 1) and price:
                equip_list = dao.getEquipRequestsByPrice(price)
            elif (len(args) == 1) and make:
                equip_list = dao.getEquipRequestsByMake(make)
            elif (len(args) == 1) and condition:
                equip_list = dao.getEquipRequestsByCondition(condition)
            elif (len(args) == 1) and equipfunction:
                equip_list = dao.getEquipRequestsByFunction(equipfunction)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in equip_list:
                result = self.build_requestequip_dict(row)
                result_list.append(result)
            return jsonify(HeavyEquip=result_list)

    def insertEquip(self, form):
        if len(form) != 6:
            return jsonify(Error="Malformed POST request"), 400
        else:
            sid = form["sid"]
            quantity = form["quantity"]
            price = form['price']
            make = form['make']
            condition = form['condition']
            equipfunction = form["function"]
            if sid and quantity and price and make and condition and equipfunction:
                dao = HeavyEquipDAO()
                rid = ResourcesDAO().insert(sid, quantity)
                rid = dao.insert(rid, price, make, condition, equipfunction)
                result = self.build_equip_attributes(rid, price, make, condition, equipfunction)
                return jsonify(HeavyEquip=result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400


    def getEquipSuppliers(self):
        dao = HeavyEquipDAO()
        suppliers_list = dao.getEquipSuppliers()
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplierequip_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)


    def getEquipSuppliersByRegion(self, region):
        dao = HeavyEquipDAO()
        suppliers_list = dao.getEquipSuppliersByRegion(region)
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplierequip_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)


    def getAllEquipRequests(self):

        dao = HeavyEquipDAO()
        equip_list = dao.getAllEquipRequests()
        result_list = []
        for row in equip_list:
            result = self.build_requestequip_dict(row)
            result_list.append(result)
        return jsonify(Equip=result_list)

