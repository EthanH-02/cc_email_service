import re

from typing import List
import edit_content.sensative_info as sensative_info

def checkFilledLogin():
    if not sensative_info.LOGIN_EMAIL or not sensative_info.LOGIN_PASSWORD:
        raise Exception("Sign in details not provided\nEnsure email and password in ./edit_content/sensative_info")

def checkEmailKey(keys:List[str]):
    if "email" not in keys:
        raise Exception("CSV File does not contain the key 'email'\nEnsure the CSV has a column with title email")

def checkNoCurlyBracesLeft(msg:str):
    rgx = r"(?<!\\)\{[^{}]*\}(?!\\)"
    rmndrs = re.findall(rgx, msg)
    # print(rmndrs)
    if len(rmndrs) != 0:
        raise Exception("Leftover { } within the code: "
                        + " ".join(rmndrs)
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