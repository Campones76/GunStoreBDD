from flask import Blueprint, render_template

salesview_bp = Blueprint('SalesView', __name__)

@salesview_bp.route('/Sales')
def sales():
    return 200