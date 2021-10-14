#!/usr/bin/env python3

import os
import sys
import shutil
from PIL import Image

fn = sys.argv[1]
os.chdir("../Downloads")
os.getcwd()

if os.path.exists(fn):  
    im = Image.open(fn)
    target_name = fn + ".jpg"
    rgb_im = im.convert('RGB')
    rgb_im.save(target_name)
    print("Saved as " + target_name)
    os.remove(fn)
    print("Original file deleted.")
else:
    print(fn + " not found")
