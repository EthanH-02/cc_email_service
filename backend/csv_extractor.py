import csv
from typing import List

from backend.errors import checkEmailKey
import edit_content.sensitive_info as sensitive_info



# Desctiption:
#   Interprets the CSV file given within
#   ./email_contents/sensitive_info,  to be utilised  within the
#   code
# Parameters:
#   - N/A
# Return:
#   - rows  List[Dict]: each  entry  corresponds to a row, with
#                       dictionary keys being the cols & values
#                       matching the row values for the col
# Time Complexity:
#   - O(m*n)
#       - m: number of cols in CSV file
#       - n: number of rows in CSV file
def csvToDictList() -> List[dict]:

    rows = []

    with open(sensitive_info.CSV_FILENAME, 'r', encoding='utf-8-sig') as csvfile:
        reader = csv.reader(csvfile)
        
        # Convert keys to lower case for standard utilisation
        keys = [x.lower() for x in next(reader)]
        checkEmailKey(keys)

        # Iterate over each row, form the dict and append it to the return list
        for row in reader:
            rows.append(makeDictFromRow(keys, row))

    return rows



# Description:
#   When given a list of keys and the corresponding values puts
#   the two together into a dictionary
# Parameters:
#   - keys  List[str]:  values to be used as the keys for the return
#                       dict, originating from CSV col headers
#   - row   List[str]:  values to be used as the values for the return
#                       dict, originating from the CSV file's rows
# Return:
#   - N/A   dict:       dictionary of values representing the row in
#                       the CSV file as a dictionary
# Time Complexity:
#   - O(n)
#       - n: number of rows in the CSV list
def makeDictFromRow(keys:List[str], row:List[str]) -> dict:
    return {key: row[idx] for idx, key in enumerate(keys)}
