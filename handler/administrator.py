from flask import jsonify
from dao.administrator import AdministratorDAO

class AdministratorHandler:


    def build_administrator_dict(self, row):
        result = {}
        result['ad_id'] = row[1]
        result['u_id'] = row[0]
        result['u_email'] = row[2]
        result['u_password'] = row[3]
        result['u_name'] = row[4]
        result['u_lastname'] = row[5]
        result['u_region'] = row[6]
        result['u_age'] = row[7]
        return result


# ===================================================================================================================
#                                        search for Administrator
# ===================================================================================================================

    def searchAdministrator(self, args):
        name = args.get('name')
        lastname = args.get('lastname')
        dao = AdministratorDAO()
        if (len(args) == 2) and name and lastname:
            administrator_list = dao.getAdministratorByNameAndLastName(name, lastname)
        elif (len(args) == 1) and name:
            administrator_list = dao.getAdministratorByName(name)
        elif (len(args) == 1) and lastname:
            administrator_list = dao.getAdministratorByLastName(lastname)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in administrator_list:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        if len(result_list)==0:
            return jsonify(Error="Administrator Not Found"), 404
        return jsonify(Administrator=result_list)

# ===================================================================================================================
#                                           get all Administrator
# ===================================================================================================================

    def getAllAdministrators(self):
        dao = AdministratorDAO()
        ad_list = dao.getAllAdministrators()
        result_list = []
        for row in ad_list:
            result = self.build_administrator_dict(row)
            result_list.append(result)
        if len(result_list)==0:
            return jsonify(Error="Administrator Not Found"), 404
        return jsonify(Administrator=result_list)

# ===================================================================================================================
#                                           get Administrator by ID
# ===================================================================================================================

    def getAdministratorByID(self, ad_id):
        dao = AdministratorDAO()
        row = dao.getAdministratorById(ad_id)
        if not row:
            return jsonify(Error="Administrator Not Found"), 404
        else:
            result = self.build_administrator_dict(row)
        return jsonify(Administrator=result)
