import requests
import os
import json
from time import localtime, strftime

time = strftime("%a, %d %b %Y %H:%M:%S", localtime())
json.dump({'distance': '10'}, open('distance.json', 'w'))
json.dump({'string': time}, open('date.json', 'w'))
url = 'http://localhost:8765/picture/4/current/'  # URL from raspberry
r = requests.get(url)
img_data = r.content
with open('current.jpg', 'wb') as handler:
    handler.write(img_data)
    

os.system('scp current.jpg webcamml@webcamml.uber.space:/home/webcamml/html/images/current.jpg')
os.system('scp distance.json webcamml@webcamml.uber.space:/home/webcamml/WebcamML/prototype/src/assets/distance.json')
os.system('scp date.json webcamml@webcamml.uber.space:/home/webcamml/WebcamML/prototype/src/assets/date.json')