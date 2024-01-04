from flask import Blueprint, render_template
import pyodbc
import datetime
from network.DBSTUFF import connection_string

license_renewal_bp = Blueprint('LicenseRenewalView', __name__)

@license_renewal_bp.route('/LicenseRenewal')
def license_renewal():
    # establish your database connection
    conn = pyodbc.connect(connection_string)

    cursor = conn.cursor()

    # get the current date and the date a month from now
    current_date = datetime.date.today()
    next_month = current_date + datetime.timedelta(days=30)

    # write your SQL query
    query = f"""
    SELECT lr.*, c.FullName, c.Contact 
    FROM LicenseRenewals lr
    INNER JOIN Customer c ON lr.CustomerID = c.CustomerID
    WHERE lr.RenewalDate BETWEEN '{current_date}' AND '{next_month}'
    """

    cursor.execute(query)
    users = cursor.fetchall()
    conn.close()
    # Now 'users' contains all users whose license renewal date is within the next month, along with the associated customer names
    # You can display this data in your template as needed
    return render_template('LicenseRenewalList.html', users=users)