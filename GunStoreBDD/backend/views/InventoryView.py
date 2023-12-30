# InventoryView.py
from flask import Blueprint, redirect, render_template, request, url_for
from flask_login import login_required
from network.DBSTUFF import connection_string
import pyodbc

InventoryView_bp = Blueprint('InventoryView', __name__)


@InventoryView_bp.route('/InventoryView/', methods=['GET', 'POST'])
def inventory():
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.Firearms WHERE bought = 0")
    data = cursor.fetchall()
    return render_template('InventoryView.html', data=data)  # replace 'your_html_file.html' with the name of your HTML file