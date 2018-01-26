from config.dbconfig import pg_config
import psycopg2


class ClientDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    #===================================================================================================================
    #                                          Get all Clients
    #===================================================================================================================

    def getAllClients(self):
        cursor = self.conn.cursor()
        query = "select * from client;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get things by id
    # ===================================================================================================================


    def getClientById(self,c_id):
        cursor = self.conn.cursor()
        query = "select * from client where c_id = %s;"
        cursor.execute(query,(c_id,))
        result = cursor.fetchone()
        return result

    def getTransactionsByClientID(self, c_id):
        cursor = self.conn.cursor()
        query = "select * from transaction where c_id = %s;"
        cursor.execute(query,(c_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getRequestsByClientID(self, c_id):
        cursor = self.conn.cursor()
        query = "select * from request where c_id = %s;"
        cursor.execute(query, (c_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getCreditCardsByClientID(self, c_id):
        cursor = self.conn.cursor()
        query = "select * from credit_card where c_id = %s;"
        cursor.execute(query, (c_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getSuppliersByClientID(self, c_id):
        cursor = self.conn.cursor()
        query = "select * from supplier where s_id IN (select s_id from transaction where c_id = %s);"
        cursor.execute(query, (c_id,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get clients by Name
    # ===================================================================================================================

    def getClientByName(self,u_name):
        cursor = self.conn.cursor()
        query = "select * from client where u_name = %s;"
        cursor.execute(query,(u_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get clients by Lastname
    # ===================================================================================================================

    def getClientByLastName(self,u_lastname):
        cursor = self.conn.cursor()
        query = "select * from client where u_lastname = %s;"
        cursor.execute(query, (u_lastname,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get clients by Name and Lastname
    # ===================================================================================================================


    def getClientByNameAndLastName(self,u_name,u_lastname):
        cursor = self.conn.cursor()
        query = "select * from client where u_name = %s and u_lastname = %s;"
        cursor.execute(query,(u_name,u_lastname))
        result = []
        for row in cursor:
            result.append(row)
        return result


    # ===================================================================================================================
    #                                           get clients by region
    # ===================================================================================================================

    def getClientByRegion(self,region):
        cursor = self.conn.cursor()
        query = "select * from client where u_region = %s;"
        cursor.execute(query,(region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get clients by region, name and lastname
    # ===================================================================================================================

    def getClientByRegionAndNameAndLastname(self, region, name, lastname):
        cursor = self.conn.cursor()
        query = "select * from client where u_region = %s and u_name = %s and u_lastname = %s;"
        cursor.execute(query, (region, name, lastname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get clients by region and  name
    # ===================================================================================================================

    def getClientByRegionAndName(self, region, name):
        cursor = self.conn.cursor()
        query = "select * from client where u_region = %s and u_name = %s;"
        cursor.execute(query, (region, name))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get clients by region and lastname
    # ===================================================================================================================

    def getClientByRegionAndLastname(self, region, lastname):
        cursor = self.conn.cursor()
        query = "select * from client where u_region = %s and u_lastname = %s;"
        cursor.execute(query, (region, lastname))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                               insert client
    # ===================================================================================================================

    def insert(self, u_email, u_password, u_name, u_last_name, u_region, u_age):
        cursor = self.conn.cursor()
        query = "insert into client (u_email, u_password, u_name, u_lastname, u_region, u_age) values " \
                "(%s, %s, %s, %s, %s, %s) returning c_id; "
        cursor.execute(query, (u_email, u_password, u_name, u_last_name, u_region, u_age))
        c_id = cursor.fetchone()[0]
        self.conn.commit()
        return c_id

    # ===================================================================================================================
    #                                               put client
    # ===================================================================================================================

    def put(self, u_email, u_password, u_name, u_last_name, u_region, u_age, c_id):
        cursor = self.conn.cursor()
        query = "update client set u_email=%s, u_password=%s, u_name=%s, u_lastname=%s, u_region=%s, u_age=%s " \
                "where c_id=%s returning c_id; "
        cursor.execute(query, (u_email, u_password, u_name, u_last_name, u_region, u_age, c_id))
        c_id = cursor.fetchone()[0]
        self.conn.commit()
        return c_id

    # ===================================================================================================================
    #                                               delete client
    # ===================================================================================================================

    def delete(self, c_id):
        cursor = self.conn.cursor()
        query = "delete from client where c_id=%s; "
        cursor.execute(query, (c_id,))
        self.conn.commit()
        return c_id


