import os

def getDirectoryList():
    dirList = []
    for root, dirs, files in os.walk('./mod/'):
        num_sep_this = root.count(os.path.sep)
        for dir in dirs:
            if '__pycache__' != dir:#except folder
                dirList.append(dir)
        break
    return dirList

