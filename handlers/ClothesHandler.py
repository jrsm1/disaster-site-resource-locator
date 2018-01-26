from flask import jsonify
from dao.ClothesDAO import ClothesDAO
from dao.ResourcesDAO import ResourcesDAO


class ClothesHandler:

    def build_clothes_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['price'] = row[1]
        result['color'] = row[2]
        result['size'] = row[3]
        result['gender'] = row[4]
        result['piece'] = row[5]
        return result


    def build_clothes_attributes(self, rid, price, color, size, gender, piece):
        result = {}
        result['rid'] = rid
        result['price'] = price
        result['color'] = color
        result['size'] = size
        result['gender'] = gender
        result['piece'] = piece
        return result

    def build_supplierclothes_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['sid'] = row[1]
        result['sname'] = row[2]
        result['saddress'] = row[3]
        result['sphone'] = row[4]
        result['sregion'] = row[5]
        return result


    def build_requestclothes_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['requestid'] = row[1]
        result['cid'] = row[2]
        result['qty'] = row[3]
        result['price'] = row[4]
        result['color'] = row[5]
        result['size'] = row[6]
        result['gender'] = row[7]
        result['piece'] = row[8]
        return result


    def getAllClothes(self):

        dao = ClothesDAO()
        clothes_list = dao.getAllClothes()
        result_list = []
        for row in clothes_list:
            result = self.build_clothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)


    def getClothesById(self, rid):

        dao = ClothesDAO()
        row = dao.getClothesById(rid)
        if not row:
            return jsonify(Error="Clothes Not Found"), 404
        else:
            clothes = self.build_clothes_dict(row)
        return jsonify(Clothes = clothes)


    def getClothesByPrice(self, price):

        dao = ClothesDAO()
        clothes_list = dao.getClothesByPrice(price)
        if not clothes_list:
            return jsonify(Error = "No Clothes found"), 404
        else:
            result_list = []
            for row in clothes_list:
                result = self.build_clothes_dict(row)
                result_list.append(result)
        return jsonify(Clothes = result_list)


    def getClothesByLessThanPrice(self, price):

        dao = ClothesDAO()
        price_list = dao.getClothesByLessThanPrice(price)
        if not price_list:
            return jsonify(Error = "No price found"), 404
        else:
            result_list = []
            for row in price_list:
                result = self.build_clothes_dict(row)
                result_list.append(result)
        return jsonify(Clothes = result_list)


    def getClothesByGreaterThanPrice(self, price):

        dao = ClothesDAO()
        price_list = dao.getClothesByGreaterThanPrice(price)
        if not price_list:
            return jsonify(Error = "No price found"), 404
        else:
            result_list = []
            for row in price_list:
                result = self.build_clothes_dict(row)
                result_list.append(result)
        return jsonify(Clothes = result_list)


    def getClothesByColor(self, color):

        dao = ClothesDAO()
        clothes_list = dao.getClothesByColor(color)
        if not clothes_list:
            return jsonify(Error = "No Clothes found"), 404
        else:
            result_list = []
            for row in clothes_list:
                result = self.build_clothes_dict(row)
                result_list.append(result)
        return jsonify(Clothes = result_list)


    def getClothesBySize(self, size):

        dao = ClothesDAO()
        clothes_list = dao.getClothesBySize(size)
        if not clothes_list:
            return jsonify(Error = "No Clothes found"), 404
        else:
            result_list = []
            for row in clothes_list:
                result = self.build_clothes_dict(row)
                result_list.append(result)
        return jsonify(Clothes = result_list)


    def getClothesByGender(self, gender):

        dao = ClothesDAO()
        clothes_list = dao.getClothesByGender(gender)
        if not clothes_list:
            return jsonify(Error = "No Clothes found"), 404
        else:
            result_list = []
            for row in clothes_list:
                result = self.build_clothes_dict(row)
                result_list.append(result)
        return jsonify(Clothes = result_list)


    def getClothesByPiece(self, piece):

        dao = ClothesDAO()
        clothes_list = dao.getClothesByPiece(piece)
        if not clothes_list:
            return jsonify(Error = "No Clothes found"), 404
        else:
            result_list = []
            for row in clothes_list:
                result = self.build_clothes_dict(row)
                result_list.append(result)
        return jsonify(Clothes = result_list)


    def searchClothes(self, args):
        if len(args) > 6:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            color = args.get("color")
            size = args.get("size")
            gender = args.get("gender")
            piece = args.get("piece")

            dao = ClothesDAO()
            clothes_list = []
            if (len(args) == 1) and rid:
                clothes_list = dao.getClothesById(rid)
            elif (len(args) == 1) and price:
                clothes_list = dao.getClothesByPrice(price)
            elif (len(args) == 1) and color:
                clothes_list = dao.getClothesByColor(color)
            elif (len(args) == 1) and size:
                clothes_list = dao.getClothesBySize(size)
            elif (len(args) == 1) and gender:
                clothes_list = dao.getClothesByGender(gender)
            elif (len(args) == 1) and piece:
                clothes_list = dao.getClothesByPiece(piece)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in clothes_list:
                result = self.build_clothes_dict(row)
                result_list.append(result)
            return jsonify(Clothes = result_list)


    def searchClothesRequests(self, args):
        if len(args) > 6:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            color = args.get("color")
            size = args.get("size")
            gender = args.get("gender")
            piece = args.get("piece")

            dao = ClothesDAO()
            clothes_list = []
            if (len(args) == 1) and rid:
                clothes_list = dao.getClothesRequestsById(rid)
            elif (len(args) == 1) and price:
                clothes_list = dao.getClothesRequestsByPrice(price)
            elif (len(args) == 1) and color:
                clothes_list = dao.getClothesRequestsByColor(color)
            elif (len(args) == 1) and size:
                clothes_list = dao.getClothesRequestsBySize(size)
            elif (len(args) == 1) and gender:
                clothes_list = dao.getClothesRequestsByGender(gender)
            elif (len(args) == 1) and piece:
                clothes_list = dao.getClothesRequestsByPiece(piece)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in clothes_list:
                result = self.build_requestclothes_dict(row)
                result_list.append(result)
            return jsonify(Clothes = result_list)


    def insertClothes(self, form):
        if len(form) != 7:
            return jsonify(Error = "Malformed POST request"), 400
        else:
            sid = form['sid']
            qty = form['qty']
            price = form['price']
            color = form['color']
            size = form['size']
            gender = form['gender']
            piece = form['piece']

            if sid and qty and price and color and size and gender and piece:
                rid = ResourcesDAO().insert(sid,qty,price)
                dao = ClothesDAO()
                dao.insert(rid, price, color, size, gender, piece)
                result = self.build_clothes_attributes(rid, price, color, size, gender, piece)
                return jsonify(Clothes = result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400


    def updateClothes(self, rid, form):
        dao = ClothesDAO()
        if not dao.getClothesById(rid):
            return jsonify(Error = "Clothes not found."), 404
        else:
            if len(form) != 5:
                return jsonify(Error="Malformed update request"), 400
            else:
                price = form['price']
                color = form['color']
                size = form['size']
                gender = form['gender']
                piece = form['piece']

                if price and color and size and gender and piece:
                    dao.update(rid, price, color, size, gender, piece)
                    result = self.build_clothes_attributes(rid, price, color, size, gender, piece)
                    return jsonify(Clothes=result), 200


    def getClothesSuppliers(self):
        dao = ClothesDAO()
        suppliers_list = dao.getClothesSuppliers()
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplierclothes_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)

    def getClothesSuppliersByRegion(self, region):
        dao = ClothesDAO()
        suppliers_list = dao.getClothesSuppliersByRegion(region)
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_supplierclothes_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)


    def getAllClothesRequests(self):

        dao = ClothesDAO()
        clothes_list = dao.getAllClothesRequests()
        result_list = []
        for row in clothes_list:
            result = self.build_requestclothes_dict(row)
            result_list.append(result)
        return jsonify(Clothes=result_list)


