from flask import jsonify


class CCardHandler:

    def ccard(self):
        result = [
            {
                'cc_id': 1,
                'cc_name': 'Orlando',
                'cc_lastName': 'Flores',
                'cc_number': '05/13/2017',
                'cc_exp_date': '07/22/1992'
            },
            {
                'cc_id': 2,
                'cc_name': 'Pedro',
                'cc_lastName': 'Rivera',
                'cc_number': '02/13/2017',
                'cc_exp_date': '02/14/2012'
            }
        ]
        return result

    # ===================================================================================================================
    #                                          search for credit cards
    # ===================================================================================================================

    def searchCCards(self, args):
        name = args.get('name')
        lastname = args.get('lastname')
        result = []
        if name and lastname:
            result = self.getCCardByNameAndLastName(name, lastname)
        elif name:
            result = self.getCCardByName(self, name)
        elif lastname:
            result = self.getCCardByLastName(self, lastname)
        if len(result) == 0:
            return jsonify(Error="Credit Card Not Found"), 404
        return jsonify(Result=result)

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
