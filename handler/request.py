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
        client = args.get('c_id')
        date = args.get('req_date')
        region = args.get('region')
        dao = RequestDAO()
        if (len(args) == 3) and client and date and region:
            request_list = dao.getRequestsByClientAndDate(client, date)
        elif (len(args) == 1) and client:
            request_list = dao.getRequestsByClient(client)
        elif (len(args) == 1) and date:
            request_list = dao.getRequestsByDate(date)
        elif (len(args) == 1) and region:
            request_list = dao.getRequestsByRegion(region)
        else:
            return jsonify(Error="Malformed query string"), 400
        result_list = []
        for row in request_list:
            result = self.build_request_dict(row)
            result_list.append(result)
        if len(result_list) == 0:
            return jsonify(Error="Request Not Found"), 404
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

# ===================================================================================================================
#                                          insert request
# ===================================================================================================================

    def insertRequest(self, form):
        if form and len(form) == 4:
            c_id = form['c_id']
            r_id = form['r_id']
            req_qty = form['req_qty']
            req_date = form['req_date']
            if c_id and r_id and req_qty and req_date:
                dao = RequestDAO()
                req_id = dao.insert(c_id, r_id, req_qty, req_date)
                result = {}
                result["req_id"] = req_id
                result["c_id"] = c_id
                result["r_id"] = r_id
                result["req_qty"] = req_qty
                result["req_date"] = req_date
                return jsonify(Request=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

# ===================================================================================================================
#                                          put request
# ===================================================================================================================

    def putRequestByID(self, form, req_id):
        if form and len(form) == 4:
            c_id = form['c_id']
            r_id = form['r_id']
            req_qty = form['req_qty']
            req_date = form['req_date']
            if c_id and r_id and req_qty and req_date and req_id:
                dao = RequestDAO()
                req_id = dao.put(c_id, r_id, req_qty, req_date, req_id)
                result = {}
                result["req_id"] = req_id
                result["c_id"] = c_id
                result["r_id"] = r_id
                result["req_qty"] = req_qty
                result["req_date"] = req_date
                return jsonify(Request=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

# ===================================================================================================================
#                                          delete request
# ===================================================================================================================

    def deleteRequestByID(self, req_id):
        dao = RequestDAO()
        if not dao.getRequestById(req_id):
            return jsonify(Error="Request not found."), 404
        else:
            dao.delete(req_id)
            return jsonify(DeleteStatus="OK"), 200
