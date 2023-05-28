import os

from typing import List
from backend.errors import checkSubtypeDeterminable

PATH_TO_FILES = './edit_content/files'

class File_Info:
    def __init__(self, filepath:str, filename:str, subtype:str):
        self.filepath = filepath
        self.filename = filename
        self.subtype = subtype


def extractSubtype(filename:str) -> str:
    subtype = os.path.splitext(filename)[1].lower()
    checkSubtypeDeterminable(subtype)
    return subtype[1:]

def getFilesInfo() -> List[File_Info]:
    files = []
    for filename in os.listdir(PATH_TO_FILES):
        filepath = (os.path.join(PATH_TO_FILES, filename))
        subtype = extractSubtype(filepath)
        files.append(File_Info(filepath, filename, subtype))
    return files
