from flask import jsonify
from dao.address import AddressDAO

class AddressHandler:

    def build_address_dict(self, row):
        result = {}
        result['add_id'] = row[0]
        result['c_id'] = row[1]
        result['add_line1'] = row[2]
        result['add_line2'] = row[3]
        result['add_city'] = row[4]
        result['add_country'] = row[5]
        result['add_zip_code'] = row[6]
        return result

    # ===================================================================================================================
    #                                          search for addresses
    # ===================================================================================================================

    def searchAddresses(self, args):
        city = args.get('city')
        country = args.get('country')
        dao = AddressDAO()
        if (len(args) == 2) and city and country:
            address_list = dao.getAddressesByCityAndCountry(city, country)
        elif (len(args) == 1) and city:
            address_list = dao.getAddressesByCity(city)
        elif (len(args) == 1) and country:
            address_list = dao.getAddressesByCountry(country)
        else:
            return jsonify(Error="Malformed query string"), 400
        if not address_list:
            return jsonify(Error="Address Not Found"), 404
        else:
            result_list = []
            for row in address_list:
                result = self.build_address_dict(row)
                result_list.append(result)
        return jsonify(Address=result_list)

    # ===================================================================================================================
    #                                           get all addresses
    # ===================================================================================================================

    def getAllAddresses(self):
        dao = AddressDAO()
        address_list = dao.getAllAddresses()
        if not address_list:
            return jsonify(Error="Address Not Found"), 404
        else:
            result_list = []
            for row in address_list:
                result = self.build_address_dict(row)
                result_list.append(result)
        return jsonify(Addresses=result_list)

    # ===================================================================================================================
    #                                           get address by id
    # ===================================================================================================================

    def getAddressByID(self, add_id):
        dao = AddressDAO()
        row = dao.getAddressById(add_id)
        if not row:
            return jsonify(Error="Address Not Found"), 404
        else:
            result = self.build_address_dict(row)
        return jsonify(Address=result)


    # ===================================================================================================================
    #                                          insert credit card
    # ===================================================================================================================

    def insertAddress(self, form,):
        if form and len(form) == 6:
            c_id = form['c_id']
            add_line1 = form['add_line1']
            add_line2 = form['add_line2']
            add_city = form['add_city']
            add_country = form['add_country']
            add_zip_code = form['add_zip_code']
            if c_id and add_line1 and add_line2 and add_city and add_country and add_zip_code:
                dao = AddressDAO()
                add_id = dao.insert(c_id,add_line1, add_line2, add_city, add_country,add_zip_code)
                result = {}
                result['add_id'] = add_id
                result['c_id'] = c_id
                result['add_line1'] = add_line1
                result['add_line2'] = add_line2
                result['add_city'] = add_city
                result['add_country'] = add_country
                result['add_zip_code'] = add_zip_code

                return jsonify(Address=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")


    # ===================================================================================================================
    #                                          update address
    # ===================================================================================================================

    def putAddressID(self, form, add_id):
        if form and len(form) == 5:
            add_line1 = form['add_line1']
            add_line2 = form['add_line2']
            add_city = form['add_city']
            add_country = form['add_country']
            add_zip_code = form['add_zip_code']

            if add_line1 and add_line2 and add_city and add_country and add_id and add_zip_code:
                dao = AddressDAO()
                add_id = dao.put(add_line1, add_line2, add_city, add_country, add_zip_code, add_id)
                result = {}
                result['add_id'] = add_id
                result['add_line1'] = add_line1
                result['add_line2'] = add_line2
                result['add_city'] = add_city
                result['add_country'] = add_country
                result['add_zip_code'] = add_zip_code

                return jsonify(Address=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")


    # ===================================================================================================================
    #                                          delete address
    # ===================================================================================================================

    def deleteAddressByID(self, add_id):
        dao = AddressDAO()
        if not dao.getAddressById(add_id):
            return jsonify(Error="Address not found."), 404
        else:
            dao.delete(add_id)
            return jsonify(DeleteStatus="OK"), 200
