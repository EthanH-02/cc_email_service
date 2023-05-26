import csv
import edit_content.sensative_info as sensative_info

from backend.errors import checkEmailKey

from typing import List

def csvToDictList() -> List[dict]:

    rows = []

    with open(sensative_info.CSV_FILENAME, "r") as csvfile:
        reader = csv.reader(csvfile)
        
        keys = [x.lower() for x in next(reader)]
        checkEmailKey(keys)

        for row in reader:
            row_dict = dict()
            for idx, key in enumerate(keys):
                row_dict[key] = row[idx]
            
            rows.append(row_dict)

    return rows


