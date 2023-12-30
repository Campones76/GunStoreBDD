from flask import Blueprint, redirect, render_template, session, url_for

from backend.forms.CustomerForm import UserForm

select_user_bp = Blueprint('SelectUser', __name__)

@select_user_bp.route('/select_user', methods=['GET', 'POST'])
def select_user():
    form = UserForm()
    if form.validate_on_submit():
        session['user_id'] = form.user.data
        return redirect(url_for('SelectFirearm.select_firearm'))
    return render_template('select_user.html', form=form)