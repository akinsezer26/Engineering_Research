#import cv2
import numpy as np
import json
import os
from keras.models import model_from_json
import subprocess
import math
import ast
from time import sleep

xScale=1.5
yScale=1.5

def l2Dist(x1,y1,x2,y2):
	dist=math.sqrt(math.pow(xScale*(x1-x2),2)+math.pow(yScale*(y1-y2),2))
	return dist

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

beforeFramePersonCount=0
FramePersonCount=0
scaleSample=0
while 1:
	sleep(0.05)
	os.system("clear")
	jsonList=os.listdir(outputLocation)
	if len(jsonList)>5:
		jsonList.sort()
		sample=jsonList[-1]
		previousSample=jsonList[-4]
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

						with open((outputLocation+"/"+previousSample)) as f:
							data1 = json.load(f)
							for i in range(len(data1["people"])):
								beforeFrameList.append([])
								myDistList.append([])
							beforeFramePersonCount=len(data1["people"])

							for t in range(len(data1["people"])):			
								for y in range(len(data1["people"][t])):
									beforeFrameList[t]=data1["people"][t]["pose_keypoints_2d"]
						with open((outputLocation+"/"+sample)) as f:
							data = json.load(f)
							FramePersonCount=len(data["people"])
							if FramePersonCount==beforeFramePersonCount:
								for z in range(len(data["people"])):
									for y in range(len(data["people"][z])):
										mylist=data["people"][z]["pose_keypoints_2d"]
									scaleSample=l2Dist(mylist[3],mylist[4],mylist[24],mylist[25])
									if scaleSample!=0:
										myDistList[z].append(l2Dist(mylist[48],mylist[49],mylist[42],mylist[43])/scaleSample)
										myDistList[z].append(l2Dist(mylist[42],mylist[43],mylist[0],mylist[1])/scaleSample)
										myDistList[z].append(l2Dist(mylist[0],mylist[1],mylist[45],mylist[46])/scaleSample)
										myDistList[z].append(l2Dist(mylist[45],mylist[46],mylist[51],mylist[52])/scaleSample)
										myDistList[z].append(l2Dist(mylist[3],mylist[4],mylist[6],mylist[7])/scaleSample)
										myDistList[z].append(l2Dist(mylist[6],mylist[7],mylist[9],mylist[10])/scaleSample)
										myDistList[z].append(l2Dist(mylist[9],mylist[10],mylist[12],mylist[13])/scaleSample)
										myDistList[z].append(l2Dist(mylist[3],mylist[4],mylist[15],mylist[16])/scaleSample)
										myDistList[z].append(l2Dist(mylist[15],mylist[16],mylist[18],mylist[19])/scaleSample)
										myDistList[z].append(l2Dist(mylist[18],mylist[19],mylist[21],mylist[22])/scaleSample)
										myDistList[z].append(l2Dist(mylist[0],mylist[1],mylist[3],mylist[4])/scaleSample)
										myDistList[z].append(l2Dist(mylist[24],mylist[25],mylist[27],mylist[28])/scaleSample)
										myDistList[z].append(l2Dist(mylist[27],mylist[28],mylist[30],mylist[31])/scaleSample)
										myDistList[z].append(l2Dist(mylist[3],mylist[4],mylist[33],mylist[34])/scaleSample)
										myDistList[z].append(l2Dist(mylist[33],mylist[34],mylist[36],mylist[37])/scaleSample)
										myDistList[z].append(l2Dist(mylist[36],mylist[37],mylist[39],mylist[40])/scaleSample)
										myDistList[z].append(mylist[2])
										myDistList[z].append(mylist[5])
										myDistList[z].append(mylist[8])
										myDistList[z].append(mylist[11])
										myDistList[z].append(mylist[14])
										myDistList[z].append(mylist[17])
										myDistList[z].append(mylist[20])
										myDistList[z].append(mylist[23])
										myDistList[z].append(mylist[26])
										myDistList[z].append(mylist[29])
										myDistList[z].append(mylist[32])
										myDistList[z].append(mylist[35])
										myDistList[z].append(mylist[38])
										myDistList[z].append(mylist[41])
										myDistList[z].append(mylist[44])
										myDistList[z].append(mylist[47])
										myDistList[z].append(mylist[50])
										myDistList[z].append(mylist[53])
										myDistList[z].append(l2Dist(mylist[0],mylist[1],beforeFrameList[z][0],beforeFrameList[z][1])/scaleSample)
										myDistList[z].append(l2Dist(mylist[3],mylist[4],beforeFrameList[z][3],beforeFrameList[z][4])/scaleSample)
										myDistList[z].append(l2Dist(mylist[6],mylist[7],beforeFrameList[z][6],beforeFrameList[z][7])/scaleSample)
										myDistList[z].append(l2Dist(mylist[9],mylist[10],beforeFrameList[z][9],beforeFrameList[z][10])/scaleSample)
										myDistList[z].append(l2Dist(mylist[12],mylist[13],beforeFrameList[z][12],beforeFrameList[z][13])/scaleSample)
										myDistList[z].append(l2Dist(mylist[15],mylist[16],beforeFrameList[z][15],beforeFrameList[z][16])/scaleSample)
										myDistList[z].append(l2Dist(mylist[18],mylist[19],beforeFrameList[z][18],beforeFrameList[z][19])/scaleSample)
										myDistList[z].append(l2Dist(mylist[21],mylist[22],beforeFrameList[z][21],beforeFrameList[z][22])/scaleSample)
										myDistList[z].append(l2Dist(mylist[24],mylist[25],beforeFrameList[z][24],beforeFrameList[z][25])/scaleSample)
										myDistList[z].append(l2Dist(mylist[27],mylist[28],beforeFrameList[z][27],beforeFrameList[z][28])/scaleSample)
										myDistList[z].append(l2Dist(mylist[30],mylist[31],beforeFrameList[z][30],beforeFrameList[z][31])/scaleSample)
										myDistList[z].append(l2Dist(mylist[33],mylist[34],beforeFrameList[z][33],beforeFrameList[z][34])/scaleSample)
										myDistList[z].append(l2Dist(mylist[36],mylist[37],beforeFrameList[z][36],beforeFrameList[z][37])/scaleSample)
										myDistList[z].append(l2Dist(mylist[39],mylist[40],beforeFrameList[z][39],beforeFrameList[z][40])/scaleSample)
										myDistList[z].append(l2Dist(mylist[42],mylist[43],beforeFrameList[z][42],beforeFrameList[z][43])/scaleSample)
										myDistList[z].append(l2Dist(mylist[45],mylist[46],beforeFrameList[z][45],beforeFrameList[z][46])/scaleSample)
										myDistList[z].append(l2Dist(mylist[48],mylist[49],beforeFrameList[z][48],beforeFrameList[z][49])/scaleSample)
										myDistList[z].append(l2Dist(mylist[51],mylist[52],beforeFrameList[z][51],beforeFrameList[z][52])/scaleSample)
										#for a in range(len(myDistList)):
										#	myDistList[a]=(myDistList[a]-minValues1[a])/(maxValues1[a]-minValues1[a])
								
								values = [x for x in myDistList if x != []]
								for z in range(len(values)):
									if(values):	
										single_test = np.array(values[z])
										single_test = single_test.reshape(1,52)
										prediction = loaded_model.predict_classes( single_test )							
										if prediction==1:
											print("Kisi {0} Ayakta".format(z+1))
										elif prediction==2:
											print("Kisi {0} Oturuyor".format(z+1))
										else:
											print("Kisi {0} Yuruyor".format(z+1))
							else:
								print("Kişi Algılanmadı")
			else:
						print("Kişi Algılanmadı")
