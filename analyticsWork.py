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
    def analytics():
        try:
            cursor = conn.cursor()
            #cursor.execute(q.createTable_Application_Data)

            cursor.execute(q.count_app_data)
            for row in cursor:
                print('Number of Applications: ', row[0])

            print('Average Experience and Salary Expectations: ')
            cursor.execute(q.avg_experience_salary_exp)
            for row in cursor:
                print('AVG_Salary_Expectation: ',row[0])
                print('AVG_Years_of_Experience: ',row[1])
            
            print('All Applications: ')
            cursor.execute(q.pull_app_data)
            for row in cursor:
                 print('--------------------------------------------')
                 print('Application ID: ',row[0])
                 print('First Name: ', row[1])
                 print('Last Name: ',row[2])
                 print('Email: ',row[3])
                 print('Date of Birth: ',row[4])
                 print('Phone: ',row[5])
                 print('Current Position: ',row[6])
                 print('Salary Expectation: ',row[7])
                 print('Years of Experience: ',row[8])
                 print('Degree: ',row[9])
                 print('Date of Submission: ',row[10])
                 print('File Name: ',row[11])
                 print('--------------------------------------------')
        except Exception as e:
                print(e.value)
                print('tasks is rolledback')
                sys.exit()
        else:
             print('data is retrieved')
             cursor.close()
        finally:
             if conn.connected == 1:
                  print('connection closed')
                  conn.close()

