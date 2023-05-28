import re
import csv

from typing import List
import edit_content.sensative_info as sensative_info

def checkFilledLogin():
    if not sensative_info.LOGIN_EMAIL or not sensative_info.LOGIN_PASSWORD:
        raise Exception("Sign in details not provided\nEnsure email and password in ./edit_content/sensative_info")

def checkEmailKey(keys:List[str]):
    if "email" not in keys:
        raise Exception("CSV File does not contain the key 'email'\nEnsure the CSV has a column with title email")

def checkNoCurlyBracesLeft():

    rgx = r'(?<!\\)\{[^{}]*\}(?!\\)'
    not_pres = []

    with open(sensative_info.CSV_FILENAME, 'r', encoding='utf-8-sig') as csv_file:
        keys = ['{' + x.lower() + '}' for x in next(csv.reader(csv_file))]

    with open('./edit_content/email_contents.txt', 'r') as content_file:
        variables = [x.lower() for x in re.findall(rgx, content_file.read())]

    for variable in variables:
        if variable not in keys:
            not_pres.append(variable)
    
    if not_pres:
        raise Exception("Leftover { } within the code:\n\t"
            + '\n\t'.join(not_pres)
            + "\nEdit the message, include the fields or cancel out with \\{\\}")
    

def checkEmailFormatted():
    checkSubjectEntered()
    checkContentEntered()

def checkSubjectEntered():
    with open('./edit_content/email_info.txt', 'r') as file:
        if file.readline() == "SUBJECT: ":
            raise Exception("Email does not contain a subject\nEnter a subject for the email to proceed into ./edit_content/email_info.txt")

def checkContentEntered():
    with open('./edit_content/email_contents.txt', 'r') as file:
        if not file.read():
            raise Exception("Email does not contain content\nEnter content into ./edit_content/email_contents.txt")
        
def checkSubtypeDeterminable(subtype:str):
    if not subtype:
        raise Exception("Unable to determine file subtype\nEnsure all attachments have a . then filetype")