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
        query = "select * from supplier;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get suppliers by things
    # ===================================================================================================================

    def getSuppliersByRegionAndNameAndLastname(self, region, name, lastname):
        cursor = self.conn.cursor()
        query = "select * from supplier where u_region = %s and u_name = %s and u_lastname = %s;"
        cursor.execute(query, (region, name, lastname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByRegionAndName(self, region, name):
        cursor = self.conn.cursor()
        query = "select * from supplier where u_region = %s and u_name = %s;"
        cursor.execute(query, (region, name))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByRegionAndLastname(self, region, lastname):
        cursor = self.conn.cursor()
        query = "select * from supplier where u_region = %s and u_lastname = %s;"
        cursor.execute(query, (region, lastname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByNameAndLastname(self, name, lastname):
        cursor = self.conn.cursor()
        query = "select * from supplier where u_name = %s and u_lastname = %s;"
        cursor.execute(query, (name, lastname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByRegion(self, region):
        cursor = self.conn.cursor()
        query = "select * from supplier where u_region = %s;"
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByName(self, name):
        cursor = self.conn.cursor()
        query = "select * from supplier where u_name = %s;"
        cursor.execute(query, (name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByLastname(self, lastname):
        cursor = self.conn.cursor()
        query = "select * from supplier where u_lastname = %s;"
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
        query = "select * from supplier where s_id = %s;"
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
        query = 'select r_id, r_category, r_name, r_description from supplier natural inner join announcement natural ' \
                'inner join resource where u_region = %s; '
        cursor.execute(query, (region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                               insert supplier
    # ===================================================================================================================

    def insert(self, u_email, u_password, u_name, u_last_name, u_region, u_age, s_bank_account):
        cursor = self.conn.cursor()
        query = "insert into supplier (u_email, u_password, u_name, u_lastname, u_region, u_age, s_bank_account) values " \
                "(%s, %s, %s, %s, %s, %s, %s) returning s_id; "
        cursor.execute(query, (u_email, u_password, u_name, u_last_name, u_region, u_age, s_bank_account))
        s_id = cursor.fetchone()[0]
        self.conn.commit()
        return s_id

    # ===================================================================================================================
    #                                               put supplier
    # ===================================================================================================================

    def put(self, u_email, u_password, u_name, u_last_name, u_region, u_age, s_bank_account, s_id):
        cursor = self.conn.cursor()
        query = "update supplier set u_email=%s, u_password=%s, u_name=%s, u_lastname=%s, u_region=%s, u_age=%s, " \
                "s_bank_account=%s where s_id=%s returning s_id; "
        cursor.execute(query, (u_email, u_password, u_name, u_last_name, u_region, u_age, s_bank_account, s_id))
        s_id = cursor.fetchone()[0]
        self.conn.commit()
        return s_id

    # ===================================================================================================================
    #                                               delete supplier
    # ===================================================================================================================

    def delete(self, s_id):
        cursor = self.conn.cursor()
        query = "delete from supplier where s_id=%s; "
        cursor.execute(query, (s_id,))
        self.conn.commit()
        return s_id
