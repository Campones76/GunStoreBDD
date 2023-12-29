from flask import Blueprint, render_template

InventoryView_bp = Blueprint('InventoryView', __name__)

@InventoryView_bp.route('/InventoryView')
def inventory():
    return 200