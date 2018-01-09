from flask import jsonify
from dao.ClientDAO import ClientDAO

class ClientHandler:
    def build_client_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['cname'] = row[1]
        result['cpassword'] = row[2]
        result['region'] = row[3]
        result['address'] = row[4]
        return result

    def build_client_attributes(self, cid, cname, cpassword, address, region):
        result = {}
        result['cid'] = cid
        result['cname'] = cname
        result['cpassword'] = cpassword
        result['address'] = address
        result['region'] = region
        return result

    def build_card_dict(self, row):
        result = {}
        result['ccnum'] = row[0]
        result['ccholder'] = row[1]
        result['expdate'] = row[2]
        return result

    def getAllClients(self):
        dao = ClientDAO()
        client_list = dao.getAllClients()
        result_list = []
        for row in client_list:
            result = self.build_client_dict(row)
            result_list.append(result)
        return jsonify(Clients=result_list)

    def searchClients(self, args):
            if len(args) > 4:
                return jsonify(Error="Malformed search string."), 400
            cregion = args.get("region")
            cid = args.get("id")
            cname = args.get("name")
            caddress = args.get("address")
            dao = ClientDAO()
            client_list = []
            if len(args) == 2 and cname and cregion:
                client_list = dao.getClientByNameRegion(cname, cregion)
            elif len(args) == 1 and cid:
                client_list= dao.getClientByID(cid)
            elif len(args) == 1 and cname:
                client_list = dao.getClientByName(cname)
            elif len(args) == 1 and caddress:
                client_list = dao.getClientByAddress(caddress)
            elif len(args) == 1 and cregion:
                client_list = dao.getClientByRegion(cregion)
            else:
                return jsonify(Error="Malformed query string"), 400
            result_list = []
            for row in client_list:
                result = self.build_client_dict(row)
                result_list.append(result)
            return jsonify(Clients=result_list)

    def getClientsBy(self, selection):
        if selection == "cname" or selection == "address" or selection == "cid" or selection == "region":
            dao = ClientDAO()
            client_list = dao.getClientBy(selection)
            return jsonify(Clients=client_list)
        else:
            return jsonify(Error="Malformed search string."), 400

    def getClientByID(self, cid):
        dao = ClientDAO()
        row = dao.getClientByID(cid)
        if not row:
            return jsonify(Error="Client Not Found"), 404
        else:
            clientID = self.build_client_dict(row)
        return jsonify(Supplier=clientID)

    def getCCByCID(self, cid):
        dao = ClientDAO()
        client_list = dao.getCCByCID(cid)
        result_list = []
        for row in client_list:
            result = self.build_client_dict(row)
            result_list.append(result)
        return jsonify(CreditCards=result_list)

    def insertClient(self, form):
        if len(form) != 4:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            cname = form['cname']
            cpassword = form['cpassword']
            address = form['caddress']
            region = form['region']
            if cname and address and region and cpassword:
                dao = ClientDAO()
                cid = dao.Insert(cname, cpassword, address, region)
                result = self.build_client_attributes(cid, cname, cpassword, address, region)
                return jsonify(Client= result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400
