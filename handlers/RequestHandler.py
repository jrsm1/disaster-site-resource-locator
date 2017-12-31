from flask import jsonify
from dao.RequestDAO import RequestDAO


class RequestHandler:

    def build_request_dict(self, row):
        result = {}
        result['requestid'] = row[0]
        result['cid'] = row[1]
        result['rid'] = row[2]
        result['qty'] = row[3]
        return result


    def build_request_attributes(self, requestid, cid, rid, qty):
        result = {}
        result['requestid'] = pid
        result['cid'] = cid
        result['rid'] = rid
        result['qty'] = qty
        return result


    def getAllRequest(self):

        dao = RequestDAO()
        request_list = dao.getAllRequest()
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)


    def getRequestById(self, requestid):

        dao = RequestDAO()

        row = dao.getRequestById(requestid)
        if not row:
            return jsonify(Error="Request Not Found"), 404
        else:
            request = self.build_request_dict(row)
        return jsonify(Request = request)


    def searchRequest(self, args):
        if len(args) > 4:
            return jsonify(Error = "Malformed search string."), 400
        else:
            requestid = args.get("pid")
            cid = args.get("cid")
            rid = args.get("rid")
            qty = args.get("qty")

            dao = RequestDAO()
            request_list = []
            if (len(args) == 2) and rid and qty:
                request_list = dao.getRequestByResourceIdAndQuantity(rid, qty)
            elif (len(args) == 1) and requestid:
                request_list = dao.getRequestById(requestid)
            elif (len(args) == 1) and cid:
                request_list = dao.getRequestByClientId(cid)
            elif (len(args) == 1) and rid:
                request_list = dao.getRequestByResourceId(rid) 
            elif (len(args) == 1) and qty:
                request_list = dao.getRequestByQuantity(qty) 
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in request_list:
                result = self.build_request_dict(row)
                result_list.append(result)
            return jsonify(Request=result_list)


    def insertRequest(self, form):
        if len(form) != 3:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            cid = form['cid']
            rid = form['rid']
            qty = form['qty']
            if cid and rid and qty:
                dao = RequestDAO()
                requestid = dao.insert(cid, rid, qty)
                result = self.build_request_attributes(requestid, cid, rid, qty)
                return jsonify(Request=result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

