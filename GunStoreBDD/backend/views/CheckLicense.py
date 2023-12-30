from flask import Blueprint, redirect, render_template, request, session, url_for
from backend.forms.LicenseForm import LicenseForm
from network.DBSTUFF import connection_string
import pyodbc

check_license_bp = Blueprint('CheckLicense', __name__)

@check_license_bp.route('/check_license', methods=['GET', 'POST'])
def check_license():
    form = LicenseForm()
    if form.validate_on_submit():
        if form.has_license.data:
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
            cursor.execute("UPDATE Customer SET HasLicense = 1 WHERE CustomerID = ?", session['user_id'])
            conn.commit()
            return redirect(url_for('EnterLicenseInfo.enter_license_info'))
        else:
            return render_template('no_license.html')
    return render_template('check_license.html', form=form)