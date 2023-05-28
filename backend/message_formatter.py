from typing import List
from backend.errors import checkNoCurlyBracesLeft

import re

def change_variables_to_lower(msg:str) -> str:
    rgx = r'\{([^}]*)\}'

    def rplc(match):
        return '{' + match.group(1).lower() + '}'
    
    msg = re.sub(rgx, rplc, msg)
    return msg

def formatMessage(msg:str, rcpnt:dict) -> str:

    msg = change_variables_to_lower(msg)

    ig_rgx_ptrn = r'\\\{(.*?)\\\}'

    keys = [elem.lower() for elem in list(rcpnt.keys())]

    for key in keys:
        to_rplc = r'\{' + key + r'\}'
        msg = re.sub(to_rplc, rcpnt[key], msg)

    ig_elems = re.findall(ig_rgx_ptrn, msg)

    for ig_elem in ig_elems:
        to_rplc = r'\\\{' + ig_elem + r'\\\}'
        rplc_val = '{' + ig_elem + '}'
        msg = re.sub(to_rplc, rplc_val, msg)
    
    return msg
