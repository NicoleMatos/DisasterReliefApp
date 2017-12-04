from flask import jsonify


class RequestHandler:

    def request(self):
        result = [
            {
                'r_id': 1,
                'r_date': '02/10/2017',
                'r_qty': 4
            },
            {
                'r_id': 2,
                'r_date': '02/15/2017',
                'r_qty': 2
            }
        ]
        return result

    def getAllRequests(self):
        return jsonify(Requests=self.request())

    def searchRequests(self, args):
        date = args.get('date')
        if date:
            self.getRequestsByDate(date)

    def getRequestsByDate(self, date):
        return self.request()
