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
    name = request.args.get('name')
    lastname = request.args.get('lastname')
    if name:
        return SupplierHandler().getSupplierByName(name)
    if lastname:
        return SupplierHandler().getSupplierByNameAndLastName(name, lastname)
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




@app.route('/suppliers/<int:s_id>/')
def getSupplierByID(s_id):
    return SupplierHandler().getSupplierByID(s_id)



if __name__ == '__main__':
app.run()


