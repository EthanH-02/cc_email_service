from typing import List
from email.message import EmailMessage

from backend.message_formatter import personalMessageFormatter
from backend.files_builder import File_Info
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
        with open(file_info.filepath, 'rb') as file:
            content = file.read()
            msg.add_attachment(content, maintype='application', subtype=file_info.subtype, filename=file_info.filename)

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
def personalEmailBuilder(generic_cont:str, rcpnt:dict, msg:EmailMessage) -> EmailMessage:

    # Set the recipent of the email
    msg['To'] = rcpnt['email'] 
 
    # Set the content of the file to be personalised
    msg.set_content(personalMessageFormatter(generic_cont, rcpnt))

    return msg
