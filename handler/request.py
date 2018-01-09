from flask import jsonify
from dao.request import RequestDAO

class RequestHandler:

    def build_request_dict(self, row):
        result = {}
        result['req_id'] = row[0]
        result['c_id'] = row[1]
        result['r_id'] = row[2]
        result['req_qty'] = row[3]
        result['req_date'] = row[4]
        return result

    # ===================================================================================================================
    #                                          search for requests
    # ===================================================================================================================

    def searchRequests(self, args):
        client = args.get('client')
        date = args.get('date')
        dao = RequestDAO()
        if (len(args) == 2) and date and client:
            request_list = dao.getRequestsByClientAndDate(client, date)
        elif (len(args) == 1) and client:
            request_list = dao.getRequestsByClient(client)
        elif (len(args) == 1) and date:
            request_list = dao.getRequestsByDate(date)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Request=result_list)

    # ===================================================================================================================
    #                                           get all requests
    # ===================================================================================================================

    def getAllRequests(self):
        dao = RequestDAO()
        request_list = dao.getAllRequests()
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        return jsonify(Requests=result_list)

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getRequestByID(self, req_id):
        dao = RequestDAO()
        row = dao.getRequestById(req_id)
        if not row:
            return jsonify(Error="Request Not Found"), 404
        else:
            result = self.build_request_dict(row)
        return jsonify(Request=result)

