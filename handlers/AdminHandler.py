from flask import jsonify
from dao.AdminDAO import AdminDAO

class AdminHandler:
    def build_admin_dict(self, row):
        result = {}
        result['aid'] = row[0]
        result['aname'] = row[1]
        result['apassword'] = row[2]
        return result

    def build_admin_attributes(self, aid, aname, apassword):
        result = {}
        result['sid'] = aid
        result['name'] = aname
        result['password'] = apassword
        return result

    def getAllAdmins(self):
        dao = AdminDAO()
        admin_list = dao.getAllAdmins()
        result_list = []
        for row in admin_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
        return jsonify(Admins=result_list)

    def getAdminIds(self):
        dao = AdminDAO()
        admin_list = dao.getAdminIds()
        if not admin_list:
            return jsonify(Error="No ids found"), 404
        else:
            result_list = []
            for row in admin_list:
                result = {}
                result['aid'] = row[0]
                result_list.append(result)
        return jsonify(Ids=result_list)


    def getAdminNames(self):
        dao = AdminDAO()
        admin_list = dao.getAdminNames()

        if not admin_list:
            return jsonify(Error="No Admin Names Found"), 404
        else:
            result_list = []
            for row in admin_list:
                result = {}
                result['aname'] = row[0]
                result_list.append(result)

        return jsonify(Anames=result_list)
    #not used

    @property
    def getAdminPasswords(self):
        dao = AdminDAO()
        admin_list = dao.getAdminPasswords()
        if not admin_list:
            return jsonify(Error="No Passwords Found"), 404
        else:
            result_list = []
            for row in admin_list:
                result = self.build_admin_dict(row)
                result_list.append(result)

        return jsonify(Passwords=result_list)

    def getAdminById(self, aid):
        dao = AdminDAO()
        admin = dao.getAdminById(aid)
        if not admin:
            return jsonify(Error="Admin Not Found"), 404
        else:
            result = self.build_admin_dict(admin)
        return jsonify(Admin=result)

    def getAdminByName(self, aname):

        dao = AdminDAO()
        admin = dao.getAdminByName(aname)
        if not admin:
            return jsonify(Error="Admin Not Found"), 404
        else:
            result = self.build_admin_dict(admin)
        return jsonify(Admin=result)

    # TODO Verify and add other queries
    def searchAdmins(self, args):
        if len(args) > 2:
            return jsonify(Error="Malformed search string."), 400
        else:
            aname = args.get("aname")
            aid = args.get("aid")
            dao = AdminDAO()
            admin_list = []
            if len(args) == 1 and aname:
                admin_list = dao.getAdminByName(aname)
            elif len(args) == 1 and aid:
                admin_list = dao.getAdminById(aid)
            else:
                return jsonify(Error="Malformed query string"), 400
            result_list = []
            for row in admin_list:
                result = self.build_admin_dict(row)
                result_list.append(result)
            return jsonify(Admins=result_list)

    def insertAdmin(self, form):
        if len(form) != 2:
            return jsonify(Error="Malformed POST request"), 400
        else:
            aname = form['name']
            apassword = form['password']
            if aname and apassword:
                dao = AdminDAO()
                aid = dao.insert(aname, apassword)
                result = self.build_admin_attributes(aid, aname, apassword)
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Unexpected attributes in POST request"), 400

