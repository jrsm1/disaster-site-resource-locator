from handlers import *
from flask import Flask, request, render_template, jsonify
app = Flask(__name__)


@app.route('/')
def greeting():
    return render_template('index.html')

################################################
#	Routes for Resource Queries
###############################################


@app.route('/resources', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        return ResourceHandler().insertResources(request.form)
    else:
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchResources(request.args)


@app.route('/resources/rid/<int:rid>')
def getResourceById(rid):
    return ResourceHandler().getResourcesById(rid)


@app.route('/resources/sid/<int:sid>')
def getResourcesBySupplierId(sid):
    return ResourceHandler().getResourcesBySupplierId(sid)


@app.route('/resources/<int:rid>/supplier')
def getSupplierByResourcesId(rid):
    return ResourceHandler().getSupplierByResourcesId(rid)


#############################################
#	Routes for Supplier Queries
#############################################


@app.route('/suppliers', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else:
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.args)


@app.route('/suppliers/<string:selection>')
def getSuppliersBy(selection):
    return SupplierHandler().getSuppliersBy(selection)


@app.route('/suppliers/<int:sid>')
def getSupplierByID(sid):
    return SupplierHandler().getSupplierByID(sid)


@app.route('/suppliers/<int:sid>/resources')
def getResourcesBySID(sid):
    return SupplierHandler().getResourcesBySID(sid)


############################################
#	Routes for Admin Queries
############################################


@app.route('/admins', methods=['GET', 'POST'])
def getAllAdmins():
    if request.method == 'POST':
        return AdminHandler().insertAdmin(request.form)
    else:
        if not request.args:
            return AdminHandler().getAllAdmins()
        else:
            return AdminHandler().searchAdmins(request.args)


@app.route('/admins/aid')
def getAdminIds():
    return AdminHandler().getAdminIds()


@app.route('/admins/aname')
def getAdminNames():
    return AdminHandler().getAdminNames()


@app.route('/admins/<int:aid>')
def getAdminById(aid):
    return AdminHandler().getAdminById(aid)


@app.route('/admins/<string:aname>')
def getAdminByName(aname):
    return AdminHandler().getAdminByName(aname)

#########################################
#	Routes for SalesRecords Queries
#########################################


@app.route('/salesrecords', methods=['GET', 'POST'])
def getAllSalesRecords():
    if request.method == 'POST':
        return SalesRecordHandler().insertSalesRecord(request.form)
    else:
        if not request.args:
            return SalesRecordHandler().getAllSalesRecords()
        else:
            return SalesRecordHandler().searchSalesRecords(request.args)


@app.route('/salesrecords/sid/<int:sid>', methods=['GET', 'PUT', 'DELETE'])
def getSalesRecordBySuppierIds(sid):
    if request.method == 'GET':
        return SalesRecordHandler().getSalesRecordById(sid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/salesrecords/earnings/<float:earnings>')
def getSalesRecordByEarnings(earnings):
    return SalesRecordHandler().getSalesRecordByEarnings(earnings)


@app.route('/salesrecords/sales/<int:sales>')
def getSalesRecordBySales(sales):
    return SalesRecordHandler().getSalesRecordBySales(sales)


############################################
#	Routes for Client Queries
#############################################


@app.route('/clients', methods=['GET', 'POST'])
def getAllClients():
    if request.method == 'POST':
        return ClientHandler().insertClient(request.form)
    else:
        if not request.args:
            return ClientHandler().getAllClients()
        else:
            return ClientHandler().searchClients(request.args)


@app.route('/clients/<string:selection>')
def getClientsBy(selection):
    return ClientHandler().getClientsBy(selection)


@app.route('/clients/<int:cid>')
def getClientsByID(cid):
    return ClientHandler().getClientByID(cid)


##############################################
#	Routes for Purchase Queries
##############################################

@app.route('/purchase', methods=['GET', 'POST'])
def getAllPurchases():
    if request.method == 'POST':
        return PurchaseHandler().insertPurchase(request.form)
    else:
        if not request.args:
            return PurchaseHandler().getAllPurchases()
        else:
            return PurchaseHandler().searchPurchases(request.args)


@app.route('/purchase/pid/<int:pid>', methods=['GET','PUT','DELETE'])
def getPurchaseById(pid):
    if request.method == 'GET':
        return PurchaseHandler().getPurchaseById(pid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/purchase/cid/<int:cid>')
def getPurchaseByClientId(cid):
    return PurchaseHandler().getPurchaseByClientId(cid)


@app.route('/purchase/sid/<int:sid>')
def getPurchaseBySupplierId(sid):
    return PurchaseHandler().getPurchaseBySupplierId(sid)


@app.route('/purchase/rid/<int:rid>')
def getPurchaseByResourceId(rid):
    return PurchaseHandler().getPurchaseByResourceId(rid)


@app.route('/purchase/qty/<int:qty>')
def getPurchaseByQuantity(qty):
    return PurchaseHandler().getPurchaseByQuantity(qty)


@app.route('/purchase/total/<float:total>')
def getPurchaseByTotal(total):
    return PurchaseHandler().getPurchaseByTotal(total)


##############################################
#	Routes for Water Queries
##############################################
@app.route('/water', methods=['GET', 'POST'])
def getAllWater():
    if request.method == 'POST':
        return WaterHandler().insertWater(request.form)
    else:
        if not request.args:
            return WaterHandler().getAllWater()
        else:
            return WaterHandler().searchWater(request.args)


@app.route('/water/rid/<int:rid>', methods=['GET','PUT','DELETE'])
def getWaterById(rid):
    if request.method == 'GET':
        return WaterHandler().getWaterById(rid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/water/price/<float:price>')
def getWaterByPrice(price):
    return WaterHandler().getWaterByPrice(price)


@app.route('/water/suppliers')
def getWaterSuppliers():
    return WaterHandler().getWaterSuppliers()


@app.route('/water/requests')
def getWaterRequests():
    if not request.args:
        return WaterHandler().getWaterRequests()
    else:
        return WaterHandler().searchWaterRequests(request.args)


@app.route('/water/suppliers/<string:region>')
def getWaterSuppliersByRegion(region):
    return WaterHandler().getWaterSuppliersByRegion(region)


@app.route('/water/bsize/<string:bsize>')
def getWaterByBottleSize(bsize):
    return WaterHandler().getWaterByBottleSize(bsize)


##############################################
#	Routes for Ice Queries
##############################################
@app.route('/ice', methods=['GET', 'POST'])
def getAllIce():
    if request.method == 'POST':
        return IceHandler().insertIce(request.form)
    else:
        if not request.args:
            return IceHandler().getAllIce()
        else:
            return IceHandler().searchIce(request.args)


@app.route('/ice/rid/<int:rid>', methods=['GET','PUT','DELETE'])
def getIceById(rid):
    if request.method == 'GET':
        return IceHandler().getIceById(rid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/ice/price/<float:price>')
def getIceByPrice(price):
    return IceHandler().getIceByPrice(price)


@app.route('/ice/bsize/<string:bsize>')
def getIceByBagSize(bsize):
    return IceHandler().getIceByBagSize(bsize)


@app.route('/ice/suppliers')
def getIceSuppliers():
    return IceHandler().getIceSuppliers()


@app.route('/ice/suppliers/<string:region>')
def getIceSuppliersByRegion(region):
    return IceHandler().getIceSuppliersByRegion(region)


@app.route('/ice/requests')
def getIceRequests():
    if not request.args:
        return IceHandler().getIceRequests()
    else:
        return IceHandler().searchIceRequests(request.args)


##############################################
#	Routes for Tools Queries
##############################################

@app.route('/tools', methods=['GET', 'POST'])
def getAllTools():
    if request.method == 'POST':
        return ToolsHandler().insertTools(request.form)
    else:
        if not request.args:
            return ToolsHandler().getAllTools()
        else:
            return ToolsHandler().searchTools(request.args)


@app.route('/tools/rid/<int:rid>', methods=['GET','PUT','DELETE'])
def getToolsById(rid):
    if request.method == 'GET':
        return ToolsHandler().getToolsById(rid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/tools/name/<string:name>')
def getToolsByName(name):
    return ToolsHandler().getToolsByName(name)


@app.route('/tools/brand/<string:brand>')
def getToolsByBrand(brand):
    return ToolsHandler().getToolsByBrand(brand)


@app.route('/tools/price/<float:price>')
def getToolsByPrice(price):
    return ToolsHandler().getToolsByPrice(price)


@app.route('/tools/suppliers')
def getToolsSuppliers():
    return ToolsHandler().getToolsSuppliers()


@app.route('/tools/suppliers/<string:region>')
def getToolsSuppliersByRegion(region):
    return ToolsHandler().getToolsSuppliersByRegion(region)


@app.route('/tools/requests')
def getToolsRequests():
    if not request.args:
        return ToolsHandler().getToolsRequests()
    else:
        return ToolsHandler().searchToolsRequests(request.args)

##############################################
#	Routes for Fuel Queries
##############################################

@app.route('/fuel', methods=['GET', 'POST'])
def getAllFuel():
    if request.method == 'POST':
        return FuelHandler().insertFuel(request.form)
    else:
        if not request.args:
            return FuelHandler().getAllFuel()
        else:
            return FuelHandler().searchFuel(request.args)


@app.route('/fuel/rid/<int:rid>', methods=['GET','PUT','DELETE'])
def getFuelById(rid):
    if request.method == 'GET':
        return FuelHandler().getFuelById(rid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/fuel/type/<string:ftype>')
def getFuelByType(ftype):
    return FuelHandler().getFuelByType(ftype)


@app.route('/fuel/price/<float:price>')
def getFuelByPrice(price):
    return FuelHandler().getFuelByPrice(price)


@app.route('/fuel/csize/<int:csize>')
def getFuelByContainerSize(csize):
    return FuelHandler().getFuelByContainerSize(csize)


@app.route('/fuel/suppliers')
def getFuelSuppliers():
    return FuelHandler().getFuelSuppliers()


@app.route('/fuel/suppliers/<string:region>')
def getFuelSuppliersByRegion(region):
    return FuelHandler().getFuelSuppliersByRegion(region)


@app.route('/fuel/requests')
def getFuelRequests():
    if not request.args:
        return FuelHandler().getFuelRequests()
    else:
        return FuelHandler().searchFuelRequests(request.args)


##############################################
#	Routes for Food Queries
##############################################

@app.route('/food', methods=['GET', 'POST'])
def getAllFood():
    if request.method == 'POST':
        return FoodHandler().insertFood(request.form)
    else:
        if not request.args:
            return FoodHandler().getAllFood()
        else:
            return FoodHandler().searchFood(request.args)


@app.route('/food/rid/<int:rid>', methods=['GET','PUT','DELETE'])
def getFoodById(rid):
    if request.method == 'GET':
        return FoodHandler().getFoodById(rid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/food/price/<float:price>')
def getFoodByPrice(price):
    return FoodHandler().getFoodByPrice(price)


@app.route('/food/type/<string:ftype>')
def getFoodByType(ftype):
    return FoodHandler().getFoodByType(ftype)


@app.route('/food/suppliers')
def getFoodSuppliers():
    return FoodHandler().getFoodSuppliers()


@app.route('/food/suppliers/<string:region>')
def getFoodSuppliersByRegion(region):
    return FoodHandler().getFoodSuppliersByRegion(region)


@app.route('/purchase/expdate/<string:expdate>')
def getFoodByExpDate(expdate):
    return FoodHandler().getFoodByExpDate(expdate)


@app.route('/food/requests')
def getFoodRequests():
    if not request.args:
        return FoodHandler().getFoodRequests()
    else:
        return FoodHandler().searchFoodRequests(request.args)


##############################################
#	Routes for Clothes Queries
##############################################

@app.route('/clothes', methods=['GET', 'POST'])
def getAllClothes():
    if request.method == 'POST':
        return ClothesHandler().insertClothes(request.form)
    else:
        if not request.args:
            return ClothesHandler().getAllClothes()
        else:
            return ClothesHandler().searchClothes(request.args)


@app.route('/clothes/rid/<int:rid>', methods=['GET','PUT','DELETE'])
def getClothesById(rid):
    if request.method == 'GET':
        return ClothesHandler().getClothesById(rid)
    elif request.method == 'PUT':
        pass
    elif request.method == 'DELETE':
        pass
    else:
        return jsonify(Error="Method not allowed."), 405


@app.route('/clothes/price/<float:price>')
def getClothesByPrice(price):
    return ClothesHandler().getClothesByPrice(price)


@app.route('/clothes/color/<string:color>')
def getClothesByColor(color):
    return ClothesHandler().getClothesByColor(color)


@app.route('/clothes/size/<string:size>')
def getClothesBySize(size):
    return ClothesHandler().getClothesBySize(size)


@app.route('/clothes/gender/<string:gender>')
def getClothesByGender(gender):
    return ClothesHandler().getClothesByGender(gender)


@app.route('/clothes/piece/<string:piece>')
def getClothesByPiece(piece):
    return ClothesHandler().getClothesByPiece(piece)


@app.route('/clothes/suppliers')
def getClothesSuppliers():
    return ClothesHandler().getClothesSuppliers()


@app.route('/clothes/suppliers/<string:region>')
def getClothesSuppliersByRegion(region):
    return ClothesHandler().getClothesSuppliersByRegion(region)


@app.route('/clothes/requests')
def getClothesRequests():
    if not request.args:
        return ClothesHandler().getClothesRequests()
    else:
        return ClothesHandler().searchClothesRequests(request.args)


##############################################
#	Routes for Generator Queries
##############################################
@app.route('/generator', methods=['GET', 'POST'])
def getAllGenerator():
    if request.method == 'POST':
        return GeneratorHandler().insertGenerator(request.form)
    else:
        if not request.args:
            return GeneratorHandler().getAllGenerator()
        else:
            return GeneratorHandler().searchGenerator(request.args)


@app.route('/generator/<int:rid>')
def getGeneratorById(rid):
    return GeneratorHandler().getGeneratorById(rid)


@app.route("/generator/price/<float:price>")
def getGeneratorByPrice(price):
    return GeneratorHandler().getGeneratorByPrice(price)


@app.route("/generator/brand/<string:brand>")
def getGeneratorByBrand(brand):
    return GeneratorHandler().getGeneratorByBrand(brand)


@app.route("/generator/fueltype/<string:fueltype>")
def getGeneratorByFuelType(fueltype):
    return GeneratorHandler().getGeneratorByFuelType(fueltype)


@app.route("/generator/power/<int:powerrating>")
def getGeneratorByPowerRating(powerrating):
    return GeneratorHandler().getGeneratorByPowerRating(powerrating)


@app.route('/generator/suppliers')
def getGeneratorSuppliers():
    return GeneratorHandler().getGeneratorSuppliers()


@app.route('/generator/suppliers/<string:region>')
def getGeneratorSuppliersByRegion(region):
    return GeneratorHandler().getGeneratorSuppliersByRegion(region)


@app.route('/clothes/requests')
def getClothesRequests():
    if not request.args:
        return ClothesHandler().getClothesRequests()
    else:
        return ClothesHandler().searchClothesRequests(request.args)


##############################################
#	Routes for Battery Queries
##############################################
@app.route('/battery', methods=['GET', 'POST'])
def getAllBattery():
    if request.method == 'POST':
        return BatteryHandler().insertBattery(request.form)
    else:
        if not request.args:
            return BatteryHandler().getAllBattery()
        else:
            return BatteryHandler().searchBattery(request.args)


@app.route('/battery/<int:rid>')
def getBatteryById(rid):
    return BatteryHandler().getBatteryById(rid)


@app.route("/battery/price/<float:price>")
def getBatteryByPrice(price):
    return BatteryHandler().getBatteryByPrice(price)


@app.route("/battery/voltage/<int:voltage>")
def getBatteryByVoltage(voltage):
    return BatteryHandler().getBatteryByVoltage(voltage)


@app.route("/battery/type/<string:btype>")
def getBatteryByType(btype):
    return BatteryHandler().getBatteryByType(btype)


@app.route('/battery/suppliers')
def getBatterySuppliers():
    return BatteryHandler().getBatterySuppliers()


@app.route('/battery/suppliers/<string:region>')
def getBatterySuppliersByRegion(region):
    return BatteryHandler().getBatterySuppliersByRegion(region)


@app.route('/battery/requests')
def getBatteryRequests():
    if not request.args:
        return BatteryHandler().getBatteryRequests()
    else:
        return BatteryHandler().searchBatteryRequests(request.args)


##############################################
#	Routes for FirstAid Queries
##############################################
@app.route('/firstaid', methods=['GET', 'POST'])
def getAllAid():
    if request.method == 'POST':
        return FirstAidHandler().insertAid(request.form)
    else:
        if not request.args:
            return FirstAidHandler().getAllAid()
        else:
            return FirstAidHandler().searchAid(request.args)


@app.route('/firstaid/<int:rid>')
def getAidById(rid):
    return FirstAidHandler().getAidById(rid)


@app.route("/firstaid/price/<float:price>")
def getAidByPrice(price):
    return FirstAidHandler().getAidByPrice(price)


@app.route("/firstaid/brand/<string:brand>")
def getAidByBrand(brand):
    return FirstAidHandler().getAidByBrand(brand)


@app.route("/firstaid/type/<string:condition>")
def getAidByMedCondition(condition):
    return FirstAidHandler().getAidByMedCondition(condition)


@app.route('/firstaid/suppliers')
def getFirstAidSuppliers():
    return FirstAidHandler().getFirstAidSuppliers()


@app.route('/firstaid/suppliers/<string:region>')
def getAidSuppliersByRegion(region):
    return FirstAidHandler().getAidSuppliersByRegion(region)

##############################################
#	Routes for HeavyEquipment Queries
##############################################
@app.route('/heavyequipment', methods=['GET', 'POST'])
def getAllEquip():
    if request.method == 'POST':
        return HeavyEquipHandler().insertEquip(request.form)
    else:
        if not request.args:
            return HeavyEquipHandler().getAllEquip()
        else:
            return HeavyEquipHandler().searchEquip(request.args)


@app.route('/heavyequip/<int:rid>')
def getEquipById(rid):
    return HeavyEquipHandler().getEquipById(rid)


@app.route("/heavyequip/price/<float:price>")
def getEquipByPrice(price):
    return HeavyEquipHandler().getEquipByPrice(price)


@app.route("/heavyequip/make/<string:make>")
def getEquipByMake(make):
    return HeavyEquipHandler().getEquipByMake(make)


@app.route("/heavyequip/condition/<string:condition>")
def getEquipByCondition(condition):
    return HeavyEquipHandler().getEquipByCondition(condition)


@app.route("/heavyequip/function/<string:equipfunction>")
def getEquipByFunction(equipfunction):
    return HeavyEquipHandler().getEquipByFunction(equipfunction)


@app.route('/heavyequip/suppliers')
def getEquipSuppliers():
    return HeavyEquipHandler().getEquipSuppliers()


@app.route('/heavyequip/suppliers/<string:region>')
def getEquipSuppliersByRegion(region):
    return HeavyEquipHandler().getEquipSuppliersByRegion(region)


##############################################
#	Routes for Request Queries
##############################################
@app.route("/request", methods=['GET', 'POST'])
def getRequestAll():
    if request.method == 'POST':
        return RequestHandler().insertRequest(request.form)
    else:
        if not request.args:
            return RequestHandler().getAllRequest()
        else:
            return RequestHandler().searchRequest(request.args)


@app.route("/request/<int:reqid>")
def getRequestById(reqid):
    return RequestHandler().getRequestById(reqid)


@app.route("/reserve", methods=['GET', 'POST'])
def getReserveAll():
    if request.method == 'POST':
        return ReservationHandler().insertReservation(request.form)
    else:
        if not request.args:
            return ReservationHandler().getAllReservation()
        else:
            return ReservationHandler().searchReservation(request.args)


@app.route("/reserve/<int:resid>")
def getReserveById(reqid):
    return ReservationHandler().getReservationById(reqid)
################################################
#	Routes for Credit Card
###############################################


@app.route('/creditcard', methods=['GET', 'POST'])
def getAllCards():
    if request.method == 'POST':
        return CreditCardHandler().insertCreditCard(request.form)
    else:
        if not request.args:
            return CreditCardHandler().getAllCreditCards()
        else:
            return CreditCardHandler().searchCards(request.args)


@app.route('/creditcard/cid/<int:cid>')
def getCardByClientId(cid):
    return CreditCardHandler().getCreditCardByClientID(cid)


@app.route('/creditcard/ccnum/<string:ccnum>')
def getCardByCardNumber(ccnum):
    return CreditCardHandler().getCardByCardNumber(ccnum)


@app.route('/creditcard/expdate/<date:expdate>')
def getCardByExpirationDate(expdate):
    return CreditCardHandler().getCreditCardByExpirationDate(expdate)

@app.route('/creditcard/limit/<float:limit>')
def getCardByLimit(limit):
    return CreditCardHandler().getCardByCardLimit(limit)

@app.route('/creditcard/cvv/<string:cvv>')
def getCardByCardVerificationValue(cvv):
    return CreditCardHandler().getCardByCardVerificationValue(cvv)

if __name__ == '__main__':
    app.run(host='0.0.0.0')
