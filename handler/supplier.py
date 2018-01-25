from flask import jsonify
from dao.supplier import SupplierDAO

class SupplierHandler:

    def build_supplier_dict(self, row):
        result = {}
        result['u_id'] = row[0]
        result['u_email'] = row[1]
        result['u_password'] = row[2]
        result['u_name'] = row[3]
        result['u_lastname'] = row[4]
        result['u_region'] = row[5]
        result['u_age'] = row[6]
        result['s_id'] = row[7]
        result['s_bank_account'] = row[8]
        return result

    def build_announcement_dict(self, row):
        result = {}
        result['a_id'] = row[0]
        result['a_price'] = row[1]
        result['a_date'] = row[2]
        result['a_sold_out'] = row[3]
        result['a_initial_qty'] = row[4]
        result['a_curr_qty'] = row[5]
        return result

    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_category'] = row[1]
        result['r_name'] = row[2]
        result['r_description'] = row[3]
        return result

    def build_transaction_dict(self, row):
        result = {}
        result['t_id'] = row[0]
        result['t_price'] = row[1]
        result['t_date'] = row[2]
        result['t_qty'] = row[3]
        return result

    # ===================================================================================================================
    #                                                get all suppliers
    # ===================================================================================================================

    def getAllSuppliers(self):
        dao = SupplierDAO()
        supplier_list = dao.getAllSuppliers()
        if not supplier_list:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            result_list = []
            for row in supplier_list:
                result = self.build_supplier_dict(row)
                result_list.append(result)
        return jsonify(Suppliers=result_list)

    # ===================================================================================================================
    #                                        search for suppliers by region
    # ===================================================================================================================

    def searchSuppliers(self, args):
        region = args.get('region')
        name = args.get('name')
        lastname = args.get('lastname')
        dao = SupplierDAO()
        if (len(args) == 3) and region and name and lastname:
            supplier_list = dao.getSuppliersByRegionAndNameAndLastname(region, name, lastname)
        elif (len(args) == 2) and region and name:
            supplier_list = dao.getSuppliersByRegionAndName(region, name)
        elif (len(args) == 2) and region and lastname:
            supplier_list = dao.getSuppliersByRegionAndLastname(region, lastname)
        elif (len(args) == 2) and name and lastname:
            supplier_list = dao.getSuppliersByNameAndLastname(name, lastname)
        elif (len(args) == 1) and region:
            supplier_list = dao.getSuppliersByRegion(region)
        elif (len(args) == 1) and name:
            supplier_list = dao.getSuppliersByName(name)
        elif (len(args) == 1) and lastname:
            supplier_list = dao.getSuppliersByLastname(lastname)
        else:
            return jsonify(Error="Malformed query string"), 400
        if not supplier_list:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            result_list = []
            for row in supplier_list:
                result = self.build_supplier_dict(row)
                result_list.append(result)
        return jsonify(Supplier=result_list)

    # ===================================================================================================================
    #                                           get things by supplier id
    # ===================================================================================================================

    def getSupplierByID(self, s_id):
        dao = SupplierDAO()
        row = dao.getSupplierById(s_id)
        if not row:
            return jsonify(Error="Supplier Not Found"), 404
        else:
            result = self.build_supplier_dict(row)
        return jsonify(Supplier=result)

    def getAnnouncementsBySupplierID(self, s_id):
        dao = SupplierDAO()
        if not dao.getSupplierById(s_id):
            return jsonify(Error="Supplier Not Found"), 404
        announcements_list = dao.getAnnouncementsBySupplierId(s_id)
        result_list = []
        for row in announcements_list:
            result = self.build_announcement_dict(row)
            result_list.append(result)
        return jsonify(Announcements=result_list)

    def getResourcesBySupplierID(self, s_id):
        dao = SupplierDAO()
        if not dao.getSupplierById(s_id):
            return jsonify(Error="Supplier Not Found"), 404
        resources_list = dao.getResourcesBySupplierId(s_id)
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    def getTransactionsBySupplierID(self, s_id):
        dao = SupplierDAO()
        if not dao.getSupplierById(s_id):
            return jsonify(Error="Supplier Not Found"), 404
        transactions_list = dao.getTransactionsBySupplierId(s_id)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    # ===================================================================================================================
    #                                    get resources by supplier region
    # ===================================================================================================================

    def getResourcesByRegion(self, region):
        dao = SupplierDAO()
        if not dao.getResourcesByRegion(region):
            return jsonify(Error='Resource Not Found.'), 404
        else:
            resource_list = dao.getResourcesByRegion(region)
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

    # ===================================================================================================================
    #                                          insert supplier
    # ===================================================================================================================

    def insertSupplier(self, form):
        if form and len(form) == 7:
            u_email = form['u_email']
            u_password = form['u_password']
            u_name = form['u_name']
            u_last_name = form['u_last_name']
            u_region = form['u_region']
            u_age = form['u_age']
            s_bank_account = form['s_bank_account']
            if u_email and u_password and u_name and u_last_name and u_region and u_age and s_bank_account:
                dao = SupplierDAO()
                s_id = dao.insert(u_email, u_password, u_name, u_last_name, u_region, u_age, s_bank_account)
                result = {}
                result["s_id"] = s_id
                result["u_email"] = u_email
                result["u_password"] = u_password
                result["u_name"] = u_name
                result["u_last_name"] = u_last_name
                result["u_region"] = u_region
                result["u_age"] = u_age
                result["s_bank_account"] = s_bank_account
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    # ===================================================================================================================
    #                                          put supplier
    # ===================================================================================================================

    def putSupplierByID(self, form, s_id):
        if form and len(form) == 7:
            u_email = form['u_email']
            u_password = form['u_password']
            u_name = form['u_name']
            u_last_name = form['u_last_name']
            u_region = form['u_region']
            u_age = form['u_age']
            s_bank_account = form['s_bank_account']
            if u_email and u_password and u_name and u_last_name and u_region and u_age and s_bank_account and s_id:
                dao = SupplierDAO()
                s_id = dao.put(u_email, u_password, u_name, u_last_name, u_region, u_age, s_bank_account, s_id)
                result = {}
                result["s_id"] = s_id
                result["u_email"] = u_email
                result["u_password"] = u_password
                result["u_name"] = u_name
                result["u_last_name"] = u_last_name
                result["u_region"] = u_region
                result["u_age"] = u_age
                result["s_bank_account"] = s_bank_account
                return jsonify(Supplier=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

    # ===================================================================================================================
    #                                          put supplier
    # ===================================================================================================================

    def deleteSupplierByID(self, s_id):
        dao = SupplierDAO()
        if not dao.getSupplierById(s_id):
            return jsonify(Error="Supplier not found."), 404
        else:
            dao.delete(s_id)
            return jsonify(DeleteStatus="OK"), 200
