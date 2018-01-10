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

    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_category'] = row[1]
        result['r_name'] = row[2]
        result['r_description'] = row[3]
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
        if not request_list:
            return jsonify(Error="Request Not Found"), 404
        else:
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

    def getResourcestByRequestID(self, req_id):
        dao = RequestDAO()
        row = dao.getResourcesByRequestId(req_id)
        if not row:
            return jsonify(Error="Resource Not Found"), 404
        else:
            result = self.build_resource_dict(row)
        return jsonify(Resource=result)

    # ===================================================================================================================
    #                                           get Resources by Requests
    # ===================================================================================================================

    def getResourcestByRequests(self):
        dao = RequestDAO()
        if not dao.getResourcesByRequests():
            return jsonify(Error='Resource Not Found.'), 404
        else:
            resource_list = dao.getResourcesByRequests()
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)
