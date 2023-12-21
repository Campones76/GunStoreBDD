from flask import Blueprint, render_template

accountstate_bp = Blueprint('AccountStateView', __name__)

@accountstate_bp.route('/account')
def accountstate():
    return render_template('accountstateview.html')