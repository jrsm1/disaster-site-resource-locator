from flask import jsonify


class ClientHandler:
    def build_client_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['cname'] = row[1]
        result['cpassword'] = row[2]
        result['ccity'] = row[3]
        result['ccard'] = row[4]
        return result

    def build_card_dict(self, row):
        result = {}
        result['ccnum'] = row[0]
        result['ccholder'] = row[1]
        result['expdate'] = row[2]
        return result

    def getClientList(self):
        client1 = [0, "Juan Rivera", "password", "Mayaguez", "7865538924567"]
        client2 = [1, "Jorge Sanchez", "password123", "Arecibo", "7861268924467"]
        client3 = [2, "Esteban Rivera", "Mayaguez", "7876943078", "7865088934769"]
        result = [client1, client2, client3]
        return result

    def getAllClients(self):
        client_list = self.getClientList()
        result_list = []
        for row in client_list:
            result = self.build_client_dict(row)
            result_list.append(result)
        return jsonify(Clients=result_list)

    def searchClients(self, args):
            ccity = args.get("city")
            cid = args.get("id")
            cname = args.get("name")
            cpassword = args.get("password")
            ccard = args.get("card")

            if ccity or cname or cpassword or ccard or cid:
                client_list = self.getClientList()
                result_list = []
                for row in client_list:
                    result = self.build_client_dict(row)
                    result_list.append(result)
                return jsonify(Clients=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

    def getClientsBy(self, selection):
        #Password and CCard maybe should be removed
        if selection == "cpassword" or selection == "cname" or selection == "ccity" or selection == "ccard" or \
                selection == "cid":
            client_list = self.getClientList()
            result_list = []
            for row in client_list:
                result = self.build_client_dict(row)
                result_list.append(result)
            return jsonify(Clients=result_list)
        else:
            return jsonify(Error="Malformed search string."), 400

    def getClientByID(self, sid):
        result = [0, "Juan Vasquez", "San Juan", "7874561925", "18.465539,-66.105735"]
        if not result:
            return jsonify(Error="Client Not Found"), 404
        else:
            clientID = self.build_client_dict(result)
        return jsonify(Client=clientID)

    def getCCByCID(self, cid):
        result = ['111', 'juan', '8/8/17']
        if not result:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            resources = self.build_card_dict(result)
        return jsonify(resources)
