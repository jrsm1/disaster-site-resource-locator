from flask import Flask, jsonify, request
from handlers.UserHandler import UserHandler
from handlers.ResourceHandler import ResourceHandler
from handlers.SupplierHandler import SupplierHandler
from handlers.AdminHandler import AdminHandler
from handlers.SalesRecordHandler import SalesRecordHandler
from handlers.ClientHandler import ClientHandler


app = Flask(__name__)

@app.route('/')
def greeting():
    return '<b>Welcome to the Resource Locator App!!!</b>'


#This one should be hidden...
@app.route('/dsrl/users/passwords')
def getUserPasswords():
    return UserHandler().getUserPasswords()


@app.route('/dsrl/users/<int:uid>')
def getUserById(uid):
    return UserHandler().getUserById(uid)                                         


@app.route('/dsrl/resources')
def getAllResources():
      if not request.args:
          return ResourceHandler().getAllResources()
      else:
          return ResourceHandler().searchResources(request.args)


@app.route('/dsrl/resources/rid')
def getResourceIds():
    return ResourceHandler().getResourceIds()


@app.route('/dsrl/resources/rname')
def getResourceNames():
    return ResourceHandler().getResourceNames()


@app.route('/dsrl/resources/categories')
def getResourceCategories():
    return ResourceHandler().getResourceCategories()


@app.route('/dsrl/resources/prices')
def getResourcePrices():
    return ResourceHandler().getResourcePrices()


@app.route('/dsrl/resources/available')
def getAvailableResources():
    return ResourceHandler().getAvailableResources()


@app.route('/dsrl/resources/requestcount')
def getRequestCount():
    return ResourceHandler().getRequestCount()


@app.route('/dsrl/resources/<int:rid>')
def getResourceById(rid):
    return ResourceHandler().getResourceById(rid)

@app.route('/dsrl/resources/<int:rid>/suppliers')
def getSuppliersByRID(rid):
    return ResourceHandler().getSuppliersByRID(rid)

#Start of Supplier


@app.route('/dsrl/suppliers')
def getAllSuppliers():
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    else:
        return SupplierHandler().searchSuppliers(request.args)


@app.route('/dsrl/suppliers/<string:selection>')
def getSuppliersBy(selection):
    return SupplierHandler().getSuppliersBy(selection)


@app.route('/dsrl/suppliers/<int:sid>')
def getSupplierByID(sid):
    return SupplierHandler().getSupplierByID(sid)

@app.route('/dsrl/suppliers/<int:sid>/resources')
def getResourcesBySID(sid):
    return SupplierHandler().getResourcesBySID(sid)

#Start of Admin


@app.route('/dsrl/admins')
def getAllAdmins():
    if not request.args:
        return AdminHandler().getAllAdmins()
    else:
        return AdminHandler().searchAdmins(request.args)


@app.route('/dsrl/admins/aid')
def getAdminIds():
    return AdminHandler().getAdminIds()


@app.route('/dsrl/admins/aname')
def getAdminNames():
    return AdminHandler().getAdminNames()

#The admin passwords should be hidden


@app.route('/dsrl/admins/passwords')
def getAdminPasswords():
    return AdminHandler().getAdminPasswords()


@app.route('/dsrl/admins/<int:aid>')
def getAdminById(aid):
    return AdminHandler().getAdminById(aid)

@app.route('/dsrl/admins/<int:aname>')
def getAdminByName(aname):
    return AdminHandler().getAdminByName(aname)


#End of Admin

#Start of Sales Records

@app.route('/dsrl/salesrecords')
def getAllSalesRecords():
    if not request.args:
        return SalesRecordHandler().getAllSalesRecords()
    else:
        return SalesRecordHandler().searchSalesRecords(request.args)


@app.route('/dsrl/salesrecords/srid')
def getSRIds():
    return SalesRecordHandler().getSRIds()


@app.route('/dsrl/salesrecords/sid')
def getSRSuppierIds():
    return SalesRecordHandler().getSRSupplierIds()

@app.route('/dsrl/salesrecords/earnings')
def getSREarnings():
    return SalesRecordHandler().getSREarnings()


@app.route('/dsrl/salesrecords/sales')
def getSRSales():
    return SalesRecordHandler().getSRSales()

@app.route('/dsrl/salesrecords/<int:srid>')
def getSRBySRId():
    return SalesRecordHandler().getSRBySRyId()
#End of Sales Records

#Start Client

@app.route('/dsrl/clients')
def getAllClients():
    if not request.args:
        return ClientHandler().getAllClients()
    else:
        return ClientHandler().searchClients(request.args)

#cpassword and CCard maybe should be removed from the method getClientsBy


@app.route('/dsrl/clients/<string:selection>')
def getClientsBy(selection):
    return ClientHandler().getClientsBy(selection)


@app.route('/dsrl/clients/<int:cid>')
def getClientsByID(cid):
    return SupplierHandler().getSupplierByID(cid)

@app.route('/dsrl/clients/<int:cid>/card')
def getCCByCID(cid):
    return ClientHandler().getCCByCID(cid)

if __name__ == '__main__':
    app.run()
