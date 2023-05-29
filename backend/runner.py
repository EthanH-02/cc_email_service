import smtplib

from backend.email_builder import genericEmailBuilder, personalEmailBuilder
from backend.csv_extractor import csvToDictList
from backend.email_confirmation import emailConfirmation
from backend.message_formatter import genericMessageFormatter
from backend.files_builder import getFilesInfo
from backend.errors import checkReadyForStartUp
import edit_content.sensitive_info as sensitive_info



def runner() -> int:

    # Run only if the code is redy to go
    checkReadyForStartUp()

    # Create the generic format for the email
    files_info = getFilesInfo()
    generic_email = genericEmailBuilder(files_info)
    with open('./edit_content/email_contents.txt', 'r') as content_file:
        generic_message = genericMessageFormatter(content_file.read())

    rcpnts = csvToDictList()

    emailConfirmation([rcpnt['email'] for rcpnt in rcpnts], [file.filename for file in files_info])

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login(sensitive_info.LOGIN_EMAIL, sensitive_info.LOGIN_PASSWORD)

    for rcpnt in rcpnts:
        personal_email = personalEmailBuilder(generic_message, rcpnt, generic_email)
        s.send_message(personal_email)
        print('Sent email to: ' + rcpnt['email'])

    s.quit()

    print('DONE: sent all emails')
    
    return 0
