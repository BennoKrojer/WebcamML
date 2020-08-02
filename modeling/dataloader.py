from PIL import Image
import config
from glob import glob
import pandas as pd


def get_image_paths():
    d = {'path': [], 'label': []}
    for file in glob(str(config.images)+'/*.jpg'):
        splits = file.split('_')
        if len(splits) == 3:
            label = splits[2][:-4]
            d['path'].append(file)
            d['label'].append(label)
    return pd.DataFrame.from_dict(d)


