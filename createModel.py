import tensorflow as tf
import keras
import pandas as pd
from keras.models import Sequential
from keras.layers import Dense
import os
from keras import optimizers
from keras import regularizers

#read in data using pandas
cwd = os.getcwd()
train_df = pd.read_csv(cwd + "/data.csv")
#validation_df = pd.read_csv(cwd + "/dataTest.csv")

#view data structure
train_df.head()
#validation_df.head()

#create a dataframe with all training data except the target column
train_X = train_df.drop(columns=['Class'])
#validation_X = validation_df.drop(columns=['Class'])

#check that the target variable has been removed
train_X.head()
#validation_X.head()

from keras.utils import to_categorical

#one-hot encode target column
train_y = to_categorical(train_df.Class)
#validation_y = to_categorical(validation_df.Class)

#vcheck that target column has been converted
train_y[0:5]
#validation_y[0:5]

#create model
model = Sequential()

#get number of columns in training data
n_cols = train_X.shape[1]

#early_stop = keras.callbacks.EarlyStopping(monitor='val_loss', min_delta=0, patience=3, verbose=1, mode='auto')
#model.add(Dense(52, input_dim=52,
#            kernel_regularizer=regularizers.l2(0.01),
#            activity_regularizer=regularizers.l1(0.01)))
#add layers to model
model.add(Dense(52, activation='sigmoid', input_shape=(n_cols,)))
model.add(Dense(20, activation='sigmoid'))
model.add(Dense(20, activation='sigmoid'))
model.add(Dense(4, activation='softmax'))

#opt=optimizers.SGD(lr=0.1, momentum=0.1)
#compile model using accuracy to measure model performance
model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

#train model
model.fit(train_X, train_y, epochs=200, validation_split=1)

print(model.evaluate(train_X, train_y, verbose=0))

# serialize model to JSON
model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)
# serialize weights to HDF5
model.save_weights("model.h5")
print("Saved model to disk")
