from flask import Blueprint, redirect, render_template, request, session, url_for
from network.DBSTUFF import connection_string
import pyodbc

filteredsalesview_bp = Blueprint('FilteredSalesView', __name__)
@filteredsalesview_bp.route('/FilteredSales', methods=['GET', 'POST'])
def filteredsalesview():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.Transactions WHERE CustomerID = ?", session['user_id'])
    data = cursor.fetchall()
    return render_template('SalesView.html', data=data)