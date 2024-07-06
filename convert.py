"""
Convert pdf to txt file, also count tokens
"""

import pypdfium2 as pdfium
import tiktoken

pdf = pdfium.PdfDocument("./ragtest/input/data.pdf")
version = pdf.get_version()  # get the PDF standard version
n_pages = len(pdf)  # get the number of pages in the document

information = ""
for idx, page in enumerate(pdf):
    if idx < 6: # no use content
        continue
    textpage = page.get_textpage()
    text_all = textpage.get_text_range()
    information = information + text_all + "\n"

with open('output.txt', 'w') as file:
    # Write the data to the file
    file.write(information)
print("Data has been written to output.txt")

COMPLETIONS_MODEL = "gpt-3.5-turbo"

def num_tokens_from_string(string: str, encoding_name = COMPLETIONS_MODEL) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.encoding_for_model(encoding_name)
    num_tokens = len(encoding.encode(string))
    return num_tokens


# Open and read the content of the file
with open('output.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Count the tokens in the content
num_token = num_tokens_from_string(content)
print("total token spend for prompt :" ,num_token)

print(f"The number of tokens in the file is: {num_token}")