from flask import jsonify
from dao.administrator import AdministratorDAO

class AdministratorHandler:


    def build_administrator_dict(self, row):
        result = {}
        result['u_id'] = row[0]
        result['u_email'] = row[1]
        result['u_password'] = row[2]
        result['u_name'] = row[3]
        result['u_lastname'] = row[4]
        result['u_region'] = row[5]
        result['u_age'] = row[6]
        result['ad_id'] = row[7]
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


# ===================================================================================================================
#                                          insert administrator
# ===================================================================================================================

    def insertAdministrator(self, form):
        if form and len(form) == 6:
            u_email = form['u_email']
            u_password = form['u_password']
            u_name = form['u_name']
            u_last_name = form['u_last_name']
            u_region = form['u_region']
            u_age = form['u_age']
            if u_email and u_password and u_name and u_last_name and u_region and u_age:
                dao = AdministratorDAO()
                ad_id = dao.insert(u_email, u_password, u_name, u_last_name, u_region, u_age)
                result = {}
                result["ad_id"] = ad_id
                result["u_email"] = u_email
                result["u_password"] = u_password
                result["u_name"] = u_name
                result["u_last_name"] = u_last_name
                result["u_region"] = u_region
                result["u_age"] = u_age

                return jsonify(Administrator=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    # ===================================================================================================================
    #                                          put administrator
    # ===================================================================================================================

    def putAdministratorByID(self, form, ad_id):
        if form and len(form) == 6:
            u_email = form['u_email']
            u_password = form['u_password']
            u_name = form['u_name']
            u_last_name = form['u_last_name']
            u_region = form['u_region']
            u_age = form['u_age']
            if u_email and u_password and u_name and u_last_name and u_region and u_age and ad_id:
                dao = AdministratorDAO()
                ad_id = dao.put(u_email, u_password, u_name, u_last_name, u_region, u_age, ad_id)
                result = {}
                result["ad_id"] = ad_id
                result["u_email"] = u_email
                result["u_password"] = u_password
                result["u_name"] = u_name
                result["u_last_name"] = u_last_name
                result["u_region"] = u_region
                result["u_age"] = u_age

                return jsonify(Administrator=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    # ===================================================================================================================
    #                                          delete administrator
    # ===================================================================================================================

    def deleteAdministratorByID(self, ad_id):
        dao = AdministratorDAO()
        if not dao.getAdministratorById(ad_id):
            return jsonify(Error="Administrator not found."), 404
        else:
            dao.delete(ad_id)
            return jsonify(DeleteStatus="OK"), 200




