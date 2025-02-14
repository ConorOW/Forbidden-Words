# Forbidden-Words
A little script that you can use to retrieve lines from a Microsoft Word file that have certain "scary" words in them


## Installation
To install the required packages, run:

```bash
pip install -r requirements.txt```

To run this script, ensure the for `forbidden-words.txt` file is in your current directory. This should be alongside the `finding-forbidden-words.py` python script.

Then you run `python finding-forbidden-words.py forbidden-words.txt`.

This will output a file called `forbidden-lines.txt` which will show each sentence from your Microsoft Word docx file that has any of the forbidden words.

Happy censoring!!