from flask import jsonify
from dao.supplier import SupplierDAO


class SupplierHandler:

    def build_supplier_dict(self, row):
        result = {}
        result['s_id'] = row[0]
        result['u_id'] = row[1]
        result['bank_account'] = row[2]
        result['u_email'] = row[3]
        result['u_password'] = row[4]
        result['u_name'] = row[5]
        result['u_lastname'] = row[6]
        result['u_region'] = row[7]
        result['u_age'] = row[8]
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
        suppliers_list = dao.getAllSuppliers()
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    # ===================================================================================================================
    #                                        search for suppliers by region
    # ===================================================================================================================

    def searchSuppliers(self, args):
        if len(args) > 1:
            return jsonify(Error='Malformed search string.'), 400
        else:
            region = args.get('region')
            if region:
                dao = SupplierDAO()
                supplier_list = dao.getSuppliersByRegion(region)
                result_list = []
                for row in supplier_list:
                    result = self.build_supplier_dict(row)
                    result_list.append(result)
                return jsonify(Suppliers=result_list)
            else:
                return jsonify(Error='Malformed search string.'), 400


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
