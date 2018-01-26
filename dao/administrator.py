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
        query = "select * from administrator natural inner join user_table;"
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
        query = "select * from administrator natural inner join user_table where ad_id = %s;"
        cursor.execute(query,(ad_id,))
        result = cursor.fetchone()
        return result

    # ===================================================================================================================
    #                                           get administrator by Name
    # ===================================================================================================================

    def getAdministratorByName(self,u_name):
        cursor = self.conn.cursor()
        query = "select * from administrator natural inner join user_table where u_name = %s;"
        cursor.execute(query,(u_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get administrator by LastName
    # ===================================================================================================================

    def getAdministratorByLastName(self,u_lastName):
        cursor = self.conn.cursor()
        query = "select * from administrator natural inner join user_table where u_lastname = %s;"
        cursor.execute(query,(u_lastName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get administrator by Name and LastName
    # ===================================================================================================================

    def getAdministratorByNameAndLastName(self,u_name,u_lastName):
        cursor = self.conn.cursor()
        query = "select * from administrator natural inner join user_table where u_name = %s and u_lastname=%s;"
        cursor.execute(query,(u_name,u_lastName))
        result = []
        for row in cursor:
            result.append(row)
        return result


    # ===================================================================================================================
    #                                               insert administrator
    # ===================================================================================================================

    def insert(self, u_email, u_password, u_name, u_last_name, u_region, u_age):
        cursor = self.conn.cursor()
        query = "insert into administrator (u_email, u_password, u_name, u_lastname, u_region, u_age) values " \
                "(%s, %s, %s, %s, %s, %s) returning ad_id; "
        cursor.execute(query, (u_email, u_password, u_name, u_last_name, u_region, u_age))
        ad_id = cursor.fetchone()[0]
        self.conn.commit()
        return ad_id

    # ===================================================================================================================
    #                                               put administrator
    # ===================================================================================================================

    def put(self, u_email, u_password, u_name, u_last_name, u_region, u_age, ad_id):
        cursor = self.conn.cursor()
        query = "update administrator set u_email=%s, u_password=%s, u_name=%s, u_lastname=%s, u_region=%s, u_age=%s, " \
                "where ad_id=%s returning ad_id; "
        cursor.execute(query, (u_email, u_password, u_name, u_last_name, u_region, u_age, ad_id))
        ad_id = cursor.fetchone()[0]
        self.conn.commit()
        return ad_id

    # ===================================================================================================================
    #                                               delete administrator
    # ===================================================================================================================

    def delete(self, ad_id):
        cursor = self.conn.cursor()
        query = "delete from administrator where ad_id=%s;"
        cursor.execute(query, (ad_id,))
        self.conn.commit()
        return ad_id


