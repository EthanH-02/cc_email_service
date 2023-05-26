from typing import List

import re

def formatMessage(msg:str, rcpnt:dict) -> str:
    rgx_ptrn = r'(?<!\\)\{(.*?)(?<!\\)\}'
    ig_rgx_ptrn = r'\\\{(.*?)\\\}'

    elems = [elem.lower() for elem in re.findall(rgx_ptrn, msg)]

    for elem in elems:
        to_rplc = '{' + elem + '}'
        msg = re.sub(to_rplc, rcpnt[elem], msg)
    
    ig_elems = re.findall(ig_rgx_ptrn, msg)

    for ig_elem in ig_elems:
        to_rplc = '\\\{' + ig_elem + '\\\}'
        rplc_val = '{' + ig_elem + '}'
        msg = re.sub(to_rplc, rplc_val, msg)
    
    return msg