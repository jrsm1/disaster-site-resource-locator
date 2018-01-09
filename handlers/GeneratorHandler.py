from flask import jsonify
from dao.GeneratorDAO import GeneratorDAO
from dao.ResourcesDAO import ResourcesDAO

class GeneratorHandler:

    def build_generator_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['price'] = row[1]
        result['brand'] = row[2]
        result['fueltype'] = row[3]
        result['powerrating'] = row[4]
        return result

    def build_generator_attributes(self, rid, price, brand, fueltype, powerrating):
        result = {}
        result['rid'] = rid
        result['price'] = price
        result['brand'] = brand
        result['fueltype'] = fueltype
        result['powerrating'] = powerrating
        return result

    def build_suppliergenerator_dict(self, row):
        result = {}
        result['rid'] = row[0]
        result['sid'] = row[1]
        result['sname'] = row[2]
        result['saddress'] = row[3]
        result['sphone'] = row[4]
        result['sregion'] = row[5]
        return result

    def getAllGenerator(self):

        dao = GeneratorDAO()
        generator_list = dao.getAllGenerator()
        result_list = []
        for row in generator_list:
            result = self.build_generator_dict(row)
            result_list.append(result)
        return jsonify(Generator=result_list)


    def getGeneratorById(self, rid):

        dao = GeneratorDAO()
        row = dao.getGeneratorById(rid)
        if not row:
            return jsonify(Error="Generator Not Found"), 404
        else:
            generator = self.build_generator_dict(row)
        return jsonify(Generator=generator)


    def getGeneratorByPrice(self, price):

        dao = GeneratorDAO()
        price_list = dao.getGeneratorByPrice(price)
        if not price_list:
            return jsonify(Error = "No price found"), 404
        else:
            result_list = []
            for row in price_list:
                result = self.build_generator_dict(row)
                result_list.append(result)
        return jsonify(Generator=result_list)

    def getGeneratorByBrand(self, brand):
        dao = GeneratorDAO()
        brand_list = dao.getGeneratorByBrand(brand)
        if not brand_list:
            return jsonify(Error = "No Brand found"), 404
        else:
            result_list = []
            for row in brand_list:
                result = self.build_generator_dict(row)
                result_list.append(result)
        return jsonify(Generator=result_list)

    def getGeneratorByFuelType(self, fueltype):
        dao = GeneratorDAO()
        fueltype_list = dao.getGeneratorByFuelType(fueltype)
        if not fueltype_list:
            return jsonify(Error="No type found"), 404
        else:
            result_list = []
            for row in fueltype_list:
                result = self.build_generator_dict(row)
                result_list.append(result)
        return jsonify(Generator=result_list)

    def getGeneratorByPowerRating(self, powerrating):
        dao = GeneratorDAO()
        power_list = dao.getGeneratorByPowerRating(powerrating)
        if not power_list:
            return jsonify(Error="No generator found"), 404
        else:
            result_list = []
            for row in power_list:
                result = self.build_generator_dict(row)
                result_list.append(result)
        return jsonify(Generator=result_list)

    def searchGenerator(self, args):
        if len(args) > 5:
            return jsonify(Error = "Malformed search string."), 400
        else:
            rid = args.get("rid")
            price = args.get("price")
            brand = args.get("brand")
            fueltype = args.get("fueltype")
            powerrating = args.get("powerrating")

            dao = GeneratorDAO()
            generator_list = []
            if (len(args) == 4) and price and brand and fueltype and powerrating:
                generator_list = dao.getGeneratorByPriceBrandFuelTypeAndPowerRating(price, brand, fueltype, powerrating)
            elif (len(args) == 3) and price and brand and fueltype:
                generator_list = dao.getGeneratorByPriceBrandAndFuelType(price, brand, fueltype)
            elif (len(args) == 3) and price and brand and powerrating:
                generator_list = dao.getGeneratorByPriceBrandAndPowerRating(price, brand, powerrating)
            elif (len(args) == 3) and price and powerrating and fueltype:
                generator_list = dao.getGeneratorByPricePowerRatingAndFuelType(price, powerrating, fueltype)
            elif (len(args) == 3) and powerrating and brand and fueltype:
                generator_list = dao.getGeneratorByPowerRatingBrandAndFuelType(powerrating, brand, fueltype)
            elif (len(args) == 2) and price and brand:
                generator_list = dao.getGeneratorByPriceAndBrand(price, brand)
            elif (len(args) == 2) and fueltype and brand:
                generator_list = dao.getGeneratorByFuelTypeAndBrand(fueltype, brand)
            elif (len(args) == 2) and price and fueltype:
                generator_list = dao.getGeneratorByPriceAndFuelType(price, fueltype)
            elif (len(args) == 2) and price and powerrating:
                generator_list = dao.getGeneratorByPriceAndPowerRating(price, powerrating)
            elif (len(args) == 2) and powerrating and fueltype:
                generator_list = dao.getGeneratorByPowerRatingAndFuelType(powerrating, fueltype)
            elif (len(args) == 2) and brand and powerrating:
                generator_list = dao.getGeneratorByBrandAndPowerRating(brand, powerrating)
            elif (len(args) == 1) and rid:
                generator_list = dao.getGeneratorById(rid)
            elif (len(args) == 1) and price:
                generator_list = dao.getGeneratorByPrice(price)
            elif (len(args) == 1) and brand:
                generator_list = dao.getGeneratorByBrand(brand)
            elif (len(args) == 1) and fueltype:
                generator_list = dao.getGeneratorByFuelType(fueltype)
            elif (len(args) == 1) and powerrating:
                generator_list = dao.getGeneratorByPowerRating(powerrating)
            else:
                return jsonify(Error = "Malformed query string"), 400
            result_list = []
            for row in generator_list:
                result = self.build_generator_dict(row)
                result_list.append(result)
            return jsonify(Generator=result_list)

    def insertGenerator(self, form):
        if len(form) != 6:
            return jsonify(Error="Malformed POST request"), 400
        else:
            sid = form["sid"]
            quantity = form["quantity"]
            price = form['price']
            brand = form['brand']
            fueltype = form['fueltype']
            powerrating = form["powerrating"]
            if sid and quantity and price and brand and fueltype and powerrating:
                dao = GeneratorDAO()
                rid = ResourcesDAO().insert(sid, quantity)
                rid = dao.insert(rid, price, brand, fueltype, powerrating)
                result = self.build_generator_attributes(rid, price, brand, fueltype, powerrating)
                return jsonify(Generator=result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

    def getGeneratorSuppliers(self):
        dao = GeneratorDAO()
        suppliers_list = dao.getGeneratorSuppliers()
        if not suppliers_list:
            return jsonify(Error = "No Suppliers found"), 404
        else:
            result_list = []
            for row in suppliers_list:
                result = self.build_suppliergenerator_dict(row)
                result_list.append(result)
        return jsonify(Suppliers = result_list)
