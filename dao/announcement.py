from config.dbconfig import pg_config
import psycopg2


class AnnouncementDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    #===================================================================================================================
    #                                          Get all Clients
    #===================================================================================================================

    def getAllAnnouncements(self):
        cursor = self.conn.cursor()
        query = "select * from announcement;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get announcement by id
    # ===================================================================================================================


    def getAnnouncementByID(self,a_id):
        cursor = self.conn.cursor()
        query = "select * from announcement where a_id = %s;"
        cursor.execute(query,(a_id,))
        result = cursor.fetchone()
        return result

    # ===================================================================================================================
    #                                           get announcement by date
    # ===================================================================================================================


    def getAnnouncementsByDate(self, a_date):
        cursor = self.conn.cursor()
        query = "select * from announcement where a_date = %s;"
        cursor.execute(query, (a_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get announcement by supplier and date
    # ===================================================================================================================

    def getAnnouncementsBySupplierAndDate(self,s_id,a_date):
        cursor = self.conn.cursor()
        query = "select * from announcement where and s_id = %s and a_date = %s;"
        cursor.execute(query, (s_id,a_date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get announcement by supplier
    # ===================================================================================================================

    def getAnnouncementsBySupplier(self,s_id):
        cursor = self.conn.cursor()
        query = "select * from announcement where s_id = %s;"
        cursor.execute(query, (s_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result
    # ===================================================================================================================
    #                                           get announcement by region
    # ===================================================================================================================


    def getAnnouncementByRegion(self,region):
        cursor = self.conn.cursor()
        query = "select a_id,s_id,r_id,a_price,a_date,a_sold_out,a_initial_qty,a_curr_qty from announcement natural inner join user_table natural inner join supplier where u_region=%s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get Resources by Announcements
    # ===================================================================================================================

    def getResourcesByAnnouncements(self):
        cursor = self.conn.cursor()
        query = "select r_id, r_category, r_name, r_description from announcement natural inner join resource;"
        cursor.execute(query,)
        result = []
        for row in cursor:
            result.append(row)
        return result





