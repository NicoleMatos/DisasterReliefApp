from flask import jsonify

class AdministratorHandler:

    def administrator(self):
        result = [
            {
                'ad_id': 0,
                'u_id': 0
            },
            {
                'ad_id': 1,
                'u_id':1
            }
        ]
        return result

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
    #                                          search for administrators
    # ===================================================================================================================

    def searchAdministrator(self, args):
        name = args.get('name')
        lastname = args.get('lastname')
        result = []
        if name and lastname:
            result = self.getAdministratorByNameAndLastName(name, lastname)
        elif name:
            result = self.getAdministratorByName(self, name)
        elif lastname:
            result = self.getAdministratorByLastName(self, lastname)
        if len(result) == 0:
            return jsonify(Error="Administrator Not Found"), 404
        return jsonify(Result=result)

    # ===================================================================================================================
    #                                           get all administrators
    # ===================================================================================================================


    def getAllAdministrators(self):
        return jsonify(Administrators=self.searchAdministratosInUsers())



    # ===================================================================================================================
    #                                           get administrator by ID
    # ===================================================================================================================


    def getAdministratorByID(self,ad_id):
        administrators = self.searchAdministratosInUsers()
        result = list(filter(lambda admi: admi['ad_id'] == ad_id, administrators))
        if len(result) > 0:
            return jsonify(Result=result)
        return jsonify(Error="Administrator Not Found"), 404


    # ===================================================================================================================
    #                                           get administrator by Name
    # ===================================================================================================================

    def getAdministratorByName(self, name):
        admi = self.searchAdministratosInUsers()
        result = list(filter(lambda administrator: administrator['u_name'] == name, admi))
        return result

    # ===================================================================================================================
    #                                           get administrator by Last Name
    # ===================================================================================================================

    def getAdministratorByLastName(self, lastname):
        admi = self.searchAdministratosInUsers()
        result = list(filter(lambda administrator: administrator['u_name'] == lastname, admi))
        return result

    # ===================================================================================================================
    #                                     get administrator by Name and Last Name
    # ===================================================================================================================

    def getAdministratorByNameAndLastName(self, name, lastname):
        admi = self.searchAdministratosInUsers()
        result = list(filter(lambda admin: admin['u_name'] == name, admi))
        result2 = list(filter(lambda admin: admin['u_lastName'] == lastname, result))
        return result2

    # ===================================================================================================================
    #                                           method to hard-wire information
    # ===================================================================================================================

    def searchAdministratosInUsers(self):
        admiDic = self.administrator()
        usersDic = self.users()
        result = []
        for i in admiDic:
            for j in usersDic:
                if i['u_id'] == j['u_id']:
                    result.append(j)
        return result
