from config.dbconfig import pg_config
import psycopg2



class AdministratorDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    # ===================================================================================================================
    #                                           get all administrators
    # ===================================================================================================================

    def getAllAdministrators(self):
        cursor = self.conn.cursor()
        query = "select * from administrator;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get administrator by ID
    # ===================================================================================================================

    def getAdministratorById(self,ad_id):
        cursor = self.conn.cursor()
        query = "select * from administrator where ad_id = %s;"
        cursor.execute(query,(ad_id,))
        result = cursor.fetchone()
        return result

    # ===================================================================================================================
    #                                           get administrator by Name
    # ===================================================================================================================

    def getAdministratorByName(self,u_name):
        cursor = self.conn.cursor()
        query = "select * from user_table natural inner join administrator where u_name = %s;"
        cursor.execute(query,(u_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get administrator by LastName
    # ===================================================================================================================

    def getUserByLastName(self,u_lastName):
        cursor = self.conn.cursor()
        query = "select * from user_table natural inner join administrator where u_lastname = %s;"
        cursor.execute(query,(u_lastName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get administrator by Name and LastName
    # ===================================================================================================================

    def getUserByNameAndLastName(self,u_name,u_lastName):
        cursor = self.conn.cursor()
        query = "select * from user_table natural inner join administrator where u_name = %s and u_lastname=%s;"
        cursor.execute(query,(u_name,u_lastName))
        result = []
        for row in cursor:
            result.append(row)
        return result


