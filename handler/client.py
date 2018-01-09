from flask import jsonify
from dao.client import ClientDAO


# Class that handles the Client
class ClientHandler:

    def build_client_dict(self,row):
        result = {}
        result['c_id'] = row[1]
        result['u_id'] = row[0]
        result['u_email'] = row[2]
        result['u_password'] = row[3]
        result['u_name'] = row[4]
        result['u_lastname'] = row[5]
        result['u_region'] = row[6]
        result['u_age'] = row[7]
        return result

    def build_transaction_dict(self, row):
        result = {}
        result['t_id'] = row[0]
        result['s_id'] = row[1]
        result['c_id'] = row[2]
        result['r_id'] = row[3]
        result['t_price'] = row[4]
        result['t_date'] = row[5]
        result['t_qty'] = row[6]
        return result

    def build_request_dict(self, row):
        result = {}
        result['req_id'] = row[0]
        result['c_id'] = row[1]
        result['r_id'] = row[2]
        result['req_qty'] = row[3]
        result['req_date'] = row[4]
        return result

    def build_credit_Card_dict(self, row):
        result = {}
        result['cc_id'] = row[0]
        result['c_id'] = row[1]
        result['cc_name'] = row[2]
        result['cc_lastname'] = row[3]
        result['cc_number'] = row[4]
        result['cc_exp_date'] = row[5]
        return result

    def build_supplier_dict(self, row):
        result = {}
        result['s_id'] = row[0]
        result['u_id'] = row[1]
        result['bank_account'] = row[2]
        return result

    # ===================================================================================================================
    #                                          search for clients
    # ===================================================================================================================

    def searchClients(self, args):
        name = args.get("name")
        lastname = args.get("lastname")
        dao = ClientDAO()
        clients_list = []
        if (len(args) == 2) and name and lastname:
            clients_list = dao.getClientByNameAndLastName(name,lastname)
        elif (len(args) == 1) and name:
            clients_list = dao.getClientByName(name)
        elif (len(args) == 1) and lastname:
            clients_list = dao.getClientByLastName(lastname)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in clients_list:
            result = self.build_client_dict(row)
            result_list.append(result)

        return jsonify(Client=result_list)


    #===================================================================================================================
    #                                          Get all Clients
    #===================================================================================================================

    def getAllClients(self):
        dao = ClientDAO()
        clients_list = dao.getAllClients()
        result_list = []
        for row in clients_list:
            result = self.build_client_dict(row)
            result_list.append(result)
        return jsonify(Clients=result_list)

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getTransactionsByClientID(self,c_id):
        dao = ClientDAO()
        if not dao.getClientById(c_id):
            return jsonify(Error="Client Not Found"), 404
        transactions_list = dao.getTransactionsByClientID(c_id)
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)

        return jsonify(Transactions=result_list)

    def getRequestsByClientID(self,c_id):
        dao = ClientDAO()
        if not dao.getClientById(c_id):
            return jsonify(Error="Client Not Found"), 404
        requests_list = dao.getRequestsByClientID(c_id)
        result_list = []
        for row in requests_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    def getCreditCardsByClientID(self,c_id):
        dao = ClientDAO()
        if not dao.getClientById(c_id):
            return jsonify(Error="Client Not Found"), 404
        cards_list = dao.getCreditCardsByClientID(c_id)
        result_list = []
        for row in cards_list:
            result = self.build_credit_Card_dict(row)
            result_list.append(result)
        return jsonify(Cards=result_list)


    def getSuppliersByClientID(self,c_id):
        dao = ClientDAO()
        if not dao.getClientById(c_id):
            return jsonify(Error="Client Not Found"), 404
        suppliers_list = dao.getSuppliersByClientID(c_id)
        result_list = []
        for row in suppliers_list:
            result = self.build_supplier_dict(row)
            result_list.append(result)
        return jsonify(Suppliers=result_list)

    def getClientByID(self, c_id):
        dao = ClientDAO()
        row = dao.getClientById(c_id)
        if not row:
            return jsonify(Error="Client Not Found"), 404
        else:
            result = self.build_client_dict(row)
        return jsonify(Client=result)


    # ===================================================================================================================
    #                                           get clients by Name
    # ===================================================================================================================

    def getClientByName(self, u_name):
        dao = ClientDAO()
        row = dao.getClientByName(u_name)
        if not row:
            return jsonify(Error="Client Not Found"), 404
        else:
            client = self.build_client_dict(row)

        return jsonify(Client=client)


    # ===================================================================================================================
    #                                           get client by Last Name
    # ===================================================================================================================

    def getClientByLastName(self, u_lastname):
        dao = ClientDAO()
        row = dao.getClientByName(u_lastname)
        if not row:
            return jsonify(Error="Client Not Found"), 404
        else:
            client = self.build_client_dict(row)

        return jsonify(Client=client)

    # ===================================================================================================================
    #                                           get client by Name And Last Name
    # ===================================================================================================================

    def getClientByNameAndLastName(self, u_name, u_last_name):
        dao = ClientDAO()
        row = dao.getClientByNameAndLastName(u_name,u_last_name)
        if not row:
            return jsonify(Error="Client Not Found"), 404
        else:
            client = self.build_client_dict(row)

        return jsonify(Client=client)

