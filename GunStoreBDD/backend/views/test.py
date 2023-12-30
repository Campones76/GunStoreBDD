#Porquê? Para guardar-mos records de compras por exemplo, não sei
from flask import Blueprint, app, send_file, after_this_request
import pandas as pd
import pyodbc
from network.DBSTUFF import connection_string
import os

excelgen_bp = Blueprint('excelgen', __name__)

@excelgen_bp.route('/generate')
def generate():
   #Establish a connection to the database
   cnxn = pyodbc.connect(connection_string)

   # Create a cursor from the connection
   cursor = cnxn.cursor()

   # Execute a SQL query
   #cursor.execute("SELECT * FROM Customer")
   cursor.execute("SELECT * FROM dbo.Firearms")

   # Fetch all rows from the last executed statement
   rows = cursor.fetchall()

   # Get the column names from the cursor description
   columns = [column[0] for column in cursor.description]

   # Create a pandas DataFrame from the fetched data
   df = pd.DataFrame.from_records(rows, columns=columns)

   # Write the DataFrame to an Excel file
   name = 'purchases.xlsx'
   path = '//mac/Home/Documents/GitHub/GunStoreBDD/'
   file_path = path + name
   df.to_excel(file_path, index=False)

   # Return the Excel file as a download response
   return send_file(file_path, as_attachment=True)
