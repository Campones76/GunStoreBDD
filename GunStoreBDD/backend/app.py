from flask import Flask
from backend.views.home import *
from backend.views.dbteste import *


app = Flask(__name__, template_folder='../frontend/templates', static_folder='../frontend/static')

# Register Blueprints
app.register_blueprint(home_bp)
app.register_blueprint(dbteste_bp)

if __name__ == '__main__':
    app.run(debug=True)