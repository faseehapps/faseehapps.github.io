import os
from functions import *

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>FaseehApps</title>
    <link href="styles.css" rel="stylesheet">

    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Roboto:ital,wght@0,100..900;1,100..900&display=swap" rel="stylesheet">
    <link rel="icon" type="image/png" href="https://faseehapps.github.io/assets/favicon.png">
</head>
<body>
    <div class="sticky-header">
        <h1 class="logo">FaseehApps</h1>
        <button class="theme-toggle-btn" id="theme-toggle"></button>
    </div>
                
    <div class="header" id="header">
        <h1 class="header-title">Hi, I am Faseeh!</h1>
        <p class="header-text">Download my apps here</p>
    </div>

    <section class="downloads-section">
{content}
    </section>

    <section class="review-section">
        <div class="review-form-list-div">
            <div id='review-form-div' class="review-form-div">
                <h2>Your Review</h2>
                <form id='review-form' class="review-form" action="/submit-review" method="post">
                    <label for="name">Name:</label>
                    <input type="text" id="name" name="name" maxlength="25" required>
                    <br><br>
                    <label for="review">Review:</label>
                    <textarea id="review" name="review" maxlength="600" required></textarea>
                    <br><br>
                    <button class="download-button" type="submit">Post</button>
                </form>
            </div>
                
            <div class="review-list-container">
                <h2>Reviews</h2>
                <div id='review-list' class="review-list"><p>Loading...</p></div>
            </div>
        </div>

    </section>
                
    <footer class="footer">
        <p>Thanks for visiting! See you again 😊</p>
    </footer>

    <script src="script.js" defer></script>
</body>
</html>
""" # Replace {content} substring with the actual content

def generator():
    print("Generaing HTML...")

    content = ""

    with open("src_files.txt", 'r', encoding='utf-8') as file:
        src_files = file.read().split()

    for src_filename in src_files:
        content += download_item(os.path.join("src", src_filename + '.yaml'))

    with open("index.html", 'w', encoding='utf-8') as html_file:
        html_file.write(HTML_TEMPLATE.replace("{content}", add_identation(content, 2)))

    print("Merging CSS files into styles.css...")
    with open("styles.css", 'w', encoding='utf-8') as css_file:
        css_file.write(merge_css_files("stylesheets"))

    print("Process complete!")

# Start

if input("Activate debug mode? (y = yes, anything else = no): ").strip().lower() == 'y':
    while True:
        generator()
        if input("Debug mode: Press Enter to refresh, 'e' to exit: ").strip().lower() == 'e':
            break
else:
    generator()
