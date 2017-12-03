from flask import jsonify


class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['scity'] = row[2]
        result['sphone'] = row[3]
        result['slocation'] = row[4]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['rname'] = row[1]
        result['category'] = row[2]
        result['rprice'] = row[3]
        result['available'] = row[4]
        result['requestcount'] = row[5]
        return result

    def getSupplierList(self):
        supplier1 = [0, "Juan Vasquez", "San Juan", "7874561925", "18.465539,-66.105735"]
        supplier2 = [1, "Pedro Sanchez", "Arecibo", "7873456890", "18.444247,-66.646407"]
        supplier3 = [2, "Esteban Rivera", "Mayaguez", "7876943078", "18.201345,-67.145155"]
        result = [supplier1, supplier2, supplier3]
        return result

    def getAllSuppliers(self):
        suppliers_list = self.getSupplierList()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def searchSuppliers(self, args):
            scity = args.get("city")
            sid = args.get("id")
            sname = args.get("name")
            sphone = args.get("phone")
            slocation = args.get("location")

            if scity or sname or sphone or slocation or sid:
                supplier_list = self.getSupplierList()
                result_list = []
                for row in supplier_list:
                    result = self.build_supplier_dict(row)
                    result_list.append(result)
                return jsonify(Suppliers=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def getSuppliersBy(self, selection):
        if selection == "scity" or selection == "sname" or selection == "sphone" or selection == "slocation" or \
                selection == "sid":
            supplier_list = self.getSupplierList()
            result_list = []
            for row in supplier_list:
                result = self.build_supplier_dict(row)
                result_list.append(result)
            return jsonify(Suppliers=result_list)
        else:
            return jsonify(Error="Malformed search string."), 400

    def getSupplierByID(self, sid):
        result = [0, "Juan Vasquez", "San Juan", "7874561925", "18.465539,-66.105735"]
        if not result:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            supplierID= self.build_supplier_dict(result)
        return jsonify(Supplier = supplierID)

    def getResourcesBySID(self, sid):
        result = [1, 'gerber', 'baby food', '.99', 'true', '50']
        if not result:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            resources = self.build_resource_dict(result)
        return jsonify(resources)
