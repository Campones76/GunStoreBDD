from flask import Blueprint, render_template

license_renewal_bp = Blueprint('LicenseRenewalView', __name__)

@license_renewal_bp.route('/LicenseRenewal')
def license_renewal():
    return 200