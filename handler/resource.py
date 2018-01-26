from flask import jsonify
from dao.resource import ResourceDAO

class ResourceHandler:

    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_category'] = row[1]
        result['r_name'] = row[2]
        result['r_description'] = row[3]
        return result

    def build_request_dict(self, row):
        result = {}
        result['req_id'] = row[0]
        result['c_id'] = row[1]
        result['r_id'] = row[2]
        result['req_qty'] = row[3]
        result['req_date'] = row[4]
        return result

    def build_announcement_dict(self, row):
        result = {}
        result['a_id'] = row[0]
        result['s_id'] = row[1]
        result['r_id'] = row[2]
        result['a_price'] = row[3]
        result['a_date'] = row[4]
        result['a_sold_out'] = row[5]
        result['a_initial_qty'] = row[6]
        result['a_curr_qty'] = row[7]
        return result

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

    # ===================================================================================================================
    #                                        search for resources
    # ===================================================================================================================

    def searchResources(self, args):
        region = args.get('region')
        category = args.get('category')
        name = args.get('name')
        dao = ResourceDAO()
        if (len(args) == 2) and region and name:
            resource_list = dao.getResourcesByRegionAndName(region, name)
        elif (len(args) == 2) and name and category:
            resource_list = dao.getResourcesByCategoryAndName(name, category)
        elif (len(args) == 1) and region:
            resource_list = dao.getResourcesByRegion(region)
        elif (len(args) == 1) and name:
            resource_list = dao.getResourcesByName(name)
        elif (len(args) == 1) and category:
            resource_list = dao.getResourcesByCategory(category)
        else:
            return jsonify(Error="Malformed query string"), 400
        if not resource_list:
            return jsonify(Error="Resource Not Found"), 404
        else:
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
        return jsonify(Resource=result_list)

    # ===================================================================================================================
    #                                           get all resources
    # ===================================================================================================================

    def getAllResources(self):
        dao = ResourceDAO()
        resources_list = dao.getAllResources()
        result_list = []
        for row in resources_list:
            result = self.build_resource_dict(row)
            result_list.append(result)
        return jsonify(Resources=result_list)

    # ===================================================================================================================
    #                                           get things by resource id
    # ===================================================================================================================

    def getResourceByID(self, r_id):
        dao = ResourceDAO()
        row = dao.getResourceById(r_id)
        if not row:
            return jsonify(Error="Resource Not Found"), 404
        else:
            result = self.build_resource_dict(row)
        return jsonify(Resource=result)

    # ===================================================================================================================
    #                                           get things by resource name
    # ===================================================================================================================

    def getRequestsByResourceCategory(self, category):
        dao = ResourceDAO()
        if not dao.getRequestsByResourceCategory(category):
            return jsonify(Error='Request Not Found.'), 404
        else:
            request_list = dao.getRequestsByResourceCategory(category)
            result_list = []
            for row in request_list:
                result = self.build_request_dict(row)
                result_list.append(result)
            return jsonify(Requests=result_list)

    def getAnnouncementsByResourceCategory(self, category):
        dao = ResourceDAO()
        if not dao.getAnnouncementsByResourceCategory(category):
            return jsonify(Error='Announcement Not Found.'), 404
        else:
            announcement_list = dao.getAnnouncementsByResourceCategory(category)
            result_list = []
            for row in announcement_list:
                result = self.build_announcement_dict(row)
                result_list.append(result)
            return jsonify(Announcement=result_list)

    def getSuppliersByResourceName(self, name):
        dao = ResourceDAO()
        if not dao.getSupplierByResourceName(name):
            return jsonify(Error='Supplier Not Found.'), 404
        else:
            supplier_list = dao.getSupplierByResourceName(name)
            result_list = []
            for row in supplier_list:
                result = self.build_supplier_dict(row)
                result_list.append(result)
            return jsonify(Supplier=result_list)



    # ===================================================================================================================
    #                                          insert resource
    # ===================================================================================================================

    def insertResource(self, form):
        if form and len(form) == 3:
            r_category = form['r_category']
            r_name = form['r_name']
            r_description = form['r_description']

            if r_category and r_name and r_description:
                dao = ResourceDAO()
                r_id = dao.insert(r_category, r_name, r_description)
                result = {}
                result['r_id'] = r_id
                result['r_category'] = r_category
                result['r_name'] = r_name
                result['r_description'] = r_description

                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")


    # ===================================================================================================================
    #                                          update resource
    # ===================================================================================================================

    def putResourceById(self, form, r_id):
        if form and len(form) == 3:
            r_category = form['r_category']
            r_name = form['r_name']
            r_description = form['r_description']

            if r_category and r_name and r_description and r_id:
                dao = ResourceDAO()
                r_id = dao.put(r_category, r_name, r_description,r_id)
                result = {}
                result["r_id"]= r_id
                result['r_category'] = r_category
                result['r_name'] = r_name
                result['r_description'] = r_description

                return jsonify(Resource=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")


