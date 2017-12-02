from flask import jsonify


class SupplierHandler:

    def transaction(self):
        result = [
            {
                'p_id': 1,
                'p_price': 5.00,
                'p_date': '02/13/2017',
                'p_qty': 4
            },
            {
                'p_id': 2,
                'p_price': 10.00,
                'p_date': '02/15/2017',
                'p_qty': 2
            }
        ]
        return result

    def suppliers(self):
        suppliers = [
            {
                's_id': 1,
                'bank_account': 123456789
            }
        ]
        return suppliers

    def client(self):
        result = [
            {
                'c_id': 1
            }
        ]
        return result

    def announcement(self):
        result = [
            {
                'a_id': 1,
                'a_price': 2.00,
                'a_date': '12/25/2017',
                'a_soldOut': 'yes',
                'a_initial_qty': 10,
                'a_curr_qty': 3
            }
        ]
        return result

    def getAllSuppliers(self):
        return jsonify({'suppliers': self.suppliers()})
