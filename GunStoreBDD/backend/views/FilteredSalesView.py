from flask import Blueprint, redirect, render_template, request, session, url_for
from network.DBSTUFF import connection_string
import pyodbc

filteredsalesview_bp = Blueprint('FilteredSalesView', __name__)
@filteredsalesview_bp.route('/FilteredSales', methods=['GET', 'POST'])
def filteredsalesview():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    query = "SELECT t.*, c.FullName FROM Transactions t INNER JOIN Customer c ON t.CustomerID = c.CustomerID WHERE Deactivated = 0 AND t.CustomerID = ?"
    params = (session['user_id'],)
    cursor.execute(query, params)
    data = cursor.fetchall()
    conn.close()
    return render_template('SalesView.html', data=data)