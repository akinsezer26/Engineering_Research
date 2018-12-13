import tensorflow as tf
import keras
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import os
import numpy as np

def sigmoid_activation(x, takeDerivate = False):
    
    if(takeDerivate == True):
        return sigmoid_activation(x) * (1 - sigmoid_activation(x))
    
    return 1 / (1 + np.exp(-x))

def trainData(inputs,t,weights,rho,iterNo):
for iter in range(100):                                   
	for i in range(inputs.shape[0]):                 
        	x=inputs[i,:]                                        
        	sum=np.dot(weights,x)                        
            	y=sigmoid_activation(sum,False)              
            	delta_w = rho*(t[i]-y)*sigmoid_activation(y,True)*x  
            	weights = np.add(weights,delta_w)                    
return weights

cwd = os.getcwd()

train_df = pd.read_csv(cwd + "/data.csv")

train_df.head()

train_X = train_df.drop(columns=['Class'])

train_X.head()

train_y = train_df[['Class']]

train_y.head()






