from flask import jsonify
from dao.ccard import CCardDAO

class CCardHandler:

    def build_ccard_dict(self, row):
        result = {}
        result['cc_id'] = row[0]
        result['c_id'] = row[1]
        result['cc_name'] = row[2]
        result['cc_lastname'] = row[3]
        result['cc_number'] = row[4]
        result['cc_exp_date'] = row[5]
        return result

    # ===================================================================================================================
    #                                          search for credit cards
    # ===================================================================================================================

    def searchCCards(self, args):
        name = args.get('name')
        lastname = args.get('lastname')
        dao = CCardDAO()
        if (len(args) == 2) and name and lastname:
            ccard_list = dao.getCCardsByNameAndLastName(name, lastname)
        elif (len(args) == 1) and name:
            ccard_list = dao.getCCardsByName(name)
        elif (len(args) == 1) and lastname:
            ccard_list = dao.getCCardsByLastname(lastname)
        else:
            return jsonify(Error="Malformed query string"), 400
        if not ccard_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            result_list = []
            for row in ccard_list:
                result = self.build_ccard_dict(row)
                result_list.append(result)
        return jsonify(CreaditCard=result_list)

    # ===================================================================================================================
    #                                           get all credit cards
    # ===================================================================================================================

    def getAllCCards(self):
        dao = CCardDAO()
        ccard_list = dao.getAllCCards()
        if not ccard_list:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            result_list = []
            for row in ccard_list:
                result = self.build_ccard_dict(row)
                result_list.append(result)
        return jsonify(CreditCards=result_list)

    # ===================================================================================================================
    #                                           get credit cards by id
    # ===================================================================================================================

    def getCCardByID(self, cc_id):
        dao = CCardDAO()
        row = dao.getSupplierById(cc_id)
        if not row:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            result = self.build_ccard_dict(row)
        return jsonify(CreditCard=result)
