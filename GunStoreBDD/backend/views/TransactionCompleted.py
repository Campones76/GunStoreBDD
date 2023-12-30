
from flask import Blueprint, render_template
transaction_completed_bp = Blueprint('TransactionCompleted', __name__)

@transaction_completed_bp.route('/transaction_complete')
def transaction_complete():
    return render_template('transaction_complete.html')