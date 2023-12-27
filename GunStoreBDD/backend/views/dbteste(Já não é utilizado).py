import pyodbc as odbc
from network.DBSTUFF import connection_string
from faker import Faker
from flask import Blueprint, jsonify, render_template

dbteste_bp = Blueprint('dbteste', __name__)

@dbteste_bp.route('/teste')
def teste():
    fake = Faker()
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    # Get the last id from the database
    cursor.execute("SELECT MAX(IdAdmin) FROM dbo.Admin")
    last_id = cursor.fetchone()[0]

    if last_id is None:
        last_id = 0
    for i in range(1,11):
        name = fake.name()
        name = name[:9]
        password = fake.password()
        password = password[:9]

        new_id = last_id + i
        cursor.execute("SET IDENTITY_INSERT dbo.Admin ON")
        cursor.execute(f"INSERT INTO dbo.Admin(IdAdmin, NomeAdmin, PasswordAdmin) VALUES ({new_id}, '{name}', '{password}')")
        cursor.execute("SET IDENTITY_INSERT dbo.Admin OFF")

    conn.commit()
    return 'Inserted 10 random names into the database', 200

    # cursor.execute("INSERT INTO dbo.test(id,name) VALUES (?,?)",('13','ESCREVEU'))
    # #results = cursor.fetchall()
    # cursor.commit()

    # conn.close()
    # conn = odbc.connect(connection_string)
    # cursor = conn.cursor()
    # cursor.execute('SELECT * FROM dbo.test')
    # results = cursor.fetchall()
    # # Convert the results to a list of dictionaries for JSON serialization
    # data = [dict(zip([column[0] for column in cursor.description], row)) for row in results]
    # return jsonify(data)