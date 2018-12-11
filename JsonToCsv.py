import json
import os
from pprint import pprint
import csv

fd1=raw_input("Enter Train File Directory(./......./):")
fd2=raw_input("Enter Train File Directory(./......./):")
fd3=raw_input("Enter Train File Directory(./......./):")


mainlist=list()
beforeFrameList=list()
momentlist=list()
def readFromJson(_class,fileDirectory):
	for a in range(len(os.listdir(fileDirectory))):
		print(a+1)
		fileList=(fileDirectory+str(a))
		jsonList=os.listdir(fileList)
		jsonList.sort()
		for b in range(1,len(jsonList)):
			print(fileList+"/"+jsonList[b])
			with open((fileList+"/"+jsonList[b-1])) as f:
				data1 = json.load(f)			
				for y in range(len(data1["people"][0])):
					beforeFrameList=data1["people"][0]["pose_keypoints_2d"]
			with open((fileList+"/"+jsonList[b])) as f:
				data = json.load(f)
				for y in range(len(data["people"][0])):
					mylist=data["people"][0]["pose_keypoints_2d"]
				for y in range(54):
					if y%3!=2:
						mylist.append(mylist[y]-beforeFrameList[y])
				mylist.append(_class)
				mainlist.append(mylist)
	

readFromJson(1,fd1)
readFromJson(2,fd2)
readFromJson(3,fd3)
with open("data.csv", 'wb') as myfile:
	wr = csv.DictWriter(myfile, fieldnames = 	       ['Point0_X',	#Headers
		     						'Point0_Y',
		     						'Point0_C',
								'Point1_X',
							     	'Point1_Y',
							     	'Point1_C',
								'Point2_X',
							     	'Point2_Y',
							     	'Point2_C',
								'Point3_X',
							     	'Point3_Y',
							     	'Point3_C',
								'Point4_X',
							     	'Point4_Y',
							     	'Point4_C',
								'Point5_X',
						       	     	'Point5_Y',
							     	'Point5_C',
								'Point6_X',
							     	'Point6_Y',
							     	'Point6_C',
								'Point7_X',
							     	'Point7_Y',
							     	'Point7_C',
								'Point8_X',
							     	'Point8_Y',
							     	'Point8_C',
								'Point9_X',
							     	'Point9_Y',
							     	'Point9_C',
								'Point10_X',
							     	'Point10_Y',
							     	'Point10_C',
								'Point11_X',
							     	'Point11_Y',
							     	'Point11_C',
								'Point12_X',
							     	'Point12_Y',
							     	'Point12_C',
								'Point13_X',
							     	'Point13_Y',
							     	'Point13_C',
								'Point14_X',
							     	'Point14_Y',
							     	'Point14_C',
								'Point15_X',
							     	'Point15_Y',
							     	'Point15_C',
								'Point16_X',
							     	'Point16_Y',
							     	'Point16_C',
								'Point17_X',
							     	'Point17_Y',
							     	'Point17_C',
								'Momentum0_X',
								'Momentum0_Y',
								'Momentum1_X',
								'Momentum1_Y',
								'Momentum2_X',
								'Momentum2_Y',
								'Momentum3_X',
								'Momentum3_Y',
								'Momentum4_X',
								'Momentum4_Y',
								'Momentum5_X',
								'Momentum5_Y',
								'Momentum6_X',
								'Momentum6_Y',
								'Momentum7_X',
								'Momentum7_Y',
								'Momentum8_X',
								'Momentum8_Y',
								'Momentum9_X',
								'Momentum9_Y',
								'Momentum10_X',
								'Momentum10_Y',
								'Momentum11_X',
								'Momentum11_Y',
								'Momentum12_X',
								'Momentum12_Y',
								'Momentum13_X',
								'Momentum13_Y',
								'Momentum14_X',
								'Momentum14_Y',
								'Momentum15_X',
								'Momentum15_Y',
								'Momentum16_X',
								'Momentum16_Y',
								'Momentum17_X',
								'Momentum17_Y',
								'Class'
							      ])
    	wr.writeheader()
	wr = csv.writer(myfile, quoting=csv.QUOTE_ALL)
	wr.writerows(mainlist)

