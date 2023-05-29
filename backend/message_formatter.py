import re

from typing import List
from backend.errors import checkNoCurlyBracesLeft



def genericMessageFormatter(msg:str) -> str:
    rgx = r'(?<!\\){(.*?)(?<!\\)}'
    res = re.sub(rgx, lambda m: '{' + m.group(1).lower() + '}', msg)
    return res.replace(r"\{", "{").replace(r"\}", "}")



def personalMessageFormatter(msg:str, rcpnt:dict) -> str:

    keys = [elem.lower() for elem in list(rcpnt.keys())]

    for key in keys:
        to_rplc = r'\{' + key + r'\}'
        msg = re.sub(to_rplc, rcpnt[key], msg)
    
    return msg
