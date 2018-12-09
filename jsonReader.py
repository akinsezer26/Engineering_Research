import json
import os
from pprint import pprint
fileDirectory = raw_input("Enter Train File Directory(./......./):")

for a in range(len(os.listdir(fileDirectory))):
	print(a+1)
	fileList=(fileDirectory+str(a+1))
	print(fileList)
	jsonList=os.listdir(fileList)
	jsonList.sort()
	for b in range(len(jsonList)):
		print(fileList+"/"+jsonList[b])
		with open((fileList+"/"+jsonList[b])) as f:
			data = json.load(f)
			for y in range(len(data["people"][0])):
					print("-------------------")					
					for x in range(len(data["people"][0]["pose_keypoints_2d"])):				
						pprint(data["people"][0]["pose_keypoints_2d"][x])
