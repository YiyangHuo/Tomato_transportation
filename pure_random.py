#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 5/31/21 7:52 PM
#@Author: Yiyang Huo
#@File  : pure_random.py


import tensorflow as tf
import numpy as np
import tensorflow.keras as keras
import os
import pandas as pd
from keras.callbacks import CSVLogger
import matplotlib.pyplot as plt

TRAIN_SET = 14000
csv_columns = [
    "Rejection_Rate",
    "Date",
    "Season_Year",
    "County",
    "#loads",
    "Tomato_variety",
    "Average_worm/insect_damage",
    "Average_mold",
    "Average_green",
    "Average_material_other_than_tomatoes",
    "Average_hue_loads",
    "Average_hue",
    "Average_color",
    "Average_solids",
    "Average_pH"
]

def create_model():
    model = keras.models.Sequential()
    model.add(keras.layers.Dense(64, input_dim=12, activation='relu'))
    model.add(keras.layers.Dense(32, activation='relu'))
    model.add(keras.layers.Dense(16, activation='relu'))
    model.add(keras.layers.Dense(8, activation='relu'))
    model.add(keras.layers.Dense(1, activation='sigmoid'))

    return model

if __name__ == "__main__":
    data = pd.read_csv("./data/ptab_conv_random.csv",thousands=',').fillna(0)
    data.County = data.County.astype("category").cat.codes
    data.Tomato_variety = data.Tomato_variety.astype("category").cat.codes
    train_set = data[:TRAIN_SET]
    Inputs = tf.convert_to_tensor(np.array(train_set[csv_columns[3:]]), dtype=tf.float64)
    Rej_rate = tf.convert_to_tensor(np.array(train_set[csv_columns[0]]), dtype=tf.float64)
    model = create_model()

    csv_logger = CSVLogger('log.csv', append=True, separator=';')
    model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
    history = model.fit(Inputs, Rej_rate, epochs=10, batch_size=10, callbacks=[csv_logger])
    model.save("./models/random_model.h5")

    print(history.history.keys())
    plt.plot(history.history['accuracy'])
    plt.plot(history.history['loss'])
    plt.title('model accuracy')
    plt.ylabel('accuracy')
    plt.xlabel('epoch')
    plt.legend(['accuracy', 'loss'], loc='upper left')
    plt.show()



