from flask import jsonify

class TransactionHandler:

    def transaction(self):
        result = [
            {
                't_id': 1,
                's_id': 1,
                'c_id': 1,
                't_price': 5.00,
                't_date': '02/13/2017',
                't_qty': 4
            },
            {
                't_id': 2,
                's_id': 2,
                'c_id': 2,
                't_price': 10.00,
                't_date': '02/15/2017',
                't_qty': 2
            }
        ]
        return result

    # ===================================================================================================================
    #                                          search for transactions
    # ===================================================================================================================

    def searchTransactions(self, args):
        date = args.get('date')
        supplier = args.get('supplier')
        client = args.get('client')
        if date:
            self.getTransactionsByDate(date)
        elif supplier:
            self.getTransactionsBySupplier(supplier)
        elif client:
            self.getTransactionsByClient(client)
        return jsonify(self.transaction())

    # ===================================================================================================================
    #                                           get all transactions
    # ===================================================================================================================

    def getAllTransactions(self):
        return jsonify(Transactions=self.transaction())

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getTransactionByID(self, t_id):
        result = list(filter(lambda transaction: transaction['t_id'] == t_id, self.transaction()))
        return jsonify(result)

    # ===================================================================================================================
    #                                           get transactions by date
    # ===================================================================================================================

    def getTransactionsByDate(self, date):
        result = list(filter(lambda transaction: transaction['t_date'] == date, self.transaction()))
        return result

    # ===================================================================================================================
    #                                         get transactions by supplier
    # ===================================================================================================================

    def getTransactionsBySupplier(self, supplier):
        result = list(filter(lambda transaction: transaction['s_id'] == supplier, self.transaction()))
        return result

    # ===================================================================================================================
    #                                           get transactions by client
    # ===================================================================================================================

    def getTransactionsByClient(self, client):
        result = list(filter(lambda transaction: transaction['c_id'] == client, self.transaction()))
        return result
