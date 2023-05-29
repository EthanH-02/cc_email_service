import re



# Desctiption:
#   Creates the generic message by switching all the variables to lowercase
#   remove any backslashs from cancelled out curly brackets
# Parameters:
#   - msg   str:    unformatted input string
# Return:
#   - res   str:    formatted string as output
# Time Complexity:
#   - O(n)
#       - n: length of msg string
def genericMessageFormatter(msg:str) -> str:
    rgx = r'(?<!\\){(.*?)(?<!\\)}'
    res = re.sub(rgx, lambda m: '{' + m.group(1).lower() + '}', msg)
    return res.replace(r"\{", "{").replace(r"\}", "}")



# Desctiption:
#   Edits the email message to be personalised to the recipient
# Parameters:
#   - msg   str:    unformatted input string
#   - rcpnt dict:   the dictionary of information regarding a user
# Return:
#   - msg   str:    formatted string as output
# Time Complexity:
#   - O(n)
#       - n: length of msg string
def personalMessageFormatter(msg:str, rcpnt:dict) -> str:

    keys = [elem.lower() for elem in list(rcpnt.keys())]

    for key in keys:
        to_rplc = r'\{' + key + r'\}'
        msg = re.sub(to_rplc, rcpnt[key], msg)
    
    return msg
