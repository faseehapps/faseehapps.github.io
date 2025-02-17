import os
import yaml

source_dir = "src/"
print(f"source-dir: {source_dir}")
source_files = sorted([os.path.join(source_dir, file) for file in os.listdir(source_dir)])
print("source_files:")
for file in source_files:
    print("   ", file)

print("Generating index.html...")

with open('index.html', 'w') as index:
    index.write("""
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
    <link rel="icon" type="image/png" href="assets/favicon.png">
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

    <div class="items-container">
""")
    
    for item in source_files:
        with open(item, 'r') as file:
            data = yaml.safe_load(file)
        
        if "path_to_vid" in data:
            index.write("\t\t<div class='item-with-img'>") # div item-with-image.
            index.write(f"<video class='item-img' autoplay muted loop playsinline><source src='{data["path_to_vid"]}' type='video/mp4'>Your browser does not support the video tag.</video>")
        elif "path_to_img" in data:
            index.write("\t\t<div class='item-with-img'>") # div item-with-image.
            index.write(f"<img src='{data["path_to_img"]}' class='item-img'>")
        else:
            index.write("\t\t<div class='item-without-img'>") # div item-without-image.

        # Content goes inside `item-content`
        index.write(f"<div class='item-content'>") # div item-content.
        index.write(f"<h1>{data["name"]}</h1>")

        if "descriptions" in data and data["descriptions"]:
            for description in data["descriptions"]:
                index.write(f"<p>{description}</p>")

        index.write("<div class='download-buttons-container'>") # div download-buttons-container
        for download_link in data["links"]:
            index.write(f"""<a href={download_link[1]}><button class='download-button'>{download_link[0]}</button></a>""")
        
        index.write("</div>") # close download-buttons-container.
        index.write("</div>") # close item-content.
        index.write("</div>\n") # close item.

    index.write("""
    </div>
                
    <div class="footer">
        <p>Thanks for visiting! See you again 😊</p>
    </div>

    <script src="script.js" defer></script>
</body>
</html>
""")

print("\nProcess Complete!")
