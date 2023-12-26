import sys
import pypyodbc as odbc 
import queries as q

DRIVER = 'SQL SERVER'
SERVER_NAME = '(local)'
DATABASE_NAME = 'JobAppDB'

conn_string = f"""
        Driver={{{DRIVER}}};
        Server={SERVER_NAME};
        Database={DATABASE_NAME};
        Trust_Connection=yes;
"""
try:
    conn = odbc.connect(conn_string)
except Exception as e:
    print(e)
    print('task is terminated')
    sys.exit()
else:
    def save_to_db(fname,lname,dob,email,phone,currPosition,salaryExp,yrsExperience,degree,today,fileName):
        applications = [
                [fname,lname,dob,email,phone,currPosition,salaryExp,yrsExperience,degree,today,fileName]
             ]
        try:
            cursor = conn.cursor()
            cursor.execute(q.createTable_Application_Data)
            for app in applications:
                print(app)
                cursor.execute(q.insert_into_Application_Data,app)
        except Exception as e:
                cursor.rollback()
                print(e.value)
                print('insert tasks is rolledback')
                sys.exit()
        else:
             print('records inserted')
             cursor.commit()
             cursor.close()
        finally:
             if conn.connected == 1:
                  print('connection closed')
                  conn.close()

