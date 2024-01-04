from flask_bcrypt import Bcrypt
from flask import Blueprint, app, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from network.DBSTUFF import connection_string
import pyodbc

# Initialize Flask-Login
login_manager = LoginManager()
bcrypt = Bcrypt()

signin_bp = Blueprint('SigninView', __name__)

class User(UserMixin):
    def __init__(self, id, Staff):
        self.id = id
        self.Staff = Staff

@login_manager.user_loader
def load_user(user_id):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.Customer WHERE CustomerID = ?', (user_id,))
   # cursorstaff = conn.cursor()
    #cursorstaff.execute('SELECT staff FROM dbo.Admin WHERE IdAdmin = ?', (user_id,))
    account = cursor.fetchone()
    if account:
        return User(account.CustomerID, Staff=account.Staff)
    return None

@signin_bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM dbo.Customer WHERE UserName = ?', (username,))
        account = cursor.fetchone()
        conn.close()
        if account:
            if account.Deactivated == 1:
                msg = 'This user account was deactivated and its personal data removed because the user made a GDPR takedown request.'
                return render_template('signin.html', msg=msg)
            elif bcrypt.check_password_hash(account.Password, password):
                user = User(account.CustomerID, Staff=account.Staff)
                login_user(user)
                return redirect(url_for('home.index'))
            else:
                msg = 'Incorrect username/password!'
                return render_template('signin.html', msg=msg)
    return render_template('signin.html', msg='')

@signin_bp.route('/login/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('SigninView.login'))