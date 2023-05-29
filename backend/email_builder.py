from typing import List
from email.message import EmailMessage
from email.mime.text import MIMEText

from backend.files_builder import File_Info
from backend.message_formatter import personalMessageFormatter
import edit_content.sensitive_info as sensitive_info



# Desctiption:
#   Attaches the elements to an emailmessage to be sent out
# Parameters:
#   - N/A
# Return:
#   - msg   EmailMessage    the complete email message to be set, now
#                           containing a recipent and customised content
# Time Complexity:
#   - O(1)
def emailBuilder(generic_cont:str, rcpnt:dict,
                 files_info: List[File_Info]) -> EmailMessage:

    msg = EmailMessage()

    # Copy the necessary attributes from the original msg
    msg['From'] = sensitive_info.LOGIN_EMAIL
    msg['To'] = rcpnt['email']
    with open('./edit_content/email_info.txt', 'r') as info_file:
        msg['Subject'] = ' '.join(info_file.readline().split()[1:])

    # Attach the files to the message
    for file_info in files_info:
        msg.add_attachment(file_info.content, maintype='application',
                           subtype=file_info.subtype, filename=file_info.filename)

    # Create a new MIMEText object for the personalized content
    personalized_content = personalMessageFormatter(generic_cont, rcpnt)

    # Add the text_part to the msg
    msg.attach(MIMEText(personalized_content, 'plain'))

    return msg
