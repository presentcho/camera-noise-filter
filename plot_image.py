import pandas as pd
import numpy as np
import tensorflow as tf
import os
from tqdm import tqdm
from glob import glob
import gc
import cv2
import matplotlib.pyplot as plt
from sklearn.utils import shuffle
import math
import zipfile
from skimage import measure
import argparse
import imutils
from PIL import Image
import seaborn as sns
from sklearn.model_selection import train_test_split
tf.compat.v1.disable_eager_execution()

# import data set
train_csv = pd.read_csv('train.csv')
test_csv = pd.read_csv('test.csv')
train_all_input = 'train_input_img/'+train_csv['input_img']
train_all_label = 'train_label_img/'+train_csv['label_img']
test_input_files = 'test_input_img/'+test_csv['input_img']

# subset 90% of train dataset as train set
train_input_files = train_all_input[62:].to_numpy()
train_label_files = train_all_label[62:].to_numpy()
# subset 10% of train dataset as validation set
val_input_files = train_all_input[:62].to_numpy()
val_label_files = train_all_label[:62].to_numpy()

# plot the image
def process_image(path):
    img = cv2.imread(path)
    img = np.asarray(img, dtype="float32")
    img = cv2.resize(img, (256, 256))
    img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    img = img/255.0
    img = np.reshape(img, (256, 256, 1))
    return img
  
X_train = np.asarray(train_set)
X_test = np.asarray(test_set)
Y_train = np.asarray(train_cleaned)

X_train, X_val, Y_train, Y_val = train_test_split(X_train, Y_train, test_size=0.15)

import scipy.signal as signal
for i in range(0, 4):
    inp_img = cv2.imread(train_input_files[i])
    inp_img = cv2.cvtColor(inp_img, cv2.COLOR_BGR2RGB)
    fig = plt.figure(figsize = (10, 9.2))
    fig.add_subplot(151)
    plt.title('X_train')
    plt.imshow(X_train[i])
    fig.add_subplot(152)
    plt.title('X_test')
    plt.imshow(X_test[i])
    fig.add_subplot(153)
    plt.title('X_val')
    plt.imshow(X_val[i])
    fig.add_subplot(154)
    plt.title('Y_train')
    plt.imshow(Y_train[i])
    fig.add_subplot(155)
    plt.title('Y_val')
    plt.imshow(Y_val[i])
    plt.show
