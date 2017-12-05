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



    # ===================================================================================================================
    #                                           Search for announcements
    # ===================================================================================================================

    def searchAnnouncements(self, args):
        supplier = args.get('supplier')
        date = args.get('date')
        result = []
        if date and supplier:
            result = self.getAnnouncementsBySupplierAndDate(supplier, date)
        elif supplier:
            result = self.getAnnouncementsBySupplier(supplier)
        elif date:
            result = self.getAnnouncementsByDate(date)
        if (len(result)== 0):
            return jsonify(Error="Client Not Found"), 404
        return jsonify(Result = result)


    # ===================================================================================================================
    #                                           get all announcements
    # ===================================================================================================================

    def getAllAnnouncements(self):
        return jsonify(Announcements=self.announcement())

    # ===================================================================================================================
    #                                           get announcements by ID
    # ===================================================================================================================

    def getAnnouncementByID(self, id):
        ann = self.announcement()
        result = list(filter(lambda announcement: announcement['a_id'] == id, ann))
        return jsonify(result)
    def getAnnouncementsBySupplierAndDate(self, supplier, date):
        return jsonify(self.request())


    def getAnnouncementsBySupplier(self, supplier):
        return jsonify(self.request())

    def getAnnouncementsByDate(self, date):
        ann = self.announcement()
        result = list(filter(lambda announcement: announcement['a_date'] == date, ann))
        return result


