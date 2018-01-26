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
            ccard_list = dao.getCCardsByLastName(lastname)
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
        row = dao.getCCardById(cc_id)
        if not row:
            return jsonify(Error="Credit Card Not Found"), 404
        else:
            result = self.build_ccard_dict(row)
        return jsonify(CreditCard=result)


    # ===================================================================================================================
    #                                          insert credit card
    # ===================================================================================================================

    def insertCCard(self, form):
        if form and len(form) == 5:
            c_id = form['c_id']
            cc_name = form['cc_name']
            cc_lastname = form['cc_lastname']
            cc_number = form['cc_number']
            cc_exp_date = form['cc_exp_date']
            if cc_name and cc_lastname and cc_number and cc_exp_date and c_id:
                dao = CCardDAO()
                cc_id = dao.insert(c_id, cc_name, cc_lastname, cc_number, cc_exp_date)
                result = {}
                result["cc_id"]= cc_id
                result["c_id"] = c_id
                result["cc_name"] = cc_name
                result["cc_lastname"] = cc_lastname
                result["cc_number"] = cc_number
                result["cc_exp_date"] = cc_exp_date

                return jsonify(CreditCard=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")


    # ===================================================================================================================
    #                                          update credit card
    # ===================================================================================================================

    def putCCardByClientID(self, form, cc_id):
        if form and len(form) == 5:
            c_id = form['c_id']
            cc_name = form['cc_name']
            cc_lastname = form['cc_lastname']
            cc_number = form['cc_number']
            cc_exp_date = form['cc_exp_date']

            if cc_name and cc_lastname and cc_number and cc_exp_date and cc_id and c_id:
                dao = CCardDAO()
                cc_id = dao.put(c_id, cc_name, cc_lastname, cc_number, cc_exp_date, cc_id)
                result = {}
                result["cc_id"]= cc_id
                result["c_id"] = c_id
                result["cc_name"] = cc_name
                result["u_password"] = cc_lastname
                result["u_name"] = cc_number
                result["u_last_name"] = cc_exp_date

                return jsonify(CreditCard=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")


    # ===================================================================================================================
    #                                          delete credit card
    # ===================================================================================================================

    def deleteCCardByID(self, cc_id):
        dao = CCardDAO()
        if not dao.getCCardById(cc_id):
            return jsonify(Error="Credit Card not found."), 404
        else:
            dao.delete(cc_id)
            return jsonify(DeleteStatus="OK"), 200
