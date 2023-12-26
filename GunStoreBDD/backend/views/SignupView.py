import pypyodbc as odbc
from flask import Blueprint, render_template, request
from .forms import RegistrationForm

signup_bp = Blueprint('SignupView', __name__)

@signup_bp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        connection_string = 'Driver={SQL Server};Server=school594b;Database=TesteArmas;Trusted_Connection=yes;'
        conn = odbc.connect(connection_string)
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dbo.lol (name, email, password) VALUES (?, ?, ?)", (form.username.data, form.email.data, form.password.data))
        conn.commit()
        return 'Thanks for registering!'
    return render_template('signup.html', form=form)
# def register():
#     # Handle signup
#     form = RegistrationForm()
#     if form.is_submitted():
#         result = request.form
#         #return render_template('user.html', form=result)
#         return render_template('signup.html', form=form)
    