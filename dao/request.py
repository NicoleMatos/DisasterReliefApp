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

    def getRequestsByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select * from request natural inner join client where u_region = %s;"
        cursor.execute(query, (region,))
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
        cursor.execute(query, )
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                               insert request
    # ===================================================================================================================

    def insert(self, c_id, r_id, req_qty, req_date):
        cursor = self.conn.cursor()
        query = "insert into request (c_id, r_id, req_qty, req_date) values " \
                "(%s, %s, %s, %s) returning req_id; "
        cursor.execute(query, (c_id, r_id, req_qty, req_date))
        req_id = cursor.fetchone()[0]
        self.conn.commit()
        return req_id

    # ===================================================================================================================
    #                                               put request
    # ===================================================================================================================

    def put(self, c_id, r_id, req_qty, req_date, req_id):
        cursor = self.conn.cursor()
        query = "update request set c_id=%s, r_id=%s, req_qty=%s, req_date=%s where req_id=%s returning req_id; "
        cursor.execute(query, (c_id, r_id, req_qty, req_date, req_id))
        req_id = cursor.fetchone()[0]
        self.conn.commit()
        return req_id

    # ===================================================================================================================
    #                                               delete request
    # ===================================================================================================================

    def delete(self, req_id):
        cursor = self.conn.cursor()
        query = "delete from request where req_id=%s; "
        cursor.execute(query, (req_id,))
        self.conn.commit()
        return req_id
