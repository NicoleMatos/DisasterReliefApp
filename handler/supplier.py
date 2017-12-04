from flask import jsonify


class SupplierHandler:

    def suppliers(self):
        result = [
            {
                's_id': 0,
                'u_id': 0,
                'bank_account': 123456788
            },
            {
                's_id': 1,
                'u_id': 1,
                'bank_account': 123456789
            },
            {
                's_id': 2,
                'u_id': 2,
                'bank_account': 987654321
            }
        ]
        return result

    def users(self):
        users = [
            {
                'u_id': 1,
                'u_email': 'jose.rivera@gmail.com',
                'u_password': '1234!@',
                'u_phone': '7872134567',
                'u_name': 'Jose',
                'u_lastName': 'Rivera',
                'u_address': 'Carr.123 km 0.8',
                'u_location': 'Andalurge',
                'u_age': 24

            },

            {
                'u_id': 2,
                'u_email': 'orla.torres@gmail.com',
                'u_password': '1234!@',
                'u_phone': '7872134567',
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
                'u_phone': '7872134567',
                'u_name': 'Nicole',
                'u_lastName': 'Matos',
                'u_address': 'Carr.123 km 0.8',
                'u_location': 'Andalurge',
                'u_age': 30

            }
        ]
        return users


    def searchSuppliers(self, args):
        name = args.get('name')
        lastname = args.get('lastname')
        if name and lastname:
            self.getSupplierByNameAndLastName(name, lastname)
        elif name:
            self.getSupplierByName(self, name)
        elif lastname:
            self.getSupplierByLastName(self, lastname)
        return jsonify(self.suppliers())

    #===================================================================================================================
    #                                           get all suppliers
    #===================================================================================================================

    def getAllSuppliers(self):
        return jsonify(Suppliers=self.searchSuppliersInUsers())

    #===================================================================================================================
    #                                           get things by id
    #===================================================================================================================

    def getSupplierByID(self, u_id):
        suppliers = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_id'] == u_id, suppliers))
        return jsonify(result)

    def getClientsByUserID(self, u_id):
        suppliers = self.getSupplierByID(self,u_id)
        return suppliers

    def getTransactionsByUserID(self, u_id):
        suppliers = self.getSupplierByID(self, u_id)
        return suppliers

    def getAnnouncementsByUserID(self, u_id):
        suppliers = self.getSupplierByID(self, u_id)
        return suppliers

    def getResourcesByUserID(self, u_id):
        suppliers = self.getSupplierByID(self, u_id)
        return suppliers

    # ===================================================================================================================
    #                                           get things by Name
    # ===================================================================================================================

    def getSupplierByName(self, name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_name'] == name, users))
        return jsonify(result)

    def getClientsByName(self, name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_name'] == name, users))
        return jsonify(result)

    def getTransactionsByName(self, name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_name'] == name, users))
        return jsonify(result)

    def getAnnouncementsByName(self, name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_name'] == name, users))
        return jsonify(result)

    # ===================================================================================================================
    #                                           get things by Last Name
    # ===================================================================================================================

    def getSupplierByLastName(self, name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_lastName'] == name, users))
        return jsonify(result)

    def getClientsByLastName(self, name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_lastName'] == name, users))
        return jsonify(result)

    def getTransactionsByLastName(self, name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_lastName'] == name, users))
        return jsonify(result)

    def getAnnouncementsByLastName(self, name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_lastName'] == name, users))
        return jsonify(result)

    # ===================================================================================================================
    #                                           get things by Name And Last Name
    # ===================================================================================================================

    def getSupplierByNameAndLastName(self, name, last_name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda f_name: f_name['u_name'] == name, users))
        result2 = list(filter(lambda l_name: l_name['u_lastName'] == last_name, result))
        return jsonify(result2)

    def getClientsByNameAndLastName(self, name, last_name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda f_name: f_name['u_name'] == name, users))
        result2 = list(filter(lambda l_name: l_name['u_lastName'] == last_name, result))
        return jsonify(result2)

    def getTransactionsByNameAndLastName(self, name, last_name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda f_name: f_name['u_name'] == name, users))
        result2 = list(filter(lambda l_name: l_name['u_lastName'] == last_name, result))
        return jsonify(result2)

    def getAnnouncementsByNameAndLastName(self, name, last_name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda f_name: f_name['u_name'] == name, users))
        result2 = list(filter(lambda l_name: l_name['u_lastName'] == last_name, result))
        return jsonify(result2)


    #===================================================================================================================
    #                                           method to hard-wire information
    #===================================================================================================================

    # def searchSuppliersInUsers(self):
    #     suppliersDic = self.suppliers()
    #     usersDic = self.users()
    #     result = []
    #     for i in suppliersDic:
    #         for j in usersDic:
    #             if (i['u_id'] == j['u_id']):
    #                 result.append(j)
    #     return result