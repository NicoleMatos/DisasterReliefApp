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
        transaction_list = dao.getAllTransactions()
        if not transaction_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
            result_list = []
            for row in transaction_list:
                result = self.build_transaction_dict(row)
                result_list.append(result)
        return jsonify(Transaction=result_list)

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
        if not transaction_list:
            return jsonify(Error="Transaction Not Found"), 404
        else:
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

# ===================================================================================================================
#                                          insert transaction
# ===================================================================================================================

    def insertTransaction(self, form):
        if form and len(form) == 6:
            s_id = form['s_id']
            c_id = form['c_id']
            r_id = form['r_id']
            t_price = form['t_price']
            t_date = form['t_date']
            t_qty = form['t_qty']
            if s_id and c_id and r_id and t_price and t_date and t_qty:
                dao = TransactionDAO()
                t_id = dao.insert(s_id, c_id, r_id, t_price, t_date, t_qty)
                result = {}
                result["t_id"] = t_id
                result["s_id"] = s_id
                result["c_id"] = c_id
                result["r_id"] = r_id
                result["t_price"] = t_price
                result["t_date"] = t_date
                result["t_qty"] = t_qty
                return jsonify(Transaction=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

# ===================================================================================================================
#                                          put transaction
# ===================================================================================================================

    def putTransactionByID(self, form, t_id):
        if form and len(form) == 6:
            s_id = form['s_id']
            c_id = form['c_id']
            r_id = form['r_id']
            t_price = form['t_price']
            t_date = form['t_date']
            t_qty = form['t_qty']
            if s_id and c_id and r_id and t_price and t_date and t_qty and t_id:
                dao = TransactionDAO()
                t_id = dao.put(s_id, c_id, r_id, t_price, t_date, t_qty, t_id)
                result = {}
                result["t_id"] = t_id
                result["s_id"] = s_id
                result["c_id"] = c_id
                result["r_id"] = r_id
                result["t_price"] = t_price
                result["t_date"] = t_date
                result["t_qty"] = t_qty
                return jsonify(Transaction=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

# ===================================================================================================================
#                                          delete transaction
# ===================================================================================================================

    def deleteTransactionByID(self, t_id):
        dao = TransactionDAO()
        if not dao.getTransactionById(t_id):
            return jsonify(Error="Transaction not found."), 404
        else:
            dao.delete(t_id)
            return jsonify(DeleteStatus="OK"), 200
