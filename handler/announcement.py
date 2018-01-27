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

    def build_resource_dict(self, row):
        result = {}
        result['r_id'] = row[0]
        result['r_category'] = row[1]
        result['r_name'] = row[2]
        result['r_description'] = row[3]
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


# ===================================================================================================================
#                                           get Resources by announcements
# ===================================================================================================================

    def getResourcesByAnnouncements(self):
        dao = AnnouncementDAO()
        if not dao.getResourcesByAnnouncements():
            return jsonify(Error='Resource Not Found.'), 404
        else:
            resource_list = dao.getResourcesByAnnouncements()
            result_list = []
            for row in resource_list:
                result = self.build_resource_dict(row)
                result_list.append(result)
            return jsonify(Resources=result_list)

# ===================================================================================================================
#                                          insert announcement
# ===================================================================================================================
    def insertAnnouncement(self, form):
        if form and len(form) == 7:
            s_id = form['s_id']
            r_id = form['r_id']
            a_price = form['a_price']
            a_date = form['a_date']
            a_sold_out = form['a_sold_out']
            a_initial_qty = form['a_initial_qty']
            a_curr_qty = form['a_curr_qty']
            if s_id and r_id and a_price and a_date and a_sold_out and a_initial_qty and a_curr_qty:
                dao = AnnouncementDAO()
                s_id = dao.insert(s_id, r_id, a_price, a_date, a_sold_out, a_initial_qty, a_curr_qty)
                result = {}
                result["s_id"] = s_id
                result["u_email"] = s_id
                result["u_password"] = r_id
                result["u_name"] = a_price
                result["u_last_name"] = a_date
                result["u_region"] = a_sold_out
                result["u_age"] = a_initial_qty
                result["s_bank_account"] = a_curr_qty
                return jsonify(Announcement=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

# ===================================================================================================================
#                                          put announcement
# ===================================================================================================================

    def putAnnouncementByID(self, form, a_id):
        if form and len(form) == 7:
            s_id = form['s_id']
            r_id = form['r_id']
            a_price = form['a_price']
            a_date = form['a_date']
            a_sold_out = form['a_sold_out']
            a_initial_qty = form['a_initial_qty']
            a_curr_qty = form['a_curr_qty']
            if s_id and r_id and a_price and a_date and a_sold_out and a_initial_qty and a_curr_qty and a_id:
                dao = AnnouncementDAO()
                s_id = dao.insert(s_id, r_id, a_price, a_date, a_sold_out, a_initial_qty, a_curr_qty, a_id)
                result = {}
                result["a_id"] = a_id
                result["s_id"] = s_id
                result["u_email"] = s_id
                result["u_password"] = r_id
                result["u_name"] = a_price
                result["u_last_name"] = a_date
                result["u_region"] = a_sold_out
                result["u_age"] = a_initial_qty
                result["s_bank_account"] = a_curr_qty
                return jsonify(Announcement=result), 201
            else:
                return jsonify(Error="Malformed post request")
        else:
            return jsonify(Error="Malformed post request")

# ===================================================================================================================
#                                          delete announcement
# ===================================================================================================================

    def deleteAnnouncementByID(self, a_id):
        dao = AnnouncementDAO()
        if not dao.getAnnouncementByID(a_id):
            return jsonify(Error="Announcement not found."), 404
        else:
            dao.delete(a_id)
            return jsonify(DeleteStatus="OK"), 200
