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
        return users

    # ===================================================================================================================
    #                                          search for suppliers
    # ===================================================================================================================

    def searchSuppliers(self, args):
        name = args.get('name')
        lastname = args.get('lastname')
        result = []
        if name and lastname:
            result = self.getSupplierByNameAndLastName(name, lastname)
        elif name:
            result = self.getSupplierByName(name)
        elif lastname:
            result = self.getSupplierByLastName(lastname)
        if len(result) == 0:
            return jsonify(Error="Supplier Not Found"), 404
        return jsonify(Result=result)

    # ===================================================================================================================
    #                                           get all suppliers
    # ===================================================================================================================

    def getAllSuppliers(self):
        return jsonify(Suppliers=self.searchSuppliersInUsers())

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getSupplierByID(self, u_id):
        suppliers = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_id'] == u_id, suppliers))
        if len(result) == 0:
            return jsonify(Error="Supplier Not Found"), 404
        return jsonify(result)

    def getAnnouncementsBySupplierID(self, u_id):
        suppliers = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_id'] == u_id, suppliers))
        if len(result) == 0:
            return jsonify(Error="Announcement Not Found"), 404
        return jsonify(result)

    def getTransactionsBySupplierID(self, u_id):
        suppliers = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_id'] == u_id, suppliers))
        if len(result) == 0:
            return jsonify(Error="Transaction Not Found"), 404
        return jsonify(result)

    # ===================================================================================================================
    #                                           get suppliers by Name
    # ===================================================================================================================

    def getSupplierByName(self, name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_name'] == name, users))
        return result

    # ===================================================================================================================
    #                                           get suppliers by Last Name
    # ===================================================================================================================

    def getSupplierByLastName(self, name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_lastName'] == name, users))
        return result

    # ===================================================================================================================
    #                                           get suppliers by Name And Last Name
    # ===================================================================================================================

    def getSupplierByNameAndLastName(self, name, last_name):
        suppliers = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_name'] == name, suppliers))
        result2 = list(filter(lambda supplier: supplier['u_lastName'] == last_name, result))
        return result2

    # ===================================================================================================================
    #                                           method to hard-wire information
    # ===================================================================================================================

    def searchSuppliersInUsers(self):
        suppliersDic = self.suppliers()
        usersDic = self.users()
        result = []
        for i in suppliersDic:
            for j in usersDic:
                if i['u_id'] == j['u_id']:
                    result.append(j)
        return result
