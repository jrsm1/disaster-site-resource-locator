from flask import jsonify
from dao.BatteryDAO import BatteryDAO
from dao.ResourcesDAO import ResourcesDAO

class BatteryHandler:

    def build_battery_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['price'] = row[1]
        result['voltage'] = row[2]
        result['type'] = row[3]
        return result


    def build_battery_attributes(self, rid, price, voltage, type):
        result = {}
        result['rid'] = rid
        result['price'] = price
        result['voltage'] = voltage
        result['type'] = type
        return result

    def build_supplierbattery_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['sid'] = row[1]
        result['sname'] = row[2]
        result['saddress'] = row[3]
        result['sphone'] = row[4]
        result['sregion'] = row[5]
        return result

    def build_requestbattery_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['requestid'] = row[1]
        result['cid'] = row[2]
        result['qty'] = row[3]
        result['price'] = row[4]
        result['voltage'] = row[5]
        result['btype'] = row[6]
        return result


    def getAllBattery(self):

        dao = BatteryDAO()
        battery_list = dao.getAllBattery()
        result_list = []
        for row in battery_list:
            result = self.build_battery_dict(row)
            result_list.append(result)
        return jsonify(Battery=result_list)


    def getBatteryById(self, rid):

        dao = BatteryDAO()
        row = dao.getBatteryById(rid)
        if not row:
            return jsonify(Error="Battery Not Found"), 404
        else:
            battery = self.build_battery_dict(row)
        return jsonify(Battery = battery)


    def getBatteryByPrice(self, price):

        dao = BatteryDAO()
        price_list = dao.getBatteryByPrice(price)
        if not price_list:
            return jsonify(Error = "No price found"), 404
        else:
            result_list = []
            for row in price_list:
                result = self.build_battery_dict(row)
                result_list.append(result)
        return jsonify(Battery=result_list)


    def getBatteryByLessThanPrice(self, price):

        dao = BatteryDAO()
        price_list = dao.getBatteryByLessThanPrice(price)
        if not price_list:
            return jsonify(Error = "No price found"), 404
        else:
            result_list = []
            for row in price_list:
                result = self.build_battery_dict(row)
                result_list.append(result)
        return jsonify(Battery=result_list)


    def getBatteryByGreaterThanPrice(self, price):

        dao = BatteryDAO()
        price_list = dao.getBatteryByGreaterThanPrice(price)
        if not price_list:
            return jsonify(Error = "No price found"), 404
        else:
            result_list = []
            for row in price_list:
                result = self.build_battery_dict(row)
                result_list.append(result)
        return jsonify(Battery=result_list)


    def getBatteryByVoltage(self, voltage):
        dao = BatteryDAO()
        voltage_list = dao.getBatteryByVoltage(voltage)
        if not voltage_list:
            return jsonify(Error = "No voltage found"), 404
        else:
            result_list = []
            for row in voltage_list:
                result = self.build_battery_dict(row)
                result_list.append(result)
        return jsonify(Battery=result_list)

    def getBatteryByType(self, type):
        dao = BatteryDAO()
        type_list = dao.getBatteryByType(type)
        if not type_list:
            return jsonify(Error="No type found"), 404
        else:
            result_list = []
            for row in type_list:
                result = self.build_battery_dict(row)
                result_list.append(result)
        return jsonify(Battery=result_list)

    def searchBattery(self, args):
        if len(args) > 4:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            voltage = args.get("voltage")
            btype = args.get("type")

            dao = BatteryDAO()
            battery_list = []
            if (len(args) == 3) and price and voltage and btype:
                battery_list = dao.getBatteryByPriceVoltageAndType(price, voltage, btype)
            elif (len(args) == 2) and price and voltage:
                battery_list = dao.getBatteryByPriceAndVoltage(price, voltage)
            elif (len(args) == 2) and btype and voltage:
                battery_list = dao.getBatteryByTypeAndVoltage(btype, voltage)
            elif (len(args) == 2) and price and btype:
                battery_list = dao.getBatteryByPriceAndType(price, btype)
            elif (len(args) == 1) and rid:
                battery_list = dao.getBatteryById(rid)
            elif (len(args) == 1) and price:
                battery_list = dao.getBatteryByPrice(price)
            elif (len(args) == 1) and voltage:
                battery_list = dao.getBatteryByVoltage(voltage)
            elif (len(args) == 1) and btype:
                battery_list = dao.getBatteryByType(btype)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in battery_list:
                result = self.build_battery_dict(row)
                result_list.append(result)
            return jsonify(Battery=result_list)


    def searchBatteryRequests(self, args):
        if len(args) > 4:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            voltage = args.get("voltage")
            btype = args.get("type")

            dao = BatteryDAO()
            battery_list = []
            if (len(args) == 3) and price and voltage and btype:
                battery_list = dao.getBatteryRequestsByPriceVoltageAndType(price, voltage, btype)
            elif (len(args) == 2) and price and voltage:
                battery_list = dao.getBatteryRequestsByPriceAndVoltage(price, voltage)
            elif (len(args) == 2) and btype and voltage:
                battery_list = dao.getBatteryRequestsByTypeAndVoltage(btype, voltage)
            elif (len(args) == 2) and price and btype:
                battery_list = dao.getBatteryRequestsByPriceAndType(price, btype)
            elif (len(args) == 1) and rid:
                battery_list = dao.getBatteryRequestsById(rid)
            elif (len(args) == 1) and price:
                battery_list = dao.getBatteryRequestsByPrice(price)
            elif (len(args) == 1) and voltage:
                battery_list = dao.getBatteryRequestsByVoltage(voltage)
            elif (len(args) == 1) and btype:
                battery_list = dao.getBatteryRequestsByType(btype)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in battery_list:
                result = self.build_requestbattery_dict(row)
                result_list.append(result)
            return jsonify(Battery=result_list)


    def insertBattery(self, form):
        if len(form) != 5:
            return jsonify(Error="Malformed POST request"), 400
        else:
            sid = form["sid"]
            quantity = form["quantity"]
            price = form['price']
            voltage = form['voltage']
            btype = form['type']
            if sid and quantity and price and voltage and btype:
                dao = BatteryDAO()
                rid = ResourcesDAO().insert(sid, quantity, price)
                rid = dao.insert(rid, price, voltage, btype)
                result = self.build_battery_attributes(rid, price, voltage, btype)
                return jsonify(Battery = result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400


    def updateBattery(self, rid, form):
        dao = BatteryDAO()
        if not dao.getBatteryById(rid):
            return jsonify(Error = "Battery not found."), 404
        else:
            if len(form) != 3:
                return jsonify(Error="Malformed update request"), 400
            else:
                price = form['price']
                voltage = form['voltage']
                btype = form['btype']

                if price and voltage and btype:
                    rdao = ResourcesDAO()
                    rdao.updatePrice(rid, price)
                    dao.update(rid, price, voltage, btype)
                    result = self.build_battery_attributes(rid, price, voltage, btype)
                    return jsonify(Battery=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400


    def getBatterySuppliers(self):
        dao = BatteryDAO()
        suppliers_list = dao.getBatterySuppliers()
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplierbattery_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)

    def getBatterySuppliersByRegion(self, region):
        dao = BatteryDAO()
        suppliers_list = dao.getBatterySuppliersByRegion(region)
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplierbattery_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)


    def getAllBatteryRequests(self):

        dao = BatteryDAO()
        battery_list = dao.getAllBatteryRequests()
        result_list = []
        for row in battery_list:
            result = self.build_requestbattery_dict(row)
            result_list.append(result)
        return jsonify(Battery=result_list)

