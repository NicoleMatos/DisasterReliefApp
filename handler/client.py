from flask import jsonify
from handler.supplier import SupplierHandler


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

            },

            {
                'c_id': 2,
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
        return users

    def suppliersDictionary(self):
        suppliers = [

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
                'req_id': 0,
                'req_qty': 12,
                'req_date' : 1/12/17
            },

            {
                'req_id': 1,
                'req_qty': 12,
                'req_date' : 1/12/17
            },

            {
                'req_id': 2,
                'req_qty': 12,
                'req_date' : 1/12/17
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

    # ===================================================================================================================
    #                                          search for clients
    # ===================================================================================================================

    def searchClients(self, args):
        name = args.get('name')
        lastname = args.get('lastname')
        result = []
        if name and lastname:
            result = self.getClientByNameAndLastName(name, lastname)
        elif name:
            result = self.getClientByName(name)
        elif lastname:
           result = self.getClientByLastName(lastname)
        if len(result) == 0:
            return jsonify(Error="Client Not Found"), 404
        return jsonify(Result=result)


    #===================================================================================================================
    #                                          Get all Clients
    #===================================================================================================================

    def getAllClients(self):
        return jsonify(Clients = self.searchClientsInUsers())

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getTransactionsByClientID(self,u_id):
        clients = self.searchClientsInUsers()
        result = list(filter(lambda client: client['u_id'] == u_id, clients))
        if len(result)== 0:
            return jsonify(Error="Transaction Not Found"), 404
        return jsonify(result)

    def getRequestsByClientID(self,u_id):
        clients = self.searchClientsInUsers()
        result = list(filter(lambda client: client['u_id'] == u_id, clients))
        if len(result) == 0:
            return jsonify(Error="Request Not Found"), 404
        return jsonify(result)

    def getCreditCardsByClientID(self,u_id):
        clients = self.searchClientsInUsers()
        result = list(filter(lambda client: client['u_id'] == u_id, clients))
        if len(result) == 0:
            return jsonify(Error="Credit Card Not Found"), 404
        return jsonify(result)

    def getSuppliersByClientID(self,u_id):
        clients = self.searchClientsInUsers()
        result = list(filter(lambda client: client['u_id'] == u_id, clients))
        if len(result) == 0:
            return jsonify(Error="Supplier Not Found"), 404
        return jsonify(result)


    def getClientByID(self, u_id):
        clients = self.searchClientsInUsers()
        result = list(filter(lambda client: client['u_id'] == u_id, clients))
        if len(result) == 0:
            return jsonify(Error="Client Not Found"), 404
        return jsonify(result)


    # ===================================================================================================================
    #                                           get clients by Name
    # ===================================================================================================================

    def getClientByName(self, c_name):
        clients = self.searchClientsInUsers()
        result = list(filter(lambda client: client['u_name'] == c_name, clients))
        return result

    # ===================================================================================================================
    #                                           get client by Last Name
    # ===================================================================================================================

    def getClientByLastName(self, c_lastname):
        clients = self.searchClientsInUsers()
        result = list(filter(lambda client: client['u_lastName'] == c_lastname, clients))
        return result

    # ===================================================================================================================
    #                                           get client by Name And Last Name
    # ===================================================================================================================

    def getClientByNameAndLastName(self, name, last_name):
        clients = self.searchClientsInUsers()
        result = list(filter(lambda client: client['u_name'] == name, clients))
        result2 = list(filter(lambda client: client['u_lastName'] == last_name, result))
        return result2

    # ===================================================================================================================
    #                                           method to hard-wire information
    # ===================================================================================================================

    def searchClientsInUsers(self):
        clientsDic = self.clientsDictionary()
        usersDic = self.usersDictionary()
        result = []
        for i in clientsDic:
            for j in usersDic:
                if i['u_id'] == j['u_id']:
                    result.append(j)
        return result
