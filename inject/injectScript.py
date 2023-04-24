import os, sys, time, json
import "./weaponObjectTemplate.json"

#this script is so you can inject sample data into a database instance for testing
def inject ():
    weaponInp = input('Enter weapon name: ')
    attachmentCount = (input('Enter number of attachments: '))
    attachmentList = []
    counter = 0
    while counter < attachmentCount:
        attachmentInp = input('Enter attachment name: ')
        attachmentList.append(attachmentInp)
        counter += 1
    
    


inject()