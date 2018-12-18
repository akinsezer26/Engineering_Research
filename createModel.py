import tensorflow as tf
import keras
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import os

#read in data using pandas
cwd = os.getcwd()
train_df = pd.read_csv(cwd + "/data.csv")

#view data structure
train_df.head()

#create a dataframe with all training data except the target column
train_X = train_df.drop(columns=['Class'])

#check that the target variable has been removed
train_X.head()

from keras.utils import to_categorical

#one-hot encode target column
train_y = to_categorical(train_df.Class)

#vcheck that target column has been converted
train_y[0:5]

#create model
model = Sequential()

#get number of columns in training data
n_cols = train_X.shape[1]

#add layers to model
model.add(Dense(250, activation='sigmoid', input_shape=(n_cols,)))
model.add(Dense(250, activation='sigmoid'))
model.add(Dense(250, activation='sigmoid'))
model.add(Dense(4, activation='softmax'))

#compile model using accuracy to measure model performance
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#train model
model.fit(train_X, train_y, epochs=30, validation_split=0.2)
#a=model.evaluate(train_X, train_y, None, verbose=1, sample_weight=None, steps=None)

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
