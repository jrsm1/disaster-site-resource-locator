from flask import jsonify


class AdminHandler:
    def build_admin_dict(self, row):
        result = {}
        result['aid'] = row[0]
        result['aname'] = row[1]
        result['apassword'] = row[2]
        return result

    @property
    def buildDummyData(self):
        admin_list = []
        admin1 = [1, 'Keith Crawford', 'pass1']
        admin2 = [2, 'Ivan Valencia', 'pass2']
        admin3 = [3, 'Rosaline Ashford', 'pass3']
        admin4 = [4, 'Brenda Santiago', 'pass4']
        admin5 = [5, 'Jaime Marrero', 'pass5']

        admin_list.append(admin1)
        admin_list.append(admin2)
        admin_list.append(admin3)
        admin_list.append(admin4)
        admin_list.append(admin5)
        return admin_list

    def getAllAdmins(self):
        admin_list = self.buildDummyData

        result_list = []
        for row in admin_list:
            result = self.build_admin_dict(row)
            result_list.append(result)
        return jsonify(Admins=result_list)

    def getAdminIds(self):
        id_list = self.buildDummyData

        if not id_list:
            return jsonify(Error="No ids found"), 404
        else:
            result_list = []
            for row in id_list:
                result = self.build_admin_dict(row)
                result_list.append(result)
        return jsonify(Ids=result_list)


    def getAdminNames(self):
        anames_list = self.buildDummyData

        if not anames_list:
            return jsonify(Error="No Admin Names Found"), 404
        else:
            result_list = []
            for row in anames_list:
                result = self.build_admin_dict(row)
                result_list.append(result)

        return jsonify(Anames=anames_list)

    def getAdminPasswords(self):
        password_list = self.buildDummyData

        if not password_list:
            return jsonify(Error="No Passwords Found"), 404
        else:
            result_list = []
            for row in password_list:
                result = self.build_admin_dict(row)
                result_list.append(result)

        return jsonify(Passwords=result_list)

    def getAdminById(self, aid):

        row = [1, 'Keith Crawford', 'pass1']
        if not row:
            return jsonify(Error="Admin Not Found"), 404
        else:
            admin = self.build_admin_dict(row)
        return jsonify(Admin=admin)

    def getAdminByName(self, aname):

        row = [1, 'Keith Crawford', 'pass1']
        if not row:
            return jsonify(Error="Admin Not Found"), 404
        else:
            admin = self.build_admin_dict(row)
        return jsonify(Admin=admin)

    # TODO Verify and add other queries
    def searchAdmins(self, args):
        if len(args) > 1:
            return jsonify(Error="Malformed search string."), 400
        else:
            name = args.get("aname")
            if name:
                admin_list = self.buildDummyData
                result_list = []

                for row in admin_list:
                    result = self.build_admin_dict(row)
                    result_list.append(row)
                return jsonify(Admins=result_list)
            else:
                return jsonify(Error="Malformed search string."), 400

