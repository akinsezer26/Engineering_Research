import cv2
import numpy as np
import json
import os
from keras.models import model_from_json
import subprocess

location=os.getcwd()

pid = subprocess.Popen(args=[
    "gnome-terminal", "--command=python3 monitorOutput.py"]).pid

os.chdir("../openpose")
terminalInput="./build/examples/openpose/openpose.bin --write_json output"
os.system(terminalInput)

