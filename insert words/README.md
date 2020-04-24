# Insert Words

A short script to personalize text

## Installation

1. Make sure you have python3

2. Download insert_words.py

3. \[optional\] Download the supplied "example.txt" in the same location insert_words.py is to get an idea of what the format should look like.

## Usage

1. Navigate to where the insert_words.py file is and double click it. A new window should pop up.

2. Type the name of a text file to look at (e.g. "example.txt"). The file should be in the same folder that insert_words.py is.

3. The script will look through the file for the words inside the curly brackets and ask what you want to replace it with. Type your responses.

4. After the script finishes running the window will close. In the same location that insert_words.py is, there should be a new file with the same name as the file you gave, except with "-changed" at the end of it. This is the personalized text that you can open, copy, and then paste to your recipient.

5. If opening the changed file, selecting the text, copying it, and pasting it is more steps than you'd like, you can install pyperclip by [following the instructions here](https://pypi.org/project/pyperclip/) and un-commenting two lines in insert_words.py.