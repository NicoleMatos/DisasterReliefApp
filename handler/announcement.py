from flask import jsonify

class AnnouncementHandler:

    def announcement(self):
        result = [
            {
                'a_id': 1,
                'a_price': 5.00,
                'a_date': '02/13/2017',
                'a_sold_out': 'yes',
                'a_initial_qty': 4,
                'a_curr_qty': 4
            },
            {
                'a_id': 2,
                'a_price': 10.00,
                'a_date': '02/20/2017',
                'a_sold_out': 'no',
                'a_initial_qty': 4,
                'a_curr_qty': 2
            }
        ]
        return result

    def getAllAnnouncements(self):
        return jsonify(Announcements=self.announcement())