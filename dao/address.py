from config.dbconfig import pg_config
import psycopg2


class AddressDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # ===================================================================================================================
    #                                           get all addresses
    # ===================================================================================================================

    def getAllAddresses(self):
        cursor = self.conn.cursor()
        query = "select * from address;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getAddressById(self, add_id):
        cursor = self.conn.cursor()
        query = "select * from address where add_id = %s;"
        cursor.execute(query, (add_id,))
        result = cursor.fetchone()
        return result

    # ===================================================================================================================
    #                                           get addresses by city
    # ===================================================================================================================

    def getAddressesByCity(self, add_city):
        cursor = self.conn.cursor()
        query = "select * from address where add_city = %s;"
        cursor.execute(query, (add_city,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                         get addresses by country
    # ===================================================================================================================

    def getAddressesByCountry(self, add_country):
        cursor = self.conn.cursor()
        query = "select * from address where add_country = %s;"
        cursor.execute(query, (add_country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                      get addresses by city and country
    # ===================================================================================================================

    def getAddressesByCityAndCountry(self, add_city, add_country):
        cursor = self.conn.cursor()
        query = "select * from address where and add_city = %s and add_country = %s;"
        cursor.execute(query, (add_city, add_country,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                               insert address
    # ===================================================================================================================

    def insert(self, c_id, add_line1, add_line2, add_city, add_country, add_zip_code):
        cursor = self.conn.cursor()
        query = "insert into address (c_id, add_line1, add_line2, add_city, add_country, add_zip_code) values " \
                "(%s, %s, %s, %s, %s, %s) returning add_id; "
        cursor.execute(query, (c_id, add_line1, add_line2, add_city, add_country, add_zip_code))
        add_id = cursor.fetchone()[0]
        self.conn.commit()
        return add_id

    # ===================================================================================================================
    #                                               update address
    # ===================================================================================================================

    def put(self, c_id, add_line1, add_line2, add_city, add_country, add_zip_code, add_id):
        cursor = self.conn.cursor()
        query = "update address set c_id=%s, add_line1=%s, add_line2=%s, add_city=%s, add_country=%s, add_zip_code=%s" \
                "where add_id=%s returning add_id; "
        cursor.execute(query, (c_id, add_line1, add_line2, add_city, add_country, add_zip_code, add_id))
        add_id = cursor.fetchone()[0]
        self.conn.commit()
        return add_id

    # ===================================================================================================================
    #                                               delete address
    # ===================================================================================================================

    def delete(self, add_id):
        cursor = self.conn.cursor()
        query = "delete from address where add_id=%s; "
        cursor.execute(query, (add_id,))
        self.conn.commit()
        return add_id
