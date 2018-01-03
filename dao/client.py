from config.dbconfig import pg_config
import psycopg2


class UserDAO:
    def __init__(self):

        return 0;


    def getAllUsers(self):
        cursor = self.conn.cursor()
        query = "select * from user;"
        cursor.execute(query)
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserById(self,u_id):
        cursor = self.conn.cursor()
        query = "select * from user where u_id = %s;"
        cursor.execute(query,(u_id,))
        result = cursor.fetchone()
        return result


    def getUserByName(self,u_name):
        cursor = self.conn.cursor()
        query = "select * from user where u_name = %s;"
        cursor.execute(query,(u_name,))
        result = []
        for row in cursor:
            result.append(row)
        return result


    def getUserByLastName(self,u_lastName):
        cursor = self.conn.cursor()
        query = "select * from user where u_lastName = %s;"
        cursor.execute(query,(u_lastName,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByNameAndLastName(self,u_name,u_lastName):
        cursor = self.conn.cursor()
        query = "select * from user where u_name = %s and u_lastName = %s;"
        cursor.execute(query,(u_name,u_lastName))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def getUserByLocation(self,u_location):
        cursor = self.conn.cursor()
        query = "select * from user where u_location = %s;"
        cursor.execute(query,(u_location,))
        result = []
        for row in cursor:
            result.append(row)
        return result

    def insert(self, u_name, u_lastName, u_age, u_address, u_location, u_email, u_password):
        cursor = self.conn.cursor()
        query = "insert into user(u_name, u_lastName, u_age, u_address, u_location, u_email, u_password) values (%s,%s,%d,%s,%s,%s,%s) returning u_id;"
        cursor.execute(query,(u_name, u_lastName, u_age, u_address, u_location, u_email, u_password))
        u_id = cursor.fetchone()[0]
        self.conn.commit()
        return u_id

