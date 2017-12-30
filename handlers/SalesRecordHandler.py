from flask import jsonify
from dao.SalesRecordDAO import SalesRecordDAO

class SalesRecordHandler:
   
    def build_srecord_dict(self, row):
        result = {}
        result['sid'] = row[0]
        result['earnings'] = row[1]
        result['sales'] = row[2]
        return result


    def build_srecord_attributes(self, sid, earnings, sales):
        result = {}
        result['sid'] = sid
        result['earnings'] = earnings
        result['sales'] = sales
        return result

    def getAllSalesRecords(self):

        dao = SalesRecordDAO()
        srecord_list = dao.getAllSalesRecord()
        result_list = []
        for row in srecord_list:
            result = self.build_srecord_dict(row)
            result_list.append(result)
        return jsonify(SRecords = result_list)


    def getSalesRecordById(self, sid):
       
        dao = SalesRecordDAO()
        row = dao.getSalesRecordById(sid)
        if not row:
            return jsonify(Error = "No SalesRecord Found"), 404
        else:
            srecord = self.build_srecord_dict(row)
        return jsonify(SRecord = srecord)


    def getSalesRecordByEarnings(self, earnings):
       
        dao = SalesRecordDAO()
        earnings_list = dao.getSalesRecordByEarnings(earnings)

        if not earnings_list:
            return jsonify(Error = "No Earnings Found"), 404
        else:
            result_list = []
            for row in earnings_list:
                result = self.build_srecord_dict(row)
                result_list.append(result)
        return jsonify(Earnings = result_list)


    def getSalesRecordBySales(self, sales):
       
        dao = SalesRecordDAO()
        sales_list = dao.getSalesRecordBySales(sales)
 
        if not sales_list:
            return jsonify(Error = "No Sales Found"), 404
        else:
            result_list = []
            for row in sales_list:
                result = self.build_srecord_dict(row)
                result_list.append(result)
        return jsonify(Sales = result_list)


    def searchSalesRecords(self, args):
        sid = args.get("sid")
        earnings = args.get("earnings")
        sales = args.get("sales")

        dao = SalesRecordDAO()
        srecord_list = []

        if (len(args) == 2) and earnings and sales:
            srecord_list = dao.getSalesRecordByEarningsAndSales(earnings, sales)
        elif (len(args) == 1) and sid:
            srecord_list = dao.getSalesRecordById(sid)
        elif (len(args) == 1) and earnings:
            srecord_list = dao.getSalesRecordByEarnings(earnings)
        elif (len(args) == 1) and sales:
            srecord_list = dao.getSalesRecordBySales(sales)
        else:
            return jsonify(Error = "Malformed query string"), 400

        result_list = []
        for row in srecord_list:
            result = self.build_srecord_dict(row)
            result_list.append(result)
        return jsonify(SalesRecords=result_list)


    def insertSalesRecord(self, form):
        if len(form) != 3:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            sid = form['sid']
            earnings = form['earnings']
            sales = form['sales']
            if sid and earnings and sales:
                dao = SalesRecordDAO()
                dao.insert(sid, earnings, sales)
                result = self.build_srecord_attributes(sid, earnings, sales)
                return jsonify(SalesRecord = result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400
