from flask import Flask, jsonify
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
    return SupplierHandler().getAllSuppliers()

@app.route('/clients/')
def getAllClients():
    return ClientHandler().getAllClients()

@app.route('/transaction/')
def getAllTransactions():
    return TransactionHandler().getAllTransactions()

@app.route('/announcements/')
def getAllAnnouncements():
    return AnnouncementHandler().getAllAnnouncements()

@app.route('/requests/')
def getAllRequests():
    return RequestHandler().getAllRequests()

@app.route('/resources/')
def getAllResources():
    return ResourceHandler().getAllResources()

@app.route('/creditcards/')
def getAllCCards():
    return CCardHandler().getAllCCards()

@app.route('/users/')
def getAllUsers():
    return UserHandler().getAllUsers()

@app.route('/client/<int:c_id>/')
def getClientByID():
    return ClientHandler().getClientByID()

@app.route('/client/<int:c_id>/suppliers')
def getSuppliersByClientID():
    return ClientHandler().getSuppliersByClientID()

@app.route('/client/<int:c_id>/transastions')
def getTransactionsByClientID():
    return ClientHandler().getTransactionsByClientID()

@app.route('/client/<int:c_id>/requests')
def getRequestsByClientID():
    return ClientHandler().getRequestsByClientID()

@app.route('/client/<int:c_id>/creditcard')
def getCreditCardsByClientID():
    return ClientHandler().getCreditCardsByClientID()

@app.route('/client/<c_name>/suppliers')
def getSuppliersByClientName():
    return ClientHandler().getSuppliersByClientID()

@app.route('/client/<c_name>/transastions')
def getTransactionsByClientName():
    return ClientHandler().getTransactionsByClientID()

@app.route('/client/<c_id>/requests')
def getRequestsByClientName():
    return ClientHandler().getRequestsByClientID()

@app.route('/client/<c_id>/creditcard')
def getCreditCardsByClientID():
    return ClientHandler().getCreditCardsByClientID()

if __name__== '__main__':
    app.run()

