from flask import jsonify


class RequestHandler:

    def request(self):
        result = [
            {
                'req_id': 1,
                'c_id': 1,
                'r_date': '02/10/2017',
                'r_qty': 4
            },
            {
                'req_id': 2,
                'c_id': 2,
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

    # ===================================================================================================================
    #                                           get requests by client
    # ===================================================================================================================

    def getRequestsByClient(self, client):
        result = list(filter(lambda transaction: transaction['c_id'] == client, self.request()))
        return result

    # ===================================================================================================================
    #                                           get requests by date
    # ===================================================================================================================

    def getRequestsByDate(self, date):
        result = list(filter(lambda transaction: transaction['req_date'] == date, self.request()))
        return result

    # ===================================================================================================================
    #                                     get requests by client and date
    # ===================================================================================================================

    def getRequestsByClientAndDate(self, client, date):
        result = list(filter(lambda resource: resource['c_id'] == client, self.request()))
        result2 = list(filter(lambda resource: resource['req_date'] == date, result))
        return result2
