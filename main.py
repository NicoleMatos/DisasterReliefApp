from flask import Flask, jsonify, request
from handler.supplier import SupplierHandler
from handler.client import ClientHandler
from handler.transaction import TransactionHandler
from handler.announcement import AnnouncementHandler
from handler.administrator import AdministratorHandler
from handler.request import RequestHandler
from handler.resource import ResourceHandler
from handler.ccard import CCardHandler
from handler.user import UserHandler


app = Flask(__name__)


# =======================================================================================================================
#                                              home route
# =======================================================================================================================

@app.route('/')
def home():
    return 'Disaster Relief Welcome Manuel Rodriguez! Hope you enjoy it.'


# =======================================================================================================================
#                                           suppliers routes
# =======================================================================================================================

@app.route('/suppliers/')
def getAllSuppliers():
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    else:
        return SupplierHandler().searchSuppliers(request.args)

@app.route('/suppliers/<int:s_id>/')
def getSupplierByID(s_id):
    return SupplierHandler().getSupplierByID(s_id)


@app.route('/suppliers/<int:s_id>/announcements/')
def getAnnouncementsBySupplierID(s_id):
    return SupplierHandler().getAnnouncementsBySupplierID(s_id)

@app.route('/suppliers/<int:s_id>/resources/')
def getResourcesBySupplierID(s_id):
    return SupplierHandler().getResourcesBySupplierID(s_id)

@app.route('/suppliers/<int:s_id>/transactions/')
def getTransactionsBySupplierID(s_id):
    return SupplierHandler().getTransactionsBySupplierID(s_id)

@app.route('/suppliers/<region>/resources')
def getResourcesByRegion(region):
    return SupplierHandler().getResourcesByRegion(region)


# =======================================================================================================================
#                                           clients routes
# =======================================================================================================================

@app.route('/clients/')
def getAllClients():
    if not request.args:
        return ClientHandler().getAllClients()
    else:
        return ClientHandler().searchClients(request.args)


@app.route('/clients/<int:c_id>/')
def getClientByID(c_id):
    return ClientHandler().getClientByID(c_id)


@app.route('/clients/<int:c_id>/requests/')
def getRequestsByClientID(c_id):
    return ClientHandler().getRequestsByClientID(c_id)


@app.route('/clients/<int:c_id>/transactions/')
def getTransactionsByClientID(c_id):
    return ClientHandler().getTransactionsByClientID(c_id)


@app.route('/clients/<int:c_id>/creditcards/')
def getCCardsByClientID(c_id):
    return ClientHandler().getCreditCardsByClientID(c_id)

@app.route('/clients/<int:c_id>/suppliers/')
def getSupplierByClientID(c_id):
    return ClientHandler().getSuppliersByClientID(c_id)


# =======================================================================================================================
#                                           transactions routes
# =======================================================================================================================

@app.route('/transactions/')
def getAllTransactions():
    if not request.args:
        return TransactionHandler().getAllTransactions()
    else:
        return TransactionHandler().searchTransactions(request.args)

@app.route('/transactions/<int:t_id>/')
def getTransactionByID(t_id):
    return TransactionHandler().getTransactionByID(t_id)

# =======================================================================================================================
#                                           announcements routes
# =======================================================================================================================

@app.route('/announcements/')
def getAllAnnouncements():
    if not request.args:
        return AnnouncementHandler().getAllAnnouncements()
    else:
        return AnnouncementHandler().searchAnnouncements(request.args)


@app.route('/announcements/<int:a_id>/')
def getAnnouncementByID(a_id):
    return AnnouncementHandler().getAnnouncementByID(a_id)

@app.route('/announcements/resources/')
def getResourcestByAnnouncements():
    return AnnouncementHandler().getResourcesByAnnouncements()


# =======================================================================================================================
#                                           requests routes
# =======================================================================================================================

@app.route('/requests/')
def getAllRequests():
    if not request.args:
        return RequestHandler().getAllRequests()
    else:
        return RequestHandler().searchRequests(request.args)


@app.route('/requests/<int:req_id>/')
def getRequestByID(req_id):
    return RequestHandler().getRequestByID(req_id)

@app.route('/requests/<int:req_id>/resources/')
def getResourcestByRequestID(req_id):
    return RequestHandler().getResourcestByRequestID(req_id)

@app.route('/requests/resources/')
def getResourcestByRequests():
    return RequestHandler().getResourcestByRequests()

# =======================================================================================================================
#                                           resources routes
# =======================================================================================================================

@app.route('/resources/')
def getAllResources():
    if not request.args:
        return ResourceHandler().getAllResources()
    else:
        return ResourceHandler().searchResources(request.args)

@app.route('/resources/<int:r_id>/')
def getResourceByID(r_id):
  return ResourceHandler().getResourceByID(r_id)

@app.route('/resources/<category>/requests/')
def getRequestsByResourceCategory(category):
    return ResourceHandler().getRequestsByResourceCategory(category)

@app.route('/resources/<category>/announcements/')
def getAnnouncementsByResourceCategory(category):
    return ResourceHandler().getAnnouncementsByResourceCategory(category)

@app.route('/resources/<name>/suppliers/')
def getSuppliersByResourceName(name):
    return ResourceHandler().getSuppliersByResourceName(name)

# =======================================================================================================================
#                                        credit cards routes
# =======================================================================================================================

@app.route('/creditcards/')
def getAllCCards():
    if not request.args:
        return CCardHandler().getAllCCards()
    else:
        return CCardHandler().searchCCards(request.args)


@app.route('/ccards/<int:cc_id>/')
def getCCardByID(cc_id):
    return CCardHandler().getCCardByID(cc_id)


# =======================================================================================================================
#                                           users routes
# =======================================================================================================================

@app.route('/users/')
def getAllUsers():
    if not request.args:
        return UserHandler().getAllUsers()
    else:
        return UserHandler().searchUsers(request.args)


@app.route('/suppliers/<int:s_id>/')
def getUserByID(u_id):
    return UserHandler().getUserByID(u_id)

# =======================================================================================================================
#                                           administrators routes
# =======================================================================================================================

@app.route('/administrators/')
def getAllAdministrators():
    if not request.args:
        return AdministratorHandler().getAllAdministrators()
    else:
        return AdministratorHandler().searchAdministrator(request.args)


@app.route('/administrators/<int:a_id>/')
def getAdministratorByID(a_id):
    return AdministratorHandler().getAdministratorByID(a_id)


# =======================================================================================================================
#                                                run
# =======================================================================================================================

if __name__ == '__main__':
    app.run()
