#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 5/31/21 6:45 PM
#@Author: Yiyang Huo
#@File  : convert_csv.py

import csv

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


import pandas as pd
import numpy as np

random = True
df = pd.read_csv('data/ptab.csv')
df = df[df["#loads"] != "0.0"]
df["Date"] = pd.to_datetime(df["Date"])

df['Average_hue_loads'] = pd.to_numeric(df['Average_hue_loads'],errors='coerce')
df['Average_hue'] = pd.to_numeric(df['Average_hue'],errors='coerce')

hue_loads_mean_value=df['Average_hue_loads'].mean()
hue_mean_value = df['Average_hue'].mean()
df['Average_hue_loads'].fillna(value=hue_loads_mean_value, inplace=True)
df['Average_hue'].fillna(value=hue_mean_value, inplace=True)
df = df.sort_values(["Date", "Tomato_variety"])
output_unique = np.array2string(df.Tomato_variety.unique(), precision=2, separator=',',
                      suppress_small=True)

f=open('unique varieties.txt','w')
f.write(output_unique)
f.close()

if not random:
    df.to_csv('data/ptab_conv.csv', index=False)
else:
    df = df.sample(frac=1)
    df.to_csv('data/ptab_conv_random.csv', index=False)