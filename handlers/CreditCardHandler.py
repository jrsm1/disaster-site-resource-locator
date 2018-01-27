from flask import jsonify
from dao.CreditCardDAO import CreditCardDAO

class CreditCardHandler:
   
    def build_card_dict(self, row):
        result = {}
        result['cid'] = row[0]
        result['ccnum'] = row[1]
        result['expdate'] = row[2]
        result['climit'] = row[3]
        result['cvv'] = row[4]
        return result

    def build_card_atttributes(self, cid, ccnum, expdate, climit, cvv):
        result = {}
        result['cid'] = cid
        result['ccnum'] = ccnum
        result['expdate'] = expdate
        result['climit'] = climit
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

    def getCreditCardByClientId(self, cid):

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

    def getCreditCardByCardNumber(self, ccnum):

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

    def getCreditCardByExpirationDate(self, expdate):

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

    def getCreditCardByLimit(self, climit):

        dao = CreditCardDAO()
        card_list = dao.getCardByLimit(climit)
        if not card_list:
            return jsonify(Error="No card found"), 404
        else:
            result_list = []
            for row in card_list:
                result = self.build_card_dict(row)
                result_list.append(result)
        return jsonify(CreditCards=result_list)

    def getCreditCardByCardVerificationValue(self, cvv):

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
            climit = args.get("climit")
            cvv = args.get("cvv")

            dao = CreditCardDAO()
            card_list = []
            if (len(args) == 4) and cid and ccnum and climit and cvv:
                card_list = dao.getCardByClientAndCardNumberAndLimitAndCardVerificationValue(cid, ccnum, climit, cvv)
            elif (len(args) == 2) and cid and ccnum:
                card_list = dao.getCardByClientAndCardNumber(cid, ccnum)
            elif (len(args) == 2) and cid and expdate:
                card_list = dao.getCardByCardNumberAndExpirationDate(cid,expdate)
            elif (len(args) == 2) and cid and climit:
                card_list = dao.getCardByClientAndLimit(cid, climit)
            elif (len(args) == 2) and cid and cvv:
                card_list = dao.getCardByClientAndCardVerificationValue(cid, cvv)
            elif (len(args) == 2) and ccnum and expdate:
                card_list = dao.getCardByCardNumberAndExpirationDate(ccnum, expdate)
            elif (len(args) == 2) and ccnum and climit:
                card_list = dao.getCardByCardNumberAndLimit(ccnum, climit)
            elif (len(args) == 2) and ccnum and cvv:
                card_list = dao.getCardByCardNumberAndCardVerificationValue(ccnum, cvv)
            elif (len(args) == 2) and expdate and climit:
                card_list = dao.getCardByExpirationDateAndLimit(expdate, climit)
            elif (len(args) == 2) and expdate and cvv:
                card_list = dao.getCardByExpirationDateAndCardVerificationValue(expdate, cvv)
            elif (len(args) == 2) and climit and cvv:
                card_list = dao.getCardByLimitAndCardVerificationValue(climit, cvv)
            elif (len(args) == 1) and cid:
                card_list = dao.getCardByClientId(cid)
            elif (len(args) == 1) and ccnum:
                card_list = dao.getCardByCardNumber(ccnum)
            elif (len(args) == 1) and expdate:
                card_list = dao.getCardByExpirationDate(expdate)
            elif (len(args) == 1) and climit:
                card_list = dao.getCardByLimit(climit)
            elif (len(args) == 1) and cvv:
                card_list = dao.getCardByCardVerificationValue(cvv)
            else:
                return jsonify(Error="Malformed query string"), 400
            result_list = []
            for row in card_list:
                result = self.build_card_dict(row)
                result_list.append(result)
            return jsonify(CreditCard=result_list)

    def insertCard(self, form):
        if len(form) != 5:
            return jsonify(Error="Malformed POST request"), 400
        else:
            cid = form["cid"]
            ccnum = form["ccnum"]
            expdate = form['expdate']
            climit = form['climit']
            cvv = form['cvv']
            if cid and ccnum and expdate and climit and cvv:
                dao = CreditCardDAO()
                dao.insert(cid, ccnum, expdate, climit, cvv)
                result = self.build_card_atttributes(cid, ccnum, expdate, climit, cvv)
                return jsonify(CreditCard=result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

    def updateCard(self, cid, form):
        dao = CreditCardDAO()
        if not dao.getCardByClientId(cid):
            return jsonify(Error="Credit card not found."), 404
        else:
            if len(form) != 4:
                return jsonify(Error="Malformed update request"), 400
            else:
                ccnum = form['ccnum']
                expdate = form['expdate']
                climit = form['climit']
                cvv = form['cvv']

                if ccnum and expdate and climit and cvv:
                    dao.update(ccnum, expdate, climit, cvv)
                    result = self.build_card_atttributes(ccnum, expdate, climit, cvv)
                    return jsonify(CreditCard=result), 200
                else:
                    return jsonify(Error="Unexpected attributes in update request"), 400





