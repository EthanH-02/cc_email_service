import os
from typing import List

from backend.errors import checkSubtypeDeterminable


PATH_TO_FILES = './edit_content/files'



# Description:
#   A class to be used in order to maintain information to be
#   utilised in file attachments
class File_Info:
    def __init__(self, filename:str):
        self.filename = filename
        self.filepath = (os.path.join(PATH_TO_FILES, filename))
        self.subtype  = extractSubtype(self.filepath)



# Desctiption:
#   Returns a list of File_Info for each file in ./edit_content/files
# Parameters:
#   - N/A
# Return:
#   - N/A   List(File_Info):    a list of File_Info for each file in
#                               ./edit_content/files
# Time Complexity:
#   - O(n)
#       - n: number of attachements
def getFilesInfo() -> List[File_Info]:
    return [File_Info(filename) for filename in os.listdir(PATH_TO_FILES) if filename != '.gitkeep']



# Desctiption:
#   Extracts the subtype of a file given its filepath.
#   i.e. file.jpg => .jpg
# Parameters:
#   - filepath  str:    the path to a given file in python script
# Return:
#   - subtype   str:    the subtype of the file
# Time Complexity:
#   - O(1)
def extractSubtype(filepath:str) -> str:
    subtype = os.path.splitext(filepath)[1].lower()
    checkSubtypeDeterminable(subtype)
    return subtype[1:]
