import json
import os
from pprint import pprint
import csv
import math

cwd = os.getcwd()
fd1= cwd + "/JsonFiles/ayaktaDurma/"
fd2= cwd + "/JsonFiles/Oturma/"
fd3= cwd + "/JsonFiles/volta/"

def l2Dist(x1,y1,x2,y2):
	dist=math.sqrt(math.pow((x1-x2),2)+math.pow((y1-y2),2))
	return dist

myDistList=list()
mainlist=list()
maxValues=list()
for y in range(52):
	maxValues.append(0)
minValues=list()
for y in range(52):
	minValues.append(10000000)
beforeFrameList=list()
def readFromJson(_class,fileDirectory):
	for a in range(len(os.listdir(fileDirectory))):
		print(a+1)
		fileList=(fileDirectory+str(a))
		jsonList=os.listdir(fileList)
		jsonList.sort()
		for b in range(3,len(jsonList)):
			print(fileList+"/"+jsonList[b])
			with open((fileList+"/"+jsonList[b-3])) as f:
				data1 = json.load(f)			
				for y in range(len(data1["people"][0])):
					beforeFrameList=data1["people"][0]["pose_keypoints_2d"]
			with open((fileList+"/"+jsonList[b])) as f:
				data = json.load(f)
				myDistList=list()
				for y in range(len(data["people"][0])):
					mylist=data["people"][0]["pose_keypoints_2d"]
				
				scaleSample=l2Dist(mylist[3],mylist[4],mylist[24],mylist[25])
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
					myDistList.append(l2Dist(mylist[0],mylist[1],mylist[3],mylist[4])/scaleSample)
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
					for a in range(52):
						if myDistList[a]<minValues[a]:
							minValues[a]=myDistList[a]
					for a in range(52):
						if myDistList[a]>maxValues[a]:
							maxValues[a]=myDistList[a]
					myDistList.append(_class)
					mainlist.append(myDistList)
					

readFromJson(1,fd1)
readFromJson(2,fd2)
readFromJson(3,fd3)
with open("data.csv", 'wb') as myfile:
	wr = csv.DictWriter(myfile, fieldnames = 	       ['dist0',	#Headers
								'dist1',
								'dist2',
								'dist3',
								'dist4',
								'dist5',
								'dist6',
								'dist7',
								'dist8',
								'dist9',
								'dist10',
								'dist11',
								'dist12',
								'dist13',
								'dist14',
								'dist15',
		     						'Point0_C',
							     	'Point1_C',
							     	'Point2_C',
							     	'Point3_C',
							     	'Point4_C',
							     	'Point5_C',
							     	'Point6_C',
							     	'Point7_C',
							     	'Point8_C',
							     	'Point9_C',
							     	'Point10_C',
							     	'Point11_C',
							     	'Point12_C',
							     	'Point13_C',
							     	'Point14_C',
							     	'Point15_C',
							     	'Point16_C',
							     	'Point17_C',	
								'Momentum0',
								'Momentum1',
								'Momentum2',
								'Momentum3',
								'Momentum4',
								'Momentum5',
								'Momentum6',
								'Momentum7',
								'Momentum8',
								'Momentum9',
								'Momentum10',	
								'Momentum11',
								'Momentum12',
								'Momentum13',
								'Momentum14',
								'Momentum15',
								'Momentum16',
								'Momentum17',
								'Class'
							      ])
#	for a in range(len(mainlist)):
#		for b in range(len(mainlist[a])-1):
#			mainlist[a][b]=(mainlist[a][b]-minValues[b])/(maxValues[b]-minValues[b])
    	wr.writeheader()
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerows(mainlist)
#with open('minValues.json', 'w') as outfile:
#    json.dump(minValues, outfile)
#with open('maxValues.json', 'w') as outfile:
#    json.dump(maxValues, outfile)
