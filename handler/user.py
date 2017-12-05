from flask import jsonify

class UserHandler:

    def user(self):
        result = [
            {
                'u_id': 1,
                'u_email': 'jose.rivera@gmail.com',
                'u_password': '1234!@',
                'u_name': 'Jose',
                'u_lastName':'Rivera',
                'u_address': 'Carr.123 km 0.8',
                'u_location' : 'Andalurge',
                'u_age' : 24

            },

            {
                'u_id': 2,
                'u_email': 'orla.torres@gmail.com',
                'u_password': '1234!@',
                'u_name': 'Orlando',
                'u_lastName': 'Torres',
                'u_address': 'Carr.123 km 0.8',
                'u_location': 'Andalurge',
                'u_age': 12

            },

            {
                'u_id': 3,
                'u_email': 'nico.matos@gmail.com',
                'u_password': '1234!@',
                'u_name': 'Nicole',
                'u_lastName': 'Matos',
                'u_address': 'Carr.123 km 0.8',
                'u_location': 'Andalurge',
                'u_age': 30

            }
        ]
        return result


    # ===================================================================================================================
    #                                           search Users
    # ===================================================================================================================

    def searchUsers(self, args):
        name = args.get('name')
        lastname = args.get('lastname')
        location = args.get('location')
        result = []
        if name and lastname:
            result = self.getUserByNameAndLastName(name, lastname)
        elif name:
            result = self.getUserByName(self, name)
        elif lastname:
            result = self.getUserByLastName(self, lastname)
        elif location:
            result = self.getUserByLocation(location)
        if (len(result) == 0):
            return jsonify(Error="User Not Found"), 404
        return jsonify(Result = result)


    # ===================================================================================================================
    #                                           get all Users
    # ===================================================================================================================
    def getAllUsers(self):
        return jsonify(Users=self.user())

    # ===================================================================================================================
    #                                           get Users by ID
    # ===================================================================================================================

    def getCCardByID(self, u_id):
        users = self.user()
        result = list(filter(lambda user: user['u_id'] == u_id, users))
        if len(result) > 0:
            return jsonify(Result=result)
        return jsonify(Error="User Not Found"), 404

    # ===================================================================================================================
    #                                           get users by Name
    # ===================================================================================================================

    def getUserByName(self, name):
        users = self.user()
        result = list(filter(lambda user: user['u_name'] == name, users))
        return result

    # ===================================================================================================================
    #                                           get users by Last Name
    # ===================================================================================================================

    def getUserByLastName(self, lastname):
        users = self.user()
        result = list(filter(lambda user: user['u_lastName'] == lastname, users))
        return result

    # ===================================================================================================================
    #                                           get users by Name and Last Name
    # ===================================================================================================================

    def getUserByNameAndLastName(self, name, lastname):
        users = self.user()
        result = list(filter(lambda user: user['u_name'] == name, users))
        result2 = list(filter(lambda user: user['u_lastName'] == lastname, result))
        return result2

    # ===================================================================================================================
    #                                           get users by Location
    # ===================================================================================================================

    def getUserByLocation(self,location):
        users = self.user()
        result = list(filter(lambda user: user['u_location'] == location, users))
        return result
