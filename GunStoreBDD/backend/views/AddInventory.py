from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required, current_user
from network.DBSTUFF import connection_string
import pyodbc

AddInventoryView_bp = Blueprint('AddInventoryView', __name__)

@AddInventoryView_bp.route('/addInventory', methods=['GET', 'POST'])
@login_required
def add_inventory():
    if request.method == 'POST':
        SerialNum = request.form['SerialNum']
        Type = request.form['Type']
        Maker_Model = request.form['Maker_Model']
        Calibre = request.form['Calibre']
        DateOfPurchase = request.form['DateOfPurchase']
        OwenershipJustification = request.form['OwenershipJustification']
        StorageDetails = request.form['StorageDetails']
        NIF = 284728632
        Bought = 0
        CustomerID = current_user.id  # get the current user's id

        conn = pyodbc.connect(connection_string)  # replace with your connection string
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dbo.Firearms (CustomerID, SerialNum, Type, Maker_Model, Calibre, DateOfPurchase, OwnershipJustification, StorageDetails, NIF, Bought) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                       (CustomerID, SerialNum, Type, Maker_Model, Calibre, DateOfPurchase, OwenershipJustification, StorageDetails, NIF, Bought))
        conn.commit()
        return redirect(url_for('InventoryView.inventory'))
    return render_template('AddToInventory.html')