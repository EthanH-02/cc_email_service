import os

from typing import List

PATH_TO_FILES = './edit_content/files'

def getListOfPathnames() -> List[str]:
    filepaths = []
    for filename in os.listdir(PATH_TO_FILES):
        filepaths.append(os.path.join(PATH_TO_FILES, filename))
    return filepaths
