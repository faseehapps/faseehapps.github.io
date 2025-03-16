import os
from functions import *

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time

def generator(logs: bool = True) -> None:
    # To print messages
    def log(message: str) -> None:
        if logs:
            print(message)
    
    with open('template.html', 'r', encoding='utf-8') as file:
        HTML_TEMPLATE = file.read() # Replace {content} substring with the actual content

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

class OnFileChange(FileSystemEventHandler):
    def on_modified(self, event):
        if event.is_directory: # Ignore directory changes, only track file changes
            return
        
        filename = os.path.basename(event.src_path)
        if filename in ("index.html", "styles.css"): # Ignore generated files
            return
        
        generator(logs=False)
        print("Refreshed.")

# Start

if input("Activate debug mode? (y/N): ").strip().lower() in ('y', 'yes'):
    print('Debug mode actiavted. Press Ctrl + C to exit.')
    generator(logs=False) # Run generator initially

    path_to_watch = "."
    event_handler = OnFileChange()
    observer = Observer()
    observer.schedule(event_handler, path_to_watch, recursive=True)

    observer.start()

    try:
        while True:
            time.sleep(0.25)
    except KeyboardInterrupt: # Ctrl + C
        observer.stop()
    
    observer.join() # Wait for the observer thread to finish
    print("Program terminated.")
else:
    generator()
