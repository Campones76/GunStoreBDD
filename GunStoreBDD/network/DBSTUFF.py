DRIVER_NAME = 'ODBC Driver 17 for SQL Server'
SERVER_NAME = 'SCHOOL594B'
DATABASE_NAME = 'GunStore'
UID = 'GunstoreStaff'
PWD = '1234'

connection_string = f"""
    DRIVER={{{DRIVER_NAME}}};
    SERVER={SERVER_NAME};
    DATABASE={DATABASE_NAME};
    PWD={PWD};
    UID={UID};
    Trust_Connection=yes;
"""
