#import cv2
import numpy as np
import json
import os
from keras.models import model_from_json
import subprocess
import math

def l2Dist(x1,y1,x2,y2):
	dist=math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))
	return dist

location=os.getcwd()
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights("model.h5")

os.chdir("..")
outputLocation=os.getcwd() + "/openpose/output"


while 1:
	jsonList=os.listdir(outputLocation)
	if len(jsonList)>3:
		jsonList.sort()
		sample=jsonList[-1]
		previousSample=jsonList[-2]
		print(sample)
		print(previousSample)
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
				myDistList.append(l2Dist(mylist[48],mylist[49],mylist[42],mylist[43])/scaleSample)
				myDistList.append(l2Dist(mylist[42],mylist[43],mylist[0],mylist[1])/scaleSample)
				myDistList.append(l2Dist(mylist[0],mylist[1],mylist[45],mylist[46])/scaleSample)
				myDistList.append(l2Dist(mylist[45],mylist[46],mylist[51],mylist[52])/scaleSample)
				myDistList.append(l2Dist(mylist[3],mylist[4],mylist[6],mylist[7])/scaleSample)
				myDistList.append(l2Dist(mylist[6],mylist[7],mylist[9],mylist[10])/scaleSample)
				myDistList.append(l2Dist(mylist[9],mylist[10],mylist[12],mylist[13])/scaleSample)
				myDistList.append(l2Dist(mylist[3],mylist[4],mylist[15],mylist[16])/scaleSample)
				myDistList.append(l2Dist(mylist[15],mylist[16],mylist[18],mylist[19])/scaleSample)
				myDistList.append(l2Dist(mylist[18],mylist[19],mylist[21],mylist[22])/scaleSample)
				myDistList.append(l2Dist(mylist[3],mylist[4],mylist[24],mylist[25])/scaleSample)
				myDistList.append(l2Dist(mylist[24],mylist[25],mylist[27],mylist[28])/scaleSample)
				myDistList.append(l2Dist(mylist[27],mylist[28],mylist[30],mylist[31])/scaleSample)
				myDistList.append(l2Dist(mylist[3],mylist[4],mylist[33],mylist[34])/scaleSample)
				myDistList.append(l2Dist(mylist[33],mylist[34],mylist[36],mylist[37])/scaleSample)
				myDistList.append(l2Dist(mylist[36],mylist[37],mylist[39],mylist[40])/scaleSample)
				myDistList.append(mylist[2])
				myDistList.append(mylist[5])
				myDistList.append(mylist[8])
				myDistList.append(mylist[11])
				myDistList.append(mylist[14])
				myDistList.append(mylist[17])
				myDistList.append(mylist[20])
				myDistList.append(mylist[23])
				myDistList.append(mylist[26])
				myDistList.append(mylist[29])
				myDistList.append(mylist[32])
				myDistList.append(mylist[35])
				myDistList.append(mylist[38])
				myDistList.append(mylist[41])
				myDistList.append(mylist[44])
				myDistList.append(mylist[47])
				myDistList.append(mylist[50])
				myDistList.append(mylist[53])
				myDistList.append(l2Dist(mylist[0],mylist[1],beforeFrameList[0],beforeFrameList[1])/scaleSample)
				myDistList.append(l2Dist(mylist[3],mylist[4],beforeFrameList[3],beforeFrameList[4])/scaleSample)
				myDistList.append(l2Dist(mylist[6],mylist[7],beforeFrameList[6],beforeFrameList[7])/scaleSample)
				myDistList.append(l2Dist(mylist[9],mylist[10],beforeFrameList[9],beforeFrameList[10])/scaleSample)
				myDistList.append(l2Dist(mylist[12],mylist[13],beforeFrameList[12],beforeFrameList[13])/scaleSample)
				myDistList.append(l2Dist(mylist[15],mylist[16],beforeFrameList[15],beforeFrameList[16])/scaleSample)
				myDistList.append(l2Dist(mylist[18],mylist[19],beforeFrameList[18],beforeFrameList[19])/scaleSample)
				myDistList.append(l2Dist(mylist[21],mylist[22],beforeFrameList[21],beforeFrameList[22])/scaleSample)
				myDistList.append(l2Dist(mylist[24],mylist[25],beforeFrameList[24],beforeFrameList[25])/scaleSample)
				myDistList.append(l2Dist(mylist[27],mylist[28],beforeFrameList[27],beforeFrameList[28])/scaleSample)
				myDistList.append(l2Dist(mylist[30],mylist[31],beforeFrameList[30],beforeFrameList[31])/scaleSample)
				myDistList.append(l2Dist(mylist[33],mylist[34],beforeFrameList[33],beforeFrameList[34])/scaleSample)
				myDistList.append(l2Dist(mylist[36],mylist[37],beforeFrameList[36],beforeFrameList[37])/scaleSample)
				myDistList.append(l2Dist(mylist[39],mylist[40],beforeFrameList[39],beforeFrameList[40])/scaleSample)
				myDistList.append(l2Dist(mylist[42],mylist[43],beforeFrameList[42],beforeFrameList[43])/scaleSample)
				myDistList.append(l2Dist(mylist[45],mylist[46],beforeFrameList[45],beforeFrameList[46])/scaleSample)
				myDistList.append(l2Dist(mylist[48],mylist[49],beforeFrameList[48],beforeFrameList[49])/scaleSample)
				myDistList.append(l2Dist(mylist[51],mylist[52],beforeFrameList[51],beforeFrameList[52])/scaleSample)
				mainlist.append(myDistList)

		single_test = np.asarray(mainlist)
		single_test = single_test.reshape(1,52)
		prediction = loaded_model.predict_classes( single_test )
		os.system("clear")
		if prediction==1:
			print("Ayakta")
		elif prediction==2:
			print("Oturuyor")
		else:
			print("Yuruyor")
