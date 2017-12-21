from flask import jsonify

class ResourceHandler:
   
    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['category'] = row[2]
        result['rprice'] = row[3]
        result['available'] = row[4]
        result['requestcount'] = row[5]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['spassword'] = row[2]
        result['scity'] = row[3]
        result['sphone'] = row[4]
        result['slocation'] = row[5]
        return result


    def buildDummyData(self):
        resource_list = []
        resource1 = [1, 'gerber', 'baby food', '.99', 'true', '50']
        resource2 = [2, 'dasani', 'water', '1.50', 'false', '200']
        resource3 = [3, 'diesel', 'fuel', '.97', 'true', '9999']
        resource4 = [4, 'syringe', 'medical devices', '.65', 'true', '777']

        resource_list.append(resource1)
        resource_list.append(resource2)
        resource_list.append(resource3)
        resource_list.append(resource4)
        return resource_list  


    def getAllResources(self):
        resource_list = self.buildDummyData()

        result_list = []
        for row in resource_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)


    def getResourceIds(self):
        id_list = self.buildDummyData()
        
        if not id_list:
            return jsonify(Error = "No Resources Found"), 404
        else:
            result_list = []
            for row in id_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
        return jsonify(Ids = result_list)


    def getResourceNames(self):
        names_list = self.buildDummyData()
        
        if not names_list:
            return jsonify(Error = "No Resource Names Found"), 404
        else:
            result_list = []
            for row in names_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
        return jsonify(Ids = result_list)


    def getResourceCategories(self):
        categories_list = self.buildDummyData()
        
        if not categories_list:
            return jsonify(Error = "No Categories Found"), 404
        else:
            result_list = []
            for row in categories_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
        return jsonify(Categories = result_list)


    def getResourcePrices(self):
        price_list = self.buildDummyData()
        
        if not price_list:
            return jsonify(Error = "No Prices Found"), 404
        else:
            result_list = []
            for row in price_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
        return jsonify(Prices = result_list)


    def getAvailableResources(self):
        available_list = self.buildDummyData()
        
        if not available_list:
            return jsonify(Error = "No Available Resources Found"), 404
        else:
            result_list = []
            for row in available_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
        return jsonify(Available = result_list)


    def getRequestCount(self):
        request_list = self.buildDummyData()
        
        if not request_list:
            return jsonify(Error = "No Requests Found"), 404
        else:
            result_list = []
            for row in request_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
        return jsonify(Requests = result_list)


    def getResourceById(self, rid):
        row = [1, 'gerber', 'baby food', '.99', 'true', '50']

        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource = resource)

    def searchResources(self, args):
        rname = args.get("rname")
        category = args.get("category")
        requestcount = args.get("requestcount")
        resources_list = []

        if (len(args) == 2) and rname and category:
            resources_list = self.buildDummyData()
        elif (len(args) == 2) and category and requestcount:
            resources_list = self.buildDummyData()
        elif (len(args) == 1) and requestcount:
            resources_list = self.buildDummyData()
        elif (len(args) == 1) and rname:
            resources_list = self.buildDummyData()
        elif (len(args) == 1) and category:
            resources_list = self.buildDummyData()
        else:
            return jsonify(Error = "Malformed query string"), 400

        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)

    def getSuppliersByRID(self, rid):
        suppliers = []
        suppliers.append([0, "Juan Vasquez", "hola123", "San Juan", "7874561925", "18.465539,-66.105735"])
        suppliers.append([2, "Esteban Rivera", "quieneres", "Mayaguez", "7876943078", "18.201345,-67.145155"])
        if not suppliers:
            return jsonify(Error="Resources Not Found"), 404
        else:
            result_list = []
            for row in suppliers:
                result = self.build_supplier_dict(row)
                result_list.append(result)
            return jsonify(Suppliers=result_list)
