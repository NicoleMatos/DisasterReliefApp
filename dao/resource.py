from config.dbconfig import pg_config
import psycopg2


class ResourceDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # ===================================================================================================================
    #                                           get all resources
    # ===================================================================================================================

    def getAllResources(self):
        cursor = self.conn.cursor()
        query = "select * from resource;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getResourceById(self, rid):
        cursor = self.conn.cursor()
        query = "select * from resource where r_id = %s;"
        cursor.execute(query, (rid,))
        result = cursor.fetchone()
        return result

    # ===================================================================================================================
    #                                           get resources by things
    # ===================================================================================================================

    def getResourcesByCategoryAndName(self, category, name):
        cursor = self.conn.cursor()
        query = "select * from resource where r_category = %s and r_name = %s;"
        cursor.execute(query, (category, name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByCategory(self, category):
        cursor = self.conn.cursor()
        query = "select * from resource where r_category = %s;"
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from resource where r_name = %s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result


