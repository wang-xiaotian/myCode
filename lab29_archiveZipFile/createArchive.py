#!/usr/bin/env python3
import os
import zipfile
DEFAULT_PATH = "./lab29_archiveZipFile/"

def zipdir(path, ziph):
    for root, dirs, files in os.walk(path):
        for file in files:
            print(os.path.join(root, file))
            ziph.write(os.path.join(root, file))

dir2zip = DEFAULT_PATH

if os.path.isdir(dir2zip):
    zippedFn = "myZipped.zip" # output file name
    zipFileObj = zipfile.ZipFile(zippedFn, 'w', zipfile.ZIP_DEFLATED) # zip object and making new zip file
    zipdir(dir2zip, zipFileObj)
    zipFileObj.close()
else:
    print("Run the script again when you have a valid directory to zip.")



