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


    # ===================================================================================================================
    #                                          search for requests
    # ===================================================================================================================

    def searchRequests(self, args):
        client = args.get('client')
        date = args.get('date')
        if date and client:
            self.getRequestsByClientAndDate(client, date)
        elif client:
            self.getRequestsByClient(client)
        elif date:
            self.getRequestsByDate(date)
        else:
            return jsonify(self.request())

    # ===================================================================================================================
    #                                           get all transactions
    # ===================================================================================================================

    def getAllRequests(self):
        return jsonify(Requests=self.request())

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getRequestByID(self, r_id):
        result = list(filter(lambda supplier: supplier['r_id'] == r_id, self.request()))
        return jsonify(result)

    def getRequestsByClientAndDate(self, client, date):
        return jsonify(self.request())

    def getRequestsByClient(self, client):
        return jsonify(self.request())

    def getRequestsByDate(self, date):
        return jsonify(self.request())
