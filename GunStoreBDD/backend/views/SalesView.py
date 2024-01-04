from flask import Blueprint, redirect, render_template, request, url_for
from network.DBSTUFF import connection_string
import pyodbc

salesview_bp = Blueprint('SalesView', __name__)
@salesview_bp.route('/Sales', methods=['GET', 'POST'])
def salesview():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    #cursor.execute("SELECT * FROM dbo.Transactions")
    # write your SQL query
    query = f"""
    SELECT t.*, c.FullName 
    FROM Transactions t
    INNER JOIN Customer c ON t.CustomerID = c.CustomerID
    """
    cursor.execute(query)
    data = cursor.fetchall()
    conn.close()
    #cursor.execute("SELECT * FROM dbo.Transactions")
    #return render_template('InventoryView.html', data=data)
    return render_template('SalesView.html', data=data)