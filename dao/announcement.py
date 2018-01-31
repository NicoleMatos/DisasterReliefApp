from config.dbconfig import pg_config
import psycopg2


class AnnouncementDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s host=%s port=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'],
                                                            pg_config['host'],
                                                            pg_config['port'])

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

    # ===================================================================================================================
    #                                               insert announcement
    # ===================================================================================================================

    def insert(self, s_id, r_id, a_price, a_date, a_sold_out, a_initial_qty, a_curr_qty):
        cursor = self.conn.cursor()
        query = "insert into announcement (s_id, r_id, a_price, a_date, a_sold_out, a_initial_qty, a_curr_qty) values " \
                "(%s, %s, %s, %s, %s, %s, %s) returning a_id; "
        cursor.execute(query, (s_id, r_id, a_price, a_date, a_sold_out, a_initial_qty, a_curr_qty))
        a_id = cursor.fetchone()[0]
        self.conn.commit()
        return a_id

    # ===================================================================================================================
    #                                               put announcement
    # ===================================================================================================================

    def put(self, s_id, r_id, a_price, a_date, a_sold_out, a_initial_qty, a_curr_qty, a_id):
        cursor = self.conn.cursor()
        query = "update announcement set s_id=%s, r_id=%s, a_price=%s, a_date=%s, a_sold_out=%s, a_initial_qty=%s, " \
                "a_curr_qty=%s where a_id=%s returning a_id; "
        cursor.execute(query, (s_id, r_id, a_price, a_date, a_sold_out, a_initial_qty, a_curr_qty, a_id))
        a_id = cursor.fetchone()[0]
        self.conn.commit()
        return a_id

    # ===================================================================================================================
    #                                               delete announcement
    # ===================================================================================================================

    def delete(self, a_id):
        cursor = self.conn.cursor()
        query = "delete from announcement where a_id=%s; "
        cursor.execute(query, (a_id,))
        self.conn.commit()
        return a_id





