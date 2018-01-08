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

    # ===================================================================================================================
    #                                        search for resources
    # ===================================================================================================================

    def searchResources(self, args):
        category = args.get('category')
        name = args.get('name')
        dao = ResourceDAO()
        if (len(args) == 2) and category and name:
            resource_list = dao.getResourcesByCategoryAndName(category, name)
        elif (len(args) == 1) and category:
            resource_list = dao.getResourcesByCategory(category)
        elif (len(args) == 1) and name:
            resource_list = dao.getResourcesByName(name)
        else:
            return jsonify(Error="Malformed query string"), 400
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
