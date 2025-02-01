import os
import yaml

source_dir = "src/"
source_files = [os.path.join(source_dir, file) for file in os.listdir(source_dir)]

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
    <div class="header">
        <h1 class="logo">FaseehApps</h1>
        <button class="theme-toggle-btn" id="theme-toggle"></button>
    </div>

    <div class="items-container">
""")
    
    for item in source_files:
        index.write("\t\t<div class='item'>\n")

        with open(item, 'r') as file:
            data = yaml.safe_load(file)
        
        index.write(f"\t\t\t<h1>{data["name"]}</h1>\n")

        if "descriptions" in data and data["descriptions"]:
            for description in data["descriptions"]:
                index.write(f"\t\t\t<p>{description}</p>\n")

        index.write("\t\t\t<div class='download-buttons-container'>\n")
        for download_link in data["links"]:
            index.write(f"""\t\t\t\t<a href={download_link[1]}><button class='download-button'>{download_link[0]}</button></a>\n""")
        index.write("\t\t\t</div>\n")

        index.write("\t\t</div>\n")

    index.write("""
    <div>

    <script src="script.js" defer></script>
</body>
</html>
""")