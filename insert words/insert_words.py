import re
import os
import sys
import traceback

# Use python3, not python2
# To run: "py.exe insert_words.py" or "./insert_words.py"

def insert_words():

    # Try to get and open the file to change
    try:
        file_name = input("Please type a file name: \n")
        with open(file_name) as opened_file:
            content = opened_file.read()
    except (IOError, EOFError, FileNotFoundError) as e:
        print(e)
        traceback.print_exc()
        sys.exit()

    # Look through the file for brackets to replace and prompt the user
    # for what to replace it with
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
insert_words()
