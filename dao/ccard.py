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