from typing import List

import edit_content.sensitive_info as sensitive_info



# Desctiption:
#   Prints out the email info to be sent so that the user can check before sending
# Parameters:
#   - rcpnt_emails  List[str]:  A list of all recipent emails
#   - filenames     List[str]:  A list of all attachments to be included
# Return:
#   - N/A
# Time Complexity:
#   - O(m + n)
#       - m: number of emails within CSV file
#       - n: number of attachements
def emailConfirmation(rcpnt_emails:List[str], filenames:List[str]):

    # Print information relating to the sender, to and subject
    print(f'SENDER: {sensitive_info.LOGIN_EMAIL}')
    print(f'TO:\n' + '\n'.join("\t" + rcpnt_email for rcpnt_email in rcpnt_emails))
    with open('./edit_content/email_info.txt', 'r') as info_file:
        print(f'SUBJECT: {" ".join(info_file.readline().split()[1:])}')

    # Print the filenames for each attachment to be sent
    print(f'Attachments:')
    if filenames:
        print('\n'.join("\t" + filename for filename in filenames))
    else:
        print('\tN/A')

    print()

    # Print the contents of the email - NOT CUSTOMISED
    with open('./edit_content/email_contents.txt', 'r') as content_file:
        print(content_file.read())

    print()

    # Ask for the email to be confirmed before sending
    confirmSend()



# Desctiption:
#   Asks to confirm is the user is happy to send the email before sending 
# Parameters:
#   - N/A
# Return:
#   - N/A
# Time Complexity:
#   - O(1)
def confirmSend():
    conf_msg = input('DO YOU WISH TO SEND THIS MESSAGE: (Y/N): ')
    if conf_msg.upper() == 'N':
        exit()
    elif conf_msg.upper() != 'Y':
        print('Invalid input try again')
        confirmSend()
