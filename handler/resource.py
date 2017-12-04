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



    def getAllResources(self):
        return jsonify(Resources=self.resource())

    def getResourceByRid(self,r_id):

        resources = self.resource()
        if(r_id == 0):
            return jsonify(resources[0])
        else:
            return jsonify(resources[1])


    def getResourceByCategory(self,r_category):

        resources = self.resource()
        if(r_category.lower() == 'water'):
            return jsonify(resources[0])
        else:
            return jsonify(resources[1])

    def getResourceByName(self, r_name):

        resources = self.resource()
        if (r_name.lower() == 'nikini water'):
            return jsonify(resources[0])
        else:
            return jsonify(resources[1])


    def searchResource(self,args):
        category = args.get("r_category")
        name = args.get("r_name")
        resourcesList = []

        if (len(args) == 2) and category and name:
            resourcesList = self.getResourceByCategoryAndName(category, name)
        elif (len(args) == 1) and category:
            resourcesList = self.getResourceByCategory(category)
        elif (len(args) == 1) and name:
            resourcesList = self.getResourceByName(name)
        else:
            return jsonify(Error="Malformed query string"), 400

        return jsonify(resourcesList)


    # def getResourceByCategoryAndName(self,r_category,r_name):
    #
    #     resources = self.resource()
    #     if (r_category.lower() == 'water' and r_name.lower() == 'nikini water')
    #         return jsonify(resources[0])
    #     else:
    #         return jsonify(resources[1])