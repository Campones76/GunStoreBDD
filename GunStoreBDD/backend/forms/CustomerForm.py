from flask_wtf import FlaskForm
from wtforms import SelectField, SubmitField
from wtforms.validators import DataRequired
from network.DBSTUFF import connection_string
import pyodbc

# Establish a database connection
conn = pyodbc.connect(connection_string)

# Create a cursor
cursor = conn.cursor()

# Fetch the users
cursor.execute("SELECT CustomerID, UserName FROM Customer WHERE Staff = 0")
users = cursor.fetchall()

# Create a list of tuples for the select field choices
choices = [(user.CustomerID, user.UserName) for user in users]

class UserForm(FlaskForm):
    user = SelectField('User', choices=choices, validators=[DataRequired()])
    submit = SubmitField('Select')
