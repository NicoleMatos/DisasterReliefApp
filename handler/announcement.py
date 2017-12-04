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

    def searchAnnouncements(self, args):
        supplier = args.get('supplier')
        date = args.get('date')
        if date and supplier:
            self.getAnnouncementsBySupplierAndDate(supplier, date)
        elif supplier:
            self.getAnnouncementsBySupplier(supplier)
        elif date:
            self.getAnnouncementsByDate(date)
        else:
            return jsonify(self.request())

    def getAnnouncementsBySupplierAndDate(self, supplier, date):
        return jsonify(self.request())

    def getAnnouncementsBySupplier(self, supplier):
        return jsonify(self.request())

    def getAnnouncementsByDate(self, date):
        return jsonify(self.request())
