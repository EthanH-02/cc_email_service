from typing import List
import edit_content.sensative_info as sensative_info

def checkFilledLogin():
    if not sensative_info.LOGIN_EMAIL or not sensative_info.LOGIN_PASSWORD:
        raise Exception("Sign in details not provided\nEnsure to enter email and password in ./edit_content/sensative_info")

def checkEmailKey(keys: List[str]):
    if "email" not in keys:
        raise Exception("CSV File does not contain the key 'email'\nEnsure the CSV has a column with title email")
