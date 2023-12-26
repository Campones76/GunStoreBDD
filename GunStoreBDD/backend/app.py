import os
from flask import Flask
from backend.views.home import *
from backend.views.AccountStateView import *
from backend.views.SigninView import *
from backend.views.SignupView import *
from backend.views.dbteste import *
from backend.views.TosView import *


app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY
print(SECRET_KEY)

# Register Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(accountstate_bp)
app.register_blueprint(signin_bp)
app.register_blueprint(signup_bp)
app.register_blueprint(tosviewer_bp)
app.register_blueprint(dbteste_bp)

if __name__ == '__main__':
    app.run(debug=True)