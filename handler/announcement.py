from flask import jsonify
from dao.announcement import AnnouncementDAO

class AnnouncementHandler:

    def build_announcement_dict(self, row):
            result = {}
            result['a_id'] = row[0]
            result['s_id'] = row[1]
            result['r_id'] = row[2]
            result['a_price'] = row[3]
            result['a_date'] = row[4]
            result['a_sold_out'] = row[5]
            result['a_initial_qty'] = row[6]
            result['a_curr_qty'] = row[7]
            return result

# ===================================================================================================================
#                                        search for announcements
# ===================================================================================================================

    def searchAnnouncements(self, args):
            supplier = args.get('s_id')
            date = args.get('a_date')
            region = args.get('region')
            dao = AnnouncementDAO()
            if (len(args) == 2) and supplier and date:
                announcement_list = dao.getAnnouncementsBySupplierAndDate(supplier,date)
            elif (len(args) == 1) and supplier:
                announcement_list = dao.getAnnouncementsBySupplier(supplier)
            elif (len(args) == 1) and date:
                announcement_list = dao.getAnnouncementsByDate(date)
            elif (len(args) == 1) and region:
                announcement_list = dao.getAnnouncementByRegion(region)
            else:
                return jsonify(Error="Malformed query string"), 400
            result_list = []
            for row in announcement_list:
                result = self.build_announcement_dict(row)
                result_list.append(result)
            if len(result_list) == 0:
                return jsonify(Error="Announcement Not Found"), 404
            return jsonify(Announcement=result_list)

# ===================================================================================================================
#                                           get all announcements
# ===================================================================================================================

    def getAllAnnouncements(self):
            dao = AnnouncementDAO()
            resources_list = dao.getAllAnnouncements()
            result_list = []
            for row in resources_list:
                result = self.build_announcement_dict(row)
                result_list.append(result)
            if len(result_list) == 0:
                return jsonify(Error="Announcement Not Found"), 404
            return jsonify(Announcement=result_list)

# ===================================================================================================================
#                                           get announcement by ID
# ===================================================================================================================

    def getAnnouncementByID(self, a_id):
            dao = AnnouncementDAO()
            row = dao.getAnnouncementByID(a_id)
            if not row:
                return jsonify(Error="Announcement Not Found"), 404
            else:
                result = self.build_announcement_dict(row)
            return jsonify(Announcement=result)
