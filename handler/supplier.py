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

    def searchSuppliersInUsers(self):
        suppliersDic = self.suppliers()
        usersDic = self.users()
        result = []
        for i in suppliersDic:
            for j in usersDic:
                if (i['u_id'] == j['u_id']):
                    result.append(j)
        return result

    def getAllSuppliers(self):
        return jsonify(Suppliers=self.searchSuppliersInUsers())

    def getSupplierByID(self, s_id):
        suppliers = self.suppliers()
        result = list(filter(lambda supplier: supplier['s_id'] == s_id, suppliers))
        return jsonify(result)

    def getSupplierByName(self, name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_name'] == name, users))
        return jsonify(result)

    def getSupplierByName(self, name):
        users = self.searchSuppliersInUsers()
        result = list(filter(lambda supplier: supplier['u_name'] == name, users))
        return jsonify(result)