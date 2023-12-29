import os
from flask import Flask
from flask_bcrypt import Bcrypt
from backend.views.home import *
from backend.views.AccountStateView import *
from backend.views.SigninView import *
from backend.views.SignupView import *
from backend.views.TosView import *
from backend.views.adminchecker import *
from backend.views.StaffPanel import *
from backend.views.SalesView import *
from backend.views.LicenseRenewalView import *
from backend.views.InventoryView import *

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
bcrypt = Bcrypt(app)
login_manager.init_app(app)
@app.context_processor
def inject_user():
    return dict(user=current_user)
SECRET_KEY = os.urandom(32)

app.config['SECRET_KEY'] = SECRET_KEY
print(SECRET_KEY)
#app.config['WTF_CSRF_SECRET_KEY'] = 'your-csrf-secret-key'
# Register Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(accountstate_bp)
app.register_blueprint(signin_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(tosviewer_bp)
app.register_blueprint(adminchecker_bp)
app.register_blueprint(StaffPanel_bp)
app.register_blueprint(salesview_bp)
app.register_blueprint(license_renewal_bp)
app.register_blueprint(InventoryView_bp)
if __name__ == '__main__':
    app.run(debug=True)