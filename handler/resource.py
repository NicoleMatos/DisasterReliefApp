from flask import jsonify


class ResourceHandler:

    def resource(self):
        result = [
            {
                'r_id': 1,
                'r_category': 'water',
                'r_name': 'nikini',
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

    def searchResources(self, args):
        category = args.get('category')
        name = args.get('name')
        result = []
        if category and name:
            result = self.getResourceByCategoryAndName(category, name)
        elif category:
            result = self.getResourceByCategory(category)
        elif name:
            result = self.getResourceByName(name)
        if len(result) == 0:
            return jsonify(Error="Resource Not Found"), 404
        return jsonify(Result=result)

    # ===================================================================================================================
    #                                           get all resources
    # ===================================================================================================================

    def getAllResources(self):
        return jsonify(Resources=self.resource())

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getResourceByID(self, r_id):
        resources = self.resource()
        result = list(filter(lambda resource: resource['r_id'] == r_id, resources))
        if len(result) > 0:
            return jsonify(Result=result)
        return jsonify(Error="Resource Not Found"), 404

    # ===================================================================================================================
    #                                         get resources by Category
    # ===================================================================================================================

    def getResourceByCategory(self, r_category):
        resources = self.resource()
        result = list(filter(lambda resource: resource['r_category'] == r_category, resources))
        return result

    # ===================================================================================================================
    #                                           get resources by Name
    # ===================================================================================================================

    def getResourceByName(self, r_name):
        resources = self.resource()
        result = list(filter(lambda resource: resource['r_name'] == r_name, resources))
        return result

    # ===================================================================================================================
    #                                   get resources by Category And Name
    # ===================================================================================================================

    def getResourceByCategoryAndName(self, r_category, r_name):
        resources = self.resource()
        result = list(filter(lambda resource: resource['r_category'] == r_category, resources))
        result2 = list(filter(lambda resource: resource['r_name'] == r_name, result))
        return result2
