import copy
from typing import List
from email.message import EmailMessage
from email.mime.text import MIMEText

from backend.files_builder import File_Info
from backend.message_formatter import personalMessageFormatter
import edit_content.sensitive_info as sensitive_info



# Desctiption:
#   Pre-computes the elements of the email message that will be standard
#   regardless of email recipent (Sender, Subject, Files).
# Parameters:
#   - N/A
# Return:
#   - msg   EmailMessage    the email to be sent with, sender, subject
#                           and files set 
# Time Complexity:
#   - O(n)
#       - n: number of files within ./edit_content/files
def genericEmailBuilder(files_info: List[File_Info]) -> EmailMessage:
    msg = EmailMessage()

    msg['From'] = sensitive_info.LOGIN_EMAIL

    # Extract the subject of the email
    with open('./edit_content/email_info.txt', 'r') as info_file:
        msg['Subject'] = ' '.join(info_file.readline().split()[1:])

    # Attach files within ./edit_content/files
    for file_info in files_info:
        msg.add_attachment(file_info.content, maintype='application',
                           subtype=file_info.subtype, filename=file_info.filename)

    return msg



# Desctiption:
#   Attaches the custom elements of the email to be sent, recipient and
#   custom elements of the email
# Parameters:
#   - N/A
# Return:
#   - msg   EmailMessage    the complete email message to be set, now
#                           containing a recipent and customised content
# Time Complexity:
#   - O(1)
def personalEmailBuilder(generic_cont:str, rcpnt:dict,
                         files_info: List[File_Info]) -> EmailMessage:

    msg = EmailMessage()

    # Copy the necessary attributes from the original msg
    msg['From'] = sensitive_info.LOGIN_EMAIL
    msg['To'] = rcpnt['email']
    with open('./edit_content/email_info.txt', 'r') as info_file:
        msg['Subject'] = ' '.join(info_file.readline().split()[1:])

    for file_info in files_info:
        msg.add_attachment(file_info.content, maintype='application',
                           subtype=file_info.subtype, filename=file_info.filename)


    # Create a new MIMEText object for the personalized content
    personalized_content = personalMessageFormatter(generic_cont, rcpnt)
    text_part = MIMEText(personalized_content, 'plain')

    # Add the text_part to the msg
    msg.attach(text_part)

    return msg
