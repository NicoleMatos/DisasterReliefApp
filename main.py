from flask import Flask, jsonify, request
from handler.supplier import SupplierHandler
from handler.client import ClientHandler
from handler.transaction import TransactionHandler
from handler.announcement import AnnouncementHandler
from handler.administrator import AdministratorHandler
from handler.request import RequestHandler
from handler.resource import ResourceHandler
from handler.ccard import CCardHandler
from handler.address import AddressHandler
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

@app.route('/suppliers/', methods=['GET', 'POST'])
def getAllSuppliers():
    if request.method == 'POST':
        return SupplierHandler().insertSupplier(request.form)
    else:
        if not request.args:
            return SupplierHandler().getAllSuppliers()
        else:
            return SupplierHandler().searchSuppliers(request.args)


@app.route('/suppliers/<int:s_id>/', methods=['GET', 'PUT', 'DELETE'])
def getSupplierByID(s_id):
    if request.method == 'GET':
        return SupplierHandler().getSupplierByID(s_id)
    elif request.method == 'PUT':
        return SupplierHandler().putSupplierByID(request.form, s_id)
    elif request.method == 'DELETE':
        return SupplierHandler().deleteSupplierByID(s_id)
    else:
        return jsonify(Error="Method not allowed"), 405


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


@app.route('/clients/', methods=['GET', 'POST'])
def getAllClients():
    if request.method == 'POST':
        return ClientHandler().insertClient(request.form)
    else:
        if not request.args:
            return ClientHandler().getAllClients()
        else:
            return ClientHandler().searchClients(request.args)


@app.route('/clients/<int:c_id>/', methods=['GET', 'PUT', 'DELETE'])
def getClientByID(c_id):
    if request.method == 'GET':
        return ClientHandler().getClientByID(c_id)
    elif request.method == 'PUT':
        return ClientHandler().putClientByID(request.form, c_id)
    elif request.method == 'DELETE':
        return ClientHandler().deleteClientByID(c_id)
    else:
        return jsonify(Error="Method not allowed"), 405

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

@app.route('/transactions/', methods=['GET', 'POST'])
def getAllTransactions():
    if request.method == 'POST':
        return TransactionHandler().insertTransaction(request.form)
    else:
        if not request.args:
            return TransactionHandler().getAllTransactions()
        else:
            return TransactionHandler().searchTransactions(request.args)


@app.route('/transactions/<int:t_id>/', methods=['GET', 'PUT', 'DELETE'])
def getTransactionByID(t_id):
    if request.method == 'GET':
        return TransactionHandler().getTransactionByID(t_id)
    elif request.method == 'PUT':
        return TransactionHandler().putTransactionByID(request.form, t_id)
    elif request.method == 'DELETE':
        return TransactionHandler().deleteTransactionByID(t_id)
    else:
        return jsonify(Error="Method not allowed"), 405


# =======================================================================================================================
#                                           announcements routes
# =======================================================================================================================

@app.route('/announcements/', methods=['GET', 'POST'])
def getAllAnnouncements():
    if request.method == 'POST':
        return AnnouncementHandler().insertAnnouncement(request.form)
    else:
        if not request.args:
            return AnnouncementHandler().getAllAnnouncements()
        else:
            return AnnouncementHandler().searchAnnouncements(request.args)


@app.route('/announcements/<int:a_id>/', methods=['GET', 'PUT', 'DELETE'])
def getAnnouncementByID(a_id):
    if request.method == 'GET':
        return AnnouncementHandler().getAnnouncementByID(a_id)
    elif request.method == 'PUT':
        return AnnouncementHandler().putAnnouncementByID(request.form, a_id)
    elif request.method == 'DELETE':
        return AnnouncementHandler().deleteAnnouncementByID(a_id)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/announcements/resources/')
def getResourcestByAnnouncements():
    return AnnouncementHandler().getResourcesByAnnouncements()


# =======================================================================================================================
#                                           requests routes
# =======================================================================================================================

