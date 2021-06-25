#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 6/5/21 11:19 PM
#@Author: Yiyang Huo
#@File  : test.py

import matplotlib.pyplot as plt
import matplotlib as mpl

import  matplotlib.font_manager
# flist = matplotlib.font_manager.get_fontconfig_fonts()
# names = [matplotlib.font_manager.FontProperties(fname=fname).get_name() for fname in flist]
# print(names)

single_cnn_loss = [0.2620,0.2192, 0.2114, 0.2073, 0.1989, 0.1927, 0.1877, 0.1819, 0.1768, 0.1752]
single_cnn_accuracy = [0.6671, 0.6731, 0.6769, 0.6790, 0.6862, 0.6975, 0.7038, 0.7178, 0.7229, 0.7239]
single_cnn_val_loss = [0.2274, 0.2193, 0.2208, 0.2081, 0.2009, 0.1979, 0.2069, 0.1905, 0.1989, 0.1788]
single_cnn_val_accuracy = [0.6591,0.6576, 0.6730, 0.6695, 0.6794, 0.6844, 0.6749, 0.6864, 0.6655, 0.7002]

double_cnn_loss  = [0.2388, 0.1902, 0.1765, 0.1698, 0.1638, 0.1598, .1570, 0.1558, 0.1507, 0.1476]
double_cnn_accuracy = [0.6650, 0.6917, 0.6959, 0.7081, 0.7250, 0.7343, 0.7426, 0.7423, 0.7540, 0.7586]
double_cnn_val_loss = [0.1960, 0.1788, 0.1674, 0.1654, 0.1601, 0.1553, 0.1554, 0.1574, 0.1520, 0.1487]
double_cnn_val_accuracy = [0.6958, 0.6779, 0.7077, 0.7236, 0.7206, 0.7390, 0.7375, 0.7464, 0.7489, 0.7573]

triple_cnn_loss = [0.2276, 0.1653, 0.1572, 0.1541, 0.1503, 0.1471, 0.1461, 0.1417, 0.1412, 0.1372]
triple_cnn_accuracy = [0.6781, 0.7235, 0.7344, 0.7391, 0.7469, 0.7535, 0.7569, 0.7679, 0.7642, 0.7747]
triple_cnn_val_loss = [0.1605, 0.1512, 0.1627, 0.1493, 0.1469, 0.1471, 0.1381, 0.1412, 0.1360, 0.1395]
triple_cnn_val_accuracy = [0.7444, 0.7474, 0.7201, 0.7424, 0.7499, 0.7593, 0.7816, 0.7588, 0.7782, 0.7707]

csfont = {'fontname':'Times New Roman',"fontsize":13}
mpl.rc('font',family='Times New Roman')
plt.rcParams.update({"font.size":13})
# plt.plot(single_cnn_loss, label='Single CNN Model')
# plt.plot(double_cnn_loss, label='CNN Model with Categorical MLP')
# plt.plot(triple_cnn_loss, label='CNN Model with Categorical MLP and Numeric MLP')
# plt.plot(single_cnn_accuracy, label='Single CNN Model')
# plt.plot(double_cnn_accuracy, label='CNN Model with Categorical MLP')
# plt.plot(triple_cnn_accuracy, label='CNN Model with Categorical MLP and Numeric MLP')
#plt.plot(single_cnn_val_loss, label='Single CNN Model')
#plt.plot(double_cnn_val_loss, label='CNN Model with Categorical MLP')
#plt.plot(triple_cnn_val_loss, label='CNN Model with Categorical MLP and Numeric MLP')
plt.plot(single_cnn_val_accuracy, label='Single CNN Model')
plt.plot(double_cnn_val_accuracy, label='CNN Model with Categorical MLP')
plt.plot(triple_cnn_val_accuracy , label='CNN Model with Categorical MLP and Numeric MLP')
plt.title('Value Accuracy Comparison',**csfont)
plt.ylabel('Value Accuracy',**csfont)
# plt.title('Loss Comparison',**csfont)
# plt.ylabel('Loss',**csfont)
#plt.ylabel('Value Accuracy',**csfont)
# plt.title('Value Loss Comparison',**csfont)
# plt.ylabel('Value Loss',**csfont)
# plt.title('Accuracy Comparison',**csfont)
# plt.ylabel('Accuracy',**csfont)
plt.xlabel('Epoch',**csfont)
plt.legend(loc='upper left')
#plt.legend(['single cnn model', 'cnn model with categorical mlp', 'cnn model with categorical mlp and numeric mlp'], loc='upper left',**csfont)
plt.show()