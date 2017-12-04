from flask import jsonify

class TransactionHandler:

    def transaction(self):
        result = [
            {
                't_id': 1,
                't_price': 5.00,
                't_date': '02/13/2017',
                't_qty': 4
            },
            {
                't_id': 2,
                't_price': 10.00,
                't_date': '02/15/2017',
                't_qty': 2
            }
        ]
        return result

    def getAllTransactions(self):
        return jsonify(Transactions=self.transaction())

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

    def getTransactionsByDate(self, date):
        return jsonify(self.transaction())

    def getTransactionsBySupplier(self, date):
        return jsonify(self.transaction())

    def getTransactionsByClient(self, date):
        return jsonify(self.transaction())
