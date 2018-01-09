from flask import jsonify
from dao.user import UserDAO

class UserHandler:



    def build_user_dict(self, row):
        result = {}
        result['u_id'] = row[0]
        result['u_email'] = row[1]
        result['u_password'] = row[2]
        result['u_name'] = row[3]
        result['u_lastname'] = row[4]
        result['u_region'] = row[5]
        result['u_age'] = row[6]
        return result

    # ===================================================================================================================
    #                                           search Users
    # ===================================================================================================================

    def searchUsers(self, args):
        name = args.get("name")
        lastname = args.get("lastname")
        dao = UserDAO()
        user_list = []
        if (len(args) == 2) and name and lastname:
            user_list = dao.getUserByNameAndLastName(name,lastname)
        elif (len(args) == 1) and name:
            user_list = dao.getUserByName(name)
        elif (len(args) == 1) and lastname:
            user_list = dao.getUserByLastName(lastname)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        if len(result_list) == 0:
            return jsonify(Error="User Not Found"), 404
        return jsonify(User=result_list)


    # ===================================================================================================================
    #                                           get all Users
    # ===================================================================================================================
    def getAllUsers(self):
        dao = UserDAO()
        user_list = dao.getAllUsers()
        result_list = []
        for row in user_list:
            result = self.build_user_dict(row)
            result_list.append(result)
        if len(result_list) == 0:
            return jsonify(Error="User Not Found"), 404
        return jsonify(Users=result_list)

    # ===================================================================================================================
    #                                           get Users by ID
    # ===================================================================================================================

    def getUserByID(self, u_id):
        dao = UserDAO()
        row = dao.getUserById(u_id)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)

        return jsonify(User=user)

    # ===================================================================================================================
    #                                           get users by Name
    # ===================================================================================================================

    def getUserByName(self, name):
        dao = UserDAO()
        row = dao.getUserByName(name)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)

        return jsonify(User=user)

    # ===================================================================================================================
    #                                           get users by Last Name
    # ===================================================================================================================

    def getUserByLastName(self, lastname):
        dao = UserDAO()
        row = dao.getUserByLastName(lastname)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)

        return jsonify(User=user)

    # ===================================================================================================================
    #                                           get users by Name and Last Name
    # ===================================================================================================================

    def getUserByNameAndLastName(self, name, lastname):
        dao = UserDAO()
        row = dao.getUserByNameAndLastName(name,lastname)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)

        return jsonify(User=user)

    # ===================================================================================================================
    #                                           get users by Region
    # ===================================================================================================================

    def getUserByRegion(self, u_region):
        dao = UserDAO()
        row = dao.getUserByRegion(u_region)
        if not row:
            return jsonify(Error="User Not Found"), 404
        else:
            user = self.build_user_dict(row)

        return jsonify(User=user)
