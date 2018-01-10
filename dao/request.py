from config.dbconfig import pg_config
import psycopg2


class RequestDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # ===================================================================================================================
    #                                           get all requests
    # ===================================================================================================================

    def getAllRequests(self):
        cursor = self.conn.cursor()
        query = "select * from request;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getRequestById(self, reqid):
        cursor = self.conn.cursor()
        query = "select * from request where req_id = %s;"
        cursor.execute(query, (reqid,))
        result = cursor.fetchone()
        return result

    def getResourcesByRequestId(self, reqid):
        cursor = self.conn.cursor()
        query = "select r_id, r_category, r_name, r_description from request natural inner join resource where req_id = %s;"
        cursor.execute(query, (reqid,))
        result = cursor.fetchone()
        return result

    # ===================================================================================================================
    #                                           get requests by things
    # ===================================================================================================================

    def getRequestsByClientAndDate(self, client, date):
        cursor = self.conn.cursor()
        query = "select * from request where c_id = %s and req_date = %s;"
        cursor.execute(query, (client, date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestsByClient(self, client):
        cursor = self.conn.cursor()
        query = "select * from request where c_id = %s;"
        cursor.execute(query, (client,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestsByDate(self, date):
        cursor = self.conn.cursor()
        query = "select * from request where req_date = %s;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get Resources by Requests
    # ===================================================================================================================

    def getResourcesByRequests(self):
        cursor = self.conn.cursor()
        query = "select r_id, r_category, r_name, r_description from request natural inner join resource;"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result