from flask import jsonify
from dao.SupplierDAO import SupplierDAO
from dao.SalesRecordDAO import SalesRecordDAO

class SupplierHandler:
    def build_supplier_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['sname'] = row[1]
        result['spassword'] = row[2]
        result['sregion'] = row[3]
        result['sphone'] = row[4]
        result['saddress'] = row[5]
        return result

    def build_supplier_attributes(self, sid, sname, spassword, saddress, sphone, sregion):
        result = {}
        result['sid'] = sid
        result['name'] = sname
        result['password']=spassword
        result['address'] = saddress
        result['phone'] = sphone
        result['region'] = sregion
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
        supplier1 = [0, "Juan Vasquez", "hola123", "San Juan", "7874561925", "Calle 18 P30 Vista Azul Arecibo PR"]
        supplier2 = [1, "Pedro Sanchez", "12345678", "Arecibo", "7873456890", "Calle 18 P30 Vista Azul Arecibo PR"]
        supplier3 = [2, "Esteban Rivera", "quieneres", "Mayaguez", "7876943078","Calle 18 P30 Vista Azul Arecibo PR"]
        result = [supplier1, supplier2, supplier3]
        return result

    def getAllSuppliers(self):
        dao = SupplierDAO()
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def searchSuppliers(self, args):
            if len(args) > 4:
                return jsonify(Error="Malformed search string."), 400
            saddress = args.get("address")
            sid = args.get("id")
            sname = args.get("name")
            sphone = args.get("phone")
            sregion = args.get("region")
            dao = SupplierDAO()
            supplier_list = []
            if len(args) == 2 and sname and sregion:
                supplier_list = dao.getSupplierByNameRegion(sname, sregion)
            elif len(args) == 1 and sid:
                supplier_list= dao.getSupplierByID(sid)
            elif len(args) == 1 and sname:
                supplier_list = dao.getSupplierByName(sname)
            elif len(args) == 1 and saddress:
                supplier_list = dao.getSupplierByAddress(saddress)
            elif len(args) == 1 and sphone:
                supplier_list = dao.getSupplierByPhone(sphone)
            elif len(args) == 1 and sregion:
                supplier_list = dao.getSupplierByRegion(sregion)
            else:
                return jsonify(Error="Malformed query string"), 400
            result_list = []
            for row in supplier_list:
                result = self.build_supplier_dict(row)
                result_list.append(result)
            return jsonify(Suppliers=result_list)

    def getSuppliersBy(self, selection):
        if selection == "sregion" or selection == "sname" or selection == "sphone" or selection == "saddress" or \
                selection == "sid":
            dao = SupplierDAO()
            supplier_list = dao.getSupplierBy(selection)
            result_list = []
            for row in supplier_list:
                result_list.append(row)
            return jsonify(Suppliers=result_list)
        else:
            return jsonify(Error="Malformed search string."), 400

    def getSupplierByID(self, sid):
        dao = SupplierDAO()
        row = dao.getSupplierByID(sid)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            supplierID = self.build_supplier_dict(row)
        return jsonify(Supplier = supplierID)
    #TODO
    def getResourcesBySID(self, sid):
        resources = []
        dao = SupplierDAO()
        dao.getResourcesBySID(sid)
        if not resources:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            result_list = []
            for row in resources:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

    def insertSupplier(self, form):
        if len(form) != 5:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            sname = form['name']
            spassword = form['password']
            saddress = form['address']
            sphone = form['phone']
            sregion = form['region']
            if sname and saddress and sphone and sregion and spassword:
                dao = SupplierDAO()
                sid = dao.Insert(sname, spassword, saddress, sphone, sregion)
                SalesRecordDAO().insert(sid, 0, 0)
                result = self.build_supplier_attributes(sid, sname, spassword, saddress, sphone, sregion)
                return jsonify(Supplier = result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

