import os
from PIL import Image
import urllib.request, json
from datetime import date

# ⚠️  File path should end with a '/'
save_dir = "YOUR/FILE/PATH/HERE/"

def get_img(filename):
    with urllib.request.urlopen("https://xkcd.com/info.0.json") as url:
        img_url = json.load(url)['img']
        urllib.request.urlretrieve(img_url, filename)
        
if os.path.isdir(save_dir):
    today = str(date.today())
    filepath = save_dir + str(today) + ".png"

    # If there isn't currently an image in the dir
    if not os.listdir(save_dir):
        get_img(filepath)
    # Or if it's outdated
    elif os.listdir(save_dir)[0] != today + ".png":    
        get_img(filepath)

    # And always show the image
    os.system(f"viu -w 140 -h 20 {filepath}")
else:
    print("😬 Save directory doesn't exist...that's awkward")
