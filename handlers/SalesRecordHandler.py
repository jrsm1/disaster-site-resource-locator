from flask import jsonify

class SalesRecordHandler:
   
    def build_srecord_dict(self, row):
        result = {}
        result['srid'] = row[0]
        result['sid'] = row[1]
        result['earnings'] = row[2]
        result['sales'] = row[3]
        return result


    def buildDummyData(self):
        srecord_list = []
        srecord1 = [1, '1', '1111', '1111']
        srecord2 = [2, '2', '2222', '2222']
        srecord3 = [3, '3', '3333', '3333']
        srecord4 = [4, '4', '4444', '4444']

        srecord_list.append(srecord1)
        srecord_list.append(srecord2)
        srecord_list.append(srecord3)
        srecord_list.append(srecord4)
        return srecord_list  


    def getAllSalesRecords(self):
        srecords_list = self.buildDummyData()

        result_list = []
        for row in srecords_list:
            result = self.build_srecord_dict(row)
            result_list.append(result)
        return jsonify(SRecords = result_list)


    def getSRIds(self):
        srid_list = self.buildDummyData()
        
        if not srid_list:
            return jsonify(Error = "No Sales Records Found"), 404
        else:
            result_list = []
            for row in srid_list:
                result = self.build_srecord_dict(row)
                result_list.append(result)
        return jsonify(SRIds = result_list)


    def getSRSupplierIds(self):
        sids_list = self.buildDummyData()
        
        if not sids_list:
            return jsonify(Error = "No Supplier Ids Found"), 404
        else:
            result_list = []
            for row in sids_list:
                result = self.build_srecord_dict(row)
                result_list.append(result)
        return jsonify(Sids = result_list)


    def getSREarnings(self):
        earnings_list = self.buildDummyData()
        
        if not earnings_list:
            return jsonify(Error = "No Earnings Found"), 404
        else:
            result_list = []
            for row in earnings_list:
                result = self.build_srecord_dict(row)
                result_list.append(result)
        return jsonify(Earnings = result_list)


    def getSRSales(self):
        sales_list = self.buildDummyData()
        
        if not sales_list:
            return jsonify(Error = "No Sales Found"), 404
        else:
            result_list = []
            for row in sales_list:
                result = self.build_srecord_dict(row)
                result_list.append(result)
        return jsonify(Sales = result_list)


    def getSRBySRId(self, srid):
        srecord = [1, '1', '1111', '1111']
  
        if not srecord:
            return jsonify(Error = "SalesRecord Not Found"), 404
        else:

            srecord = self.build_srecord_dict(srecord)
            return jsonify(SalesRecord = srecord)

    def searchSalesRecords(self, args):
        sid = args.get("sid")
        earnings = args.get("earnings")
        sales = args.get("sales")
        srecord_list = []

        if (len(args) == 2) and sid and earnings:
            srecord_list = self.buildDummyData()
        elif (len(args) == 2) and sid and sales:
            srecord_list = self.buildDummyData()
        elif (len(args) == 2) and earnings and sales:
            srecord_list = self.buildDummyData()
        elif (len(args) == 1) and sid:
            srecord_list = self.buildDummyData()

        elif (len(args) == 1) and earnings:
            srecord_list = self.buildDummyData()
        elif (len(args) == 1) and sales:
            srecord_list = self.buildDummyData()
        else:
            return jsonify(Error = "Malformed query string"), 400

        result_list = []
        for row in srecord_list:
            result = self.build_srecord_dict(row)
            result_list.append(result)
        return jsonify(SalesRecords = result_list)

