import pypyodbc as odbc
from faker import Faker
from flask import Blueprint, jsonify, render_template

dbteste_bp = Blueprint('dbteste', __name__)

@dbteste_bp.route('/teste')
def teste():
    # Database connection and query logic here
    DRIVER_NAME = 'SQL SERVER'
    SERVER_NAME = 'SCHOOL594B'
    DATABASE_NAME = 'ArmasTeste'

    connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
    """
    fake = Faker()
    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    # Get the last id from the database
    cursor.execute("SELECT MAX(id) FROM dbo.test")
    last_id = cursor.fetchone()[0]

    if last_id is None:
        last_id = 0
    for i in range(1,11):
        name = fake.name()
        name = name[:9]
        new_id = last_id + i
        cursor.execute("SET IDENTITY_INSERT dbo.test ON")
        cursor.execute(f"INSERT INTO dbo.test(id, name) VALUES ({new_id}, '{name}')")
        cursor.execute("SET IDENTITY_INSERT dbo.test OFF")

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