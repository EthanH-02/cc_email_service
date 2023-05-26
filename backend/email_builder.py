from email.message import EmailMessage

def emailBuilder(sender:str, recipient:str, subj:str) -> EmailMessage:
    
    msg = EmailMessage()

    # Extract the information regarding the email
    with open('email_info.txt', 'r') as info_file:
        msg["From"] = info_file.readline().split()[1]
        msg["To"] = info_file.readline().split()[1]
        msg["Subject"] = " ".join(info_file.readline().split()[1:])

    # Extract the infromation regarding the contents of the email
    with open('email_contents.txt', 'r') as content_file:
        msg.set_content(content_file.read())

    return msg
