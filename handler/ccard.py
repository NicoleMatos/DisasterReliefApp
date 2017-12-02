from flask import jsonify

class CCardHandler:

    def ccard(self):
        result = [
            {
                'cc_id': 1,
                'cc_name': 'Orlando Flores',
                'cc_number': '05/13/2017',
                'cc_exp_date': '07/22/1992'
            },
            {
                'cc_id': 2,
                'cc_name': 'Pedro Rivera',
                'cc_number': '02/13/2017',
                'cc_exp_date': '02/14/2012'
            }
        ]
        return result

    def getAllCCards(self):
        return jsonify(CCards=self.ccard())
