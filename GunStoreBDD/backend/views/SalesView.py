from flask import Blueprint, redirect, render_template, request, url_for
from network.DBSTUFF import connection_string
import pyodbc

salesview_bp = Blueprint('SalesView', __name__)
@salesview_bp.route('/Sales', methods=['GET'])
def salesview():
    return 200