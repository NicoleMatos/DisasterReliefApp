from flask import jsonify

class UserHandler:

    def user(self):
        result = [
            {
                'u_id': 1,
                'u_name': 'Pedro',
                'u_last_name': 'Rivera',
                'u_email': 'pedro.rivera300@upr.edu',
                'u_password': '02/13/2017',
                'u_phone': 7875554422,
                'u_age': 15,
                'u_address': 'Vega Baja, PR',
                'u_location': 'North'
            },
            {
                'u_id': 2,
                'u_name': 'Orlando',
                'u_last_name': 'Torres',
                'u_email': 'ordlando.torres350@upr.edu',
                'u_password': '03/22/2016',
                'u_phone': 7872345422,
                'u_age': 20,
                'u_address': 'San Juan, PR',
                'u_location': 'Metro'
            }
        ]
        return result

    def getAllUsers(self):
        return jsonify(Users=self.user())