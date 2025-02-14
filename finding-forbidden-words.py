import sys
import re
from docx import Document

def load_search_words(file_path):
    """
    Loads search words from a text file.
    Each non-empty line is considered a search word.
    """
    with open(file_path, 'r', encoding='utf-8') as f:
        words = [line.strip() for line in f if line.strip()]
    return words

def main(docx_path, words_file_path):
    # Load search words and convert them to lowercase for case-insensitive search.
    search_words = load_search_words(words_file_path)
    search_words = [word.lower() for word in search_words]

    # Open the Word document.
    doc = Document(docx_path)

    # Combine all paragraphs into one continuous text block.
    full_text = " ".join(para.text for para in doc.paragraphs)

    # Split the text into sentences using a regular expression.
    sentences = re.split(r'(?<=[.!?])\s+', full_text)

    found_count = 0  # Counter for the number of instances found.
    output_lines = []  # List to store the output lines.

    # Iterate over each sentence.
    for sentence in sentences:
        sentence_lower = sentence.lower()
        found_word = None
        # Find the first matching search word in the sentence.
        for word in search_words:
            if word in sentence_lower:
                found_word = word
                break

        # If a matching word is found, add it to our output list.
        if found_word:
            output_lines.append(f"{found_word} ::: {sentence.strip()}")
            found_count += 1

    # Open the output file for writing.
    with open("forbidden-lines.txt", "w", encoding="utf-8") as outfile:
        # Write the header with the count.
        outfile.write(f"The document had {found_count} instances of forbidden words, listed below\n\n")
        # Write each matching sentence followed by a blank line.
        for line in output_lines:
            outfile.write(line + "\n\n")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python script.py <document.docx> <words.txt>")
    else:
        docx_path = sys.argv[1]
        words_file_path = sys.argv[2]
        main(docx_path, words_file_path)
