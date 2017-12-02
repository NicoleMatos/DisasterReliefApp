from flask import Flask, jsonify
from handler.supplier import SupplierHandler

app = Flask(__name__)


@app.route('/')
def home():
    return 'Disaster Relief'


@app.route('/suppliers/')
def getAllSuppliers():
    return SupplierHandler().getAllSuppliers()


if __name__== '__main__':
    app.run()

