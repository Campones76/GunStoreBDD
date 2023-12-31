from flask import Blueprint, redirect, render_template, request, url_for
from network.DBSTUFF import connection_string
import pyodbc

salesview_bp = Blueprint('SalesView', __name__)
@salesview_bp.route('/Sales', methods=['GET', 'POST'])
def salesview():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.Transactions")
    data = cursor.fetchall()
    #return render_template('InventoryView.html', data=data)  # replace 'your_html_file.html' with the name of your HTML file
    return render_template('SalesView.html', data=data)