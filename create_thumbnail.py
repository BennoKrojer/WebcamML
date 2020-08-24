#!
import json
import os
from PIL import Image

size = (120, 120)
image_dir = '/home/webcamml/html/images'
assets_dir = '/home/webcamml/WebcamML/prototype/src/assets'
new_filename = json.load(open(assets_dir + '/date.json', 'r'))['filename']
os.makedirs(image_dir + '/thumbnails', exist_ok=True)
os.makedirs(image_dir + '/compressed', exist_ok=True)
im = Image.open(image_dir+'/current.jpg')
im_thumbnail = im.copy()
im_thumbnail.thumbnail(size)
im_thumbnail.save(f'{image_dir}/thumbnail/{new_filename}.jpg')
im.save(f'{image_dir}/compressed/{new_filename}.jpg', quality=30)
