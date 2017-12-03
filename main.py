from flask import Flask, jsonify, request
from handlers.UserHandler import UserHandler
from handlers.ResourceHandler import ResourceHandler


app = Flask(__name__)

@app.route('/')
def greeting():
    return '<b>Welcome to the Resource Locator App!!!</b>'


@app.route('/dsrl/users')
def getAllUsers():
    if not request.args:
        return UserHandler().getAllUsers()
    else:
        return UserHandler().searchUsers(request.args)


@app.route('/dsrl/users/uid')
def getUserIds():
    return UserHandler().getUserIds()


@app.route('/dsrl/users/role')
def getUserRoles():
    return UserHandler().getUserRoles()


@app.route('/dsrl/users/uname')
def getUserNames():
    return UserHandler().getUserNames()

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


if __name__ == '__main__':
    app.run()
