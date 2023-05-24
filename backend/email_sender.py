import smtplib

import edit_content.sensative_info as sensative_info
from message_former import emailFormat

def email_sender() -> int:
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()

    s.login(sensative_info.LOGIN_EMAIL, sensative_info.LOGIN_PASSWORD)
    
    # Create the message to be sent
    msg = emailFormat
    
    # SEND THE MESSAGE
    s.send_message(msg)
    s.quit()
    
    return 0
