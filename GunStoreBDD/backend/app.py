import glob
import os
from threading import Thread
import time
from flask import Flask
from flask_bcrypt import Bcrypt
import schedule
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
from backend.views.AddInventory import *
from backend.views.test import *
from backend.views.SelectUser import *
from backend.views.SelectFirearm import *
from backend.views.CheckLicense import *
from backend.views.EnterLicenseInfo import *
from backend.views.TransactionCompleted import *
from backend.views.MakeTransaction import *
from backend.views.SelectUserTransactions import *
from backend.views.FilteredSalesView import *
from backend.views.Products import *
from backend.views.Sobre import *



# # Define the job that deletes .xlsx files
# def delete_xlsx_files():
#     files = glob.glob('//mac/Home/Documents/GitHub/GunStoreBDD/GunStoreBDD/temp/*.xlsx')
#     for file in files:
#         os.remove(file)

# # Schedule the job every 10 minutes
# schedule.every(1).minutes.do(delete_xlsx_files)

# # Define the runner function to start the scheduler in a separate thread
# def run_schedule():
#     while True:
#         schedule.run_pending()
#         time.sleep(1)

# # Start the scheduler in a separate thread
# Thread(target=run_schedule).start()

app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
bcrypt = Bcrypt(app)
login_manager.init_app(app)
@app.context_processor
def inject_user():
    return dict(user=current_user)
SECRET_KEY = "YOUR-SECRET-KEY-HERE"

app.config['SECRET_KEY'] = SECRET_KEY

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
app.register_blueprint(AddInventoryView_bp)
app.register_blueprint(excelgen_bp)
app.register_blueprint(select_user_bp)
app.register_blueprint(select_firearm_bp)
app.register_blueprint(check_license_bp)
app.register_blueprint(enter_license_info_bp)
app.register_blueprint(transaction_completed_bp)
app.register_blueprint(make_transaction_bp)
app.register_blueprint(SelectUserTransactions_bp)
app.register_blueprint(filteredsalesview_bp)
app.register_blueprint(products_page)
app.register_blueprint(sobre_page)

if __name__ == '__main__':
    app.run(debug=True)
