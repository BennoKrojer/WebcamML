import json
import os
from PIL import Image

size = (120, 120)
file = 'current.jpg'
new_filename = json.load(open('assets/date.json', 'r'))['filename']
os.makedirs('assets/thumbnails', exist_ok=True)
os.makedirs('assets/compressed', exist_ok=True)
im = Image.open(file)
im_thumbnail = im.copy()
im_thumbnail.thumbnail(size)
im_thumbnail.save("assets/thumbnails/"+new_filename+'.jpg')
im.save("assets/compressed/"+new_filename+'.jpg', quality=30)
