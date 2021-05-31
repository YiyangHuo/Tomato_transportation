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
random = True
df = pd.read_csv('data/ptab.csv')
df = df[df["#loads"] != "0.0"]
df["Date"] = pd.to_datetime(df["Date"])
df = df.sort_values(["Date", "Tomato_variety"])
if not random:
    df.to_csv('data/ptab_conv.csv', index=False)
else:
    df = df.sample(frac=1)
    df.to_csv('data/ptab_conv_random.csv', index=False)