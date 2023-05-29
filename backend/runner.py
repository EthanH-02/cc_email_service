import copy
import smtplib

from backend.csv_extractor import csvToDictList
from backend.email_builder import genericEmailBuilder, personalEmailBuilder
from backend.email_confirmation import emailConfirmation
from backend.errors import checkReadyForStartUp
from backend.files_builder import getFilesInfo
from backend.message_formatter import genericMessageFormatter
import edit_content.sensitive_info as sensitive_info



def runner() -> int:

    # Run only if the code is redy to go
    checkReadyForStartUp()

    # Unpack the csv file
    rcpnts = csvToDictList()

    # Create the generic format for the email
    files_info = getFilesInfo()
    generic_email = genericEmailBuilder(files_info)
    with open('./edit_content/email_contents.txt', 'r') as content_file:
        generic_message = genericMessageFormatter(content_file.read())

    emailConfirmation([rcpnt['email'] for rcpnt in rcpnts], [file.filename for file in files_info])

    # Sign into smtplib
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login(sensitive_info.LOGIN_EMAIL, sensitive_info.LOGIN_PASSWORD)

    # Send a message for each recipient
    for rcpnt in rcpnts:
        personal_email = personalEmailBuilder(generic_message, rcpnt, files_info)
        s.send_message(personal_email)
        print('Sent email to: ' + rcpnt['email'])

    # Quit the email service and print a message as feedback
    s.quit()
    print('DONE: sent all emails')
    
    return 0
