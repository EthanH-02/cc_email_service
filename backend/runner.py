import smtplib

import edit_content.sensative_info as sensative_info
from backend.email_builder import emailBuilder
from backend.csv_extractor import csvToDictList
from backend.errors import checkFilledLogin, checkEmailFormatted

def runner() -> int:

    checkFilledLogin()
    checkEmailFormatted()

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    checkFilledLogin()
    s.login(sensative_info.LOGIN_EMAIL, sensative_info.LOGIN_PASSWORD)
    
    rcpnts = csvToDictList()

    for rcpnt in rcpnts:
        email = emailBuilder(rcpnt)
        s.send_message(email)
        print('Sent email to: ' + rcpnt['email'])

    s.quit()

    print('DONE: sent all emails')
    
    return 0
