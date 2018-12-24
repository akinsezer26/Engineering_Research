#import cv2
import numpy as np
import json
import os
from keras.models import model_from_json
import subprocess

os.chdir("../openpose/output")
location=os.getcwd()
jsonFilesToDelete=os.listdir(location)
print(jsonFilesToDelete)
for i in range(0,len(jsonFilesToDelete)):
	os.system("rm -f "+jsonFilesToDelete[i])

os.chdir("..")
os.chdir("../Engineering_Research")
pid = subprocess.Popen(args=[
    "gnome-terminal","--zoom=1.8","--command=python3 monitorOutput.py"]).pid

os.chdir("../openpose")
terminalInput="./build/examples/openpose/openpose.bin --write_json output"
#terminalInput="./build/examples/openpose/openpose.bin --video examples/media/VID_20181224_112714.mp4 --write_json output"

os.system(terminalInput)

