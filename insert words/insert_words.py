import re, os, sys

# Use python3, not python2
# To run: "py.exe insert_words.py" or "./insert_words.py"

def ree():
    try:
        FileName = input("Please type a file name: \n")
        originalFile = open(FileName)
        originalContent = originalFile.read()
        originalFile.close()
    except Exception as e:
        print("Error: " +e)
        sys.exit()

    braketWords = re.search(r'{([a-z A-z]*)}', originalContent)
    company = ""
    while braketWords:
        replaceWith = input("insert " + braketWords.group(1) +": ")
        originalContent = re.sub(braketWords.group(), replaceWith, originalContent)
        braketWords = re.search(r'{([a-z A-z]*)}', originalContent)
    newFile = open(FileName +" - changed.txt", 'w')
    newFile.write(originalContent)
    newFile.close()
ree()