@app.route('/requests/', methods=['GET', 'POST'])
def getAllRequests():
    if request.method == 'POST':
        return RequestHandler().insertRequest(request.form)
    else:
        if not request.args:
            return RequestHandler().getAllRequests()
        else:
            return RequestHandler().searchRequests(request.args)


@app.route('/requests/<int:req_id>/', methods=['GET', 'PUT', 'DELETE'])
def getRequestByID(req_id):
    if request.method == 'GET':
        return RequestHandler().getRequestByID(req_id)
    elif request.method == 'PUT':
        return RequestHandler().putRequestByID(request.form, req_id)
    elif request.method == 'DELETE':
        return RequestHandler().deleteRequestByID(req_id)
    else:
        return jsonify(Error="Method not allowed"), 405


@app.route('/requests/<int:req_id>/resources/')
def getResourcestByRequestID(req_id):
    return RequestHandler().getResourcestByRequestID(req_id)


@app.route('/requests/resources/')
def getResourcestByRequests():
    return RequestHandler().getResourcestByRequests()


# =======================================================================================================================
#                                           resources routes
# =======================================================================================================================

@app.route('/resources/', methods=['GET', 'POST'])
def getAllResources():
    if request.method == 'POST':
        return ResourceHandler().insertResource(request.form)
    else:
        if not request.args:
            return ResourceHandler().getAllResources()
        else:
            return ResourceHandler().searchResources(request.args)


@app.route('/resources/<int:r_id>/', methods=['GET', 'PUT'])
def getResourceByID(r_id):
    if request.method == 'GET':
        return ResourceHandler().getResourceByID(r_id)
    elif request.method == 'PUT':
        return ResourceHandler().putResourceById(request.form, r_id)
    else:
        return jsonify(Error="Method not allowed"), 405


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
@app.route('/creditcards/', methods=['GET', 'POST'])
def getAllCCards():
    if request.method == 'POST':
        return CCardHandler().insertCCard(request.form)
    else:
        if not request.args:
            return CCardHandler().getAllCCards()
        else:
            return CCardHandler().searchCCards(request.args)


@app.route('/creditcards/<int:cc_id>/', methods=['GET', 'PUT', 'DELETE'])
def getCCardByID(cc_id):
    if request.method == 'GET':
        return CCardHandler().getCCardByID(cc_id)
    elif request.method == 'PUT':
        return CCardHandler().putCCardByClientID(request.form, cc_id)
    elif request.method == 'DELETE':
        return CCardHandler().deleteCCardByID(cc_id)
    else:
        return jsonify(Error="Method not allowed"), 405



# =======================================================================================================================
#                                        addresses routes
# =======================================================================================================================

@app.route('/addresses/')
def getAllAddresses():
    if not request.args:
        return AddressHandler().getAllAddresses()
    else:
        return AddressHandler().searchAddresses(request.args)


@app.route('/addresses/<int:cc_id>/')
def getAddressByID(add_id):
    return AddressHandler().getAddressByID(add_id)


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

@app.route('/administrators/', methods=['GET', 'POST'])
def getAllAdministrators():
    if request.method == 'POST':
        return AdministratorHandler().insertAdministrator(request.form)
    else:
        if not request.args:
            return AdministratorHandler().getAllAdministrators()
        else:
            return AdministratorHandler().searchAdministrator(request.args)


@app.route('/administrators/<int:ad_id>/', methods=['GET', 'PUT', 'DELETE'])
def getAdministratorByID(ad_id):
    if request.method == 'GET':
        return AdministratorHandler().getAdministratorByID(ad_id)
    elif request.method == 'PUT':
        return AdministratorHandler().putAdministratorByID(request.form, ad_id)
    elif request.method == 'DELETE':
        return AdministratorHandler().deleteAdministratorByID(ad_id)
    else:
        return jsonify(Error="Method not allowed"), 405


# =======================================================================================================================
#                                                run
# =======================================================================================================================

if __name__ == '__main__':
    app.run()
