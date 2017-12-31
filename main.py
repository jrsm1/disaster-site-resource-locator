from handlers import *
from flask import Flask, request, render_template, jsonify
app = Flask(__name__)


@app.route('/')
def greeting():
    return render_template('index.html')

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


if __name__ == '__main__':
    app.run(host='0.0.0.0')
