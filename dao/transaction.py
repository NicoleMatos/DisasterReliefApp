from config.dbconfig import pg_config
import psycopg2


class TransactionDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])
        self.conn = psycopg2._connect(connection_url)

    # ===================================================================================================================
    #                                           get all suppliers
    # ===================================================================================================================

    def getAllTransactions(self):
        cursor = self.conn.cursor()
        query = "select * from transaction;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get suppliers by things
    # ===================================================================================================================

    def getTransactionsByDateAndSupplierAndClient(self, date, supplier, client):
        cursor = self.conn.cursor()
        query = "select * from transaction where t_date = %s and s_id = %s and c_id = %s;"
        cursor.execute(query, (date, supplier, client))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByDateAndSupplier(self, date, supplier):
        cursor = self.conn.cursor()
        query = "select * from transaction where t_date = %s and s_id = %s;"
        cursor.execute(query, (date, supplier))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByDateAndClient(self, date, client):
        cursor = self.conn.cursor()
        query = "select * from transaction where t_date = %s and c_id = %s;"
        cursor.execute(query, (date, client))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplierAndClient(self, supplier, client):
        cursor = self.conn.cursor()
        query = "select * from transaction where s_id = %s and c_id = %s;"
        cursor.execute(query, (supplier, client))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByDate(self, date):
        cursor = self.conn.cursor()
        query = "select * from transaction where t_date = %s;"
        cursor.execute(query, (date,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsBySupplier(self, supplier):
        cursor = self.conn.cursor()
        query = "select t_id, s_id, c_id, r_id, t_price, t_date, t_qty from transaction natural inner join user_table " \
                "natural inner join supplier where u_name = %s; "
        cursor.execute(query, (supplier,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getTransactionsByClient(self, client):
        cursor = self.conn.cursor()
        query = "select t_id, s_id, c_id, r_id, t_price, t_date, t_qty from transaction natural inner join user_table " \
                "natural inner join client where u_name = %s; "
        cursor.execute(query, (client,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================

    def getTransactionById(self, tid):
        cursor = self.conn.cursor()
        query = "select * from transaction where t_id = %s;"
        cursor.execute(query, (tid,))
        result = cursor.fetchone()
        return result