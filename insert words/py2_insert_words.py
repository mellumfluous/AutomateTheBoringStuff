import re, os, sys

# Use python2, not python3
# To run: "py.exe py2_insert_words.py" or "./py2_insert_words.py"

def ree():
    try:
        FileName = raw_input("Please type a file name: \n")
        originalFile = open(FileName)
        originalContent = originalFile.read()
    except Exception as e:
        print("Error: "+3)
        sys.exit()

    bracketWords = re.search(r'{([a-z A-z]*)}', originalContent)
    company = ""
    while bracketWords:
        replaceWith = raw_input("insert " + bracketWords.group(1) + ": ") 
        originalContent = re.sub(bracketWords.group(), replaceWith, originalContent)
        bracketWords = re.search(r'{([a-z A-z]*)}', originalContent)
    newFile = open(FileName + " - changed.txt", 'w')
    newFile.write(originalContent)
    newFile.close()
ree()