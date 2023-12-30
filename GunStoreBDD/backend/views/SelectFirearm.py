from flask import Blueprint, redirect, render_template, session, url_for
from backend.forms.FirearmsForm import FirearmForm

select_firearm_bp = Blueprint('SelectFirearm', __name__)

@select_firearm_bp.route('/select_firearm', methods=['GET', 'POST'])
def select_firearm():
    form = FirearmForm()
    if form.validate_on_submit():
        session['firearm_id'] = form.firearm.data
        return redirect(url_for('CheckLicense.check_license'))
    return render_template('select_firearm.html', form=form)
