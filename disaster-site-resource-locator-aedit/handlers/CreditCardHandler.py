from flask import jsonify

class CreditCardHandler:
   
    def build_card_dict(self, row):
        result = {}
        result['ccnum'] = row[0]
        result['ccholder'] = row[1]
        result['expdate'] = row[2]
        return result


    def buildDummyData(self):
        card_list = []
        card1 = ['111', 'juan', '8/8/17']
        card2 = ['222', 'mark', '2/4/19']
        card3 = ['333', 'edd', '7/2/22']
        card4 = ['444', 'tim', '4/3/20']

        card_list.append(card1)
        card_list.append(card2)
        card_list.append(card3)
        card_list.append(card4)
        return card_list  


    def getAllCreditCards(self):
        card_list = self.buildDummyData()

        result_list = []
        for row in card_list:
            result = self.build_card_dict(row)
            result_list.append(result)
        return jsonify(Cards = result_list)


    def getCreditCardNumbers(self):
        ccnum_list = self.buildDummyData()
        
        if not ccnum_list:
            return jsonify(Error = "No CCNumbers Found"), 404
        else:
            result_list = []
            for row in ccnum_list:
                result = self.build_card_dict(row)
                result_list.append(result)
        return jsonify(CCNums = result_list)


    def getCardHolders(self):
        names_list = self.buildDummyData()
        
        if not names_list:
            return jsonify(Error = "No CardHolders Found"), 404
        else:
            result_list = []
            for row in names_list:
                result = self.build_card_dict(row)
                result_list.append(result)
        return jsonify(Names = result_list)

    def getCardExpDates(self):
        dates_list = self.buildDummyData()

        if not dates_list:
            return jsonify(Error = "No Dates Found"), 404
        else:
            result_list = []
            for row in dates_list:
                result = self.build_card_dict(row)
                result_list.append(result)
        return jsonify(Dates = dates_list)


