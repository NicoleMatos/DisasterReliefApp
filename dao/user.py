from config.dbconfig import pg_config
import psycopg2



class UserDAO:
    def __init__(self):

        connection_url = "dbname=%s user=%s password=%s" % (pg_config['dbname'],
                                                            pg_config['user'],
                                                            pg_config['passwd'])

        self.conn = psycopg2._connect(connection_url)

    # ===================================================================================================================
    #                                           get all users
    # ===================================================================================================================

    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from users;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get user by ID
    # ===================================================================================================================

    def getUserById(self,u_id):
        cursor = self.conn.cursor()
        query = "select * from users where u_id = %s;"
        cursor.execute(query,(u_id,))
        result = cursor.fetchone()
        return result

    # ===================================================================================================================
    #                                           get user by Name
    # ===================================================================================================================

    def getUserByName(self,u_name):
        cursor = self.conn.cursor()
        query = "select * from users where u_name = %s;"
        cursor.execute(query,(u_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get user by LastName
    # ===================================================================================================================

    def getUserByLastName(self,u_lastName):
        cursor = self.conn.cursor()
        query = "select * from users where u_lastName = %s;"
        cursor.execute(query,(u_lastName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get user by Name and LastName
    # ===================================================================================================================

    def getUserByNameAndLastName(self,u_name,u_lastName):
        cursor = self.conn.cursor()
        query = "select * from users where u_name = %s and u_lastName = %s;"
        cursor.execute(query,(u_name,u_lastName))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           get user by region
    # ===================================================================================================================
    def getUserByRegion(self,u_region):
        cursor = self.conn.cursor()
        query = "select * from users where u_region = %s;"
        cursor.execute(query,(u_region,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    # ===================================================================================================================
    #                                           insert user
    # ===================================================================================================================

    def insert(self, u_name, u_last_name, u_age, u_address, u_region, u_email, u_password):
        cursor = self.conn.cursor()
        query = "insert into user_table(u_email, u_password, u_name, u_lastname, u_region, u_age) values (%s," \
                "%s,%s,%s,%s,%d) returning u_id; "
        cursor.execute(query, (u_name, u_last_name, u_age, u_address, u_region, u_email, u_password))
        u_id = cursor.fetchone()[0]
        self.conn.commit()
        return u_id

