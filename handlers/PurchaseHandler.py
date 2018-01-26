from flask import jsonify
from dao.PurchaseDAO import PurchaseDAO
from dao.SalesRecordDAO import SalesRecordDAO
from dao.ResourcesDAO import ResourcesDAO


class PurchaseHandler:

    def build_purchase_dict(self, row):
        result = {}
        result['pid'] = row[0]
        result['cid'] = row[1]
        result['sid'] = row[2]
        result['rid'] = row[3]
        result['qty'] = row[4]
        result['total'] = row[5]
        result['ccnum'] = row[6]
        return result


    def build_purchase_attributes(self, pid, cid, sid, rid, qty, total, ccnum):
        result = {}
        result['pid'] = pid
        result['cid'] = cid
        result['sid'] = sid
        result['rid'] = rid
        result['qty'] = qty
        result['total'] = total
        result['ccnum'] = ccnum
        return result


    def getAllPurchases(self):

        dao = PurchaseDAO()
        purchase_list = dao.getAllPurchases()
        result_list = []
        for row in purchase_list:
            result = self.build_purchase_dict(row)
            result_list.append(result)
        return jsonify(Purchase=result_list)


    def getPurchaseById(self, pid):

        dao = PurchaseDAO()

        row = dao.getPurchaseById(pid)
        if not row:
            return jsonify(Error="Purchase Not Found"), 404
        else:
            purchase = self.build_purchase_dict(row)
        return jsonify(Purchase = purchase)


    def getPurchaseByClientId(self, cid):
       
        dao = PurchaseDAO()
        purchase_list = dao.getPurchaseByClientId(cid)

        if not purchase_list:
            return jsonify(Error = "No Purchase Found"), 404
        else:
            result_list = []
            for row in purchase_list:
                result = self.build_purchase_dict(row)
                result_list.append(result)
        return jsonify(Purchase = result_list)


    def getPurchaseBySupplierId(self, sid):
       
        dao = PurchaseDAO()
        purchase_list = dao.getPurchaseBySupplierId(sid)

        if not purchase_list:
            return jsonify(Error = "No Purchase Found"), 404
        else:
            result_list = []
            for row in purchase_list:
                result = self.build_purchase_dict(row)
                result_list.append(result)
        return jsonify(Purchase = result_list)


    def getPurchaseByResourceId(self, rid):
       
        dao = PurchaseDAO()
        purchase_list = dao.getPurchaseByResourceId(rid)

        if not purchase_list:
            return jsonify(Error = "No Purchase Found"), 404
        else:
            result_list = []
            for row in purchase_list:
                result = self.build_purchase_dict(row)
                result_list.append(result)
        return jsonify(Purchase = result_list)


    def getPurchaseByQuantity(self, qty):
       
        dao = PurchaseDAO()
        purchase_list = dao.getPurchaseByQuantity(qty)

        if not purchase_list:
            return jsonify(Error = "No Purchase Found"), 404
        else:
            result_list = []
            for row in purchase_list:
                result = self.build_purchase_dict(row)
                result_list.append(result)
        return jsonify(Purchase = result_list)


    def getPurchaseByTotal(self, total):
       
        dao = PurchaseDAO()
        purchase_list = dao.getPurchaseByTotal(total)

        if not purchase_list:
            return jsonify(Error = "No Purchase Found"), 404
        else:
            result_list = []
            for row in purchase_list:
                result = self.build_purchase_dict(row)
                result_list.append(result)
        return jsonify(Purchase = result_list)


    def searchPurchases(self, args):
        if len(args) > 6:
            return jsonify(Error = "Malformed search string."), 400
        else:
            pid = args.get("pid")
            cid = args.get("cid")
            sid = args.get("sid")
            rid = args.get("rid")
            qty = args.get("qty")
            total = args.get("total")

            dao = PurchaseDAO()
            purchases_list = []
            if (len(args) == 2) and sid and total:
                purchases_list = dao.getPurchaseBySupplierAndTotal(sid, total)
            elif (len(args) == 2) and sid and qty:
                purchases_list = dao.getPurchaseBySupplierAndQuantity(sid, qty)
            elif (len(args) == 2) and cid and total:
                purchases_list = dao.getPurchaseByClientAndTotal(cid, total)
            elif (len(args) == 2) and cid and qty:
                purchases_list = dao.getPurchaseByClientAndQuantity(cid, qty)
            elif (len(args) == 1) and pid:
                purchases_list = dao.getPurchaseById(pid)
            elif (len(args) == 1) and cid:
                purchases_list = dao.getPurchaseByClientId(cid)
            elif (len(args) == 1) and sid:
                purchases_list = dao.getPurchaseBySupplierId(sid)
            elif (len(args) == 1) and rid:
                purchases_list = dao.getPurchaseByResourceId(rid) 
            elif (len(args) == 1) and qty:
                purchases_list = dao.getPurchaseByQuantity(qty) 
            elif (len(args) == 1) and total:
                purchases_list = dao.getPurchaseByTotal(total)  
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in purchases_list:
                result = self.build_purchase_dict(row)
                result_list.append(result)
            return jsonify(Purchases=result_list)


    def insertPurchase(self, form):
        if len(form) != 5:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            cid = form['cid']
            sid = form['sid']
            rid = form['rid']
            qty = form['qty']
            ccnum = form['ccnum']
            if cid and sid and rid and qty and ccnum:
                pdao = PurchaseDAO()
                srdao = SalesRecordDAO()
                rdao = ResourcesDAO()
                currentPrice = rdao.getResourcePrice(rid)
                currentQty = rdao.getResourceQuantity(rid)
                currentSid = rdao.getResourceSupplierId(rid)
                if(int(currentQty) - int(qty) < 0):
                    return jsonify(Error = "Invalid Purchase request"), 400
                elif(int(currentSid) != int(sid)):
                    return jsonify(Error = "Invalid Purchase request"), 400
                else:
                    total = currentPrice*currentPrice
                    srdao.update(sid, total)
                    rdao.updateQuantity(rid, qty)
                    pid = pdao.insert(cid, sid, rid, qty,total,ccnum)
                    result = self.build_purchase_attributes(pid, cid, sid, rid, qty, total, ccnum)
                return jsonify(Purchase=result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

