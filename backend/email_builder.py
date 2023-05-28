from email.message import EmailMessage
from backend.message_formater import formatMessage
from backend.files_builder import getFilesInfo
import edit_content.sensative_info as sensative_info

def emailBuilder(rcpnt:dict) -> EmailMessage:
    
    msg = EmailMessage()

    msg["From"] = sensative_info.LOGIN_EMAIL
    msg["To"] = rcpnt['email']

    # Extract the information regarding the email
    with open('./edit_content/email_info.txt', 'r') as info_file:
        msg["Subject"] = " ".join(info_file.readline().split()[1:])
 
    # Extract the infromation regarding the contents of the email
    with open('./edit_content/email_contents.txt', 'r') as content_file:
        msg.set_content(formatMessage(content_file.read(), rcpnt))

    for file_info in getFilesInfo():
        with open(file_info.filepath, 'rb') as file:
            content = file.read()
            msg.add_attachment(content, maintype='application', subtype=file_info.subtype, filename=file_info.filename)

    return msg
