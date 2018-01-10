from flask import jsonify
from dao.CreditCardDAO import CreditCardDAO

class CreditCardHandler:
   
    def build_card_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['ccnum'] = row[1]
        result['expdate'] = row[2]
        result['limit'] = row[3]
        result['cvv'] = row[4]
        return result

    def build_card_atttributes(self, cid, ccnum, expdate, limit, cvv):
        result = {}
        result['cid'] = cid
        result['ccnum'] = ccnum
        result['expdate'] = expdate
        result['limit'] = limit
        result['cvv'] = cvv
        return result



    def getAllCreditCards(self):
        dao = CreditCardDAO()
        card_list = dao.getAllCards()

        result_list = []
        for row in card_list:
            result = self.build_card_dict(row)
            result_list.append(result)
        return jsonify(CreditCards = result_list)

    def getCardByClient(self, cid):

        dao = CreditCardDAO()
        card_list = dao.getCardByClientId(cid)
        if not card_list:
            return jsonify(Error="No card found"), 404
        else:
            result_list = []
            for row in card_list:
                result = self.build_card_dict(row)
                result_list.append(result)
        return jsonify(CreditCards=result_list)

    def getCardByCardNumber(self, ccnum):

        dao = CreditCardDAO()
        card_list = dao.getCardByCardNumber(ccnum)
        if not card_list:
            return jsonify(Error="No card found"), 404
        else:
            result_list = []
            for row in card_list:
                result = self.build_card_dict(row)
                result_list.append(result)
        return jsonify(CreditCards=result_list)

    def getCardByExpirationDate(self, expdate):

        dao = CreditCardDAO()
        card_list = dao.getCardByExpirationDate(expdate)
        if not card_list:
            return jsonify(Error="No card found"), 404
        else:
            result_list = []
            for row in card_list:
                result = self.build_card_dict(row)
                result_list.append(result)
        return jsonify(CreditCards=result_list)

    def getCardByLimit(self, limit):

        dao = CreditCardDAO()
        card_list = dao.getCardByLimit(limit)
        if not card_list:
            return jsonify(Error="No card found"), 404
        else:
            result_list = []
            for row in card_list:
                result = self.build_card_dict(row)
                result_list.append(result)
        return jsonify(CreditCards=result_list)

    def getCardByCardVerificationValue(self, cvv):

        dao = CreditCardDAO()
        card_list = dao.getCardByCardVerificationValue(cvv)
        if not card_list:
            return jsonify(Error="No card found"), 404
        else:
            result_list = []
            for row in card_list:
                result = self.build_card_dict(row)
                result_list.append(result)
        return jsonify(CreditCards=result_list)

    def searchCards(self, args):
        if len(args) > 5:
            return jsonify(Error="Malformed search string."), 400
        else:
            cid= args.get("cid")
            ccnum = args.get("ccnum")
            expdate = args.get("expdate")
            limit = args.get("limit")
            cvv = args.get("cvv")

            dao = CreditCardDAO()
            card_list = []
            if (len(args) == 4) and cid and ccnum and limit and cvv:
                card_list = dao.getCardByClientAndCardNumberAndLimitAndCardVerificationValue(cid, ccnum, limit, cvv)
            elif (len(args) == 2) and cid and ccnum:
                card_list = dao.getCardByClientAndCardNumber(cid, ccnum)
            elif (len(args) == 2) and cid and expdate:
                card_list = dao.getCardByCardNumberAndExpirationDate(cid,expdate)
            elif (len(args) == 2) and cid and limit:
                card_list = dao.getCardByClientAndLimit(cid, limit)
            elif (len(args) == 2) and cid and cvv:
                card_list = dao.getCardByClientAndCardVerificationValue(cid, cvv)
            elif (len(args) == 2) and ccnum and expdate:
                card_list = dao.getCardByCardNumberAndExpirationDate(ccnum, expdate)
            elif (len(args) == 2) and ccnum and limit:
                card_list = dao.getCardByCardNumberAndLimit(ccnum, limit)
            elif (len(args) == 2) and ccnum and cvv:
                card_list = dao.getCardByCardNumberAndCardVerificationValue(ccnum, cvv)
            elif (len(args) == 2) and expdate and limit:
                card_list = dao.getCardByExpirationDateAndLimit(expdate, limit)
            elif (len(args) == 2) and expdate and cvv:
                card_list = dao.getCardByExpirationDateAndCardVerificationValue(expdate, cvv)
            elif (len(args) == 2) and limit and cvv:
                card_list = dao.getCardByLimitAndCardVerificationValue(limit, cvv)
            elif (len(args) == 1) and cid:
                card_list = dao.getCardByClientId(cid)
            elif (len(args) == 1) and ccnum:
                card_list = dao.getCardByCardNumber(ccnum)
            elif (len(args) == 1) and expdate:
                card_list = dao.getCardByExpirationDate(expdate)
            elif (len(args) == 1) and limit:
                card_list = dao.getCardByLimit(limit)
            elif (len(args) == 1) and cvv:
                card_list = dao.getCardByCardVerificationValue(cvv)
            else:
                return jsonify(Error="Malformed query string"), 400
            result_list = []
            for row in card_list:
                result = self.build_aid_dict(row)
                result_list.append(result)
            return jsonify(CreditCard=result_list)

    def insertCard(self, form):
        if len(form) != 5:
            return jsonify(Error="Malformed POST request"), 400
        else:
            cid = form["cid"]
            ccnum = form["ccnum"]
            expdate = form['expdate']
            limit = form['limit']
            cvv = form['cvv']
            if cid and ccnum and expdate and limit and cvv:
                dao = CreditCardDAO()
                dao.insert(cid, ccnum, expdate, limit, cvv)
                result = self.build_card_attributes(cid, ccnum, expdate, limit, cvv)
                return jsonify(CreditCard=result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400





