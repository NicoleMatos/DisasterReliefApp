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

@app.route('/clients/<int:c_id>/')
def getClientById(c_id):
    return ClientHandler().getClientById(c_id)

@app.route('/transactions/')
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

if __name__== '__main__':
    app.run()

