from flask import Flask, jsonify, request
from handler.supplier import SupplierHandler
from handler.client import ClientHandler
from handler.transaction import TransactionHandler
from handler.announcement import AnnouncementHandler
from handler.request import RequestHandler
from handler.resource import ResourceHandler
from handler.ccard import CCardHandler
from handler.user import UserHandler

app = Flask(__name__)


@app.route('/')
def home():
    return 'Disaster Relief'


@app.route('/suppliers/')
def getAllSuppliers():
    if not request.args:
        return SupplierHandler().getAllSuppliers()
    else:
        return SupplierHandler().searchSuppliers(request.args)


@app.route('/clients/')
def getAllClients():
    if not request.args:
        return ClientHandler().getAllClients()
    else:
        return ClientHandler().searchClients(request.args)


@app.route('/transaction/')
def getAllTransactions():
    if not request.args:
        return TransactionHandler().getAllTransactions()
    else:
        return TransactionHandler().searchTransactions(request.args)


@app.route('/announcements/')
def getAllAnnouncements():
    if not request.args:
        return AnnouncementHandler().getAllAnnouncements()
    else:
        return AnnouncementHandler().searchAnnouncements(request.args)


@app.route('/requests/')
def getAllRequests():
    if not request.args:
        return RequestHandler().getAllRequests()
    else:
        return RequestHandler().searchRequests(request.args)


@app.route('/resources/')
def getAllResources():
    if not request.args:
        return ResourceHandler().getAllResources()
    else:
        return ResourceHandler().searchResources(request.args)


@app.route('/creditcards/')
def getAllCCards():
    if not request.args:
        return CCardHandler().getAllCCards()
    else:
        return CCardHandler().searchCCards(request.args)


@app.route('/users/')
def getAllUsers():
    if not request.args:
        return UserHandler().getAllUsers()
    else:
        return UserHandler().searchUsers(request.args)



@app.route('/suppliers/<int:s_id>/')
def getSupplierByID(s_id):
    if not request.args:
        return SupplierHandler().getSupplierByID(s_id)

@app.route('/clients/<int:s_id>/')
def getClientByID(c_id):
    if not request.args:
        return ClientHandler().getClientByID(c_id)

@app.route('/transactions/<int:s_id>/')
def getTransactionByID(t_id):
    if not request.args:
        return TransactionHandler().getTransactionByID(t_id)

@app.route('/announcement/<int:s_id>/')
def getAnnouncementByID(a_id):
    if not request.args:
        return AnnouncementHandler().getAnnouncementByID(a_id)

@app.route('/requests/<int:s_id>/')
def getRequestByID(r_id):
    if not request.args:
        return RequestHandler().getRequestByID(r_id)

@app.route('/ccards/<int:cc_id>/')
def getCCardByID(cc_id):
    if not request.args:
        return CCardHandler().getCCardByID(cc_id)

@app.route('/resources/<int:r_id>/')
def getResourceByID(r_id):
    if not request.args:
        return ResourceHandler().getResourceByID(r_id)

@app.route('/suppliers/<int:s_id>/')
def getUserByID(u_id):
    if not request.args:
        return UserHandler().getUserByID(u_id)


if __name__ == '__main__':
app.run()


