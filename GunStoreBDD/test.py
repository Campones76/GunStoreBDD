import pypyodbc as odbc 
from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/teste')
def teste():
    # Your database connection and query logic here
    DRIVER_NAME = 'SQL SERVER'
    SERVER_NAME = 'SCHOOL594B'
    DATABASE_NAME = 'ArmasTeste'

    connection_string = f"""
        DRIVER={{{DRIVER_NAME}}};
        SERVER={SERVER_NAME};
        DATABASE={DATABASE_NAME};
        Trust_Connection=yes;
    """

    conn = odbc.connect(connection_string)
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.test')
    results = cursor.fetchall()

    # Convert the results to a list of dictionaries for JSON serialization
    data = [dict(zip([column[0] for column in cursor.description], row)) for row in results]

    conn.close()

    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)