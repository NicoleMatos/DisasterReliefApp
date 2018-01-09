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
        result_list = []
        for row in ccard_list:
            result = self.build_ccard_dict(row)
            result_list.append(result)
        return jsonify(CCard=result_list)

    # ===================================================================================================================
    #                                           get all credit cards
    # ===================================================================================================================

    def getAllCCards(self):
        return jsonify(CCards=self.ccard())

    # ===================================================================================================================
    #                                           get credit cards by id
    # ===================================================================================================================

    def getCCardByID(self, cc_id):
        ccards = self.ccard()
        result = list(filter(lambda card: card['cc_id'] == cc_id, ccards))
        if len(result) > 0:
            return jsonify(Result=result)
        return jsonify(Error="Credit Card Not Found"), 404

    # ===================================================================================================================
    #                                         get credit cards by name
    # ===================================================================================================================

    def getCCardByName(self, name):
        ccard = self.ccard()
        result = list(filter(lambda card: card['cc_name'] == name, ccard))
        return result

    # ===================================================================================================================
    #                                      get credit cards by last name
    # ===================================================================================================================

    def getCCardByLastName(self, lastname):
        ccard = self.ccard()
        result = list(filter(lambda card: card['cc_lastName'] == lastname, ccard))
        return result

    # ===================================================================================================================
    #                                  get credit cards by name and last name
    # ===================================================================================================================

    def getCCardByNameAndLastName(self, name, lastname):
        ccard = self.ccard()
        result = list(filter(lambda card: card['cc_name'] == name, ccard))
        result2 = list(filter(lambda card: card['cc_lastName'] == lastname, result))
        return result2
