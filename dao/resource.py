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
    #                                         get things by resource name
    # ===================================================================================================================

    def getRequestsByResourceCategory(self, category):
        cursor = self.conn.cursor()
        query = "select req_id, c_id, r_id, req_qty, req_date from resource natural inner join request where " \
                "r_category = %s order by r_name; "
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getAnnouncementsByResourceCategory(self, category):
        cursor = self.conn.cursor()
        query = "select a_id, s_id, r_id, a_price, a_date, a_sold_out, a_initial_qty, a_curr_qty from resource " \
                "natural inner join announcement where r_category = %s order by r_name; "
        cursor.execute(query, (category,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSupplierByResourceName(self, name):
        cursor = self.conn.cursor()
        query = "select distinct u_id, s_id, bank_account, u_email, u_password, u_name, u_lastname, u_region, " \
                "u_age from resource natural inner join supplier natural inner join user_table where r_name = %s; "
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
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

    def getResourcesByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select * from resource natural inner join user_table where u_region = %s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesByRegionAndName(self, region, name):
        cursor = self.conn.cursor()
        query = "select * from resource natural inner join user_table where u_region = %s and r_name = %s;"
        cursor.execute(query, (region, name,))
        result = []
        for row in cursor:
            result.append(row)
        return result



    # ===================================================================================================================
    #                                               insert resource
    # ===================================================================================================================

    def insert(self,r_category, r_name, r_description):
        cursor = self.conn.cursor()
        query = "insert into resource (r_category, r_name, r_description) values " \
                "(%s, %s, %s) returning r_id; "
        cursor.execute(query, (r_category, r_name, r_description))
        r_id = cursor.fetchone()[0]
        self.conn.commit()
        return r_id


    # ===================================================================================================================
    #                                               update resource
    # ===================================================================================================================

    def put(self, r_category, r_name, r_description,r_id):
        cursor = self.conn.cursor()
        query = "update resource set r_category=%s, r_name=%s, r_description=%s" \
                "where r_id=%s returning r_id;"
        cursor.execute(query, (r_category, r_name, r_description,r_id))
        r_id = cursor.fetchone()[0]
        self.conn.commit()
        return r_id


