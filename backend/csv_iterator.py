import csv
import edit_content.sensative_info as sensative_info
from typing import List

def get_emails() -> List[str]:

    emails = []

    with open(sensative_info.CSV_FILENAME, "r") as csvfile:
        reader = csv.reader(csvfile)
        col_titles = next(reader)
        
        col_titles = [x.lower() for x in col_titles]

        name_idx = col_titles.index('name')
        email_idx = col_titles.index('email')

        for row in reader:
            print("hello " + row[name_idx] + " your email is " + row[email_idx])
            emails.append(row[email_idx])
    return emails


