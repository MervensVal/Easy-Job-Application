from datetime import date
import os
import random

try:
    print("Thank you for applying with BizCorp using our Quick App!")
    print('Please enter the following information:')

    today = date.today()
    fname = input('First Name: ')
    lname = input('Last Name: ')
    dob = input('Date of Birth (Format: MM-DD-YYYY): ')
    email = input('Email: ')
    phone = input('Phone number (###-###-####): ')
    currPosition = input('Current Position: ')
    salary= int(input('Salary Expectations (must be a number): '))
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

    #Create folder if not already exists
    if eligible:
        directory = './Candidates'
        isExist = os.path.exists(directory)
        if not isExist:
            os.mkdir(directory)
        fileName = fname+'_'+lname+'_'+str(random.randint(1,1000000))
        filePath = './'+directory+'/'+fileName
        f = open(filePath,'x')
        f = open(filePath,'a')
        f.write(fname + '|' + lname + '|' + dob + '|' + email + '|' + phone + '|' + currPosition + '|' + str(salary) + '|' + str(yrsExperience)+ '|' + degree+ '|' + today.strftime("%m/%d/%Y, %H:%M:%S"))
        f.close

        #Save results in DB 
        #Create table if does not exists
        #insert data into table including filename
        print("Information has been saved")

except Exception as e:
    print('Error Occured')
    print('-----------------------------------------------------')
    print(e,'-',type(e).__name__)
    print('-----------------------------------------------------')