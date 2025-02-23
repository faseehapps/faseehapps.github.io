import os
from functions import *

def generator(logs: bool = True) -> None:
    # To print messages
    def log(message: str) -> None:
        if logs:
            print(message)

    # Generate HTML
    log("Generaing HTML...")

    content = ""
    src_files = []

    with open("src_files.txt", 'r', encoding='utf-8') as file:
        src_files = file.read().split()

    for src_filename in src_files:
        content += download_item(os.path.join("src", src_filename + '.yaml'))

    with open("index.html", 'w', encoding='utf-8') as html_file:
        html_file.write(HTML_TEMPLATE.replace("{content}", add_identation(content, 2)))

    # Merge CSS
    log("Merging CSS files into styles.css...")
    with open("styles.css", 'w', encoding='utf-8') as css_file:
        css_file.write(merge_css_files("stylesheets"))

    log("Process complete!")

# Start

with open('template.html', 'r', encoding='utf-8') as file:
    HTML_TEMPLATE = file.read() # Replace {content} substring with the actual content

if input("Activate debug mode? (y = yes, anything else = no): ").strip().lower() == 'y':
    while True:
        generator(logs=False)
        if input("Debug mode: Press Enter to refresh, 'e' to exit: ").strip().lower() == 'e':
            break
else:
    generator()
