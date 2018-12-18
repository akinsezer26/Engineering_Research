import tensorflow as tf
import keras
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import os
from keras.models import model_from_json
import numpy

#read in data using pandas
cwd = os.getcwd()
test_data = pd.read_csv(cwd + "/dataTest.csv")

#view data structure
test_data.head()

#create a dataframe with all training data except the target column
test_data_X = test_data.drop(columns=['Class'])

#check that the target variable has been removed
test_data_X.head()

from keras.utils import to_categorical

#one-hot encode target column
test_data_y = to_categorical(test_data.Class)

#vcheck that target column has been converted
test_data_y[0:5]

json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

# evaluate loaded model on test data
loaded_model.compile(loss='binary_crossentropy', optimizer='rmsprop', metrics=['accuracy'])
score = loaded_model.evaluate(test_data_X, test_data_y, None, verbose=1, sample_weight=None, steps=None)
print("%s: %.2f%%" % (loaded_model.metrics_names[1], score[1]*100))
