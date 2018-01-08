from flask import jsonify


class AnnouncementHandler:

    def announcement(self):
        result = [
            {
                'a_id': 1,
                's_id': 1,
                'a_price': 5.00,
                'a_date': '02/13/2017',
                'a_sold_out': 'yes',
                'a_initial_qty': 4,
                'a_curr_qty': 4
            },
            {
                'a_id': 2,
                's_id': 2,
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
        if len(result) == 0:
            return jsonify(Error="Announcement Not Found"), 404
        return jsonify(Result=result)

    # ===================================================================================================================
    #                                          get all announcements
    # ===================================================================================================================

    def getAllAnnouncements(self):
        return jsonify(Announcements=self.announcement())

    # ===================================================================================================================
    #                                         get announcements by ID
    # ===================================================================================================================

    def getAnnouncementByID(self, a_id):
        ann = self.announcement()
        result = list(filter(lambda announcement: announcement['a_id'] == a_id, ann))
        if len(result) > 0:
            return jsonify(Result=result)
        return jsonify(Error="Announcement Not Found"), 404



    # ===================================================================================================================
    #                                         get announcements by Date
    # ===================================================================================================================

    def getAnnouncementsByDate(self, date):
        ann = self.announcement()
        result = list(filter(lambda announcement: announcement['a_date'] == date, ann))
        return result

    # ===================================================================================================================
    #                                   get announcements by Supplier And Date
    # ===================================================================================================================

    def getAnnouncementsBySupplierAndDate(self, supplier, date):
        ann = self.announcement()
        result = list(filter(lambda announcement: announcement['s_id'] == supplier, ann))
        result2 = list(filter(lambda announcement: announcement['a_date'] == date, result))
        return result2
