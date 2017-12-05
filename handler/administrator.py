from flask import jsonify

class AdministratorHandler:

    def administrator(self):
        result = [
            {
                'a_id': 0
            },
            {
                'a_id': 1
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
        if(len(result)== 0):
            return jsonify(Error="Client Not Found"), 404
        return jsonify(Result = result)

    # ===================================================================================================================
    #                                           get all suppliers
    # ===================================================================================================================


    def getAllAdministrators(self):
        return jsonify(Administrators=self.searchAdministratosInUsers())

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

    def getAdministratorByNameAndLastName(self, name, lastname):
        admi = self.searchAdministratosInUsers()
        result = list(filter(lambda f_name: f_name['u_name'] == name, admi))
        result2 = list(filter(lambda l_name: l_name['u_lastName'] == lastname, result))
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
                if (i['u_id'] == j['u_id']):
                    result.append(j)
        return result
