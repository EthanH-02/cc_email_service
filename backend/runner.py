import smtplib

import edit_content.sensitive_info as sensitive_info
from backend.email_builder import emailBuilder
from backend.csv_extractor import csvToDictList
from backend.email_confirmation import emailConfirmation
from backend.errors import checkFilledLogin, checkEmailFormatted, checkNoCurlyBracesLeft

def runner() -> int:

    checkFilledLogin()
    checkEmailFormatted()
    checkNoCurlyBracesLeft()

    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    checkFilledLogin()
    s.login(sensitive_info.LOGIN_EMAIL, sensitive_info.LOGIN_PASSWORD)
    
    rcpnts = csvToDictList()

    emailConfirmation(rcpnts)

    for rcpnt in rcpnts:
        email = emailBuilder(rcpnt)
        s.send_message(email)
        print('Sent email to: ' + rcpnt['email'])

    s.quit()

    print('DONE: sent all emails')
    
    return 0
