# Forbidden-Words
A little script that you can use to retrieve sections from a Microsoft Word file that have certain "scary" words in them


## Installation
To install the required packages, use bash and run:\
&nbsp;&nbsp;&nbsp;&nbsp;`pip install -r requirements.txt`

## Running your Forbidden Word Checker
To run this script, ensure the `forbidden-words.txt file` is in your current directory. This should be alongside the `finding-forbidden-words.py` python script and the Microsoft Word docx file.

Then you run:\
&nbsp;&nbsp;&nbsp;&nbsp;`python finding-forbidden-words.py Offending-Word-File.docx forbidden-words.txt`.

This will output a file called `forbidden-lines.txt` which will show each sentence from your Microsoft Word docx file that has any of the forbidden words.

## Happy Censoring!!