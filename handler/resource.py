from flask import jsonify

class ResourceHandler:

    def resource(self):
        result = [
            {
                'r_id': 1,
                'r_category': 'Water',
                'r_name': 'Nikini water',
                'r_description': "24 bottles"
            },
            {
                'r_id': 2,
                'r_category': 'Clothing',
                'r_name': 't-shirt',
                'r_description': "medium"
            }
        ]
        return result

    def getAllResourses(self):
        return jsonify(Resources=self.resource())