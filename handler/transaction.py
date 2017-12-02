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
