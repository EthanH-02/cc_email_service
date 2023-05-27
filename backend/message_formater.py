from typing import List
from backend.errors import checkNoCurlyBracesLeft

import re

def formatMessage(msg:str, rcpnt:dict) -> str:
    ig_rgx_ptrn = r'\\\{(.*?)\\\}'

    keys = [elem.lower() for elem in list(rcpnt.keys())]

    for key in keys:
        to_rplc = '{' + key + '}'
        msg = re.sub(to_rplc, rcpnt[key], msg)

    ig_elems = re.findall(ig_rgx_ptrn, msg)

    for ig_elem in ig_elems:
        to_rplc = '\\\{' + ig_elem + '\\\}'
        rplc_val = '{' + ig_elem + '}'
        msg = re.sub(to_rplc, rplc_val, msg)
    
    return msg