from config.dbconfig import pg_config
import psycopg2


class CCardDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # ===================================================================================================================
    #                                           get all requests
    # ===================================================================================================================

    def getAllCCards(self):
        cursor = self.conn.cursor()
        query = "select * from credit_card;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getCCardById(self, ccid):
        cursor = self.conn.cursor()
        query = "select * from credit_card where cc_id = %s;"
        cursor.execute(query, (ccid,))
        result = cursor.fetchone()
        return result

    # ===================================================================================================================
    #                                           get ccard by name
    # ===================================================================================================================


    def getCCardsByName(self, cc_name):
        cursor = self.conn.cursor()
        query = "select * from credit_card where cc_name = %s;"
        cursor.execute(query, (cc_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                         get ccard by lastname
    # ===================================================================================================================

    def getCCardsByLastName(self, cc_lastname):
        cursor = self.conn.cursor()
        query = "select * from credit_card where cc_lastname = %s;"
        cursor.execute(query, (cc_lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                 get credit card by name and lastname
    # ===================================================================================================================

    def getCCardsByNameAndLastName(self, cc_name, cc_lastname):
        cursor = self.conn.cursor()
        query = "select * from credit_card where and cc_name = %s and cc_lastname = %s;"
        cursor.execute(query, (cc_name, cc_lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    # ===================================================================================================================
    #                                               insert credit card
    # ===================================================================================================================

    def insert(self, c_id, cc_name, cc_lastname, cc_number, cc_exp_date):
        cursor = self.conn.cursor()
        query = "insert into credit_card (c_id, cc_name, cc_lastname, cc_number, cc_exp_date) values " \
                "(%s, %s, %s, %s, %s) returning cc_id; "
        cursor.execute(query, (c_id, cc_name, cc_lastname, cc_number, cc_exp_date))
        cc_id = cursor.fetchone()[0]
        self.conn.commit()
        return cc_id


    # ===================================================================================================================
    #                                               update credit card
    # ===================================================================================================================

    def put(self, c_id, cc_name, cc_lastname, cc_number, cc_exp_date, cc_id):
        cursor = self.conn.cursor()
        query = "update credit_card set c_id=%s, cc_name=%s, cc_lastname=%s, cc_number=%s, cc_exp_date=%s" \
                "where cc_id=%s returning cc_id; "
        cursor.execute(query, (c_id, cc_name, cc_lastname, cc_number, cc_exp_date, cc_id))
        cc_id = cursor.fetchone()[0]
        self.conn.commit()
        return cc_id

    # ===================================================================================================================
    #                                               delete client
    # ===================================================================================================================

    def delete(self, cc_id):
        cursor = self.conn.cursor()
        query = "delete from credit_card where cc_id=%s; "
        cursor.execute(query, (cc_id,))
        self.conn.commit()
        return cc_id