import os
import yaml

def index_content(source_files: list) -> str:
    index_content = ""
    index_content += """
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
    """
        
    for item in source_files:
        with open(item, 'r') as file:
            data = yaml.safe_load(file)
        
        if "path_to_vid" in data:
            index_content += "\t\t<div class='item-with-img'>" # div item-with-image.
            index_content += f"<video class='item-img' autoplay muted loop playsinline><source src='{data["path_to_vid"]}' type='video/mp4'>Your browser does not support the video tag.</video>"
        elif "path_to_img" in data:
            index_content += "\t\t<div class='item-with-img'>" # div item-with-image.
            index_content += f"<img src='{data["path_to_img"]}' class='item-img'>"
        else:
            index_content += "\t\t<div class='item-without-img'>" # div item-without-image.

        # Content goes inside `item-content`
        index_content += f"<div class='item-content'>" # div item-content.
        index_content += f"<h1>{data["name"]}</h1>"

        if "descriptions" in data and data["descriptions"]:
            for description in data["descriptions"]:
                index_content += f"<p>{description}</p>"

        index_content += "<div class='download-buttons-container'>" # div download-buttons-container
        for download_link in data["links"]:
            index_content += f"""<a href={download_link[1]}><button class='download-button'>{download_link[0]}</button></a>"""
        
        index_content += "</div>" # close download-buttons-container.
        index_content += "</div>" # close item-content.
        index_content += "</div>\n" # close item.

    index_content += """
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
                    
        <div class="footer">
            <p>Thanks for visiting! See you again 😊</p>
        </div>

        <script src="script.js" defer></script>
    </body>
    </html>
"""

    print("HTML file generation complete.")
    return index_content

def merged(css_source_dir: str) -> None:
    print(f"\ncss_source_dir: {css_source_dir}")
    source_files = sorted([os.path.join(css_source_dir, file) for file in os.listdir(css_source_dir)])

    styles = ""
    for item in source_files:
        with open(item, 'r') as file:
            print(f"Reading {item}...")
            styles += file.read() + '\n'
    
    return styles

# main

css_source_dir = "src/"
print(f"source_dir: {css_source_dir}")
source_files = sorted([os.path.join(css_source_dir, file) for file in os.listdir(css_source_dir)])
print("source_files:")
for i in range(0, len(source_files)):
    print(f"{i + 1}. {source_files[i]}")

print("Generating index.html...")

with open('index.html', 'w') as index:
    index.write(index_content(source_files))

print(f"Writing styles into 'styles.css'...")

css_source_dir = "stylesheets/"
with open ('styles.css', 'w') as styles_css:
    styles_css.write(merged(css_source_dir))

print("All stylesheets successfully merged into 'styles.css'.")
print("\nStatic site successfully generated.")
