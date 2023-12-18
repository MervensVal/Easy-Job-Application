from datetime import date
import os

try:
    print("Thank you for applying with BuzCorp using our Quick App.")
    print('Please enter the following information:')

    today = date.today()
    fname = input('First Name: ')
    lname = input('Last Name: ')
    dob = input('Date of Birth (Format: MM-DD-YYYY): ')
    email = input('Email: ')
    currPosition = input('Current Position: ')
    salary= int(input('Salary Expectations (must be a number): '))
    yrsExperience = int(input('Years of experience (minimum of 2 is required): '))
    degreeLevel = input('Do you have at least a bachelors degree? Yes or No: ')[0]
    degree = input('Degree: ')

    degreeLevel = degreeLevel.upper()
    month,day,year = map(int,dob.split("-"))
    age = today.year - year - ((today.month,today.day) < (month,day))

    #check age, experience, degree
    eligible = True
    if (age < 18) or (yrsExperience < 2) or (degreeLevel != 'Y'):
        eligible = False

    #Create folder if not already exists
    if eligible:
        directory = './Candidates'
        isExist = os.path.exists(directory)
        if not isExist:
            os.mkdir(directory)
        filePath = './'+directory+'/'+fname+lname+email[0]+dob[0:1]
        f = open(filePath,'x')
        f = open(filePath,'a')
        f.write(fname + '|' + lname + '|' + dob + '|' + email + '|' + currPosition + '|' + str(salary) + '|' + str(yrsExperience)+ '|' + degree+ '|' + today.strftime("%m/%d/%Y, %H:%M:%S"))
        f.close        
except Exception as e:
    print('Error Occured')
    print('-----------------------------------------------------')
    print(e)
    print('-----------------------------------------------------')