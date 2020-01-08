#! python
import pyperclip
import re

# bulletPointAdder.py - Adds Wikipedia bullet points to the start
# of each line of text on the clipboard.
def bulletPointAdder():
    text = pyperclip.paste()

    # Separate lines and add stars.
    lines = text.split('\n')
    for i in range(len(lines)):    # loop through all indexes for "lines" list
        lines[i] = '* ' + lines[i] # add star to each string in "lines" list
    text = '\n'.join(lines)
    pyperclip.copy(text)

def printTable(tableData):
    colWidths = [0] * len(tableData)
    for i in range(len(tableData)):
        maxLetters = len(tableData[i][0])
        for j in range(len(tableData[i])):
            maxLetters = max(maxLetters, len(tableData[i][j]))
        colWidths[i] = maxLetters
    adjust = max(colWidths) + 2

    for eachList in tableData:
        for eachWord in eachList:
            print(eachWord.rjust(adjust), end ="")
        print("\n")

TheList = [['apples', 'oranges', 'cherries', 'banana'],
    ['Alice', 'Bob', 'Carol', 'David'],
    ['dogs', 'cats', 'moose', 'goose']]

# printTable(TheList)

# phoneAndEmail - Finds phone numbers and email addresses on the clipboard.
def phoneAndEmail():
    phoneRegex = re.compile(r'''(
        (\d{3}|\(\d{3}\))?                # area code
        (\s|-|\.)?                        # separator
        (\d{3})                           # first 3 digits
        (\s|-|\.)                         # separator
        (\d{4})                           # last 4 digits
        (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
        )''', re.VERBOSE)

    emailRegex = re.compile(r'''(
        [a-zA-Z0-9._%+-]+      # username
        @                      # @ symbol
        [a-zA-Z0-9.-]+         # domain name
        (\.[a-zA-Z]{2,4})      # dot-something
        )''', re.VERBOSE)

    # Find matches in clipboard text.
    text = str(pyperclip.paste())
    matches = []
    for groups in phoneRegex.findall(text):
        phoneNum = '-'.join([groups[1], groups[3], groups[5]])
        if groups[8] != '':
            phoneNum += ' x' + groups[8]
        matches.append(phoneNum)
    for groups in emailRegex.findall(text):
        matches.append(groups[0])

    # Copy results to the clipboard.
    if len(matches) > 0:
        pyperclip.copy('\n'.join(matches))
        print('Copied to clipboard:')
        print('\n'.join(matches))
    else:
        print('No phone numbers or email addresses found.')

# phoneAndEmail()

# checkPassword - at least 8 characters, has upper and lower chars, at least 1 digit
def checkPassword(userMadePass):

    PasswordRegEx = re.compile(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$')

    try:
        PasswordRegEx.search(userMadePass).group()
        print("Congrats! " + userMadePass +" is a strong password")
    except AttributeError:
        print("Sorry, "+userMadePass+" is not a strong password. Try again.")

# checkPassword("a1aaaaaaaaaaaaaaaaaAa")

# myStripFunc - functions the same way as the strip() method
#   no args besides string - strip beginning and end whitespace chars
#   o/w - the specified characters will be removed from the string

def myStripFunc(userString, removeThisChar = '\s'):
    print("This is the string: " + userString)
    print("Remove this character: " + removeThisChar)
    RegexWithCharToSub = re.compile(removeThisChar)
    userString = RegexWithCharToSub.sub('', userString)
    print(userString)

# myStripFunc("hello, how are you?", "h")