import smtplib

import edit_content.sensative_info as sensative_info
from email_builder import emailBuilder
from csv_extractor import csvToDictList

def runner() -> int:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login(sensative_info.LOGIN_EMAIL, sensative_info.LOGIN_PASSWORD)
    
    rcpnts = csvToDictList

    for rcpnt in rcpnts:
        email = emailBuilder(rcpnt)
        s.send_message(email)

    s.quit()
    
    return 0
