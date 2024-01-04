from datetime import datetime
from network.DBSTUFF import connection_string
from flask import Blueprint, redirect, render_template, session, url_for
from backend.forms.TransactionForm import TransactionForm
from backend.forms.CustomerForm import UserForm
import pyodbc

make_transaction_bp = Blueprint('MakeTransaction', __name__)

@make_transaction_bp.route('/make_transaction', methods=['GET', 'POST'])
def make_transaction():
    form = TransactionForm()
    if form.validate_on_submit():
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Transactions (CustomerID, FirearmID, TimeOfPurchase, PurchaseInvoice, Total, BackgroundCheckResults, WaitingPeriodInfo, AdditionalNotes) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                       session['user_id'], session['firearm_id'], datetime.now(), form.purchase_invoice.data, form.total.data, form.background_check_results.data, form.waiting_period_info.data, form.additional_notes.data)
        cursor.execute("UPDATE Firearms SET CustomerID = ?, OwnershipJustification = ?, Bought = 1 WHERE FirearmID = ?", session['user_id'], form.OwnershipJustification.data ,session['firearm_id'])
        cursor.execute("INSERT INTO CustomerFirearms (CustomerID, FirearmID) VALUES (?, ?)", session['user_id'], session['firearm_id'])
        conn.commit()
        conn.close()
        return redirect(url_for('TransactionCompleted.transaction_complete'))
    return render_template('make_transaction.html', form=form)
