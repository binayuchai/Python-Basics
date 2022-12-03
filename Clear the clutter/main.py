import os

files = os.listdir()
files.remove('main.py')

def createIfNotExist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)
        
#Moving files to their respective folders     
def moveFiles(folder,files):   
    for file in files:
        os.replace(file,f"{folder}/{files}")



createIfNotExist('Images')
createIfNotExist('Docs')
createIfNotExist('Others')

imgeExt = ['.png','.jpg','.jpeg','.webp']
docsExt = ['.txt','.pdf','.doc','.docx']

# use of List Comprehension
images = [file for file in files if os.path.splitext(file)[1].lower() in imgeExt]   # newlist = [expression for item in iterable if condition == True]
docs = [file for file in files if os.path.splitext(file)[1].lower() in docsExt]
others = []


for file in files:
    ext = os.path.splitext(file)[1].lower()
    if (ext not in imgeExt) and (ext not in docsExt) and os.path.isfile(file):
        others.append(file)
        
#Moving files to folder

moveFiles('Images',images)
moveFiles('Docs',docs)
moveFiles('Others',others)