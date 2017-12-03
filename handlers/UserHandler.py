from flask import jsonify


class UserHandler:
    def build_user_dict(self, row):
        result = {}
        result['uid'] = row[0]
        result['role'] = row[1]
        result['uname'] = row[2]
        result['password'] = row[3]
        return result


    def buildDummyData(self):
        user_list = []
        user1 = [1, 'admin', 'test', 'pass1']
        user2 = [2, 'supplier', 'ivan', 'pass2']
        user3 = [3, 'client', 'pete', 'pass3']
        user4 = [4, 'client', 'sape', 'pass4']

        user_list.append(user1)
        user_list.append(user2)
        user_list.append(user3)
        user_list.append(user4)
        return user_list    


    def getAllUsers(self):
        user_list = self.buildDummyData()

        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        return jsonify(Users = result_list)


    def getUserIds(self):
        id_list = self.buildDummyData()
        
        if not id_list:
            return jsonify(Error = "No ids found"), 404
        else:
            result_list = []
            for row in id_list:
                result = self.build_user_dict(row)
                result_list.append(result)
        return jsonify(Ids = result_list)


    def getUserRoles(self):
        role_list = self.buildDummyData()

        if not role_list:
            return jsonify(Error = "No Roles Found"), 404
        else:
            result_list = []
            for row in role_list:
                result = self.build_user_dict(row)
                result_list.append(result)

        return jsonify(Roles = result_list)


    def getUserNames(self):
        unames_list = self.buildDummyData()

        if not unames_list:
            return jsonify(Error = "No UserNames Found"), 404
        else:
            result_list = []
            for row in unames_list:
                result = self.build_user_dict(row)
                result_list.append(result)

        return jsonify(Unames = unames_list)

    
    def getUserPasswords(self):
        password_list = self.buildDummyData()

        if not password_list:
            return jsonify(Error = "No Passwords Found"), 404
        else:
            result_list = []
            for row in password_list:
                result = self.build_user_dict(row)
                result_list.append(result)

        return jsonify(Passwords = result_list)


    def getUserById(self, uid):
  
        row = [1, 'admin', 'test', 'pass1']
        if not row:
            return jsonify(Error = "User Not Found"), 404
        else:
            user = self.build_user_dict(row)
        return jsonify(User = user)

#TODO Verify and add other queries
    def searchUsers(self, args):
        if len(args) > 1:
            return jsonify(Error = "Malformed search string."), 400
        else:
            role = args.get("role")
            if role:
                user_list = self.buildDummyData()
                result_list = []

                for row in user_list:
                    result = self.build_user_dict(row)
                    result_list.append(row)
                return jsonify(Users = result_list)
            else:
                return jsonify(Error="Malformed search string."), 400


