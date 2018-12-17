import json
import os
from pprint import pprint

hareket1="ayaktaDurma"
hareket2="Oturma"
hareket3="volta"

hareket=hareket2
print os.getcwd()
videoLocations = "/home/celal/openpose/train/"+str(hareket)
os.chdir('/home/celal/openpose')
print os.getcwd()
files=os.listdir(videoLocations)
files.sort()

for i in range(len(files)):
	if not os.path.exists("/home/celal/openpose/train/JsonFiles/"+str(hareket)+"/"+str(i)):
		os.makedirs("/home/celal/openpose/train/JsonFiles/"+str(hareket)+"/"+str(i))
	print(i)
	terminalInput="./build/examples/openpose/openpose.bin --video train/"+hareket+"/"+ str(files[i]) +"  --write_json train/JsonFiles/"+str(hareket)+"/"+str(i)
	os.system(terminalInput)
os.system("echo 'DONE!!'")



