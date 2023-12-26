import os
import random
def save_to_file(fname,lname,dob,email,phone,currPosition,salaryExp,yrsExperience,degree,today):
        try:
            directory = './Candidates'
            isExist = os.path.exists(directory)
            if not isExist:
                os.mkdir(directory)
            global fileName
            fileName = fname+'_'+lname+'_'+str(random.randint(1,1000000))
            filePath = './'+directory+'/'+fileName
            f = open(filePath,'x')
            f = open(filePath,'a')
            f.write('First Name - ' + fname + '\n')
            f.write('First Name - ' + lname + '\n')
            f.write('Date of Birth - ' + dob + '\n')
            f.write('Email - ' + email + '\n')
            f.write('Phone - ' + phone + '\n')
            f.write('Current Position - ' + currPosition + '\n')
            f.write('Salary Expectation - ' + str(salaryExp) + '\n')
            f.write('Years of Experience - ' + str(yrsExperience) + '\n')
            f.write('File Name - ' + today.strftime("%m/%d/%Y, %H:%M:%S"))
            #f.write(fname + '|' + lname + '|' + dob + '|' + email + '|' + phone + '|' + currPosition + '|' + str(salaryExp) + '|' + str(yrsExperience)+ '|' + degree+ '|' + today.strftime("%m/%d/%Y, %H:%M:%S"))
            f.close
            print("File created and information has been saved")
        except Exception as e:
             print(e)
             print('Error while saving to file')

