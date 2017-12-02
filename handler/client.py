from flask import jsonify


# Class that handles the Consumer
class ClientHandler:

    def clientsDictionary(self):
        clients = [

            {
                'c_id': 0,
                'u_id': 2

            },

            {
                'c_id': 1,
                'u_id': 3

            }

        ]
        return clients


    def usersDictionary(self):
        users = [
            {
                'u_id': 1,
                'u_email': 'jose.rivera@gmail.com',
                'u_password': '1234!@',
                'u_phone': '7872134567',
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

    def suppliersDictionary(self):
        suppliers = [

            {
                's_id': 0,
                'bank_account': 123456789
            },

            {
                's_id': 1,
                'bank_account': 234567890
            },

            {
                's_id': 2,
                'bank_account': 345678901
            }

        ]
        return suppliers

    def transactionsDictionary(self):
        transactions = [

            {
                't_id': 0,
                't_price' : 1.00,
                't_date' : '1/enero/17',
                't_qty' : 1
            },

            {
                't_id': 1,
                't_price': 2.00,
                't_date': '4/enero/17',
                't_qty': 2
            },

            {
                't_id': 2,
                't_price': 50.00,
                't_date': '1/febrero/17',
                't_qty': 4
            },

            {
                't_id': 3,
                't_price': 100.00,
                't_date': '1/enero/18',
                't_qty': 15
            },


        ]
        return transactions


    def requestsDictionary(self):
        requests = [

            {
                'r_id': 0,
                'r_qty': 12,
                'r_date' : 1/12/17
            },

            {
                'r_id': 1,
                'r_qty': 12,
                'r_date' : 1/12/17
            },

            {
                'r_id': 2,
                'r_qty': 12,
                'r_date' : 1/12/17
            }

        ]
        return requests


    def creditCardsDictionary(self):
        cCards = [

            {
                'cc_id': 0,
                'cc_name': 'Nicole Matos',
                'cc_number': 12345678,
                'cc_exp_date' : 1/12/17
            },

            {
                'cc_id': 1,
                'cc_name': 'Gilissa Matos',
                'cc_number': 45678001,
                'cc_exp_date' : 1/12/17
            },

            {
                'cc_id': 2,
                'cc_name': 'Orlando Perez',
                'cc_number': 23456788,
                'cc_exp_date' : 1/12/18
            }

        ]
        return cCards


    def searchClientsInUsers(self):

        clientDic = self.clientsDictionary()
        usersDic = self.usersDictionary()
        result =[]

        for i in clientDic:
            for j in usersDic:
                if (i['u_id'] == j['u_id']):
                    result.append(j)
        return result

    def getAllClients(self):
        return jsonify({'result': self.searchClientsInUsers()})

    def getClientById(self, c_id):
        result = self.searchClientsInUsers()
        if (c_id >= 0 and c_id <=10):

            return jsonify(result[0])
        else:
            return jsonify(Error = "Client Not Found"), 404


    def getSuppliersByClientId(self,c_id):
        result = self.suppliersDictionary()
        if (c_id >= 0 and c_id <= 10):

            return jsonify(result[0])
        else:
            return jsonify(Error="Client Not Found"), 404

    def getTransactionsByClientId(self,c_id):
        result = self.transactionsDictionary()
        if (c_id >= 0 and c_id <= 10):

            return jsonify(result[0])
        else:
            return jsonify(Error="Client Not Found"), 404


    def getRequestsByClientId(self,c_id):
        result = self.requestsDictionary()
        if (c_id >= 0 and c_id <= 10):

            return jsonify(result[0])
        else:
            return jsonify(Error="Client Not Found"), 404
    def getCreditCardsByClientId(self,c_id):
        result = self.creditCardsDictionary()
        if (c_id >= 0 and c_id <= 10):

            return jsonify(result[0])
        else:
            return jsonify(Error="Client Not Found"), 404



    #===================================================================================================================
    #                                           get things by Name
    #===================================================================================================================

    def getClientByName(self, c_name):
        result = self.searchClientsInUsers()
        return jsonify(result[0])


    def getSuppliersByClientName(self, c_name):
        result = self.suppliersDictionary()
        return jsonify(result[0])


    def getTransactionsByClientName(self, c_name):
        result = self.transactionsDictionary()
        return jsonify(result[0])


    def getRequestsByClientName(self, c_name):
        result = self.requestsDictionary()
        return jsonify(result[0])


    def getCreditCardsByClientName(self, c_name):
        result = self.creditCardsDictionary()
        return jsonify(result[0])

#========================






