from flask import jsonify
from dao.ResourcesDAO import ResourcesDAO

class ResourceHandler:
   
    def build_resource_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['sid'] = row[1]
        result['qty'] = row[2]
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


    def build_resource_attributes(self, rid, sid, qty):
        result = {}
        result['rid'] = rid
        result['sid'] = sid
        result['qty'] = qty
        return result

    def getAllResources(self):
        dao = ResourcesDAO()
        resources_list = dao.getAllResources()

        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)


    def getResourcesById(self, rid):
        dao = ResourcesDAO()
        row = dao.getResourcesById(rid)

        if not row:
            return jsonify(Error = "Resource Not Found"), 404
        else:
            resource = self.build_resource_dict(row)
            return jsonify(Resource = resource)


    def getResourcesBySupplierId(self, sid):
        dao = ResourcesDAO()
        resource_list = dao.getResourcesBySupplierId(sid)

        if not resource_list:
            return jsonify(Error = "No Resource found"), 404
        else:
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
        return jsonify(Resources = result_list)


    def getResourcesByQuantity(self, qty):
        dao = ResourcesDAO()
        resource_list = dao.getResourcesByQuantity(qty)

        if not resource_list:
            return jsonify(Error = "No Resource found"), 404
        else:
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
        return jsonify(Resources = result_list)


    def getSuppliersByResourcesId(self, rid):
        dao = ResourcesDAO()
        resources_list = dao.getSupplierByResourcesId(rid)

        suppliers_list = []

        if not suppliers_list:
            return jsonify(Error="Suppliers Not Found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplier_dict(row)
                result_list.append(result)
            return jsonify(Suppliers=result_list)


    def searchResources(self, args):
        if len(args) > 2:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            sid = args.get("sid")
            qty = args.get("qty")

            dao = ResourcesDAO()
            resources_list = []

            if (len(args) == 1) and rid:
                resources_list = dao.getResourcesById(rid)
            elif (len(args) == 1) and sid:
                resources_list = dao.getResourcesBySupplierId(sid)
            elif (len(args) == 1) and qty:
                resources_list = dao.getResourcesByQuantity(qty)
            else:
                return jsonify(Error = "Malformed query string"), 400

        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources = result_list)


    def insertResources(self, form):
        if len(form) != 2:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            
            sid = form['sid']
            qty = form['qty']
            if sid and qty:
                dao = ResourcesDAO()
                rid = dao.insert(sid, qty)
                result = self.build_resources_attributes(rid, sid, qty)
                return jsonify(Resources=result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

