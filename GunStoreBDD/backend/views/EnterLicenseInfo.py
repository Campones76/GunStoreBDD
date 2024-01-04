from flask import Blueprint, render_template, request, redirect, url_for, session
from backend.forms.LicenseInfoForm import LicenseInfoForm
from network.DBSTUFF import connection_string
import pyodbc

enter_license_info_bp = Blueprint('EnterLicenseInfo', __name__)


@enter_license_info_bp.route('/enter_license_info', methods=['GET', 'POST'])
def enter_license_info():
    form = LicenseInfoForm()
    if form.validate_on_submit():
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO LicenseRenewals (CustomerID, RenewalDate, ExpiryDate, RenewalProcessRecords) VALUES (?, ?, ?, ?)",
                       session['user_id'], form.renewal_date.data, form.expiry_date.data, form.renewal_process_records.data)
        conn.commit()
        conn.close()
        return redirect(url_for('MakeTransaction.make_transaction'))
    return render_template('enter_license_info.html', form=form)
