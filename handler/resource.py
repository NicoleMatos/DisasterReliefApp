from flask import jsonify


class ResourceHandler:

    def resource(self):
        result = [
            {
                'r_id': 1,
                'r_category': 'water',
                'r_name': 'nikini water',
                'r_description': "24 bottles"
            },
            {
                'r_id': 2,
                'r_category': 'clothing',
                'r_name': 't-shirt',
                'r_description': "medium"
            }
        ]
        return result

    # ===================================================================================================================
    #                                          search for resources
    # ===================================================================================================================

    def searchResources(self,args):
        category = args.get('category')
        name = args.get('name')
        result = []
        if category:
            result = self.getResourceByCategory(category)
        elif name:
            result = self.getResourceByName(name)
        if not result:
            return jsonify(Error="Resource Not Found"), 404
        return jsonify(Result = result)
    # ===================================================================================================================
    #                                           get all suppliers
    # ===================================================================================================================
    def getAllResources(self):
        return jsonify(Resources=self.resource())

    # Get Resource by ID

    def getResourceByID(self,r_id):
        resources = self.resource()
        result = list(filter(lambda resource: resource['r_id'] == r_id, resources))
        if len(result) > 0:
            return jsonify(Result=result)
        return jsonify(Error="Resource Not Found"), 404


    # Get Resource by Category
    def getResourceByCategory(self,r_category):
        resources = self.resource()
        result = list(filter(lambda resource: resource['r_category'] == r_category, resources))
        return result


    def getResourceByName(self, r_name):
        resources = self.resource()
        result = list(filter(lambda resource: resource['r_name'] == r_name, resources))
        return result

    # def getResourceByCategoryAndName(self,r_category,r_name):
    #
    #     resources = self.resource()
    #     if (r_category.lower() == 'water' and r_name.lower() == 'nikini water')
    #         return jsonify(resources[0])
    #     else:
    #         return jsonify(resources[1])