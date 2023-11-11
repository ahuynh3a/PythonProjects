import random
import pandas as pd

#List Declarations
names = ["Annie Huynh","Jordan Childs", "Travis Kelce","Taylor Swift", "Christina Nguyen", "Anna Huynh", "Alex Huynh"]
ids = []
lastThreeIdDigits = []
firstHalfOfEmails = []
secondHalfOfEmails = []
finalEmails = []

#Helper Functions
def generateStudentIds(studentNames, students_ids):
  for student in range(len(studentNames)):
    students_ids.append(random.randint(111111,999999))
  return students_ids

def getThreeIDDigtsForEmail(studentIds, emailDigits):
  for studentId in studentIds:
    truncatedId = str(studentId)[3:]
    emailDigits.append(truncatedId)
  return emailDigits

def getNamesForEmail(studentNames, studentEmails):
    for name in studentNames:
        name = name[0] + name.split(" ")[1]
        studentEmails.append(name)
    return studentEmails

def generateSecondHalfOfEmail(emailDigits, secondHalfsOfEmails):
    for truncatedId in emailDigits:
        secondHalf = truncatedId + "example.org"
        secondHalfsOfEmails.append(secondHalf)
    return secondHalfsOfEmails 
    

def createStudentEmails(firstHalfEmail, secondHalfEmail, finalEmails):
    for i in range(len(firstHalfEmail)):
       finalEmails.append(firstHalfEmail[i] + secondHalfEmail[i])
    return finalEmails

def generateStudentAccounts(studentNames, studentIds, finalEmails):
   emailDataFrame = pd.DataFrame(studentNames, columns=['Name'])
   emailDataFrame['ID'] = studentIds
   emailDataFrame['Email'] = finalEmails
   print(emailDataFrame)
   

def Main():
    generateStudentIds(names, ids)
    getThreeIDDigtsForEmail(ids,lastThreeIdDigits)
    getNamesForEmail(names, firstHalfOfEmails)
    generateSecondHalfOfEmail(lastThreeIdDigits, secondHalfOfEmails)
    createStudentEmails(firstHalfOfEmails, secondHalfOfEmails, finalEmails)
    generateStudentAccounts(names, ids, finalEmails)
Main() 



