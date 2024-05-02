# -*- coding: utf-8 -*-
"""
Created on Wed May  1 23:51:56 2024

@author: 112473
"""

import pandas as pd
url1 ="https://raw.githubusercontent.com/BinglinChang/fin_data/main/"
url2 ="https://raw.githubusercontent.com/MengenLee/fin_data/main/"
url3 ="https://raw.githubusercontent.com/leo920609/Llll/main/"

list1=["2601","2603","2605","2606","2607","2608","2609","2610","2611","2612"]
list2=["1201","1203","1210","1213","1215","1216","1217","1218","1225","1227"]
list3=["2330","2317","6505","2412","1301","1303","1326","2882","2881","2002"]

for i in list1:
    url = url1+ i + ".csv"
    df = pd.read_csv(url, index_col=0)
    display(df.head(5))
    df.to_csv(i+'TW.csv')
    
for i in list2:
    url = url2+ i + ".csv"
    df = pd.read_csv(url, index_col=0)
    display(df.head(5))
    df.to_csv(i+'TW.csv')
    
for i in list3:
    url = url3+ i + ".csv"
    df = pd.read_csv(url, index_col=0)
    display(df.head(5))
    df.to_csv(i+'TW.csv')