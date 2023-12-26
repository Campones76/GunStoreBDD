from flask import Blueprint, app, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, current_user, login_user, login_required, logout_user
from network.DBSTUFF import connection_string
import pyodbc

# Initialize Flask-Login
login_manager = LoginManager()


signin_bp = Blueprint('SigninView', __name__)

class User(UserMixin):
    def __init__(self, id, staff):
        self.id = id
        self.staff = staff

@login_manager.user_loader
def load_user(user_id):
    conn = pyodbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.Admin WHERE IdAdmin = ?', (user_id,))
   # cursorstaff = conn.cursor()
    #cursorstaff.execute('SELECT staff FROM dbo.Admin WHERE IdAdmin = ?', (user_id,))
    account = cursor.fetchone()
    if account:
        return User(account.IdAdmin, staff=account.staff)
    return None

@signin_bp.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST' and 'username' in request.form and 'password' in request.form:
        username = request.form['username']
        password = request.form['password']
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute('SELECT * FROM dbo.Admin WHERE NomeAdmin = ? AND PasswordAdmin = ?', (username, password,))
        account = cursor.fetchone()
        if account:
            user = User(account.IdAdmin, staff=account.staff)
            login_user(user)
            #return 'Logged in successfully!'
            return render_template('index.html')
        else:
            msg = 'Incorrect username/password!'
            return render_template('signin.html', msg=msg)
    return render_template('signin.html', msg='')

@signin_bp.route('/login/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('SigninView.login'))