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
        result = []
        if date and client:
            result = self.getRequestsByClientAndDate(client, date)
        elif client:
            result = self.getRequestsByClient(client)
        elif date:
            result = self.getRequestsByDate(date)
        if len(result) == 0:
            return jsonify(Error="Request Not Found"), 404
        return jsonify(Result=result)

    # ===================================================================================================================
    #                                           get all transactions
    # ===================================================================================================================

    def getAllRequests(self):
        return jsonify(Requests=self.request())

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getRequestByID(self, req_id):
        result = list(filter(lambda request: request['req_id'] == req_id, self.request()))
        if len(result) == 0:
            return jsonify(Error="Request Not Found"), 404
        return jsonify(result)

    # ===================================================================================================================
    #                                           get requests by client
    # ===================================================================================================================

    def getRequestsByClient(self, client):
        result = list(filter(lambda request: request['c_id'] == client, self.request()))
        return result

    # ===================================================================================================================
    #                                           get requests by date
    # ===================================================================================================================

    def getRequestsByDate(self, date):
        result = list(filter(lambda request: request['req_date'] == date, self.request()))
        return result

    # ===================================================================================================================
    #                                     get requests by client and date
    # ===================================================================================================================

    def getRequestsByClientAndDate(self, client, date):
        result = list(filter(lambda request: request['c_id'] == client, self.request()))
        result2 = list(filter(lambda request: request['req_date'] == date, result))
        return result2
