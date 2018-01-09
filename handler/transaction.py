from flask import jsonify
from dao.transaction import TransactionDAO

class TransactionHandler:

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

    # ===================================================================================================================
    #                                           get all transactions
    # ===================================================================================================================

    def getAllTransactions(self):
        dao = TransactionDAO()
        transactions_list = dao.getAllTransactions()
        result_list = []
        for row in transactions_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transactions=result_list)

    # ===================================================================================================================
    #                                          search for transactions
    # ===================================================================================================================

    def searchTransactions(self, args):
        date = args.get('date')
        supplier = args.get('supplier')
        client = args.get('client')
        dao = TransactionDAO()
        if (len(args) == 3) and date and supplier and client:
            transaction_list = dao.getTransactionsByDateAndSupplierAndClient(date, supplier, client)
        elif (len(args) == 2) and date and supplier:
            transaction_list = dao.getTransactionsByDateAndSupplier(date, supplier)
        elif (len(args) == 2) and date and client:
            transaction_list = dao.getTransactionsByDateAndClient(date, client)
        elif (len(args) == 2) and supplier and client:
            transaction_list = dao.getTransactionsBySupplierAndClient(supplier, client)
        elif (len(args) == 1) and date:
            transaction_list = dao.getTransactionsByDate(date)
        elif (len(args) == 1) and supplier:
            transaction_list = dao.getTransactionsBySupplier(supplier)
        elif (len(args) == 1) and client:
            transaction_list = dao.getTransactionsByClient(client)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in transaction_list:
            result = self.build_transaction_dict(row)
            result_list.append(result)
        return jsonify(Transaction=result_list)

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getTransactionByID(self, t_id):
        dao = TransactionDAO()
        row = dao.getTransactionById(t_id)
        if not row:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            result = self.build_transaction_dict(row)
        return jsonify(Transaction=result)
