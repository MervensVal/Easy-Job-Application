from datetime import date
import fileWork as fw
import dbWork as db
import analyticsWork as aw
import findApplicant as fa
try:
    userType = input('Select an option: [1] if you are an applicant [2] if you are the Employer: ')
    if userType == '1' or userType == '[1]':
        print("Thank you for applying with BizCorp using our Quick App!")
        print('Please enter the following information:')
        today = date.today()
        fname = input('First Name: ')
        lname = input('Last Name: ')
        dob = input('Date of Birth (Format: MM-DD-YYYY): ')
        email = input('Email: ')
        phone = input('Phone number (###-###-####): ')
        currPosition = input('Current Position: ')
        salaryExp= int(input('Salary Expectations (must be a number): '))
        yrsExperience = int(input('Years of experience (minimum of 2 is required): '))
        degreeLevel = input('Do you have at least a bachelors degree? Yes (Y) or No (N): ')[0]
        degree = input('Degree: ')
        degreeLevel = degreeLevel.upper()
        month,day,year = map(int,dob.split("-"))
        age = today.year - year - ((today.month,today.day) < (month,day))

        #check user input
        eligible = True
        if (len(fname)<0 or len(lname)<0  or len(dob)<0  or len(email)<0 or len(phone)<0  ):
            eligible = False
            print('Error: First Name, Last Name, DOB, Email, and Phone are all required')
        elif (email.count('@')== 0) or (email.count('.')== 0):
            eligible = False
            print('Error: invalid email')
        elif (age < 18) or (yrsExperience < 2) or (degreeLevel != 'Y'):
            eligible = False
            print('Error: Age, Experience, or Degree Level does not meet minnimum requirements')
            
        #Create folder & save to db            
        if eligible:
            fileName = 'no_file_name'
            fw.save_to_file(fname,lname,dob,email,phone,currPosition,salaryExp,yrsExperience,degree,today)
            fileName = fw.fileName
            db.save_to_db(fname,lname,dob,email,phone,currPosition,salaryExp,yrsExperience,degree,today,fileName)
    elif userType == '2' or userType == '[2]':
         decision = input('Type [A] for analytics and [S] to search for a person\'s application: ')[0].upper()
         if decision == 'A' or decision == '[A]':
            #pull data and do analysis
            aw.analytics()
         elif decision == 'S' or decision == '[S]':
            #find an applicant
            print('Find an application using fist and last name.')
            fname = input('First Name: ')
            lname = input('Last Name: ')
            fa.find_Applicant(fname,lname)
         else:
            print('incorrect input')
    else:
         print('incorrect input')
except Exception as e:
        print('Error Occured')
        print('-----------------------------------------------------')
        print(e,'-',type(e).__name__)
        print('-----------------------------------------------------')

