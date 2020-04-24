import re
import os
import sys
import traceback

# If you'd like the edited contents to be available to paste after running
# the script, install pyperclip and un-cumment the following line as
# well as the very last line
# import pyperclip

# Try to get and open the file to change
try:
    file_name = input("Please type a file name: \n")
    with open(file_name) as opened_file:
        content = opened_file.read()
except (IOError, EOFError, FileNotFoundError) as e:
    print(e)
    traceback.print_exc()
    sys.exit()

# Look through the file for brackets to replace and prompt the user for input
brackets = re.search(r'{([a-z A-z]*)}', content)
company = ""
while brackets:
    replace = input("insert " + brackets.group(1) +": ")
    content = re.sub(brackets.group(), replace, content)
    brackets = re.search(r'{([a-z A-z]*)}', content)
# Add " - changed.txt" to the original file prefix and write the content
prefix = re.search(r'(.*).(?<=(\.))(.*)', file_name)
with open("{} - changed.txt".format(prefix.group(1)), 'w') as new_file:
    new_file.write(content)

# un-comment the following line if you'd like the edited contents to be
# available to paste
# pyperclip.copy(content)
