import os
import yaml

def add_identation(string: str, identation_level: int) -> str:
    return string.replace('\n', '\n' + '    ' * identation_level)

def download_item(path_to_src: str) -> str:
    """Returns the HTML code for a download item from the yaml file where the metadata is stored."""
    with open(path_to_src, 'r') as file:
        data = yaml.safe_load(file)
    
    asset = "<!-- No Asset -->" # An asset might be a video or an image.
    if path := data.get("path_to_vid"):
        class_name, asset = "item-with-img", f"<video class='item-img' autoplay muted loop playsinline><source src='{path}' type='video/mp4'>Your browser does not support the video tag.</video>"
    elif path := data.get("path_to_img"):
        class_name, asset = "item-with-img", f"<img src='{path}' class='item-img'>"
    else:
        class_name = "item-without-img"

    description = ""
    if "description" in data and data["description"]:
        for paragraph in data["description"]:
            description += f"""<p>{paragraph}</p>"""

    download_btns = []
    for download_link in data["links"]:
        download_btns.append(f"""<a href={download_link[1]}><button class='download-button'>{download_link[0]}</button></a>""")

    return f"""
<div class="{class_name}">
    {asset}
    <div class="item-content">
        <h1>{data["name"]}</h1>
        {description}
        <div class="download-buttons-container">
            {"\n\t\t\t".join(download_btns)}
        </div>
    </div>
</div>
"""

def merge_css_files(src_dir: str) -> str:
    src_files = sorted([os.path.join(src_dir, file) for file in os.listdir(src_dir)])
    contents = []
    
    for file in src_files:
        with open(file, 'r', encoding='utf-8') as opened_file:
            contents.append(opened_file.read())
    
    return "\n".join(contents)