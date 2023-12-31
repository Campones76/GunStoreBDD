from flask import Blueprint, redirect, render_template, session, url_for
from backend.forms.CustomerTransactionForm import UserTransactionForm



SelectUserTransactions_bp = Blueprint('SelectUserTransactions', __name__)

@SelectUserTransactions_bp.route('/selectusertransaction', methods=['GET', 'POST'])
def select_user():
    form = UserTransactionForm()
    if form.validate_on_submit():
        session['user_id'] = form.user.data
        return redirect(url_for('FilteredSalesView.filteredsalesview'))
    return render_template('select_user.html', form=form)