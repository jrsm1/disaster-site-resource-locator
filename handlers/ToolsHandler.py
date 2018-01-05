from flask import jsonify
from dao.ToolsDAO import ToolsDAO


class ToolsHandler:

    def build_tools_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['name'] = row[1]
        result['brand'] = row[2]
        result['price'] = row[3]
        return result


    def build_tools_attributes(self, rid, name, brand, price):
        result = {}
        result['rid'] = rid
        result['name'] = name
        result['brand'] = brand
        result['price'] = price
        return result


    def getAllTools(self):

        dao = ToolsDAO()
        tools_list = dao.getAllTools()
        result_list = []
        for row in tools_list:
            result = self.build_tools_dict(row)
            result_list.append(result)
        return jsonify(Tools=result_list)


    def getToolsById(self, rid):

        dao = ToolsDAO()
        row = dao.getToolsById(rid)
        if not row:
            return jsonify(Error="Tools Not Found"), 404
        else:
            tools = self.build_tools_dict(row)
        return jsonify(Tools = tools)


    def getToolsByName(self, name):

        dao = ToolsDAO()
        tools_list = dao.getToolsByName(name)
        if not tools_list:
            return jsonify(Error = "No Tools found"), 404
        else:
            result_list = []
            for row in tools_list:
                result = self.build_tools_dict(row)
                result_list.append(result)
        return jsonify(Tools = result_list)


    def getToolsByBrand(self, brand):

        dao = ToolsDAO()
        tools_list = dao.getToolsByBrand(brand)
        if not tools_list:
            return jsonify(Error = "No Tools found"), 404
        else:
            result_list = []
            for row in tools_list:
                result = self.build_tools_dict(row)
                result_list.append(result)
        return jsonify(Tools = result_list)


    def getToolsByPrice(self, price):

        dao = ToolsDAO()
        tools_list = dao.getToolsByPrice(price)
        if not tools_list:
            return jsonify(Error = "No Tools found"), 404
        else:
            result_list = []
            for row in tools_list:
                result = self.build_tools_dict(row)
                result_list.append(result)
        return jsonify(Tools = result_list)


    def searchTools(self, args):
        if len(args) > 4:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            name = args.get("name")
            brand = args.get("brand")
            price = args.get("price")

            dao = ToolsDAO()
            tools_list = []
            if (len(args) == 2) and name and brand:
                tools_list = dao.getToolsByNameAndBrand(name, brand)
            elif (len(args) == 1) and rid:
                tools_list = dao.getToolsById(rid)
            elif (len(args) == 1) and name:
                tools_list = dao.getToolsByName(name)
            elif (len(args) == 1) and brand:
                tools_list = dao.getToolsByBrand(brand)
            elif (len(args) == 1) and price:
                tools_list = dao.getToolsByPrice(price)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in tools_list:
                result = self.build_tools_dict(row)
                result_list.append(result)
            return jsonify(Tools = result_list)


    def insertTools(self, form):
        if len(form) != 4:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            rid = form['rid']
            name = form['name']
            brand = form['brand']
            price = form['price']
            if rid and name and brand and price:
                dao = ToolsDAO()
                dao.insert(rid, name, brand, price)
                result = self.build_tools_attributes(rid, name, brand, price)
                return jsonify(Tools = result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

