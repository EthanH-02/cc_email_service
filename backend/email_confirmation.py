import edit_content.sensative_info as sensative_info

from typing import List

def emailConfirmation(rcpnts:List[dict]):
    print("SENDER: " + sensative_info.LOGIN_EMAIL)
    print("TO:")
    for rcpnt in rcpnts:
        print(f"\t{rcpnt['email']}")
    with open('./edit_content/email_info.txt', 'r') as info_file:
        print("SUBJECT: " + " ".join(info_file.readline().split()[1:]))

    print()

    with open('./edit_content/email_contents.txt', 'r') as content_file:
        print(content_file.read())

    print()

    conf_msg = 'A'
    while (conf_msg != 'Y'):
        conf_msg = input("DO YOU WISH TO SEND THIS MESSAGE: (Y/N): ")
        if conf_msg == 'N':
            exit()
        elif conf_msg == 'Y':
            break
        else:
            print("Invalid input try again")
