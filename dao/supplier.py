from config.dbconfig import pg_config
import psycopg2


class SupplierDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # ===================================================================================================================
    #                                           get all suppliers
    # ===================================================================================================================

    def getAllSuppliers(self):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join user_table;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get suppliers by Region
    # ===================================================================================================================

    def getSuppliersByRegionAndNameAndLastname(self, region, name, lastname):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join user_table where u_region = %s and u_name = %s and u_lastname = %s;"
        cursor.execute(query, (region, name, lastname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByRegionAndName(self, region, name):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join user_table where u_region = %s and u_name = %s;"
        cursor.execute(query, (region, name))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByRegionAndLastname(self, region, lastname):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join user_table where u_region = %s and u_lastname = %s;"
        cursor.execute(query, (region, lastname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByNameAndLastname(self, name, lastname):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join user_table where u_name = %s and u_lastname = %s;"
        cursor.execute(query, (name, lastname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join user_table where u_region = %s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join user_table where u_name = %s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByLastname(self, lastname):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join user_table where u_lastname = %s;"
        cursor.execute(query, (lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getSupplierById(self, sid):
        cursor = self.conn.cursor()
        query = "select * from supplier natural inner join user_table where s_id = %s;"
        cursor.execute(query, (sid,))
        result = cursor.fetchone()
        return result

    def getAnnouncementsBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select a_id, a_price, a_date, a_sold_out, a_initial_qty, a_curr_qty from supplier natural inner join " \
                "announcement where s_id = %s; "
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getResourcesBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select r_id, r_category, r_name, r_description from resource natural inner join supplier natural " \
                "inner join announcement where s_id = %s; "
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierId(self, sid):
        cursor = self.conn.cursor()
        query = "select t_id, t_price, t_date, t_qty from supplier natural inner join transaction where s_id = %s; "
        cursor.execute(query, (sid,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get resources by Region
    # ===================================================================================================================

    def getResourcesByRegion(self, region):
        cursor = self.conn.cursor()
        query = 'select r_id, r_category, r_name, r_description from supplier natural inner join user_table natural inner join announcement natural inner join resource where u_region = %s;'
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                               insert supplier
    # ===================================================================================================================

    def insert(self, sname, sregion, sphone):
        cursor = self.conn.cursor()
        query = "insert into supplier(s_name, s_region, s_phone) values (%s, %s, %s) returning s_id;"
        cursor.execute(query, (sname, sregion, sphone))
        sid = cursor.fetchone()[0]
        self.conn.commit()
        return sid
