#import cv2
import numpy as np
import json
import os
from keras.models import model_from_json
import subprocess
import math
import ast
import matplotlib.pyplot as plt
import matplotlib.lines as mlines

xScale=1920/1280
yScale=1080/720

def l2Dist(x1,y1,x2,y2):
	plt.plot([x1,x2],[y1,y2])

location=os.getcwd()

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")

#json_file1 = open('minValues.json', 'r')
#minValues = json_file1.read()
#json_file1.close()
#minValues = ast.literal_eval(minValues)

#json_file2 = open('maxValues.json', 'r')
#maxValues = json_file2.read()
#json_file2.close()
#maxValues = ast.literal_eval(maxValues)
#maxValues1=list()
#minValues1=list()
#for y in range(52):
#	maxValues1.append(maxValues.pop(0))
#	minValues1.append(minValues.pop(0))

#maxValues1=np.array(maxValues1)
#minValues1=np.array(minValues1)

os.chdir("..")
outputLocation=os.getcwd() + "/openpose/output"

loaded_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])


jsonList=os.listdir(outputLocation)
if len(jsonList)>3:
	jsonList.sort()
	sample=jsonList[-1]
	previousSample=jsonList[-2]
	with open((outputLocation+"/"+previousSample)) as f:		
		data2 = json.load(f)
		if len(data2["people"])!=0:
			with open((outputLocation+"/"+sample)) as f:		
				data3 = json.load(f)
				if len(data3["people"])!=0:		
					mainlist=list()
					myDistList=list()
					beforeFrameList=list()
					mylist=list()
					with open((outputLocation+"/"+sample)) as f:
						data1 = json.load(f)			
						for y in range(len(data1["people"][0])):
							beforeFrameList=data1["people"][0]["pose_keypoints_2d"]
					with open((outputLocation+"/"+previousSample)) as f:
						data = json.load(f)
						for y in range(len(data["people"][0])):
							mylist=data["people"][0]["pose_keypoints_2d"]
						scaleSample=l2Dist(mylist[0],mylist[1],mylist[3],mylist[4])
						if scaleSample!=0:
							l2Dist(mylist[48],mylist[49],mylist[42],mylist[43])
							l2Dist(mylist[42],mylist[43],mylist[0],mylist[1])
							l2Dist(mylist[0],mylist[1],mylist[45],mylist[46])
							l2Dist(mylist[45],mylist[46],mylist[51],mylist[52])
							l2Dist(mylist[3],mylist[4],mylist[6],mylist[7])
							l2Dist(mylist[6],mylist[7],mylist[9],mylist[10])
							l2Dist(mylist[9],mylist[10],mylist[12],mylist[13])
							l2Dist(mylist[3],mylist[4],mylist[15],mylist[16])
							l2Dist(mylist[15],mylist[16],mylist[18],mylist[19])
							l2Dist(mylist[18],mylist[19],mylist[21],mylist[22])
							l2Dist(mylist[3],mylist[4],mylist[24],mylist[25])
							l2Dist(mylist[24],mylist[25],mylist[27],mylist[28])
							l2Dist(mylist[27],mylist[28],mylist[30],mylist[31])
							l2Dist(mylist[3],mylist[4],mylist[33],mylist[34])
							l2Dist(mylist[33],mylist[34],mylist[36],mylist[37])
							l2Dist(mylist[36],mylist[37],mylist[39],mylist[40])
plt.show()
