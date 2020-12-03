import os

for folderName, subfolders, filename in os.walk(os.getcwd()):
    for file in filename:
        if ' ' not in file and file.islower():
            continue
        newFileName = os.path.abspath(file.replace(' ', '-').lower())

        # newFileName = os.path.abspath(folderName + '/' + newFileName)
        # file = os.path.abspath(folderName + '/' + file)

        print(f'{file} was renamed to {newFileName}')
        os.rename(os.path.abspath(file), newFileName)
