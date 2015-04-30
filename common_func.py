import os

def getDirectoryList():
    dirList = []
    for root, dirs, files in os.walk('./mod/'):
        for dir in dirs:
            if '__pycache__' != dir:#except folder
                dirList.append(dir)
    return dirList

