from flask import Flask, request
from handlers import *

app = Flask(__name__)


@app.route('/')
def greeting():
    return '<b>Welcome to the Resource Locator App!!!</b>'

################################################
#	Routes for Resource Queries
###############################################


@app.route('/resources')
def getAllResources():
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchResources(request.args)


@app.route('/resources/rid')
def getResourceIds():
    return ResourceHandler().getResourceIds()


@app.route('/resources/rname')
def getResourceNames():
    return ResourceHandler().getResourceNames()


@app.route('/resources/categories')
def getResourceCategories():
    return ResourceHandler().getResourceCategories()


@app.route('/resources/prices')
def getResourcePrices():
    return ResourceHandler().getResourcePrices()


@app.route('/resources/available')
def getAvailableResources():
    return ResourceHandler().getAvailableResources()


@app.route('/resources/requestcount')
def getRequestCount():
    return ResourceHandler().getRequestCount()


@app.route('/resources/<int:rid>')
def getResourceById(rid):
    return ResourceHandler().getResourceById(rid)


@app.route('/resources/<int:rid>/suppliers')
def getSuppliersByRID(rid):
    return ResourceHandler().getSuppliersByRID(rid)


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


@app.route('/admins')
def getAllAdmins():
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


@app.route('/salesrecords')
def getAllSalesRecords():
    if not request.args:
        return SalesRecordHandler().getAllSalesRecords()
    else:
        return SalesRecordHandler().searchSalesRecords(request.args)


@app.route('/salesrecords/srid')
def getSRIds():
    return SalesRecordHandler().getSRIds()


@app.route('/salesrecords/sid')
def getSRSuppierIds():
    return SalesRecordHandler().getSRSupplierIds()


@app.route('/salesrecords/sales')
def getSRSales():
    return SalesRecordHandler().getSRSales()


@app.route('/salesrecords/<int:srid>')
def getSRBySRId(srid):
    return SalesRecordHandler().getSRBySRId(srid)


############################################
#	Routes for Client Queries
#############################################


@app.route('/clients')
def getAllClients():
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


@app.route('/statistics')
def getStatistics():
    return ResourceHandler().getRequestCount()


##############################################
#	Routes for Purchase Queries
##############################################

@app.route('/purchases', methods=['GET', 'POST'])
def getAllPurchases():
    if request.method == 'POST':
        return PurchaseHandler().insertPurchase(request.form)
    else:
        if not request.args:
            return PurchaseHandler().getAllPurchases()
        else:
            return PurchaseHandler().searchPurchases(request.args)


if __name__ == '__main__':
    app.run(host='0.0.0.0')
